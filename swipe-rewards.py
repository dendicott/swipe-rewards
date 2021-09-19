#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from datetime import datetime
from datetime import date
from datetime import timedelta
import math
import os

os.system('python main_gui.py')

# In[2]:


#credit = pd.ExcelFile('credit_cards.xlsx')
credit = pd.ExcelFile('credit_cards_test.xlsx')
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

#add points value column
credit['Points Value'] = 0
for card in credit.index:
    credit.loc[card, 'Points Value'] = credit.loc[card, 'Bonus Earned'] * points_value[credit.loc[card, 'Points Currency']]

# In[3]:


credit.head()


# In[ ]:


points_value = {'CASH':1.0, 'UR':0.02, 'MR':0.02, 'AMZN':1.0,
                'SW':0.015, 'VR':0.017, 'COSTCO':1.0, 'TY':0.017,
                'SKY':0.011, 'HH':0.006, 'IHG':0.005, 'AA':0.014,
                'AM':0.018, 'MB':0.008, 'BTC':30000}


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

def amex_2_90(dframe):
    """Amex 2 in 90 says that you cannot be approved for more than 2
    credit cards in the past 90 days.

    Args:
        dframe (pandas dataframe): credit dataframe built from GUI or excel file

    Returns:
        cards: list of cards you've applied for in the last 90 days
        amex_2_90_flag: boolean flag to identify whether you violate 2 in 90 or not
        amex_2_90_message: string fed to rollup function to identify which rule you are violating
    """
    cards = []
    open_dates = []
    amex_2_90_flag = 0
    amex_2_90_message = 'AMEX 2 in 90 calculation error'
    for i in dframe.index:
        if dframe['Date Opened'][i] > (datetime.today() - timedelta(days=90)) and dframe['Product Change'][i] == 'NO' and dframe['Business Card'][i] == 'NO':
            y1 = dframe['Date Opened'][i]
            y2 = i
            cards.append(y2)
            open_dates.append(y1)
    
    opened_cards = pd.DataFrame(open_dates,columns=['open dates'])
    opened_cards = opened_cards.sort_values(by='open dates',ascending=False)
    opened_cards = opened_cards.reset_index(drop=True)
    
    if len(opened_cards) < 2:
        amex_2_90_flag = 1
        amex_2_90_message = 'Per AMEX 2 in 90 you are eligible to apply to a American Express card now.'
    else:
        new_card = opened_cards['open dates'][1] + timedelta(days=90)
        amex_2_90_message = 'you will be eligible for a new American Express card on ' + new_card.day_name() + ' ' + new_card.month_name() + ' ' + str(new_card.day) + ' '+ str(new_card.year) + '.'
    
    #print('You have opened the following cards in the past 90 days:')
    
    return cards, amex_2_90_flag, amex_2_90_message

def amex_1_5(dframe):
    """AMEX 1 in 5 says that you cannot apply for more than 1 card in a 5 day period

    Args:
        dframe (pandas dataframe): credit dataframe built from GUI or excel file

    Returns:
        cards: list of cards you've applied for in the last 5 days
        amex_1_5_flag: boolean flag to identify whether you violate 1 in 5 or not
        amex_1_5_message: string fed to rollup function to identify which rule you are violating
    """
    cards = []
    open_dates = []
    amex_1_5_flag = 0
    amex_1_5_message = 'AMEX 1 in 5 calculation error'
    for i in dframe.index:
        if dframe['Date Opened'][i] > (datetime.today() - timedelta(days=5)) and dframe['Product Change'][i] == 'NO' and dframe['Business Card'][i] == 'NO':
            y1 = dframe['Date Opened'][i]
            y2 = i
            cards.append(y2)
            open_dates.append(y1)
    
    opened_cards = pd.DataFrame(open_dates,columns=['open dates'])
    opened_cards = opened_cards.sort_values(by='open dates',ascending=False)
    opened_cards = opened_cards.reset_index(drop=True)
    
    if len(opened_cards) < 1:
        amex_1_5_flag = 1
        amex_1_5_message = 'Per AMEX 1 in 5 you are eligible to apply to a American Express card now.'
    else:
        new_card = opened_cards['open dates'][0] + timedelta(days=5)
        amex_1_5_message = 'you will be eligible for a new American Express card on ' + new_card.day_name() + ' ' + new_card.month_name() + ' ' + str(new_card.day) + ' '+ str(new_card.year) + '.'
    
    #print('You have opened the following cards in the past 5 days:')
    
    return cards, amex_1_5_flag, amex_1_5_message

