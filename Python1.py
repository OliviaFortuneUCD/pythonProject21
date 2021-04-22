
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

dataset = sns.load_dataset('flights')

dataset.head()

data = dataset.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(data)