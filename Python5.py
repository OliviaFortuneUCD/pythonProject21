import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

dataset = sns.load_dataset('diamonds')

dataset.head()

sns.lmplot(x='carat', y='price', data=dataset)