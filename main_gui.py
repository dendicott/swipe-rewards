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
        self.card_string = 1
        self.variable_dict_col0 = {}
        self.variable_dict_col1 = {}
        self.variable_dict_col2 = {}
        self.variable_dict_col3 = {}
        self.variable_dict_col4 = {}
        self.variable_dict_col5 = {}
        self.variable_dict_col6 = {}
        self.variable_dict_col7 = {}
        self.variable_dict_col8 = {}
        self.variable_dict_col9 = {}

        #self.window = QWidget()
        self.layout = QGridLayout(self)
        self.setGeometry(300, 300, 1300, 110)
        self.setWindowTitle("Credit Card Analyzer")
        self.initUI()
        
    def initUI(self):
        issuers = ["American Express", "Chase", "Bank of America","Discover",
            "Citi", "Barclays", "US Bank", "Capital One"]

        selector = ["NO", "YES"]

        points = ["MR (AMEX)", "UR (Chase)", "Cash", "TY (Citi)", "SKY (Delta)",
                    "RR (Southwest)", "AMZN (Amazon)", "COST (Costco)", "VR (CapOne)",
                    "HH (Hilton)", "AA"]
        
        b1 = QPushButton(self)
        b1.setText("Add Row")
        b1.clicked.connect(self.clickedButton)
        
        b2 = QPushButton(self)
        b2.setText("Save")
        b2.clicked.connect(self.clickedDataSave)
        
        self.layout.addWidget(b1,0,0)
        self.layout.addWidget(b2,0,1)

        self.variable_dict_col0['self.row1'] = QLabel("Card Name")
        self.variable_dict_col1['self.row1'] = QLabel("Issuer")
        self.variable_dict_col2['self.row1'] = QLabel("Date Opened")
        self.variable_dict_col3['self.row1'] = QLabel("Date Closed")
        self.variable_dict_col4['self.row1'] = QLabel("Bonus Earned")
        self.variable_dict_col5['self.row1'] = QLabel("Date Bonus Earned")
        self.variable_dict_col6['self.row1'] = QLabel("Product Change")
        self.variable_dict_col7['self.row1'] = QLabel("Business Card")
        self.variable_dict_col8['self.row1'] = QLabel("Annual Fee")
        self.variable_dict_col9['self.row1'] = QLabel("Points Currency")

        self.layout.setSpacing(10)
        self.layout.addWidget(self.variable_dict_col0['self.row1'],1,0)
        self.layout.addWidget(self.variable_dict_col1['self.row1'],1,1)
        self.layout.addWidget(self.variable_dict_col2['self.row1'],1,2)
        self.layout.addWidget(self.variable_dict_col3['self.row1'],1,3)
        self.layout.addWidget(self.variable_dict_col4['self.row1'],1,4)
        self.layout.addWidget(self.variable_dict_col5['self.row1'],1,5)
        self.layout.addWidget(self.variable_dict_col6['self.row1'],1,6)
        self.layout.addWidget(self.variable_dict_col7['self.row1'],1,7)
        self.layout.addWidget(self.variable_dict_col8['self.row1'],1,8)
        self.layout.addWidget(self.variable_dict_col9['self.row1'],1,9)    
        
        dict = {}

        for x in range(self.low,self.rows):
            dict[f'comboIssuers{x}'] = QComboBox(self)
            dict[f'comboProductChange{x}'] = QComboBox(self)
            dict[f'comboBusinessCard{x}'] = QComboBox(self)
            dict[f'comboPoints{x}'] = QComboBox(self)
            
            self.variable_dict_col0[f'self.row{x}'] = QLineEdit("e.g. AMEX Gold " + str(self.card_string))
            self.variable_dict_col1[f'self.row{x}'] = dict[f'comboIssuers{x}']
            self.variable_dict_col2[f'self.row{x}'] = QLineEdit("YYYY-MM-DD")
            self.variable_dict_col3[f'self.row{x}'] = QLineEdit("YYYY-MM-DD")
            self.variable_dict_col4[f'self.row{x}'] = QLineEdit("XXXXX")
            self.variable_dict_col5[f'self.row{x}'] = QLineEdit("YYYY-MM-DD")
            self.variable_dict_col6[f'self.row{x}'] = dict[f'comboProductChange{x}']
            self.variable_dict_col7[f'self.row{x}'] = dict[f'comboBusinessCard{x}']
            self.variable_dict_col8[f'self.row{x}'] = QLineEdit("e.g. 0, 95")
            self.variable_dict_col9[f'self.row{x}'] = dict[f'comboPoints{x}']

            self.layout.addWidget(self.variable_dict_col0[f'self.row{x}'],x,0)
            self.layout.addWidget(self.variable_dict_col1[f'self.row{x}'],x,1)
            self.layout.addWidget(self.variable_dict_col3[f'self.row{x}'],x,3)
            self.layout.addWidget(self.variable_dict_col4[f'self.row{x}'],x,4)
            self.layout.addWidget(self.variable_dict_col2[f'self.row{x}'],x,2)
            self.layout.addWidget(self.variable_dict_col5[f'self.row{x}'],x,5)
            self.layout.addWidget(self.variable_dict_col6[f'self.row{x}'],x,6)
            self.layout.addWidget(self.variable_dict_col7[f'self.row{x}'],x,7)
            self.layout.addWidget(self.variable_dict_col8[f'self.row{x}'],x,8)
            self.layout.addWidget(self.variable_dict_col9[f'self.row{x}'],x,9)

            dict[f'comboIssuers{x}'].addItems(issuers)
            dict[f'comboProductChange{x}'].addItems(selector)
            dict[f'comboBusinessCard{x}'].addItems(selector)
            dict[f'comboPoints{x}'].addItems(points)
            
    def clickedButton(self):
        self.rows += 1
        self.low += 1
        self.card_string += 1
        self.update()
        
    def clickedDataSave(self):
        
        df = pd.DataFrame()
        
        col0_data = [self.variable_dict_col0[f'self.row{row}'].text() for row in range(2,self.rows)]
        col1_data = [self.variable_dict_col1[f'self.row{row}'].currentText() for row in range(2,self.rows)]
        col2_data = [self.variable_dict_col2[f'self.row{row}'].text() for row in range(2,self.rows)]
        col3_data = [self.variable_dict_col3[f'self.row{row}'].text() for row in range(2,self.rows)]
        col4_data = [self.variable_dict_col4[f'self.row{row}'].text() for row in range(2,self.rows)]
        col5_data = [self.variable_dict_col5[f'self.row{row}'].text() for row in range(2,self.rows)]
        col6_data = [self.variable_dict_col6[f'self.row{row}'].currentText() for row in range(2,self.rows)]
        col7_data = [self.variable_dict_col7[f'self.row{row}'].currentText() for row in range(2,self.rows)]
        col8_data = [self.variable_dict_col8[f'self.row{row}'].text() for row in range(2,self.rows)]
        col9_data = [self.variable_dict_col9[f'self.row{row}'].currentText() for row in range(2,self.rows)]
        
        df[self.variable_dict_col0['self.row1'].text()] = col0_data
        df[self.variable_dict_col1['self.row1'].text()] = col1_data
        df[self.variable_dict_col2['self.row1'].text()] = col2_data
        df[self.variable_dict_col3['self.row1'].text()] = col3_data
        df[self.variable_dict_col4['self.row1'].text()] = col4_data
        df[self.variable_dict_col5['self.row1'].text()] = col5_data
        df[self.variable_dict_col6['self.row1'].text()] = col6_data
        df[self.variable_dict_col7['self.row1'].text()] = col7_data
        df[self.variable_dict_col8['self.row1'].text()] = col8_data
        df[self.variable_dict_col9['self.row1'].text()] = col9_data
        
        # df.set_index(df.columns[0],inplace=True)
        
        df.to_excel("gui_output.xlsx")
        print(df)
        sys.exit()
    
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

