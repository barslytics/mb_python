# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 00:20:38 2021

@author: muratb
"""

import pandas as pd
import numpy as np
import seaborn as sns
#import matplotlib.pyplot as plt
from statsmodels.formula.api import ols


taiwan_real_estate = pd.read_csv('C:\\Users\\muratb\\Desktop\\Ipekyol\\python\\Data_camp_files\\taiwan_real_estate2.csv')
# Histograms of price_twd_msq with 10 bins, split by the age of each house
sns.displot(data=taiwan_real_estate,
         x="price_twd_msq",
         col="house_age_years",
         col_wrap=3,
         bins=10)
# Show the plot