#from PySide2.QtCore import Qt
from PyQt5 import QtWidgets
#from PyQt5.QtGui import QPointingDeviceUniqueId
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget
from PyQt5.QtWidgets import QGridLayout, QPushButton, QComboBox, QLineEdit
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.rows = 3
        self.low = 2
        #self.window = QWidget()
        self.layout = QGridLayout(self)
        self.setGeometry(300, 300, 1100, 110)
        self.setWindowTitle("Credit Card Analyzer")
        self.initUI()
        
    def initUI(self):
        #self.label = QtWidgets.QLabel(self)
        #self.label.setText("Credit Card")
        #self.label.move(50,50)
        issuers = ["American Express", "Chase", "Bank of America","Discover",
            "Citi", "Barclays", "US Bank", "Capital One"]

        selector = ["No", "Yes"]

        points = ["MR (AMEX)", "UR (Chase)", "Cash", "TY (Citi)", "SKY (Delta)",
                    "SW (Southwest)", "AMZN (Amazon)", "COST (Cotsco)", "VR (CapOne)",
                    "HH (Hilton)"]
        
        b1 = QtWidgets.QPushButton(self)
        b1.setText("Add Row")
        b1.clicked.connect(self.clickedButton)
        
        b2 = QtWidgets.QPushButton(self)
        b2.setText("Save")
        b2.clicked.connect(self.clickedDataSave)
        
        self.layout.addWidget(b1,0,0)
        self.layout.addWidget(b2,0,1)

        self.layout.setSpacing(10)
        self.layout.addWidget(QLabel("Card Name"),1,0)
        self.layout.addWidget(QLabel("Issuer"),1,1)
        self.layout.addWidget(QLabel("Date Opened"),1,2)
        self.layout.addWidget(QLabel("Date Closed"),1,3)
        self.layout.addWidget(QLabel("Points Earned"),1,4)
        self.layout.addWidget(QLabel("Product Change"),1,5)
        self.layout.addWidget(QLabel("Business Card"),1,6)
        self.layout.addWidget(QLabel("Annual Fee"),1,7)
        self.layout.addWidget(QLabel("Points Currency"),1,8)    
        
        dict = {}

        for x in range(self.low,self.rows):
            dict[f'comboIssuers{x}'] = QComboBox(self)
            dict[f'comboProductChange{x}'] = QComboBox(self)
            dict[f'comboBusinessCard{x}'] = QComboBox(self)
            dict[f'comboPoints{x}'] = QComboBox(self)

            self.layout.addWidget(QLineEdit("e.g. AMEX Gold"),x,0)
            self.layout.addWidget(dict[f'comboIssuers{x}'], x, 1)
            self.layout.addWidget(QLineEdit("YYYY-MM-DD"),x,2)
            self.layout.addWidget(QLineEdit("YYYY-MM-DD"),x,3)
            self.layout.addWidget(QLineEdit("XX,XXX"),x,4)
            self.layout.addWidget(dict[f'comboProductChange{x}'],x,5)
            self.layout.addWidget(dict[f'comboBusinessCard{x}'],x,6)
            self.layout.addWidget(QLineEdit(),x,7)
            self.layout.addWidget(dict[f'comboPoints{x}'],x,8)

            dict[f'comboIssuers{x}'].addItems(issuers)
            dict[f'comboProductChange{x}'].addItems(selector)
            dict[f'comboBusinessCard{x}'].addItems(selector)
            dict[f'comboPoints{x}'].addItems(points)
            
    def clickedButton(self):
        self.rows += 1
        self.low += 1
        print(self.rows)
        self.update()
        #return rows
    
    def clickedDataSave(self):
        print("save data")
    
    def update(self):
        #self.label.adjustSize()
        self.initUI()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
    
window()

# if __name__ == "__main__":
#     window()

