from PyQt5 import QtCore, QtGui, QtWidgets


# MARK: ngochdm

class ZoomWidget(QtWidgets.QWidget):
    valueChanged = QtCore.pyqtSignal(int)

    def __init__(self, value=100):
        super().__init__()
        self._value = value

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setRange(1, 1000)
        self.slider.setValue(value)
        self.slider.setMinimumWidth(180)
        self.slider.setToolTip(self.tr("Zoom Level"))

        self.spin_box = QtWidgets.QSpinBox()
        self.spin_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spin_box.setRange(1, 1000)
        self.spin_box.setSuffix("%")
        self.spin_box.setValue(value)
        self.spin_box.setFixedWidth(64)
        self.spin_box.setKeyboardTracking(False)
        self.spin_box.setToolTip(self.tr("Zoom Level"))
        self.spin_box.setStatusTip(self.spin_box.toolTip())
        self.spin_box.setAlignment(QtCore.Qt.AlignCenter)

        font = self.spin_box.font()
        font.setPointSize(9)
        self.spin_box.setFont(font)

        self.setMinimumHeight(34)

        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(6, 2, 6, 2)
        layout.setSpacing(6)
        layout.addWidget(self.slider, 1)
        layout.addWidget(self.spin_box)
        self.setLayout(layout)

        self.slider.valueChanged.connect(self._on_slider_changed)
        self.spin_box.lineEdit().returnPressed.connect(
            self._on_spin_box_committed
        )

    def value(self):
        return self._value

    def setValue(self, value):
        self._set_value(value, emit=True)

    def _on_slider_changed(self, value):
        self._set_value(value, emit=True)

    def _on_spin_box_committed(self):
        self._set_value(self.spin_box.value(), emit=True)

    def _set_value(self, value, emit):
        value = max(
            self.spin_box.minimum(),
            min(self.spin_box.maximum(), int(value)),
        )
        if value == self._value:
            return

        self._value = value

        self.slider.blockSignals(True)
        self.spin_box.blockSignals(True)
        self.slider.setValue(value)
        self.spin_box.setValue(value)
        self.spin_box.blockSignals(False)
        self.slider.blockSignals(False)

        if emit:
            self.valueChanged.emit(value)

    def setEnabled(self, enabled):
        super().setEnabled(enabled)
        self.slider.setEnabled(enabled)
        self.spin_box.setEnabled(enabled)

    def minimumSizeHint(self):
        height = super().minimumSizeHint().height()
        font_metric = QtGui.QFontMetrics(self.spin_box.font())
        width = font_metric.horizontalAdvance(str(self.spin_box.maximum())) + 44
        return QtCore.QSize(width + 180, height)


# Old ZoomWidget
# class ZoomWidget(QtWidgets.QSpinBox):
#     def __init__(self, value=100):
#         super().__init__()
#         self.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
#         self.setRange(1, 1000)
#         self.setSuffix("%")
#         self.setValue(value)
#         self.setToolTip(self.tr("Zoom Level"))
#         self.setStatusTip(self.toolTip())
#         self.setAlignment(QtCore.Qt.AlignCenter)
#         font = self.font()
#         font.setPointSize(9)
#         self.setFont(font)

#     # QT Overload
#     def minimumSizeHint(self):
#         height = super().minimumSizeHint().height()
#         font_metric = QtGui.QFontMetrics(self.font())
#         width = font_metric.horizontalAdvance(str(self.maximum()))
#         return QtCore.QSize(width, height)
