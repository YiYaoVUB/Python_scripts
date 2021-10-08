import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

f = plt.figure(figsize = (16, 8), dpi=1000)  # initiate the figure

f.subplots_adjust(hspace=0.4, wspace=0.4, left = 0.1, right = 0.9, top = 0.95, bottom = 0.1)
plt.title('Relative changes of runoff-limited simulations')

ax1 = plt.subplot(2, 5, 1)
ax1.text(-0.2,1.05,'(a)',color='black',fontsize=14, transform=ax1.transAxes, weight = 'bold')
ax1.text(-0.7,1.05,'Bias',color='black',fontsize=16, transform=ax1.transAxes, weight = 'bold')
bias = np.loadtxt(open("E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\Castellaro_Bias.csv","rb"), delimiter=",",skiprows=0)
bias_plot = np.zeros((5,3))
bias_plot[:,0] = (bias[:,1] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,1] = (bias[:,2] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,2] = (bias[:,2] - bias[:,1]) / (bias[:,1]) * 100
colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']
cmap_bias = mpl.colors.ListedColormap(colors)
bounds = [-5, -2, -1, -0.001, 0.001, 1, 2, 5]
norm_bias = mpl.colors.BoundaryNorm(bounds,cmap_bias.N,extend='both')
im = ax1.imshow(bias_plot,cmap = cmap_bias, norm= norm_bias)
simulations = ["CTL-NOI", "IRR-NOI", "IRR-CTL"]
variables = ['LHF', 'SHF', 'NEE', 'SWup', 'SM']
# We want to show all ticks...
ax1.set_xticks(np.arange(len(simulations)))
ax1.set_yticks(np.arange(len(variables)))
# ... and label them with the respective list entries
ax1.set_xticklabels(simulations, rotation=-45,fontsize=12)
ax1.set_yticklabels(variables,fontsize=12)
ax1.set_title('Castellaro',fontsize=14)
#cbar = ax1.figure.colorbar(im, ax=ax1, cmap=cmap_bias)
#cbar.ax.set_ylabel('Relative change (%)', rotation=-90, va="bottom")

ax1 = plt.subplot(2, 5, 6)
ax1.text(-0.2,1.05,'(f)',color='black',fontsize=14, transform=ax1.transAxes, weight = 'bold')
ax1.text(-0.7,1.05,'RMSE',color='black',fontsize=16, transform=ax1.transAxes, weight = 'bold')
bias = np.loadtxt(open("E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\Castellaro_Rmse.csv","rb"), delimiter=",",skiprows=0)
bias_plot = np.zeros((5,3))
bias_plot[:,0] = (bias[:,1] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,1] = (bias[:,2] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,2] = (bias[:,2] - bias[:,1]) / (bias[:,1]) * 100
colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']
cmap_bias = mpl.colors.ListedColormap(colors)
bounds = [-5, -2, -1, -0.001, 0.001, 1, 2, 5]
norm_bias = mpl.colors.BoundaryNorm(bounds,cmap_bias.N,extend='both')
im = ax1.imshow(bias_plot,cmap = cmap_bias, norm= norm_bias)
simulations = ["CTL-NOI", "IRR-NOI", "IRR-CTL"]
variables = ['LHF', 'SHF', 'NEE', 'SWup', 'SM']
# We want to show all ticks...
ax1.set_xticks(np.arange(len(simulations)))
ax1.set_yticks(np.arange(len(variables)))
# ... and label them with the respective list entries
ax1.set_xticklabels(simulations, rotation=-45,fontsize=12)
ax1.set_yticklabels(variables,fontsize=12)
ax1.set_title('Castellaro',fontsize=14)
#cbar = ax1.figure.colorbar(im, ax=ax1, cmap=cmap_bias)
#cbar.ax.set_ylabel('Relative change (%)', rotation=-90, va="bottom")


