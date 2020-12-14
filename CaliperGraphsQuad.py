import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mp

file = 'No Stamp'
types =['625nm', '660nm', '730nm', 'White']

fig, axes = plt.subplots(nrows=1, ncols=4, sharex=True, sharey=True)

for i in range(4): # Iterate through plots
    data = pd.read_excel(file + '.xlsx')
    thisData = data[types[i]]
    axes[i].hist(thisData.values.tolist(),
                 density=False,
                 color='black',
                 alpha=0.75,
                 bins=5)
    axes[i].set_title(types[i])
    
fig.suptitle(file, fontsize=18)
fig.text(0.5, 0.02, 'Measured Pitch (microns)', ha='center')
fig.text(0.04, 0.5, 'Count', va='center', rotation='vertical')
plt.subplots_adjust(top=0.85)
plt.show()
