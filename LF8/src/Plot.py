import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def plotTimeframe(csv):
    data_df = pd.read_csv(csv)
    plt.style.use('default')
    data_df.plot.bar(x = 'datetime', y = 'value')
    plt.show()

plotTimeframe(os.path.join('output','LF8ocupied harddrive space.csv'))