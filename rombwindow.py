from PyQt5.QtWidgets import *

def rombwindow():
    window = QDialog()
    window.setWindowTitle("Ромб")

    layout = QVBoxLayout()

    btn1 = QPushButton("За довжиною стороналейи та висотою")
    btn2 = QPushButton("За довжиною діагон")
    btn3 = QPushButton("За довжиною сторони та кутом")

    layout.addWidget(btn1)
    layout.addWidget(btn2)
    layout.addWidget(btn3)

    window.setLayout(layout)
    window.show()
    window.exec()