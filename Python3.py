import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

dataset = sns.load_dataset('flights')

dataset.head()


sns.pairplot(dataset)