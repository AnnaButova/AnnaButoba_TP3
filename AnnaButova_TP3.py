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

# creating a custom spinbox class to set the range of values
class CustomSpinBox(QSpinBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRange(-1000, 1000)
        self.setValue(100)
        
# creating a custom window class for the animation menu
class AnimationMenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Animation Generator")
        self.setFixedWidth(400)
        self.build_ui()

    def build_ui(self):
        # Animation Timing --------------------------------
        v_layout1 = QVBoxLayout()
        group1 = QGroupBox("Animation Timing")
        h_layout1 = QHBoxLayout()
        
        self.duration_label = QLabel("Duration (Frames):")
        self.step_label = QLabel("Step (Frames):")
        self.duration_spinbox = CustomSpinBox()
        self.step_spinbox = CustomSpinBox()

        h_layout1.addWidget(self.duration_label)
        h_layout1.addWidget(self.duration_spinbox)
        h_layout1.addWidget(self.step_label)
        h_layout1.addWidget(self.step_spinbox)
        group1.setLayout(h_layout1)
        # ------------------------------------------------
    
        # Translate Parameters --------------------------------
        group2 = QGroupBox("Translate Parameters")
        v_layout2 = QVBoxLayout()
        h_layout2 = QHBoxLayout()
        h_layout3 = QHBoxLayout()
        self.minTX_label = QLabel("Min X:")
        self.minTY_label = QLabel("Min Y:")
        self.minTZ_label = QLabel("Min Z:")
        self.maxTX_label = QLabel("Max X:")
        self.maxTY_label = QLabel("Max Y:")
        self.maxTZ_label = QLabel("Max Z:")

        self.minTX_spinbox = CustomSpinBox()
        self.minTY_spinbox = CustomSpinBox()
        self.minTZ_spinbox = CustomSpinBox()
        self.maxTX_spinbox = CustomSpinBox()
        self.maxTY_spinbox = CustomSpinBox()
        self.maxTZ_spinbox = CustomSpinBox()

        h_layout2.addWidget(self.minTX_label)
        h_layout2.addWidget(self.minTX_spinbox)
        h_layout2.addWidget(self.minTY_label)
        h_layout2.addWidget(self.minTY_spinbox)
        h_layout2.addWidget(self.minTZ_label)
        h_layout2.addWidget(self.minTZ_spinbox)

        h_layout3.addWidget(self.maxTX_label)
        h_layout3.addWidget(self.maxTX_spinbox)
        h_layout3.addWidget(self.maxTY_label)
        h_layout3.addWidget(self.maxTY_spinbox)
        h_layout3.addWidget(self.maxTZ_label)
        h_layout3.addWidget(self.maxTZ_spinbox)
        v_layout2.addLayout(h_layout2)
        v_layout2.addLayout(h_layout3)
        group2.setLayout(v_layout2)
        # ------------------------------------------------

        # Rotate Parameters --------------------------------
        group3 = QGroupBox("Rotate Parameters")
        v_layout3 = QVBoxLayout()
        h_layout4 = QHBoxLayout()
        h_layout5 = QHBoxLayout()

        self.minRX_label = QLabel("Min X:")
        self.minRY_label = QLabel("Min Y:")
        self.minRZ_label = QLabel("Min Z:")
        self.maxRX_label = QLabel("Max X:")
        self.maxRY_label = QLabel("Max Y:")
        self.maxRZ_label = QLabel("Max Z:")


        self.minRX_spinbox = CustomSpinBox()
        self.minRY_spinbox = CustomSpinBox()
        self.minRZ_spinbox = CustomSpinBox()
        self.maxRX_spinbox = CustomSpinBox()
        self.maxRY_spinbox = CustomSpinBox()
        self.maxRZ_spinbox = CustomSpinBox()

        h_layout4.addWidget(self.minRX_label)
        h_layout4.addWidget(self.minRX_spinbox)
        h_layout4.addWidget(self.minRY_label)
        h_layout4.addWidget(self.minRY_spinbox)
        h_layout4.addWidget(self.minRZ_label)
        h_layout4.addWidget(self.minRZ_spinbox)

        h_layout5.addWidget(self.maxRX_label)
        h_layout5.addWidget(self.maxRX_spinbox)
        h_layout5.addWidget(self.maxRY_label)
        h_layout5.addWidget(self.maxRY_spinbox)
        h_layout5.addWidget(self.maxRZ_label)
        h_layout5.addWidget(self.maxRZ_spinbox)

        v_layout3.addLayout(h_layout4)
        v_layout3.addLayout(h_layout5)
        group3.setLayout(v_layout3)
        # ------------------------------------------------

        # Scale Parameters --------------------------------
        group4 = QGroupBox("Scale Parameters")
        v_layout4 = QVBoxLayout()
        h_layout6 = QHBoxLayout()
        h_layout7 = QHBoxLayout()

        self.minSX_label = QLabel("Min X:")
        self.minSY_label = QLabel("Min Y:")
        self.minSZ_label = QLabel("Min Z:")
        self.maxSX_label = QLabel("Max X:")
        self.maxSY_label = QLabel("Max Y:")
        self.maxSZ_label = QLabel("Max Z:")

        self.minSX_spinbox = CustomSpinBox()
        self.minSY_spinbox = CustomSpinBox()
        self.minSZ_spinbox = CustomSpinBox()
        self.maxSX_spinbox = CustomSpinBox()
        self.maxSY_spinbox = CustomSpinBox()
        self.maxSZ_spinbox = CustomSpinBox()

        h_layout6.addWidget(self.minSX_label)
        h_layout6.addWidget(self.minSX_spinbox)
        h_layout6.addWidget(self.minSY_label)
        h_layout6.addWidget(self.minSY_spinbox)
        h_layout6.addWidget(self.minSZ_label)
        h_layout6.addWidget(self.minSZ_spinbox)

        h_layout7.addWidget(self.maxSX_label)
        h_layout7.addWidget(self.maxSX_spinbox)
        h_layout7.addWidget(self.maxSY_label)
        h_layout7.addWidget(self.maxSY_spinbox)
        h_layout7.addWidget(self.maxSZ_label)
        h_layout7.addWidget(self.maxSZ_spinbox)

        v_layout4.addLayout(h_layout6)
        v_layout4.addLayout(h_layout7)
        group4.setLayout(v_layout4)
        # ------------------------------------------------

        self.generate_button = QPushButton("Generate Animation") # making a button to generate the animation

        # Layout for the main window ---------------------
        v_layout1.addWidget(group1)
        v_layout1.addWidget(group2)
        v_layout1.addWidget(group3)
        v_layout1.addWidget(group4)
        v_layout1.addWidget(self.generate_button)
        self.setLayout(v_layout1)
        # -----------------------------------------------

window = AnimationMenuWindow()
window.show()