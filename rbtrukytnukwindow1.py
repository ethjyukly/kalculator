from PyQt5.QtWidgets import*
import math
def rbtrukutnukwindow1():
    window = QDialog()
    inputdiagonal=QLineEdit("ведіть діфгональ")
    inputstorona=QLineEdit("ведіть сторону")
    outplosha=QLineEdit('площа')
    Btn1=QPushButton('вивести')
    linia=QVBoxLayout()
    linia.addWidget(inputstorona)
    linia.addWidget(inputdiagonal)
    linia.addWidget(outplosha)
    linia.addWidget(Btn1)


    def plosha():
        storona=int(inputstorona.text())
        diagonal=int(inputdiagonal.text())
        plosha1=(storona * math.sqrt(diagonal**2 - (storona**2))) / 2
        outplosha.setText(str(plosha1))
    Btn1.clicked.connect(plosha)
    window.setLayout(linia)
    window.show()
    window.exec()


