from PyQt5.QtWidgets import*
import kvadratwindow
import trukytnuk90window
import rombwindow
import rbtrukytnukwindow
import pramokytnukwindow
import paralelogramtwindow
App=QApplication([])
window=QWidget()
Btn1=QPushButton("рівнобедрений трикутник")
Btn2=QPushButton("паралелограм")
Btn3=QPushButton("ромб ")
Btn4=QPushButton("прямокутний трикутник")
Btn5=QPushButton("прямокутник")
Btn6=QPushButton("квадрат")
figurabox=QGroupBox()
formulabox=QGroupBox()
linia=QVBoxLayout()
liniabuton =QHBoxLayout()
liniabuton1=QHBoxLayout()
linia1=QHBoxLayout()
linia2=QHBoxLayout()
linia3=QHBoxLayout()
linia4=QHBoxLayout()
linia5=QHBoxLayout()
linia6=QHBoxLayout()
linia7=QHBoxLayout()
linia8=QHBoxLayout()
linia9=QHBoxLayout()
linia10=QHBoxLayout()
linia11=QHBoxLayout()
linia12=QHBoxLayout()
linia13=QHBoxLayout()
linia.addLayout(linia1)
linia.addLayout(linia2)
linia.addLayout(linia3)
linia.addLayout(linia4)
linia.addLayout(linia5)
linia.addLayout(linia6)
linia.addLayout(linia7)
linia.addLayout(linia8)
linia.addLayout(linia9)
linia.addLayout(linia10)
linia.addLayout(linia11)
linia.addLayout(linia12)
linia.addLayout(linia13)
liniabuton.addWidget(Btn1)
liniabuton.addWidget(Btn2)
liniabuton.addWidget(Btn3)
liniabuton.addWidget(Btn4)
liniabuton.addWidget(Btn5)
liniabuton.addWidget(Btn6)
linia1.addWidget(figurabox)
def kvadrat():
    kvadratwindow.kvadratwindow()
def trukytnuk90():
    trukytnuk90window.trukytnuk90window()
def romb():
    rombwindow.rombwindow()
def paralelogram():
    paralelogramtwindow.paralelogramt()
def pramokytnuk():
    pramokytnukwindow.pramokytnuktwindow()
def rbtrukytnuk():
    rbtrukytnukwindow.rbtrukytnukwindow()




Btn6.clicked.connect(kvadrat)
Btn5.clicked.connect(pramokytnuk)
Btn4.clicked.connect(trukytnuk90)
Btn3.clicked.connect(romb)
Btn2.clicked.connect(paralelogram)
Btn1.clicked.connect(rbtrukytnuk)

figurabox.setLayout(liniabuton)
window.setLayout(linia)
window.show()
App.exec()



