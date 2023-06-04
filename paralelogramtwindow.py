from PyQt5.QtWidgets import*
"""
S=a*h-
S=ab sinA
S=1/2*d1d2sinY

"""

def paralelogramt():
    window=QDialog()
    liniabuton = QVBoxLayout()
    Btn1 = QPushButton("за висотою і стороною")
    Btn2 = QPushButton("за 2 сторонами і синусом прилеглого кута")
    Btn3 = QPushButton("через 2 діагоналі і синус кута між ними ")
    liniabuton.addWidget(Btn1)
    liniabuton.addWidget(Btn2)
    liniabuton.addWidget(Btn3)
    window.setLayout(liniabuton)
    window.show()
    window.exec()