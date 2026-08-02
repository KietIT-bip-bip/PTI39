import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic

class CalulatorApp(QMainWindow):
    def __init__(self):
        super().__init__() # ke thua tu lop cha QMainWindow
        # khai bao bien input/ output
        self.input = ""
        
        #hien thi giao dien
        ui_path = "B2/Lab_2/cal.ui"
        uic.loadUi(ui_path, self)
        self.show()
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalulatorApp()
    sys.exit(app.exec())