ax1 = plt.subplot(2, 5, 2)
ax1.text(-0.2,1.05,'(b)',color='black',fontsize=14, transform=ax1.transAxes, weight = 'bold')
bias = np.loadtxt(open("E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\Cheorwon_Bias.csv","rb"), delimiter=",",skiprows=0)
bias_plot = np.zeros((5,3))
bias_plot[:,0] = (bias[:,1] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,1] = (bias[:,2] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,2] = (bias[:,2] - bias[:,1]) / (bias[:,1]) * 100
colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']
cmap_bias = mpl.colors.ListedColormap(colors)
bounds = [-5, -2, -1, -0.001, 0.001, 1, 2, 5]
norm_bias = mpl.colors.BoundaryNorm(bounds,cmap_bias.N,extend='both')
im = ax1.imshow(bias_plot,cmap = cmap_bias, norm= norm_bias)
simulations = ["CTL-NOI", "IRR-NOI", "IRR-CTL"]
variables = ['LHF', 'SHF', 'NEE', 'SWup', 'LWup']
# We want to show all ticks...
ax1.set_xticks(np.arange(len(simulations)))
ax1.set_yticks(np.arange(len(variables)))
# ... and label them with the respective list entries
ax1.set_xticklabels(simulations, rotation=-45,fontsize=12)
ax1.set_yticklabels(variables,fontsize=12)
ax1.set_title('Cheorwon',fontsize=14)
#cbar = ax1.figure.colorbar(im, ax=ax1, cmap=cmap_bias)
#cbar.ax.set_ylabel('Relative change (%)', rotation=-90, va="bottom")

ax1 = plt.subplot(2, 5, 7)
ax1.text(-0.2,1.05,'(g)',color='black',fontsize=14, transform=ax1.transAxes, weight = 'bold')
bias = np.loadtxt(open("E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\Cheorwon_Rmse.csv","rb"), delimiter=",",skiprows=0)
bias_plot = np.zeros((5,3))
bias_plot[:,0] = (bias[:,1] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,1] = (bias[:,2] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,2] = (bias[:,2] - bias[:,1]) / (bias[:,1]) * 100
colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']
cmap_bias = mpl.colors.ListedColormap(colors)
bounds = [-5, -2, -1, -0.001, 0.001, 1, 2, 5]
norm_bias = mpl.colors.BoundaryNorm(bounds,cmap_bias.N,extend='both')
im = ax1.imshow(bias_plot,cmap = cmap_bias, norm= norm_bias)
simulations = ["CTL-NOI", "IRR-NOI", "IRR-CTL"]
variables = ['LHF', 'SHF', 'NEE', 'SWup', 'LWup']
# We want to show all ticks...
ax1.set_xticks(np.arange(len(simulations)))
ax1.set_yticks(np.arange(len(variables)))
# ... and label them with the respective list entries
ax1.set_xticklabels(simulations, rotation=-45,fontsize=12)
ax1.set_yticklabels(variables,fontsize=12)
ax1.set_title('Cheorwon',fontsize=14)
#cbar = ax1.figure.colorbar(im, ax=ax1, cmap=cmap_bias)
#cbar.ax.set_ylabel('Relative change (%)', rotation=-90, va="bottom")




ax1 = plt.subplot(2, 5, 3)
ax1.text(-0.2,1.05,'(c)',color='black',fontsize=14, transform=ax1.transAxes, weight = 'bold')
bias = np.loadtxt(open("E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\Japan_Bias.csv","rb"), delimiter=",",skiprows=0)
bias_plot = np.zeros((6,3))
bias_plot[:,0] = (bias[:,1] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,1] = (bias[:,2] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,2] = (bias[:,2] - bias[:,1]) / (bias[:,1]) * 100
colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']
cmap_bias = mpl.colors.ListedColormap(colors)
bounds = [-5, -2, -1, -0.001, 0.001, 1, 2, 5]
norm_bias = mpl.colors.BoundaryNorm(bounds,cmap_bias.N,extend='both')
im = ax1.imshow(bias_plot,cmap = cmap_bias, norm= norm_bias)
simulations = ["CTL-NOI", "IRR-NOI", "IRR-CTL"]
variables = ['LHF', 'SHF', 'NEE', 'SWup', 'LWup', 'SM']
# We want to show all ticks...
ax1.set_xticks(np.arange(len(simulations)))
ax1.set_yticks(np.arange(len(variables)))
# ... and label them with the respective list entries
ax1.set_xticklabels(simulations, rotation=-45,fontsize=12)
ax1.set_yticklabels(variables,fontsize=12)
ax1.set_title('Japan',fontsize=14)
#cbar = ax1.figure.colorbar(im, ax=ax1, cmap=cmap_bias)
#cbar.ax.set_ylabel('Relative change (%)', rotation=-90, va="bottom")

