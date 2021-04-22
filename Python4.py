import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

dataset = sns.load_dataset('flights')

grids = sns.PairGrid(dataset)
grids.map_diag(sns.distplot)
grids.map_upper(sns.kdeplot)
grids.map_lower(plt.scatter)