import sys
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QRunnable, QThreadPool, QObject
from ui_files.ui_SeabreezeGui import Ui_MainWindow
from seabreeze.spectrometers import Spectrometer, SeaBreezeError
import time
import os
from datetime import datetime
import pyqtgraph as pg
import qdarkstyle
from pyqtgraph.Qt import QtGui

os.environ['PYQTGRAPH_QT_LIB'] = 'PyQt5'
# Switch to using white background and black foreground
pg.setConfigOption('background', pg.mkColor(25, 35, 45))


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)


class Worker(QRunnable):

    def __init__(self, parent, spectrometer):
        super(Worker, self).__init__()
        self.signals = WorkerSignals()
        self.continue_acquisition = True
        self.parent = parent
        self.spectrometer = spectrometer

    @pyqtSlot()
    def run(self):
        while self.continue_acquisition:
            res = self.spectrometer.intensities()
            self.signals.result.emit(res)
            self.continue_acquisition = self.parent.get_acquisition_state('spec')
        self.signals.finished.emit()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # self.plot_camera_layout.addWidget(self.plot_camera.toolbar)
        self.thread_pool = QThreadPool()
        print("Multi-threading with maximum %d threads" % self.thread_pool.maxThreadCount())
        # Testing variables
        self.t_start = time.time()
        self.plotted_images = 0
        self.averaged_images = 0
        self.busy = False

        # Spectrometer setup
        # self.spec_serial_nbr = 'FLMS15932'
        self.spec_serial_nbr = 'FLMS12200'
        self.plot_item = self.spectrum_plot.addPlot()
        self.plot_item.enableAutoRange('xy', False)
        self.plot_item.setYRange(0, 2**16)
        self.plot_item.setXRange(400, 1000)
        self.plot_item.setLabel('left', "Counts",)
        self.plot_item.setLabel('bottom', "Wavelength")
        self.plot_item.showGrid(x=True, y=True)
        # self.plot_spec.axes.set_xlim([340, 1020])
        # self.plot_spec.axes.set_ylim([0, 65000])
        self.integration_time = 10
        self.spec_acquisition_state = False
        self.spectrometer = None
        self._plot_ref = None
        self.wavelengths = np.zeros((2048,))
        self.intensities = np.zeros((2048,))
        self.connect_spec()
        self.spectrum_pending = False

        self.connect_signals()

    def connect_signals(self):
        self.bt_spec_set_int_time.clicked.connect(self.set_integration_time)
        self.bt_spec_acquire.clicked.connect(self.acquire_spectrum)
        self.rb_spec_contin_acquisition.clicked.connect(self.change_spec_acquisition_state)

        self.action_connect_spec.triggered.connect(self.connect_spec)
        self.action_disconnect_spec.triggered.connect(self.disconnect_spec)

        self.action_save.triggered.connect(self.save_current)

    def get_acquisition_state(self, device):
        if device == 'camera':
            return self.camera_acquisition_state
        elif device == 'spec':
            return self.spec_acquisition_state

    @pyqtSlot()
    def connect_spec(self):
        try:
            self.spectrometer = Spectrometer.from_serial_number(self.spec_serial_nbr)
        except SeaBreezeError:
            print('Could not connect to spectrometer.')  # TODO: Write message to user
        else:
            self.lbl_spec_status.setText('Connected to ' + self.spec_serial_nbr)
            self.action_connect_spec.setEnabled(False)
            self.action_disconnect_spec.setEnabled(True)
            self.gb_spec.setEnabled(True)
            # Acquire first spectrum and plot it to get _plot_ref:
            self.set_integration_time()
            self.wavelengths = self.spectrometer.wavelengths()
            self.intensities = self.spectrometer.intensities()
            self._plot_ref = self.plot_item.plot(self.wavelengths, self.intensities)

    @pyqtSlot()
    def disconnect_spec(self):
        self.spectrometer.close()
        self.lbl_spec_status.setText('No spectrometer connected')
        self.action_connect_spec.setEnabled(True)
        self.action_disconnect_spec.setEnabled(False)
        self.gb_spec.setEnabled(False)

    @pyqtSlot()
    def set_integration_time(self):
        self.integration_time = self.sb_spec_int_time.value()
        self.spectrometer.integration_time_micros(self.integration_time * 1000)

    @pyqtSlot()
    def acquire_spectrum(self):
        print('Acquiring...')
        worker = Worker(self, self.spectrometer)
        worker.signals.result.connect(self.update_plot)
        worker.signals.finished.connect(self.worker_finished)
        self.spec_acquisition_state = False
        self.thread_pool.start(worker)

    @pyqtSlot(bool)
    def change_spec_acquisition_state(self, value):
        self.bt_spec_acquire.setEnabled(not value)
        if value:
            self.spec_acquisition_state = True
            print('Acquiring...')
            worker = Worker(self, self.spectrometer)
            worker.signals.result.connect(self.update_plot)
            worker.signals.finished.connect(self.worker_finished)
            # self.signals.stop_acquisition.connect(worker.stop_acquisition)
            self.thread_pool.start(worker)
        else:
            print('Stopping acquisition...')
            self.spec_acquisition_state = False

    def is_busy(self):
        return self.busy

    @pyqtSlot(object)
    def update_plot(self, value):
        self.busy = True
        # t_start = time.time()
        self.intensities = value
        # # Matplotlib
        # self._plot_ref.set_ydata(self.intensities)
        # self.plot_spec.draw()
        # Pyqtgraph
        self._plot_ref.setData(self.wavelengths, self.intensities)
        # self.t_plot = time.time()
        self.spectrum_pending = False
        # print('Plotted spectrum in %.2f ms' % ((time.time() - t_start) * 1e3))
        self.busy = False

    @pyqtSlot()
    def worker_finished(self):
        print('Worker finished')
        print('Handled %d images. Averaged %d and plotted %d' % (self.averaged_images + self.plotted_images,
                                                                 self.averaged_images, self.plotted_images))

    @pyqtSlot()
    def save_current(self):
        save_dir = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                              'Select a folder to save in',
                                                              'D:\\',  # TODO: Change to OS independent
                                                              QtWidgets.QFileDialog.ShowDirsOnly)
        if save_dir:
            now = datetime.now()
            np.savetxt(os.path.join(save_dir, now.strftime("%Y%m%d-%H%M%S") + '_spectrum.dat'),
                       np.array([self.wavelengths, self.intensities]).T)

    def closeEvent(self, event):
        if self.spectrometer:
            self.spectrometer.close()

        event.accept()

    @staticmethod
    def print_output(s):
        print(s)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api=os.environ['PYQTGRAPH_QT_LIB']))
    window = MainWindow()
    window.show()
    app.exec_()