def amex_rule_rollup(dframe):
    """Rollup fucntion for american express rules

    Args:
        credit ([type]): [description]
    """
    amex_message = "Error caculating AMEX eligibility rules."
    
    amex_2_90_list = amex_2_90(dframe)[0]
    amex_2_90_flag = amex_2_90(dframe)[1]
    amex_2_90_message = amex_2_90(dframe)[2]
    amex_1_5_list = amex_1_5(dframe)[0]
    amex_1_5_flag = amex_1_5(dframe)[1]
    amex_1_5_message = amex_1_5(dframe)[2]
    
    if amex_1_5_flag == 1 and amex_2_90_flag == 1:
        amex_message = "You are eligible for an American Express card now."
    
    elif amex_1_5_flag == 1 and amex_2_90_flag == 0:
        amex_message = 'Per the 2 in 90 Rule, ' + amex_2_90_message
    
    elif amex_1_5_flag == 0 and amex_2_90_flag == 1:
        amex_message = 'Per the 1 in 5 Rule, ' + amex_1_5_message
    
    else:
        amex_message = 'Per the 1 in 5 Rule, ' + amex_1_5_message + ' Per the 2 in 90 Rule, ' + amex_2_90_message
    
    return amex_message

def annual_fees(dframe):
    dframe.sort_values(by="Month Opened",inplace=True)
    print('You have the following annual fees this year:')
    for card in dframe.index:
        #credit.loc[card,'Date Opened'] = datetime.strptime(credit.loc[card,'Date Opened'],'%Y-%m-%d')
        if dframe.loc[card,'Date Closed'] == 0 and dframe.loc[card,'Annual Fee'] != 0:
            due_date = dframe.loc[card,'Date Opened'] + timedelta(days=30)
            #print(str(dframe.loc[card,'Date Opened'].month) + '/' + str(dframe.loc[card,'Date Opened'].day) + ' ' + card + ' [$' + str(dframe.loc[card,'Annual Fee']) + ']')
            print(str(due_date.month) + '/' + str(due_date.day) + ' ' + card + ' [$' + str(dframe.loc[card,'Annual Fee']) + ']')

    return


# In[5]:



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




# In[16]:

def amex_2_90(dframe):
    """Amex 2 in 90 says that you cannot be approved for more than 2
    credit cards in the past 90 days.

    Args:
        dframe (pandas dataframe): credit dataframe built from GUI or excel file

    Returns:
        cards: list of cards you've applied for in the last 90 days
        amex_2_90_flag: boolean flag to identify whether you violate 2 in 90 or not
        amex_2_90_message: string fed to rollup function to identify which rule you are violating
    """
    cards = []
    open_dates = []
    amex_2_90_flag = 0
    amex_2_90_message = 'AMEX 2 in 90 calculation error'
    for i in dframe.index:
        if dframe['Date Opened'][i] > (datetime.today() - timedelta(days=90)) and dframe['Product Change'][i] == 'NO' and dframe['Business Card'][i] == 'NO':
            y1 = dframe['Date Opened'][i]
            y2 = i
            cards.append(y2)
            open_dates.append(y1)
    
    opened_cards = pd.DataFrame(open_dates,columns=['open dates'])
    opened_cards = opened_cards.sort_values(by='open dates',ascending=False)
    opened_cards = opened_cards.reset_index(drop=True)
    
    if len(opened_cards) < 2:
        amex_2_90_flag = 1
        amex_2_90_message = 'Per AMEX 2 in 90 you are eligible to apply to a American Express card now.'
    else:
        new_card = opened_cards['open dates'][1] + timedelta(days=90)
        amex_2_90_message = 'you will be eligible for a new American Express card on ' + new_card.day_name() + ' ' + new_card.month_name() + ' ' + str(new_card.day) + ' '+ str(new_card.year) + '.'
    
    #print('You have opened the following cards in the past 90 days:')
    
    return cards, amex_2_90_flag, amex_2_90_message


