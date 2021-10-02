from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtWidgets import QGridLayout, QPushButton, QComboBox, QLineEdit
import sys
import os
import pandas as pd

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.rows = 3
        self.low = 2
        self.variable_dict = {}
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
        
        b1 = QPushButton(self)
        b1.setText("Add Row")
        b1.clicked.connect(self.clickedButton)
        
        b2 = QPushButton(self)
        b2.setText("Save")
        b2.clicked.connect(self.clickedDataSave)
        
        self.layout.addWidget(b1,0,0)
        self.layout.addWidget(b2,0,1)

        # self.col0Label = QLabel("Card Name")
        # self.col1label = QLabel("Issuer")
        # self.col2label = QLabel("Date Opened")
        # self.col3label = QLabel("Date Closed")
        # self.col4label = QLabel("Points Earned")
        # self.col5label = QLabel("Product Change")
        # self.col6label = QLabel("Business Card")
        # self.col7label = QLabel("Annual Fee")
        # self.col8label = QLabel("Points Currency")

        self.variable_dict['self.row1Col0'] = QLabel("Card Name")
        self.variable_dict['self.row1Col1'] = QLabel("Issuer")
        self.variable_dict['self.row1Col2'] = QLabel("Date Opened")
        self.variable_dict['self.row1Col3'] = QLabel("Date Closed")
        self.variable_dict['self.row1Col4'] = QLabel("Points Earned")
        self.variable_dict['self.row1Col5'] = QLabel("Product Change")
        self.variable_dict['self.row1Col6'] = QLabel("Business Card")
        self.variable_dict['self.row1Col7'] = QLabel("Annual Fee")
        self.variable_dict['self.row1Col8'] = QLabel("Points Currency")

        self.layout.setSpacing(10)
        self.layout.addWidget(self.variable_dict['self.row1Col0'],1,0)
        self.layout.addWidget(self.variable_dict['self.row1Col1'],1,1)
        self.layout.addWidget(self.variable_dict['self.row1Col2'],1,2)
        self.layout.addWidget(self.variable_dict['self.row1Col3'],1,3)
        self.layout.addWidget(self.variable_dict['self.row1Col4'],1,4)
        self.layout.addWidget(self.variable_dict['self.row1Col5'],1,5)
        self.layout.addWidget(self.variable_dict['self.row1Col6'],1,6)
        self.layout.addWidget(self.variable_dict['self.row1Col7'],1,7)
        self.layout.addWidget(self.variable_dict['self.row1Col8'],1,8)    
        
        dict = {}

        for x in range(self.low,self.rows):
            dict[f'comboIssuers{x}'] = QComboBox(self)
            dict[f'comboProductChange{x}'] = QComboBox(self)
            dict[f'comboBusinessCard{x}'] = QComboBox(self)
            dict[f'comboPoints{x}'] = QComboBox(self)
            
            self.variable_dict[f'self.row{x}Col0'] = QLineEdit("e.g. AMEX Gold")
            self.variable_dict[f'self.row{x}Col1'] = dict[f'comboIssuers{x}']
            self.variable_dict[f'self.row{x}Col2'] = QLineEdit("YYYY-MM-DD")
            self.variable_dict[f'self.row{x}Col3'] = QLineEdit("YYYY-MM-DD")
            self.variable_dict[f'self.row{x}Col4'] = QLineEdit("XX,XXX")
            self.variable_dict[f'self.row{x}Col5'] = dict[f'comboProductChange{x}']
            self.variable_dict[f'self.row{x}Col6'] = dict[f'comboBusinessCard{x}']
            self.variable_dict[f'self.row{x}Col7'] = QLineEdit("e.g. 0, 95")
            self.variable_dict[f'self.row{x}Col8'] = dict[f'comboPoints{x}']

            self.layout.addWidget(self.variable_dict[f'self.row{x}Col0'],x,0)
            self.layout.addWidget(self.variable_dict[f'self.row{x}Col1'],x,1)
            self.layout.addWidget(self.variable_dict[f'self.row{x}Col2'],x,2)
            self.layout.addWidget(self.variable_dict[f'self.row{x}Col3'],x,3)
            self.layout.addWidget(self.variable_dict[f'self.row{x}Col4'],x,4)
            self.layout.addWidget(self.variable_dict[f'self.row{x}Col5'],x,5)
            self.layout.addWidget(self.variable_dict[f'self.row{x}Col6'],x,6)
            self.layout.addWidget(self.variable_dict[f'self.row{x}Col7'],x,7)
            self.layout.addWidget(self.variable_dict[f'self.row{x}Col8'],x,8)

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
        #file_path = os.path.abspath(os.path.dirname(__file__))
        #print(self.variable_dict['self.row2Col1'].currentText())
        column_names = [self.variable_dict['self.row1Col0'].text(),self.variable_dict['self.row1Col1'].text(),self.variable_dict['self.row1Col2'].text(),
                        self.variable_dict['self.row1Col3'].text(),self.variable_dict['self.row1Col4'].text(),self.variable_dict['self.row1Col5'].text(),
                        self.variable_dict['self.row1Col6'].text(),self.variable_dict['self.row1Col7'].text(),self.variable_dict['self.row1Col8'].text()]
        
        df = pd.DataFrame.from_dict(self.variable_dict, orient='index',
                          columns=column_names)
        # df[self.variable_dict['self.row1Col0'].text()] = [self.variable_dict['self.row2Col0'].text(),self.variable_dict['self.row3Col0'].text()]
        
        # for column in self.variable_dict.keys():
        #     print(column)
        
        # df.to_excel("output.xlsx")
        print(df)
        return self.variable_dict['self.row1Col0'].text()
    
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

