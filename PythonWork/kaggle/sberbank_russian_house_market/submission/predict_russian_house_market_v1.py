#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd 
from numpy.polynomial.chebyshev import *
import matplotlib.pyplot as plt
import seaborn as sns


def monitor_time(func):

    @wraps(func)
    def calculate_time(*args, **kwargs ):
        start_time = time.time()
        result=func(*args, **kwargs)
        end_time=time.time()
        cost_time=end_time-start_time
        print(cost_time)
        return result

    return calculate_time

def load_data(file):

    df=pd.read_csv(file)
    return df

# ###### Service Read routines ###
# def condition_train(value, col):
#     vals = (macro_df[macro_df['mo_ye'] == value])
    
#     ret = vals[col].asobject
  
#     ret = ret[0]

#     return ret

# def condition_test(value, col):
#     vals = (macro[macro['mo_ye'] == value])

#     ret = vals[col].asobject

#     ret = ret[0]

#     return ret

# def condition(value,col):
#     vals = (macro_df[macro_df['timestamp'] == value])
#     ret=vals[col].asobject
#     ret=ret[0]

#     return ret

# def init_anlz_file(train_df, read_columns):

#     anlz_df = train_df
#     for clmn in read_columns:
#         if clmn == 'timestamp':
#             continue
#         anlz_df[clmn] = np.nan
#         anlz_df[clmn] = anlz_df['timestamp'].apply(condition, col=clmn)
#         print(clmn)
#     return anlz_df



def main():
    train=load_data('../input/train.csv')
    print train.head(5)
    print train.shape
    print ('************************')
    print train.describe()
    print pd.isnull(train).any()
    print train.mean()

    read_columns= ['timestamp', 'oil_urals', 'gdp_quart_growth', 'cpi', 'usdrub', \
                'salary_growth', 'unemployment', 'average_provision_of_build_contract_moscow', 'mortgage_rate', \
                 'deposits_rate','deposits_growth','rent_price_3room_eco',\
                 'rent_price_3room_bus']

    train_df = pd.read_csv("../input/train.csv",usecols=['timestamp','price_doc','full_sq'])
    macro_df = pd.read_csv("../input/macro.csv",usecols=read_columns)

    ###### Service Read routines ###
    def condition_train(value, col):
        vals = (macro_df[macro_df['mo_ye'] == value])
        
        ret = vals[col].asobject
      
        ret = ret[0]

        return ret

    def condition_test(value, col):
        vals = (macro[macro['mo_ye'] == value])

        ret = vals[col].asobject

        ret = ret[0]

        return ret

    def condition(value,col):
        vals = (macro_df[macro_df['timestamp'] == value])
        ret=vals[col].asobject
        ret=ret[0]

        return ret

    def init_anlz_file(train_df, read_columns):

        anlz_df = train_df
        for clmn in read_columns:
            if clmn == 'timestamp':
                continue
            anlz_df[clmn] = np.nan
            anlz_df[clmn] = anlz_df['timestamp'].apply(condition, col=clmn)
            print(clmn)
        return anlz_df

    print ('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    ### Read Data for macro analysis
    anlz_df=init_anlz_file(train_df, read_columns)


    methods=['pearson', 'kendall', 'spearman']
    def plot_grouped_trends(df,feat1,feat2,corr_df):
       
        fig, ax = plt.subplots(1, 2, figsize=(10, 5))
        x=df.index.values
        ch=chebfit(x,df[feat1].values,7)
        trendf1=chebval(x,ch)
        ax[0].plot(x,df[feat1].values,x,trendf1)
        ax[0].set_ylabel(feat1)
        ax[0].set_title('Chart '+feat1+' vs trend' )
        ax[0].set_xlabel('months count')
        ch2=chebfit(x,df[feat2].values,7)
        trendf2=chebval(x,ch2)
        ax[1].plot(x,df[feat2].values,x,trendf2)
        ax[1].set_ylabel(feat2)
        ax[1].set_title('Chart '+feat2+' vs trend' )
        ax[1].set_xlabel('months count')
        ##### do here two charts density distribition
        
        ls=[feat2]
        for method in methods:
            corr=df[[feat1,feat2]].corr(method=method)
            ls.append(corr[feat1][1])
        corr_df.loc[len(corr_df)]=ls


    anlz_df['timestamp']=pd.to_datetime(anlz_df['timestamp'])
    anlz_df['mo_ye']=anlz_df['timestamp'].apply(lambda x: x.strftime('%m-%Y'))
    anlz_df['price_per_sqm']=anlz_df['price_doc']/anlz_df['full_sq']


    macro_columns = ['price_doc','price_per_sqm','full_sq','oil_urals', 'gdp_quart_growth', 'cpi', 'usdrub', \
                    'salary_growth', 'unemployment', 'average_provision_of_build_contract_moscow', 'mortgage_rate', \
                     'deposits_rate','deposits_growth','rent_price_3room_eco',\
                     'rent_price_3room_bus']
    macro_df=pd.DataFrame(anlz_df.groupby('mo_ye')[macro_columns].mean())
    macro_df.reset_index(inplace=True)


    macro_df['mo_ye']=pd.to_datetime(macro_df['mo_ye'])
    macro_df=macro_df.sort_values(by='mo_ye')


    macro_df.reset_index(inplace=True)
    macro_df.drop(['index'],axis=1,inplace=True)


    corr_df=pd.DataFrame(columns=['feature','pearson', 'kendall', 'spearman'])
    corr=macro_df[macro_columns].corr(method='spearman')
    fig, ax = plt.subplots(figsize=(10,10))         # Sample figsize in inches
    sns.heatmap(corr, annot=True, linewidths=.5, ax=ax)


    for feat in macro_columns:
        if (feat=='price_doc'):
            continue
            plot_grouped_trends(macro_df,'price_doc',feat,corr_df)

        print(corr_df)

    sig_macro_columns=['oil_urals', 'gdp_quart_growth', 'cpi', 'usdrub', \
                'salary_growth', 'unemployment', 'mortgage_rate', \
                 'deposits_rate','rent_price_3room_bus']


if __name__=="__main__":
    main()