import pandas as pd
import numpy as np
import statistics as st

import matplotlib.pyplot as plt
import seaborn as sns

import statsmodels.api as sm

df = pd.read_csv('forestfires.csv')
df.info()
df.head()
