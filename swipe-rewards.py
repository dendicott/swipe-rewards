"""
TODO
-translate notebook functions here
-add Citi, BoA, USBank application rules
-add points-to-cash conversion dictionary
-add rewards report by year
"""

import numpy as np
import pandas as pd
from datetime import datetime
from datetime import date
from datetime import timedelta

credit = pd.ExcelFile('credit_cards.xlsx')
credit = credit.parse(index_col=0)

today = datetime.now()
credit['Date Closed']['Chase Southwest']


for card in credit.index:
    credit['Date Opened'][card] = datetime.strptime(credit['Date Opened'][card],'%Y-%m-%d')

for card in credit.index:
    if credit['Date Closed'][card] == 'OPEN':
        continue
    else:
        credit['Date Closed'][card] = datetime.strptime(credit['Date Closed'][card],'%Y-%m-%d')

for card in credit.index:
    if credit['Date Bonus Earned'][card]:
        continue
    else:
        credit['Date Bonus Earned'][card] = datetime.strptime(credit['Date Bonus Earned'][card],'%Y-%m-%d')
"""

for i in credit.index:
    if credit['Date Opened'][i] > (datetime.today() - timedelta(days=730)) and credit['Upgrade?'][i] == 'NO':
        y = credit['Date Opened'][i]
        print(i)
"""

credit['Date Opened'][0] > datetime.today() - timedelta(days=730)