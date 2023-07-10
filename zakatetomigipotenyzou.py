from PyQt5.QtWidgets import*
def zakatetomgipjtenuzou():
    window = QDialog()
    inputgipotenuza=QLineEdit("ведіть гіпотенузу")
    inputkatet=QLineEdit("ведіть катет")
    outplosha=QLineEdit('площа')
    Btn1=QPushButton('вивести')
    linia=QVBoxLayout()
    linia.addWidget(inputkatet)
    linia.addWidget(inputgipotenuza)
    linia.addWidget(outplosha)
    linia.addWidget(Btn1)


    def plosha():
        gipotenuza=int(inputgipotenuza.text())
        katet=int(inputkatet.text())
        plosha1=0.5*gipotenuza*katet
        outplosha.setText(str(plosha1))
    Btn1.clicked.connect(plosha)
    window.setLayout(linia)
    window.show()
    window.exec()


