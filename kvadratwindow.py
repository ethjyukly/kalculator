from PyQt5.QtWidgets import*
"""
S=a^2
S=p^2/16
S=d^2/2
S=2R^2
S=Do^2/2
S=4R^2
S=Dv^2
"""


def kvadratwindow():
    window=QDialog()
    liniabuton = QVBoxLayout()
    Btn1 = QPushButton("за двома сторонами ")
    Btn2 = QPushButton("за периметром ")
    Btn3 = QPushButton("за діагналю  ")
    Btn4 = QPushButton("за діаметром описаного кола  ")
    Btn5 = QPushButton("за діаметром вписаного кола   ")
    Btn6 = QPushButton("за радіусом  ")
    Btn7 = QPushButton("за радіусом  ")
    liniabuton.addWidget(Btn1)
    liniabuton.addWidget(Btn2)
    liniabuton.addWidget(Btn3)
    liniabuton.addWidget(Btn4)
    liniabuton.addWidget(Btn5)
    liniabuton.addWidget(Btn6)
    liniabuton.addWidget(Btn7)

    window.setLayout(liniabuton)
    window.show()
    window.exec()