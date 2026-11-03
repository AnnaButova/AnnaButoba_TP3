from maya import cmds
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QMainWindow,
    QSpinBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QGroupBox,
    QHBoxLayout
    )

class AnimationMenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Animation Generator")
        self.setFixedWidth(400)
        self.build_ui()

    def build_ui(self):
        v_layout1 = QVBoxLayout()
        group1 = QGroupBox("Animation Timing")
        h_layout1 = QHBoxLayout()
        
        self.duration_label = QLabel("Duration (Frames):")
        self.step_label = QLabel("Step (Frames):")
        self.duration_spinbox = QSpinBox()
        self.step_spinbox = QSpinBox()

        h_layout1.addWidget(self.duration_label)
        h_layout1.addWidget(self.duration_spinbox)
        h_layout1.addWidget(self.step_label)
        h_layout1.addWidget(self.step_spinbox)
        group1.setLayout(h_layout1)


        group2 = QGroupBox("Translate Parameters")
        v_layout2 = QVBoxLayout()
        h_layout2 = QHBoxLayout()
        h_layout3 = QHBoxLayout()
        self.minX_label = QLabel("Min X:")
        self.minY_label = QLabel("Min Y:")
        self.minZ_label = QLabel("Min Z:")
        self.maxX_label = QLabel("Max X:")
        self.maxY_label = QLabel("Max Y:")
        self.maxZ_label = QLabel("Max Z:")

        self.minX_spinbox = QSpinBox()
        self.minY_spinbox = QSpinBox()
        self.minZ_spinbox = QSpinBox()
        self.maxX_spinbox = QSpinBox()
        self.maxY_spinbox = QSpinBox()
        self.maxZ_spinbox = QSpinBox()

        h_layout2.addWidget(self.minX_label)
        h_layout2.addWidget(self.minX_spinbox)
        h_layout2.addWidget(self.minY_label)
        h_layout2.addWidget(self.minY_spinbox)
        h_layout2.addWidget(self.minZ_label)
        h_layout2.addWidget(self.minZ_spinbox)

        h_layout3.addWidget(self.maxX_label)
        h_layout3.addWidget(self.maxX_spinbox)
        h_layout3.addWidget(self.maxY_label)
        h_layout3.addWidget(self.maxY_spinbox)
        h_layout3.addWidget(self.maxZ_label)
        h_layout3.addWidget(self.maxZ_spinbox)
        v_layout2.addLayout(h_layout2)
        v_layout2.addLayout(h_layout3)
        group2.setLayout(v_layout2)


        v_layout1.addWidget(group1)
        v_layout1.addWidget(group2)
        self.setLayout(v_layout1)




window = AnimationMenuWindow()
window.show()