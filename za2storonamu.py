from PyQt5.QtWidgets import*
def za2storonamu():
    window = QDialog()
    inputstorona1=QLineEdit("ведіть першу сторону")
    inputstorona2=QLineEdit("ведіть другу сторону")
    outplosha=QLineEdit('площа')
    Btn1=QPushButton('вивести')
    linia=QVBoxLayout()
    linia.addWidget(inputstorona1)
    linia.addWidget(inputstorona2)
    linia.addWidget(outplosha)
    linia.addWidget(Btn1)


    def plosha():
        storona1=int(inputstorona1.text())
        storona2=int(inputstorona2.text())
        plosha1=storona1*storona2
        outplosha.setText(str(plosha1))
    Btn1.clicked.connect(plosha)
    window.setLayout(linia)
    window.show()
    window.exec()
