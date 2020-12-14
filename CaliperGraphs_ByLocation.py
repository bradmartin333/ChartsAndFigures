import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mp

file = 'LED-PDMS interaction data'

# Describe the sheets within the .xlsx
dataInfo = [[1, 'No Stamp',  'black', 0.25, ''  ],
            [4, 'Over Post', 'white', 0.35, '\\'],
            [7, 'Over Mesa', 'black', 0.55, ''  ]]

# Make 3 formatted plots in the same row
fig, axes = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True)
kwargs = dict(histtype='stepfilled', density=False, bins=5, ec='k')

for i in range(3): # Iterate through plots
    axes[i].set_title(dataInfo[i][1])
    for j in range(3): # Iterate through LEDs
        sheet = 'Split' + str(dataInfo[i][0] + j)
        split = pd.read_excel(file + '.xlsx', sheet_name=sheet, usecols='E,R')
        picData = split[split['Image #']==1] # Take data for specified image
        data = picData['Measured Width']
        axes[j].hist(data.values.tolist(), **kwargs, color=dataInfo[i][2], alpha=dataInfo[i][3], hatch=dataInfo[i][4])

#fig.suptitle('LED-PDMS Interaction', fontsize=18)
axes[0].set_ylabel('Count')
axes[1].set_xlabel('Measured Pitch (microns)')

# Custom legend
legend = [mp.Patch(facecolor=dataInfo[0][2],alpha=dataInfo[0][3],hatch=dataInfo[0][4],label='White'),
          mp.Patch(facecolor=dataInfo[1][2],alpha=dataInfo[1][3],hatch=dataInfo[1][4],label='625nm'),
          mp.Patch(facecolor=dataInfo[2][2],alpha=dataInfo[2][3],hatch=dataInfo[2][4],label='660nm')]

axes[1].legend(handles=legend, loc='upper center')

#plt.subplots_adjust(top=0.85)
plt.show()