ax1 = plt.subplot(2, 5, 8)
ax1.text(-0.2,1.05,'(h)',color='black',fontsize=14, transform=ax1.transAxes, weight = 'bold')
bias = np.loadtxt(open("E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\Japan_Rmse.csv","rb"), delimiter=",",skiprows=0)
bias_plot = np.zeros((6,3))
bias_plot[:,0] = (bias[:,1] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,1] = (bias[:,2] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,2] = (bias[:,2] - bias[:,1]) / (bias[:,1]) * 100
colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']
cmap_bias = mpl.colors.ListedColormap(colors)
bounds = [-5, -2, -1, -0.001, 0.001, 1, 2, 5]
norm_bias = mpl.colors.BoundaryNorm(bounds,cmap_bias.N,extend='both')
im = ax1.imshow(bias_plot,cmap = cmap_bias, norm= norm_bias)
simulations = ["CTL-NOI", "IRR-NOI", "IRR-CTL"]
variables = ['LHF', 'SHF', 'NEE', 'SWup', 'LWup', 'SM']
# We want to show all ticks...
ax1.set_xticks(np.arange(len(simulations)))
ax1.set_yticks(np.arange(len(variables)))
# ... and label them with the respective list entries
ax1.set_xticklabels(simulations, rotation=-45,fontsize=12)
ax1.set_yticklabels(variables,fontsize=12)
ax1.set_title('Japan',fontsize=14)
#cbar = ax1.figure.colorbar(im, ax=ax1, cmap=cmap_bias)
#cbar.ax.set_ylabel('Relative change (%)', rotation=-90, va="bottom")


ax1 = plt.subplot(2, 5, 4)
ax1.text(-0.2,1.05,'(d)',color='black',fontsize=14, transform=ax1.transAxes, weight = 'bold')
bias = np.loadtxt(open("E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\Nebraska_Bias.csv","rb"), delimiter=",",skiprows=0)
bias_plot = np.zeros((5,3))
bias_plot[:,0] = (bias[:,1] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,1] = (bias[:,2] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,2] = (bias[:,2] - bias[:,1]) / (bias[:,1]) * 100
colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']
cmap_bias = mpl.colors.ListedColormap(colors)
bounds = [-5, -2, -1, -0.001, 0.001, 1, 2, 5]
norm_bias = mpl.colors.BoundaryNorm(bounds,cmap_bias.N,extend='both')
im = ax1.imshow(bias_plot,cmap = cmap_bias, norm= norm_bias)
simulations = ["CTL-NOI", "IRR-NOI", "IRR-CTL"]
variables = ['LHF', 'SHF', 'NEE', 'SWup', 'LWup']
# We want to show all ticks...
ax1.set_xticks(np.arange(len(simulations)))
ax1.set_yticks(np.arange(len(variables)))
# ... and label them with the respective list entries
ax1.set_xticklabels(simulations, rotation=-45,fontsize=12)
ax1.set_yticklabels(variables,fontsize=12)
ax1.set_title('Nebraska',fontsize=14)
#cbar = ax1.figure.colorbar(im, ax=ax1, cmap=cmap_bias)
#cbar.ax.set_ylabel('Relative change (%)', rotation=-90, va="bottom")

