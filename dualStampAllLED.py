import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mp

file = 'LED'

##types =[['ContactPost', 'NoStampPost'],
##        ['625nm', '660nm', '730nm', 'White'],
##        ['black', 'black', 'black', 'white'],
##        [0.25, 0.35, 0.45, 0.55],
##        ['/', '', '', '\\'],
##        ['Stamp Post in Contact', 'Control']]

types =[['100umMesa', 'NoStampMesa'],
        ['625nm', '660nm', '730nm', 'White'],
        ['black', 'black', 'black', 'white'],
        [0.25, 0.35, 0.45, 0.55],
        ['/', '', '', '\\'],
        ['Stamp Mesa at 100 microns', 'Control']]

order = [0, 1, 3]
legendItems = []

fig, axes = plt.subplots(nrows=1, ncols=2, sharex=True, sharey=True)

for j in range(2):
    axes[j].set_title(types[5][j])
    for i in order: # Iterate through plots
        legendItems.append(types[1][i])
        data = pd.read_excel(file + '.xlsx', sheet_name=types[0][j])
        thisData = data[types[1][i]]
        axes[j].hist(thisData.values.tolist(),
                     color=types[2][i],
                     alpha=types[3][i],
                     hatch=types[4][i],
                     histtype='stepfilled',
                     density=False,
                     bins=3,
                     ec='k')


fig.text(0.5, 0.02, 'Measured Pitch (microns)', ha='center')
fig.text(0.04, 0.5, 'Count', va='center', rotation='vertical')

plt.legend(legendItems, loc='upper center');
plt.show()
