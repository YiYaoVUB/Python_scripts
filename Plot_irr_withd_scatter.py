import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io as scio

def set_plot_param():
    """Set my own customized plotting parameters"""

    mpl.rc('axes', edgecolor='black')
    mpl.rc('axes', labelcolor='dimgrey')
    mpl.rc('xtick', color='dimgrey')
    mpl.rc('xtick', labelsize=16)
    mpl.rc('ytick', color='dimgrey')
    mpl.rc('ytick', labelsize=16)
    mpl.rc('axes', titlesize=18)
    mpl.rc('axes', labelsize=16)
    mpl.rc('legend', fontsize='large')
    mpl.rc('text', color='dimgrey')

fig = plt.figure(figsize=[18,6], dpi=1000)
fig.subplots_adjust(hspace=0.2, wspace=0.3, left = 0.05, right = 0.95, top = 0.9, bottom = 0.2)

set_plot_param()

ax3 = plt.subplot(1, 3, 3)
ax3.text(0.01,1.02,'c',color='dimgrey',fontsize=14, transform=ax3.transAxes, weight = 'bold')


dataFile = 'E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\aquastat.mat'
data = scio.loadmat(dataFile)
data = data['Qirr_obs']
data = np.array(data)
plt.scatter(data[:,0], data[:,1],color = 'purple',label='CTL', alpha = 0.5)
#plt.scatter(data[:,0], data[:,2],color = 'yellow',label='IRR', alpha = 0.5)
plt.scatter(data[:,0], data[:,3],color = 'green',label='IRR_drai', alpha = 0.5)

plt.plot([0,70],[0,70], color = 'black', linewidth=1)
plt.ylabel('Simulated irrigation ($km^3/year$)')
plt.xlabel('Observed irrigation ($km^3/year$)')
plt.legend(loc='best',frameon=False, fontsize = 14)
plt.title('Other countries')


ax4 = plt.subplot(1, 3, 2)
ax4.text(0.01,1.02,'b',color='dimgrey',fontsize=14, transform=ax4.transAxes, weight = 'bold')
dataFile = 'E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\china.mat'
data = scio.loadmat(dataFile)
data = data['Qirr_obs']
data = np.array(data)
plt.scatter(data[:,0], data[:,1],color = 'purple',label='CTL', alpha = 0.5)
#plt.scatter(data[:,0], data[:,2],color = 'yellow',label='IRR', alpha = 0.5)
plt.scatter(data[:,0], data[:,3],color = 'green',label='IRR_drai', alpha = 0.5)

plt.plot([0,45],[0,45], color = 'black', linewidth=1)
plt.ylabel('Simulated irrigation ($km^3/year$)')
plt.xlabel('Observed irrigation ($km^3/year$)')
plt.legend(loc='best',frameon=False, fontsize = 14)
plt.title('China provinces')

ax5 = plt.subplot(1, 3, 1)
ax5.text(0.01,1.02,'a',color='dimgrey',fontsize=14, transform=ax5.transAxes, weight = 'bold')
dataFile = 'E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\usa.mat'
data = scio.loadmat(dataFile)
data = data['Qirr_obs']
data = np.array(data)
plt.scatter(data[:,0], data[:,1],color = 'purple',label='CTL', alpha = 0.5)
#plt.scatter(data[:,0], data[:,2],color = 'yellow',label='IRR', alpha = 0.5)
plt.scatter(data[:,0], data[:,3],color = 'green',label='IRR_drai', alpha = 0.5)

plt.plot([0,40],[0,40], color = 'black', linewidth=1)
plt.ylabel('Simulated irrigation ($km^3/year$)')
plt.xlabel('Observed irrigation ($km^3/year$)')
plt.legend(loc='best',frameon=False, fontsize = 14)
plt.title('USA states')
plt.savefig('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\7.png')

fig = plt.figure(figsize=[18,6], dpi=1000)
fig.subplots_adjust(hspace=0.2, wspace=0.3, left = 0.05, right = 0.95, top = 0.9, bottom = 0.2)

ax3 = plt.subplot(1, 3, 3)
ax3.text(0.01,1.02,'c',color='dimgrey',fontsize=14, transform=ax3.transAxes, weight = 'bold')
dataFile = 'E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\aquastat.mat'
data = scio.loadmat(dataFile)
data = data['Qirr_obs']
data = np.array(data)
plt.scatter(data[:,0], data[:,6],color = 'purple',label='CTL_limit', alpha = 0.5)
#plt.scatter(data[:,0], data[:,7],color = 'yellow',label='IRR_limit', alpha = 0.5)
plt.scatter(data[:,0], data[:,8],color = 'green',label='IRR_drai_limit', alpha = 0.5)

plt.plot([0,70],[0,70], color = 'black', linewidth=1)
plt.ylabel('Simulated irrigation ($km^3/year$)')
plt.xlabel('Observed irrigation ($km^3/year$)')
plt.legend(loc='best',frameon=False, fontsize = 14)
plt.title('Other countries')


ax4 = plt.subplot(1, 3, 2)
ax4.text(0.01,1.02,'b',color='dimgrey',fontsize=14, transform=ax4.transAxes, weight = 'bold')
dataFile = 'E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\china.mat'
data = scio.loadmat(dataFile)
data = data['Qirr_obs']
data = np.array(data)
plt.scatter(data[:,0], data[:,6],color = 'purple',label='CTL_limit', alpha = 0.5)
#plt.scatter(data[:,0], data[:,7],color = 'yellow',label='IRR_limit', alpha = 0.5)
plt.scatter(data[:,0], data[:,8],color = 'green',label='IRR_drai_limit', alpha = 0.5)
plt.plot([0,45],[0,45], color = 'black', linewidth=1)
plt.ylabel('Simulated irrigation ($km^3/year$)')
plt.xlabel('Observed irrigation ($km^3/year$)')
plt.legend(loc='best',frameon=False, fontsize = 14)
plt.title('China provinces')

ax5 = plt.subplot(1, 3, 1)
ax5.text(0.01,1.02,'a',color='dimgrey',fontsize=14, transform=ax5.transAxes, weight = 'bold')
dataFile = 'E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\usa.mat'
data = scio.loadmat(dataFile)
data = data['Qirr_obs']
data = np.array(data)
plt.scatter(data[:,0], data[:,6],color = 'purple',label='CTL_limit', alpha = 0.5)
#plt.scatter(data[:,0], data[:,7],color = 'yellow',label='IRR_limit', alpha = 0.5)
plt.scatter(data[:,0], data[:,8],color = 'green',label='IRR_drai_limit', alpha = 0.5)

plt.plot([0,40],[0,40], color = 'black', linewidth=1)
plt.ylabel('Simulated irrigation ($km^3/year$)')
plt.xlabel('Observed irrigation ($km^3/year$)')
plt.legend(loc='best',frameon=False, fontsize = 14)
plt.title('USA states')

#plt.show()
plt.savefig('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\71.png')