def amex_1_5(dframe):
    """AMEX 1 in 5 says that you cannot apply for more than 1 card in a 5 day period

    Args:
        dframe (pandas dataframe): credit dataframe built from GUI or excel file

    Returns:
        cards: list of cards you've applied for in the last 5 days
        amex_1_5_flag: boolean flag to identify whether you violate 1 in 5 or not
        amex_1_5_message: string fed to rollup function to identify which rule you are violating
    """
    cards = []
    open_dates = []
    amex_1_5_flag = 0
    amex_1_5_message = 'AMEX 1 in 5 calculation error'
    for i in dframe.index:
        if dframe['Date Opened'][i] > (datetime.today() - timedelta(days=5)) and dframe['Product Change'][i] == 'NO' and dframe['Business Card'][i] == 'NO':
            y1 = dframe['Date Opened'][i]
            y2 = i
            cards.append(y2)
            open_dates.append(y1)
    
    opened_cards = pd.DataFrame(open_dates,columns=['open dates'])
    opened_cards = opened_cards.sort_values(by='open dates',ascending=False)
    opened_cards = opened_cards.reset_index(drop=True)
    
    if len(opened_cards) < 1:
        amex_1_5_flag = 1
        amex_1_5_message = 'Per AMEX 1 in 5 you are eligible to apply to a American Express card now.'
    else:
        new_card = opened_cards['open dates'][0] + timedelta(days=5)
        amex_1_5_message = 'you will be eligible for a new American Express card on ' + new_card.day_name() + ' ' + new_card.month_name() + ' ' + str(new_card.day) + ' '+ str(new_card.year) + '.'
    
    #print('You have opened the following cards in the past 5 days:')
    
    return cards, amex_1_5_flag, amex_1_5_message

def amex_rule_rollup(dframe):
    """Rollup fucntion for american express rules

    Args:
        credit ([type]): [description]
    """
    amex_message = "Error caculating AMEX eligibility rules."
    
    amex_2_90_list = amex_2_90(dframe)[0]
    amex_2_90_flag = amex_2_90(dframe)[1]
    amex_2_90_message = amex_2_90(dframe)[2]
    amex_1_5_list = amex_1_5(dframe)[0]
    amex_1_5_flag = amex_1_5(dframe)[1]
    amex_1_5_message = amex_1_5(dframe)[2]
    
    if amex_1_5_flag == 1 and amex_2_90_flag == 1:
        amex_message = "You are eligible for an American Express card now."
    
    elif amex_1_5_flag == 1 and amex_2_90_flag == 0:
        amex_message = 'Per the 2 in 90 Rule, ' + amex_2_90_message
    
    elif amex_1_5_flag == 0 and amex_2_90_flag == 1:
        amex_message = 'Per the 1 in 5 Rule, ' + amex_1_5_message
    
    else:
        amex_message = 'Per the 1 in 5 Rule, ' + amex_1_5_message + ' Per the 2 in 90 Rule, ' + amex_2_90_message
    
    return amex_message

# In[ ]:

#amex_1_5(credit)
amex_rule_rollup(credit)



# In[ ]:


# In[68]:


# In[ ]:




# In[69]:




# In[ ]:

