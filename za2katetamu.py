from PyQt5.QtWidgets import*
def za2katetamu():
    window = QDialog()
    inputkatet1=QLineEdit("ведіть перший катет")
    inputkatet2=QLineEdit("ведіть другий катет катет")
    outplosha=QLineEdit('площа')
    Btn1=QPushButton('вивести')
    linia=QVBoxLayout()
    linia.addWidget(inputkatet1)
    linia.addWidget(inputkatet2)
    linia.addWidget(outplosha)
    linia.addWidget(Btn1)


    def plosha():
        katet1=int(inputkatet1.text())
        katet2=int(inputkatet2.text())
        plosha1=0.5*katet1*katet2
        outplosha.setText(str(plosha1))
    Btn1.clicked.connect(plosha)
    window.setLayout(linia)
    window.show()
    window.exec()


