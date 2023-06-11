from PyQt5.QtWidgets import *

def trukytnuk90window():
    window = QDialog()
    window.setWindowTitle("Прямокутний трикутник")

    layout = QVBoxLayout()

    btn1 = QPushButton("За катетами")
    btn2 = QPushButton("За катетом і гіпотенузою")
    btn3 = QPushButton("За двома катетами")
    btn4 = QPushButton("За катетом і радіусом вписаного кола")
    btn5 = QPushButton("За катетом і радіусом описаного кола")

    layout.addWidget(btn1)
    layout.addWidget(btn2)
    layout.addWidget(btn3)
    layout.addWidget(btn4)
    layout.addWidget(btn5)

    window.setLayout(layout)
    window.show()
    window.exec()

