from PyQt5.QtWidgets import *
import rbtrukytnukwindow1
import rbtrukytnukwindow2
import rbtrukytnukwindow3
import rbtrukytnukwindow4
import rbtrukytnukwindow5
def rbtrukytnukwindow():
    window = QDialog()
    window.setWindowTitle("рівнобедрений трикутник")
    liniabuton = QVBoxLayout()

    Btn1 = QPushButton("За діагоналлю і основою")
    Btn2 = QPushButton("За двома сторонами і основою")
    Btn3 = QPushButton("За основою і висотою")
    Btn4 = QPushButton("За довжиною сторони і радіусом вписаного кола")
    Btn5 = QPushButton("За радіусом описаного кола і довжиною сторони")
    liniabuton.addWidget(Btn1)
    liniabuton.addWidget(Btn2)
    liniabuton.addWidget(Btn3)
    liniabuton.addWidget(Btn4)
    liniabuton.addWidget(Btn5)

    window.setLayout(liniabuton)
    window.show()
    window.exec()

