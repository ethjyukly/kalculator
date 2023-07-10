from PyQt5.QtWidgets import*
import za2storonamu
import zaPorstorona
"""
S=a*b
S=(Pa-2a^2):2
S=a*sqrt(d^2-a^2)
S=(d^2*sin B ):2
S=a*sqrt(4R^2-a^2
S=a*sqrt(Do^2-a^2)
"""
def pramokytnuktwindow():
    window=QDialog()
    window.setWindowTitle("прямокуттник")
    liniabuton = QVBoxLayout()
    Btn1 = QPushButton("за  двома перпендикудярних  сторонаами")
    Btn2 = QPushButton("за периметром і стороною")
    Btn3 = QPushButton("за діагналю і будьякій стороні   ")
    Btn4 = QPushButton("за діагоналю і синусом гстрого кута між ними   ")
    Btn5 = QPushButton("за діаметром описаного кола  і строною  ")
    Btn6 = QPushButton("за радіусом описаного кола і стороною  ")
    liniabuton.addWidget(Btn1)
    liniabuton.addWidget(Btn2)
    liniabuton.addWidget(Btn3)
    liniabuton.addWidget(Btn4)
    liniabuton.addWidget(Btn5)
    liniabuton.addWidget(Btn6)
    def za2storonamu():
        za2storonamu.za2storonamu()
    def zaPorstorona():
        zaPorstorona.zaPorstorona()

    Btn1.clicked.connect(za2storonamu)
    Btn2.clicked.connect(zaPorstorona)
    window.setLayout(liniabuton)
    window.show()
    window.exec()
