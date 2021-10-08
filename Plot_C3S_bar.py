import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # 绘图库

csvframe = pd.read_csv("E:\Data_Evaluation\Data_for_evaluation\Soil_Moisture\\bias.csv",header=None)
csvframe1 = pd.read_csv("E:\Data_Evaluation\Data_for_evaluation\Soil_Moisture\\rmse.csv",header=None)
array = np.array(csvframe)
array1 = np.array(csvframe1)

x = list(range(7))
y1 = []
Y1 = []
y2 = []
Y2 = []
y3 = []
Y3 = []
y4 = []
Y4 = []
y5 = []
y6 = []
y7 = []
for i in range(7):
    y1.append(float(array[i+1, 1]))
    Y1.append(float(array1[i+1, 1]))
    y2.append(float(array[i + 1,2]))
    Y2.append(float(array1[i + 1, 2]))
    y3.append(float(array[i + 1,3]))
    Y3.append(float(array1[i + 1, 3]))
    y4.append(float(array[i + 1,4]))
    Y4.append(float(array1[i + 1, 4]))


#fig = plt.figure(figsize=[8,8], dpi=100)
fig = plt.figure(figsize=[18,8], dpi=100)
ax1 = fig.add_subplot(1,2,1)
total_width, n = 0.8, 4
width = total_width / n
plt.bar(x, y1, width=width, label=array[0,1],fc = 'tomato')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, y2, width=width, label=array[0,2],fc = 'dodgerblue')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, y3, width=width, label=array[0,3],fc = 'chartreuse')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, y4, width=width, label=array[0,4],fc = 'orange')

plt.plot([-0.3,7],[0,0], color = 'black', linewidth=1)
plt.xticks([0.3, 1.3, 2.3, 3.3, 4.3, 5.3, 6.3], [r'GLO', r'WNA', r'NCA', r'MED', r'WCA', r'EAS', r'SAS'], fontsize=12)
plt.legend(loc='best')
plt.title('Bias (soil moisture)', fontsize=16)
plt.ylabel('Bias', fontsize=14)

ax1 = fig.add_subplot(1,2,2)
x = list(range(7))
total_width, n = 0.8, 4
width = total_width / n
plt.bar(x, Y1, width=width, label=array[0,1],fc = 'tomato')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, Y2, width=width, label=array[0,2],fc = 'dodgerblue')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, Y3, width=width, label=array[0,3],fc = 'chartreuse')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, Y4, width=width, label=array[0,4],fc = 'orange')
plt.plot([-0.3,7],[0,0], color = 'black', linewidth=1)
plt.xticks([0.3, 1.3, 2.3, 3.3, 4.3, 5.3, 6.3], [r'GLO', r'WNA', r'NCA', r'MED', r'WCA', r'EAS', r'SAS'], fontsize=12)
plt.legend(loc='best')
plt.title('RMSE (soil moisture)', fontsize=16)
plt.ylabel('RMSE', fontsize=14)

plt.show()
