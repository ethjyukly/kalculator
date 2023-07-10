from PyQt5.QtWidgets import*
def zaPorstorona():
    window = QDialog()
    inputP=QLineEdit("ведіть периметр")
    inputstorona=QLineEdit("ведіть сторону")
    outplosha=QLineEdit('площа')
    Btn1=QPushButton('вивести')
    linia=QVBoxLayout()
    linia.addWidget(inputstorona)
    linia.addWidget(inputP)
    linia.addWidget(outplosha)
    linia.addWidget(Btn1)


    def plosha():
        storona=int(inputstorona.text())
        P=int(inputP.text())
        plosha1=(P - 2storona * storona **2) / 2
        outplosha.setText(str(plosha1))
    Btn1.clicked.connect(plosha)
    window.setLayout(linia)
    window.show()
    window.exec()


