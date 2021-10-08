import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio

fig = plt.figure(figsize=[12,5], dpi=100)
fig.subplots_adjust(hspace=0.2, wspace=0.3, left = 0.05, right = 0.95, top = 0.8, bottom = 0.2)
ax3 = plt.subplot(1, 3, 3)

dataFile = 'E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Aquastat.mat'
data = scio.loadmat(dataFile)
data = data['Qirr_obs']
data = np.array(data)
plt.scatter(data[:,0], data[:,1],color = 'green',label='IRR', alpha = 0.8)
plt.scatter(data[:,0], data[:,2],color = 'purple',label='CTL', alpha = 0.8)
#plt.scatter(data[:,0], data[:,3],color = 'orange',label='DU', alpha = 0.8)
plt.plot([0,70],[0,70], color = 'black', linewidth=1)
plt.ylabel('Simulated irrigation ($km^3/year$)')
plt.xlabel('Observed irrigation ($km^3/year$)')
plt.legend(loc='upper left')
plt.title('Other countries')


ax4 = plt.subplot(1, 3, 2)
dataFile = 'E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\\China.mat'
data = scio.loadmat(dataFile)
data = data['Qirr_obs']
data = np.array(data)
plt.scatter(data[0,:], data[1,:],color = 'green',label='IRR', alpha = 0.8)
plt.scatter(data[0,:], data[2,:],color = 'purple',label='CTL', alpha = 0.8)
#plt.scatter(data[0,:], data[3,:],color = 'orange',label='DU', alpha = 0.8)
plt.plot([0,30],[0,30], color = 'black', linewidth=1)
plt.ylabel('Simulated irrigation ($km^3/year$)')
plt.xlabel('Observed irrigation ($km^3/year$)')
plt.legend(loc='upper left')
plt.title('China provinces')

ax5 = plt.subplot(1, 3, 1)
dataFile = 'E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\\USA.mat'
data = scio.loadmat(dataFile)
data = data['Qirr_obs']
data = np.array(data)
plt.scatter(data[:,0], data[:,1],color = 'green',label='IRR', alpha = 0.8)
plt.scatter(data[:,0], data[:,2],color = 'purple',label='CTL', alpha = 0.8)
#plt.scatter(data[:,0], data[:,3],color = 'orange',label='DU', alpha = 0.8)
plt.plot([0,40],[0,40], color = 'black', linewidth=1)
plt.ylabel('Simulated irrigation ($km^3/year$)')
plt.xlabel('Observed irrigation ($km^3/year$)')
plt.legend(loc='upper left')
plt.title('USA states')

plt.show()
