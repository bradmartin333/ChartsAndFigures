import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mp

file = 'LED'
variable = 'White'
types =[['ContactPost', 'NoStampPost', '100umMesa', 'NoStampMesa'],
        ['black', 'black', 'black', 'white'],
        [0.25, 0.35, 0.45, 0.55],
        ['/', '', '', '\\']]

fig = plt.figure()
ax = fig.add_subplot(111)

for i in range(4): # Iterate through plots
    data = pd.read_excel(file + '.xlsx', sheet_name=types[0][i])
    thisData = data[variable]
    ax.hist(thisData.values.tolist(),
            color=types[1][i],
            alpha=types[2][i],
            hatch=types[3][i],
            histtype='stepfilled',
            density=True,
            bins=3,
            ec='k')
ax.set_title(variable)
ax.set_ylabel('Density')
ax.set_xlabel('Measured Pitch (microns)')
plt.legend(types[0], loc='upper left');
plt.show()