ax1 = plt.subplot(2, 5, 9)
ax1.text(-0.2,1.05,'(i)',color='black',fontsize=14, transform=ax1.transAxes, weight = 'bold')
bias = np.loadtxt(open("E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\Nebraska_Rmse.csv","rb"), delimiter=",",skiprows=0)
bias_plot = np.zeros((5,3))
bias_plot[:,0] = (bias[:,1] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,1] = (bias[:,2] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,2] = (bias[:,2] - bias[:,1]) / (bias[:,1]) * 100
colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']
cmap_bias = mpl.colors.ListedColormap(colors)
bounds = [-5, -2, -1, -0.001, 0.001, 1, 2, 5]
norm_bias = mpl.colors.BoundaryNorm(bounds,cmap_bias.N,extend='both')
im = ax1.imshow(bias_plot,cmap = cmap_bias, norm= norm_bias)
simulations = ["CTL-NOI", "IRR-NOI", "IRR-CTL"]
variables = ['LHF', 'SHF', 'NEE', 'SWup', 'LWup']
# We want to show all ticks...
ax1.set_xticks(np.arange(len(simulations)))
ax1.set_yticks(np.arange(len(variables)))
# ... and label them with the respective list entries
ax1.set_xticklabels(simulations, rotation=-45,fontsize=12)
ax1.set_yticklabels(variables,fontsize=12)
ax1.set_title('Nebraska',fontsize=14)
#cbar = ax1.figure.colorbar(im, ax=ax1, cmap=cmap_bias)
#cbar.ax.set_ylabel('Relative change (%)', rotation=-90, va="bottom")

ax1 = plt.subplot(2, 5, 5)
ax1.text(-0.2,1.05,'(e)',color='black',fontsize=14, transform=ax1.transAxes, weight = 'bold')
bias = np.loadtxt(open("E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\Philippines_Bias.csv","rb"), delimiter=",",skiprows=0)
bias_plot = np.zeros((6,3))
bias_plot[:,0] = (bias[:,1] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,1] = (bias[:,2] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,2] = (bias[:,2] - bias[:,1]) / (bias[:,1]) * 100
colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']
cmap_bias = mpl.colors.ListedColormap(colors)
bounds = [-5, -2, -1, -0.001, 0.001, 1, 2, 5]
norm_bias = mpl.colors.BoundaryNorm(bounds,cmap_bias.N,extend='both')
im = ax1.imshow(bias_plot,cmap = cmap_bias, norm= norm_bias)
simulations = ["CTL-NOI", "IRR-NOI", "IRR-CTL"]
variables = ['LHF', 'SHF', 'NEE', 'SWup', 'LWup', 'SM']
# We want to show all ticks...
ax1.set_xticks(np.arange(len(simulations)))
ax1.set_yticks(np.arange(len(variables)))
# ... and label them with the respective list entries
ax1.set_xticklabels(simulations, rotation=-45,fontsize=12)
ax1.set_yticklabels(variables,fontsize=12)
ax1.set_title('Philippines',fontsize=14)
cbar = ax1.figure.colorbar(im, ax=ax1, cmap=cmap_bias, pad=0.05)
cbar.ax.set_ylabel('Relative change (%)', rotation=-90, va="bottom",fontsize=12)

ax1 = plt.subplot(2, 5, 10)
ax1.text(-0.2,1.05,'(j)',color='black',fontsize=14, transform=ax1.transAxes, weight = 'bold')
bias = np.loadtxt(open("E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\Philippines_Rmse.csv","rb"), delimiter=",",skiprows=0)
bias_plot = np.zeros((6,3))
bias_plot[:,0] = (bias[:,1] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,1] = (bias[:,2] - bias[:,0]) / (bias[:,0]) * 100
bias_plot[:,2] = (bias[:,2] - bias[:,1]) / (bias[:,1]) * 100
colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']
cmap_bias = mpl.colors.ListedColormap(colors)
bounds = [-5, -2, -1, -0.001, 0.001, 1, 2, 5]
norm_bias = mpl.colors.BoundaryNorm(bounds,cmap_bias.N,extend='both')
im = ax1.imshow(bias_plot,cmap = cmap_bias, norm= norm_bias)
simulations = ["CTL-NOI", "IRR-NOI", "IRR-CTL"]
variables = ['LHF', 'SHF', 'NEE', 'SWup', 'LWup', 'SM']
# We want to show all ticks...
ax1.set_xticks(np.arange(len(simulations)))
ax1.set_yticks(np.arange(len(variables)))
# ... and label them with the respective list entries
ax1.set_xticklabels(simulations, rotation=-45,fontsize=12)
ax1.set_yticklabels(variables,fontsize=12)
ax1.set_title('Philippines',fontsize=14)
cbar = ax1.figure.colorbar(im, ax=ax1, cmap=cmap_bias, pad=0.05)
cbar.ax.set_ylabel('Relative change (%)', rotation=-90, va="bottom",fontsize=12)


plt.savefig('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\9.png')







#plt.show()

print('test')