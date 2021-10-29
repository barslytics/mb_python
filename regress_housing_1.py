# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 16:08:16 2021

@author: muratb
"""
import pandas as pd
import numpy as np
import seaborn as sns
#import matplotlib.pyplot as plt
from statsmodels.formula.api import ols


taiwan_real_estate = pd.read_csv('C:\\Users\\muratb\\Desktop\\Ipekyol\\python\\Data_camp_files\\taiwan_real_estate2.csv')
#sns.scatterplot(x="n_convenience", y="price_twd_msq",data=taiwan_real_estate)
#plt.show()
mdl_price_vs_conv = ols("price_twd_msq~n_convenience", data=taiwan_real_estate)
# Fit the model
mdl_price_vs_conv = mdl_price_vs_conv.fit()
# Print the parameters of the fitted model
print(mdl_price_vs_conv.params)

sns.regplot(x=taiwan_real_estate["n_convenience"],y=taiwan_real_estate["price_twd_msq"],data =taiwan_real_estate,scatter =True)

#print(taiwan_real_estate)
