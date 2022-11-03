
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")

# # Create and save dataset
# from bioinfokit import analys
# result = analys.get_data('volcano').data
# result.to_csv('result.csv', index=False)

# (1) The first step is to make a data frame of the difference analysis result
# load dataset as pandas dataframe
result = pd.read_csv('result.csv')

result['log(pvalue)'] = -np.log10(result['p-value'])
result.rename(columns={'log2FC': 'FoldChange'}, inplace=True)
result.rename(columns={'p-value': 'pvalue'}, inplace=True)

# (2) Preparations for making volcano map in the second step
result['sig'] = 'normal'

result.loc[(result.FoldChange > 1) & (result.pvalue < 0.05), 'sig'] = 'up'
result.loc[(result.FoldChange < -1) & (result.pvalue < 0.05), 'sig'] = 'down'

# (3) Volcano plot
ax = sns.scatterplot(x="FoldChange", y="log(pvalue)",
                     hue='sig',
                     hue_order=('down', 'normal', 'up'),
                     palette=("#377EB8", "grey", "#E41A1C"),
                     data=result, linewidth=0)  # 'linewidth=0' removes dot edge color
ax.set_ylabel('-log(pvalue)', fontweight='bold')
ax.set_xlabel('log2FC', fontweight='bold')
