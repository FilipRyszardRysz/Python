import PyQt5.QtCore
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget

class sygnalizacja():
    def __init__(self):
        self.app = PyQt5.QtWidgets.QApplication([])
        self.okno = PyQt5.QtWidgets.QWidget()
        self.czasomierz = PyQt5.QtCore.QTimer()
        self.okno.setStyleSheet("background-color: black; margin 0 0;")
        self.okno.setFixedSize(100, 300)
        self.uklad = PyQt5.QtWidgets.QVBoxLayout()
        self.flag = 1;
       #______________________________________________________

        self.layout1 = PyQt5.QtWidgets.QLabel("")
        self.layout1.setStyleSheet("background-color: black;")
        self.layout1.setFixedSize(80, 80)
       #______________________________________________________

        self.layout2 = PyQt5.QtWidgets.QLabel("")
        self.layout2.setStyleSheet("background-color: black;")
        self.layout2.setFixedSize(80, 80)
       #______________________________________________________

        self.layout3 = PyQt5.QtWidgets.QLabel("")
        self.layout3.setStyleSheet("background-color: black;")
        self.layout3.setFixedSize(80, 80)
       #______________________________________________________

        self.uklad.addWidget(self.layout1)
        self.uklad.addWidget(self.layout2)
        self.uklad.addWidget(self.layout3)
       #______________________________________________________

        self.colors()
        self.okno.setLayout(self.uklad)
        self.okno.show()
        self.app.exec_()

    def colors(self):
        if self.flag == 1:
            self.layout2.setStyleSheet("background-color: black;")
            self.layout1.setStyleSheet("background-color: red;border-radius: 40px;")
            self.czasomierz.singleShot(5000, self.colors)
            self.flag = 2;

        elif self.flag == 2:
            self.layout2.setStyleSheet("background-color: yellow;border-radius: 40px;")
            self.czasomierz.singleShot(2000, self.colors)
            self.flag = 3;

        elif self.flag == 3:
            self.layout1.setStyleSheet("background-color: black;")
            self.layout2.setStyleSheet("background-color: black;")
            self.layout3.setStyleSheet("background-color: green;border-radius: 40px;")
            self.czasomierz.singleShot(5000, self.colors)
            self.flag = 4;

        else:
            self.layout3.setStyleSheet("background-color: black;")
            self.layout2.setStyleSheet("background-color: yellow;border-radius: 40px;")
            self.czasomierz.singleShot(2000, self.colors)
            self.flag = 1;

x = sygnalizacja()