#!/usr/bin/env python
# coding: utf-8

"""
TODO
-translate notebook functions here
-add Citi, BoA, USBank application rules
-add points-to-cash conversion dictionary
-add rewards report by year
"""

# In[1]:


import numpy as np
import pandas as pd
from datetime import datetime
from datetime import date
from datetime import timedelta
import math


# In[2]:


credit = pd.ExcelFile('credit_cards.xlsx')
credit = credit.parse(index_col=0)
credit = credit.fillna(0)
today = datetime.now()

#format all date strings to datetime object for math
for card in credit.index:
    credit.loc[card,'Date Opened'] = datetime.strptime(credit.loc[card,'Date Opened'],'%Y-%m-%d')
    if credit.loc[card,'Date Closed'] == 0:
        continue
    else:
        credit.loc[card,'Date Closed'] = datetime.strptime(credit.loc[card,'Date Closed'],'%Y-%m-%d')
    if credit.loc[card,'Date Bonus Earned'] == 0:
        continue
    else:
        credit.loc[card,'Date Bonus Earned'] = datetime.strptime(credit.loc[card,'Date Bonus Earned'],'%Y-%m-%d')

#add month opened column for data sort purposes        
credit.insert(1,'Month Opened',credit['Date Opened'])
for card in credit.index:
    credit.loc[card,'Month Opened'] = credit.loc[card,'Date Opened'].month


# In[3]:


credit.head()


# In[ ]:





# In[4]:


def chase_5_24(dframe):
    cards = []
    open_dates = []
    for i in dframe.index:
        if dframe['Date Opened'][i] > (datetime.today() - timedelta(days=730)) and dframe['Product Change'][i] == 'NO'        and dframe['Business Card'][i] == 'NO':
            y1 = dframe['Date Opened'][i]
            y2 = i
            cards.append(y2)
            open_dates.append(y1)
    
    opened_cards = pd.DataFrame(open_dates,columns=['open dates'])
    opened_cards = opened_cards.sort_values(by='open dates',ascending=False)
    opened_cards = opened_cards.reset_index(drop=True)
    
    if len(opened_cards) < 5: 
        print('You are eligible to apply to a Chase card now.')
    else:
        new_card = opened_cards['open dates'][3] + timedelta(days=730)
        print('You will be eligible for a new Chase card on ' + new_card.day_name() + ' '           + new_card.month_name() + ' ' + str(new_card.day) + ' '+ str(new_card.year) + '.')
    
    print('You have opened the following cards in the past 24 months:')
    
    return cards

def annual_fees(dframe):
    dframe.sort_values(by="Month Opened",inplace=True)
    print('You have the following annual fees this year:')
    for card in dframe.index:
        #credit.loc[card,'Date Opened'] = datetime.strptime(credit.loc[card,'Date Opened'],'%Y-%m-%d')
        if dframe.loc[card,'Date Closed'] == 0 and dframe.loc[card,'Annual Fee'] != 0:
            print(str(dframe.loc[card,'Date Opened'].month) + '/' + str(dframe.loc[card,'Date Opened'].day)                  + ' ' + card + ' [$' + str(dframe.loc[card,'Annual Fee']) + ']')

    return


# In[5]:


annual_fees(credit)


# # amex credit card rules
# 
# 1. Once in a lifetime signup bonus - self explanatory
# 2. 5 card limit - only have 5 amex credit cards at once, charge cards do not count
# 3. 1 in 5 rule - only get approved for 1 credit card every 5 days, charge cards do not count
# 4. 2 in 90 rule - only get approved for 2 credit cards in 90 day window, charge cards do not count

# In[6]:


def annual_fees(dframe):
    dframe.sort_values(by="Date Opened",inplace=True)
    print('You have the following annual fees this year:')
    for card in dframe.index:
        #credit.loc[card,'Date Opened'] = datetime.strptime(credit.loc[card,'Date Opened'],'%Y-%m-%d')
        if dframe.loc[card,'Date Closed'] == 0 and dframe.loc[card,'Annual Fee'] != 0:
            print(str(dframe.loc[card,'Date Opened'].month) + '/' + str(dframe.loc[card,'Date Opened'].day)                  + ' ' + card + ' [$' + str(dframe.loc[card,'Annual Fee']) + ']')

    return


# In[7]:


chase_5_24(credit)


# In[16]:


credit.loc['AMEX Gold','Date Opened'].month


# In[ ]:


dframe = credit
cards = []
open_dates = []
for card in dframe.index:
    if dframe.loc[card,'Date Closed'] == 0 and dframe.loc[card,'Annual Fee'] != 0:
        y1 = card
        y2 = dframe.loc[card,'Date Opened']
        cards.append(y1)
        open_dates.append(y2)

opened_cards = pd.DataFrame(open_dates,columns=['open dates'])
opened_cards.insert(0,'Cards',cards)
opened_cards.insert(2,'open months',open_dates)
opened_cards = opened_cards.sort_values(by='open dates',ascending=False)
opened_cards = opened_cards.set_index('Cards')

for fee in opened_cards.index:
    print(opened_cards.loc[fee,'open dates'].month)


# In[ ]:





# In[68]:


dframe = credit
#dframe.sort_values(by=dframe['Date Opened'].month,inplace=True)
dframe.insert(1,'Month Opened',dframe['Date Opened'])
for card in dframe.index:
    dframe.loc[card,'Month Opened'] = dframe.loc[card,'Date Opened'].month


# In[ ]:





# In[69]:


dframe


# In[ ]:


# format dates for math using datetime.strptime


for card in credit.index:
    credit['Date Opened'][card] = datetime.strptime(credit['Date Opened'][card],'%Y-%m-%d')

for card in credit.index:
    if credit['Date Closed'][card] == 0:
        continue
    else:
        credit['Date Closed'][card] = datetime.strptime(credit['Date Closed'][card],'%Y-%m-%d')


for card in credit.index:
    if credit['Date Bonus Earned'][card] == 0:
        continue
    else:
        credit['Date Bonus Earned'][card] = datetime.strptime(credit['Date Bonus Earned'][card],'%Y-%m-%d')
        
# update the above to remove dataframe slice errors using .loc method
for card in credit.index:
    credit.loc[card,'Date Opened'] = datetime.strptime(credit.loc[card,'Date Opened'],'%Y-%m-%d')
    if credit.loc[card,'Date Closed'] == 0:
        continue
    else:
        credit.loc[card,'Date Closed'] = datetime.strptime(credit.loc[card,'Date Closed'],'%Y-%m-%d')
    if credit.loc[card,'Date Bonus Earned'] == 0:
        continue
    else:
        credit.loc[card,'Date Bonus Earned'] = datetime.strptime(credit.loc[card,'Date Bonus Earned'],'%Y-%m-%d')

