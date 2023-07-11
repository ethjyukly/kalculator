from PyQt5.QtWidgets import *
import zakatetomigipotenyzou
import za2katetamu
def trukytnuk90window():
    window = QDialog()
    window.setWindowTitle("Прямокутний трикутник")

    layout = QVBoxLayout()

    btn1 = QPushButton("За катетами")
    btn2 = QPushButton("За катетом і гіпотенузою")
    btn3 = QPushButton("За двома катетами")
    btn4 = QPushButton("За катетом і радіусом вписаного кола")
    btn5 = QPushButton("За катетом і радіусом описаного кола")

    layout.addWidget(btn1)
    layout.addWidget(btn2)
    layout.addWidget(btn3)
    layout.addWidget(btn4)
    layout.addWidget(btn5)

    def zakatetomigipotenuzoufunc():
        zakatetomigipotenyzou.zakatetomgipjtenuzou()
    def za2katetamufunc():
        za2katetamu.za2katetamu()


    btn2.clicked.connect(zakatetomigipotenuzoufunc)
    btn3.clicked.connect(za2katetamufunc)
    window.setLayout(layout)
    window.show()
    window.exec()

