import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mp

file = 'LED-PDMS interaction data'

# Describe the sheets within the .xlsx
dataInfo = [[1, 'White', 'black', 0.25, ''  ],
            [4, '625nm', 'white', 0.35, '\\'],
            [7, '660nm', 'black', 0.55, ''  ]]

# Make 3 formatted plots in the same row
fig, axes = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True)
kwargs = dict(histtype='stepfilled', density=False, bins=5, ec='k')

for i in range(3):
    axes[i].set_title(dataInfo[i][1])
    for j in range(3):
        sheet = 'Split' + str(dataInfo[i][0] + j)
        split = pd.read_excel(file + '.xlsx', sheet_name=sheet, usecols='E,R')
        picData = split[split['Image #']==1] # Take data for specified image
        data = picData['Measured Width']
        axes[i].hist(data.values.tolist(), **kwargs, color=dataInfo[j][2], alpha=dataInfo[j][3], hatch=dataInfo[j][4])

#fig.suptitle('LED-PDMS Interaction', fontsize=18)
axes[0].set_ylabel('Count')
axes[1].set_xlabel('Measured Pitch (microns)')

# Custom legend
legend = [mp.Patch(facecolor=dataInfo[0][2],alpha=dataInfo[0][3],hatch=dataInfo[0][4],label='No Stamp' ),
          mp.Patch(facecolor=dataInfo[1][2],alpha=dataInfo[1][3],hatch=dataInfo[1][4],label='Over Post'),
          mp.Patch(facecolor=dataInfo[2][2],alpha=dataInfo[2][3],hatch=dataInfo[2][4],label='Over Mesa')]

axes[1].legend(handles=legend, loc='upper center')

#plt.subplots_adjust(top=0.85)
plt.show()
