#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import date
from datetime import timedelta
import math
import os
import sys

os.system('python main_gui.py')

# In[2]:

points_value = {'CASH':1.0, 'UR (Chase)':0.02, 'MR (AMEX)':0.02, 'AMZN (Amazon)':1.0,
                'RR (Southwest)':0.015, 'VR (CapOne)':0.017, 'COST (Costco)':1.0, 'TY (Citi)':0.017,
                'SKY (Delta)':0.011, 'HH (Hilton)':0.006, 'IHG':0.005, 'AA':0.014,
                'AM':0.018, 'MB':0.008, 'BTC':40000}

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
            print(str(due_date.month) + '/' + str(due_date.day) + ' ' + dframe.loc[card,'Card Name'] + ' [$' + str(dframe.loc[card,'Annual Fee']) + ']')

    return

def points_performance(credit_df, today):
    
    bins = np.arange(today.year-4,today.year+1)
    to_drop = ['Issuer', 'Month Opened','Date Opened', 'Date Closed', 'Product Change',
           'Business Card','Annual Fee']
    year_cutoff = today.year-4

    points_df = credit_df
    points_df.drop(credit_df[credit_df['Year Bonus Earned']<year_cutoff].index,inplace=True)
    points_df.drop(columns=to_drop,inplace=True)
    
    points_earned = pd.DataFrame()
    for year in bins:
        points_earned[year] = points_df.loc[points_df['Year Bonus Earned']==year,['Points Value']].sum()

    points_earned = points_earned.transpose()
    points_earned.plot(kind='bar')
    plt.title("Credit Card Rewards Performance")
    plt.ylabel("Points Value Earned ($)")
# In[3]:

path = os.path.abspath(os.path.dirname(__file__))

if os.path.isfile(path+'/gui_output.xlsx'):
    credit = pd.ExcelFile('gui_output.xlsx')
    credit = credit.parse(index_col=0)
    credit = credit.fillna(0)
    
else:
    credit = pd.ExcelFile('credit_cards.xlsx')
    credit = credit.parse()
    #credit = credit.parse(index_col=0)
    credit = credit.fillna(0)

today = datetime.now()
# blank_date = str(date.today() - timedelta(365*5))
blank_date = datetime(1970, 1, 1)

credit.replace(to_replace='YYYY-MM-DD',value=blank_date,inplace=True)
credit.replace(to_replace='XXXXX',value=0,inplace=True)
credit.replace(to_replace='e.g. 0, 95',value=0,inplace=True)


# In[7]:

for card in credit.index:
    # clean data coming from gui output
    try:
        credit.loc[card,'Bonus Earned'] = int(credit.loc[card,'Bonus Earned'])
    except:
        credit.loc[card,'Bonus Earned'] = 0
    
    try:
        credit.loc[card,'Annual Fee'] = int(credit.loc[card,'Annual Fee'])
    except:
        credit.loc[card,'Annual Fee'] = 0
    
    #format all date strings to datetime object for math
    credit.loc[card,'Date Opened'] = datetime.strptime(credit.loc[card,'Date Opened'],'%Y-%m-%d')
    
    if credit.loc[card,'Date Closed'] == 0:
        pass
    else:
        credit.loc[card,'Date Closed'] = datetime.strptime(credit.loc[card,'Date Closed'],'%Y-%m-%d')
    
    if credit.loc[card,'Date Bonus Earned'] == 0:
        #continue
        credit.loc[card,'Date Bonus Earned'] = blank_date
    else:
        credit.loc[card,'Date Bonus Earned'] = datetime.strptime(credit.loc[card,'Date Bonus Earned'],'%Y-%m-%d')




# In[ ]:
#add month opened column for data sort purposes        

credit.insert(2,'Month Opened',credit['Date Opened'])
credit.insert(7,'Year Bonus Earned',credit['Date Bonus Earned'])
for card in credit.index:
    credit.loc[card,'Month Opened'] = credit.loc[card,'Date Opened'].month
    
    if credit.loc[card,'Date Bonus Earned'] == 0:
        credit.loc[card,'Year Bonus Earned'] = blank_date.year
    else:
        credit.loc[card,'Year Bonus Earned'] = credit.loc[card,'Date Bonus Earned'].year

#add points value column
credit['Points Value'] = 0
for card in credit.index:
    credit.loc[card, 'Points Value'] = credit.loc[card, 'Bonus Earned'] * points_value[credit.loc[card, 'Points Currency']]



# In[4]:

points_performance(credit, today)




# In[5]:



# In[6]:



# In[16]:




# In[ ]:



# In[ ]:


# In[68]:


# In[ ]:

bins = np.arange(today.year-4,today.year+1)

to_drop = ['Issuer', 'Month Opened','Date Opened', 'Date Closed', 'Product Change',
           'Business Card','Annual Fee']

year_cutoff = today.year-4

points_df = credit
points_df.drop(credit[credit['Year Bonus Earned']<year_cutoff].index,inplace=True)
points_df.drop(columns=to_drop,inplace=True)






# In[69]:

points_df.loc[points_df['Year Bonus Earned']==2018,'Bonus Earned'].sum()



# In[ ]:
points_earned = pd.DataFrame()

for year in bins:
    points_earned[year] = points_df.loc[points_df['Year Bonus Earned']==year,['Points Value']].sum()



# %%
points_earned = points_earned.transpose()
points_earned.plot(kind='bar')
plt.title("Credit Card Rewards Performance")
plt.ylabel("Points Value Earned ($)")
# %%




    
# %%

# %%
