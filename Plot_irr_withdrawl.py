import geopandas as gp
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
from matplotlib import colors
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# function definition
def subplotdefi(row, col, num, title,fontsize):
    ax = plt.subplot(row, col, num)
    plt.title(title,fontsize=fontsize)
    right_side1 = ax.spines['right']    # right_side1.set_visible(False)
    left_side1 = ax.spines['left']  # left_side1.set_visible(False)
    top_side1 = ax.spines['top']    # top_side1.set_visible(False)
    bottom_side1 = ax.spines['bottom']  # bottom_side1.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    return ax

def plotmap(boundary, ax, colomn, cmap,  norm, legend_kwds):
    base = boundary.boundary.plot(ax=ax, edgecolor='lightgrey', linewidth=0.1)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("bottom", size="3%", pad=0.1)
    h = data_geod.plot(column=colomn, cmap=cmap, ax=base, norm=norm, alpha=10, legend=True, cax=cax,
                       legend_kwds=legend_kwds,
                       missing_kwds={"color": "lightgray", "label": "Missing values"})    #missing_kwds={"color": "lightgrey", "edgecolor": "white", "label": "Missing values"})
    return h

def plotmap2(boundary, ax, colomn, cmap,  norm, legend_kwds):
    base = boundary.boundary.plot(ax=ax, edgecolor='lightgrey', linewidth=0.1)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("bottom", size="3%", pad=0.1)
    h = data_geod.plot(column=colomn, cmap=cmap, ax=base, norm=norm, alpha=10, legend=True, cax=cax,
                       legend_kwds=legend_kwds,
                       missing_kwds={"color": "white", "label": "Missing values"})    #missing_kwds={"color": "lightgrey", "edgecolor": "white", "label": "Missing values"})
    return h


def set_plot_param():
    """Set my own customized plotting parameters"""

    mpl.rc('axes', edgecolor='lightgrey')
    mpl.rc('axes', labelcolor='dimgrey')
    mpl.rc('xtick', color='dimgrey')
    mpl.rc('xtick', labelsize=12)
    mpl.rc('ytick', color='dimgrey')
    mpl.rc('ytick', labelsize=12)
    mpl.rc('axes', titlesize=14)
    mpl.rc('axes', labelsize=12)
    mpl.rc('legend', fontsize='large')
    mpl.rc('text', color='dimgrey')

projection = ccrs.PlateCarree()
boundary = gp.GeoDataFrame.from_file('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\\Example_final.shp', encoding = 'gb18030')
data_geod = gp.GeoDataFrame.from_file('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\\Example_final.shp', encoding = 'gb18030')

# plot 1
f = plt.figure(figsize = (12, 7), dpi=1000)  # initiate the figure
f.subplots_adjust(hspace=0.1, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)
set_plot_param()
ax = subplotdefi(1,1,1,'Mean observed irrigation water withdrawal',18)
# plot water withdrawal
vmax = data_geod.Obs.max()
vmin = data_geod.Obs.min()
norm_withd = colors.DivergingNorm(vmin=vmin,
                             vcenter=0.01,
                             vmax=vmax)
cmap_withd='Blues'



bounds_Blues = [0, 0.5, 1, 2, 5, 10, 15, 30]
Blues = mpl.cm.get_cmap('Blues')
colors_Blues = [Blues(0.125), Blues(0.25), Blues(0.375), Blues(0.5), Blues(0.625), Blues(0.75), Blues(0.875), Blues(0.99)]

print(colors_Blues)
cmap_Blues = mpl.colors.ListedColormap(colors_Blues)
norm_Blues = mpl.colors.BoundaryNorm(bounds_Blues,cmap_Blues.N,extend='max')
h = plotmap(boundary, ax, 'Obs', cmap_Blues, norm_Blues,legend_kwds={'label': r"water withdrawal ($km^3$/yr)",'orientation': "horizontal"})
plt.savefig('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\1.png')
#plt.show()

#plot 2
f2 = plt.figure(figsize = (6, 7), dpi=1000)  # initiate the figure
f2.subplots_adjust(hspace=0.1, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)
ax = subplotdefi(2,1,1,'Mean simulated irrigation water withdrawal (CTL)',14)
ax.text(0.01,0.92,'a',color='dimgrey',fontsize=12, transform=ax.transAxes, weight = 'bold')

ax1 = subplotdefi(2,1,2,'Mean error (CTL - OBS)',14)
ax1.text(0.01,0.92,'b',color='dimgrey',fontsize=12, transform=ax1.transAxes, weight = 'bold')



h2 = plotmap2(boundary, ax, 'Ctl', cmap_Blues, norm_Blues,legend_kwds={'label': r"water withdrawal ($km^3$/yr)",'orientation': "horizontal"})


PRGn = mpl.cm.get_cmap('PRGn_r')
colors = [PRGn(0.01),PRGn(0.1),PRGn(0.2),PRGn(0.3),PRGn(0.5),PRGn(0.7),PRGn(0.8),PRGn(0.9),PRGn(0.99)]
colors = [PRGn(0.01),PRGn(0.1),PRGn(0.2),PRGn(0.3),'whitesmoke',PRGn(0.7),PRGn(0.8),PRGn(0.9),PRGn(0.99)]
#colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']

cmap_bias = mpl.colors.ListedColormap(colors)
bounds = [-15, -10, -5, -0.001, 0.001, 5, 10, 15]
bounds = [-5, -3, -1, -0.1, 0.1, 1, 3, 5]
norm_bias = mpl.colors.BoundaryNorm(bounds,cmap_bias.N,extend='both')

bwr = mpl.cm.get_cmap('bwr_r')
colors = [bwr(0.1),bwr(0.2),bwr(0.3),bwr(0.4),bwr(0.5),bwr(0.6),bwr(0.7),bwr(0.8),bwr(0.9)]
colors = [bwr(0.1),bwr(0.2),bwr(0.3),bwr(0.4),'whitesmoke',bwr(0.6),bwr(0.7),bwr(0.8),bwr(0.9)]
#colors = ['darkgoldenrod', 'goldenrod', 'gold', 'yellow', 'white', 'aqua', 'dodgerblue', 'blue', 'darkblue']
cmap_bias1 = mpl.colors.ListedColormap(colors)
bounds = [-15, -10, -5, -0.001, 0.001, 5, 10, 15]
bounds = [-10, -5, -2, -0.5, 0.5, 2, 5, 10]
norm_bias1 = mpl.colors.BoundaryNorm(bounds,cmap_bias1.N,extend='both')

h2 = plotmap(boundary, ax1, 'Bias_ctl', cmap_bias1, norm_bias1,legend_kwds={'label': r"mean error ($km^3$/yr)",'orientation': "horizontal"})
plt.savefig('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\2.png')

#plt.show()
f2 = plt.figure(figsize = (6, 7), dpi=1000)  # initiate the figure
f2.subplots_adjust(hspace=0.1, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)
ax0 = subplotdefi(2,1,1,'Mean simulated irrigation water withdrawal (CTL_limit)',14)
ax0 = subplotdefi(2,1,1,'Mean simulated irrigation water withdrawal (CTL_limit)',14)
ax0.text(0.01,0.92,'a',color='dimgrey',fontsize=12, transform=ax0.transAxes, weight = 'bold')
ax2 = subplotdefi(2,1,2,'Mean error (CTL_limit - OBS)',14)
ax2.text(0.01,0.92,'b',color='dimgrey',fontsize=12, transform=ax2.transAxes, weight = 'bold')
h3 = plotmap2(boundary, ax0, 'Ctl_limit', cmap_Blues, norm_Blues,legend_kwds={'label': r"water withdrawal ($km^3$/yr)",'orientation': "horizontal"})
h3 = plotmap(boundary, ax2, 'Bias_ctl_li', cmap_bias1, norm_bias1,legend_kwds={'label': r"mean error ($km^3$/yr)",'orientation': "horizontal"})
plt.savefig('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\21.png')


#plot 3

f2 = plt.figure(figsize = (12, 7), dpi=1000)  # initiate the figure
f2.subplots_adjust(hspace=0.1, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)
#ax1 = subplotdefi(2,2,1,'Mean error (IRR_meth - OBS)',14)
ax1 = subplotdefi(2,2,1,'',14)
ax1.set_title('IRR_meth - OBS',loc='right',fontsize = 12)
ax1.text(0.01,0.92,'a',color='dimgrey',fontsize=12, transform=ax1.transAxes, weight = 'bold')
#ax2 = subplotdefi(2,2,2,'Mean error (IRR_drai - OBS)',14)
ax2 = subplotdefi(2,2,2,'',14)
ax2.set_title('IRR_drai - OBS',loc='right',fontsize = 12)
ax2.text(0.01,0.92,'b',color='dimgrey',fontsize=12, transform=ax2.transAxes, weight = 'bold')
#ax3 = subplotdefi(2,2,3,'Mean error (IRR_pool - OBS)',14)
ax3 = subplotdefi(2,2,3,'',14)
ax3.set_title('IRR_pool - OBS',loc='right',fontsize = 12)
ax3.text(0.01,0.92,'c',color='dimgrey',fontsize=12, transform=ax3.transAxes, weight = 'bold')
#ax4 = subplotdefi(2,2,4,'Mean error (IRR_satu - OBS)',14)
ax4 = subplotdefi(2,2,4,'',14)
ax4.set_title('IRR_satu - OBS',loc='right',fontsize = 12)
ax4.text(0.01,0.92,'d',color='dimgrey',fontsize=12, transform=ax4.transAxes, weight = 'bold')

h1 = plotmap(boundary, ax1, 'Bias_irr', cmap_bias1, norm_bias1,legend_kwds={'label': r"mean error ($km^3$/yr)",'orientation': "horizontal"})
h2 = plotmap(boundary, ax2, 'Bias_drai', cmap_bias1, norm_bias1,legend_kwds={'label': r"mean error ($km^3$/yr)",'orientation': "horizontal"})
h3 = plotmap(boundary, ax3, 'Bias_pool', cmap_bias1, norm_bias1,legend_kwds={'label': r"mean error ($km^3$/yr)",'orientation': "horizontal"})
h4 = plotmap(boundary, ax4, 'Bias_satu', cmap_bias1, norm_bias1,legend_kwds={'label': r"mean error ($km^3$/yr)",'orientation': "horizontal"})
plt.savefig('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\3.png')
#plt.show()


#plot 4
f2 = plt.figure(figsize = (12, 7), dpi=1000)  # initiate the figure
f2.subplots_adjust(hspace=0.1, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)
#ax1 = subplotdefi(2,2,1,'Mean absolute error (MAE) change (IRR_meth - CTL)',14)
ax1 = subplotdefi(2,2,1,'',14)
ax1.set_title('MAE(IRR_meth) - MAE(CTL)',loc='right',fontsize = 12)
ax1.text(0.01,0.92,'a',color='dimgrey',fontsize=12, transform=ax1.transAxes, weight = 'bold')
#ax2 = subplotdefi(2,2,2,'Mean absolute error (MAE) change (IRR_drai - CTL)',14)
ax2 = subplotdefi(2,2,2,'',14)
ax2.set_title('MAE(IRR_drai) - MAE(CTL)',loc='right',fontsize = 12)
ax2.text(0.01,0.92,'b',color='dimgrey',fontsize=12, transform=ax2.transAxes, weight = 'bold')
#ax3 = subplotdefi(2,2,3,'Mean absolute error (MAE) change (IRR_pool - CTL)',14)
ax3 = subplotdefi(2,2,3,'',14)
ax3.set_title('MAE(IRR_pool) - MAE(CTL)',loc='right',fontsize = 12)
ax3.text(0.01,0.92,'c',color='dimgrey',fontsize=12, transform=ax3.transAxes, weight = 'bold')
#ax4 = subplotdefi(2,2,4,'Mean absolute error (MAE) change (IRR_satu - CTL)',14)
ax4 = subplotdefi(2,2,4,'',14)
ax4.set_title('MAE(IRR_satu) - MAE(CTL)',loc='right',fontsize = 12)
ax4.text(0.01,0.92,'d',color='dimgrey',fontsize=12, transform=ax4.transAxes, weight = 'bold')

h1 = plotmap(boundary, ax1, 'AbBias_1', cmap_bias, norm_bias,legend_kwds={'label': r"MAE change ($km^3$/yr)",'orientation': "horizontal"})
h2 = plotmap(boundary, ax2, 'AbBias_2', cmap_bias, norm_bias,legend_kwds={'label': r"MAE change ($km^3$/yr)",'orientation': "horizontal"})
h3 = plotmap(boundary, ax3, 'AbBias_3', cmap_bias, norm_bias,legend_kwds={'label': r"MAE change ($km^3$/yr)",'orientation': "horizontal"})
h4 = plotmap(boundary, ax4, 'AbBias_4', cmap_bias, norm_bias,legend_kwds={'label': r"MAE change ($km^3$/yr)",'orientation': "horizontal"})
plt.savefig('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\4.png')
#plt.show()

#plot 5
f2 = plt.figure(figsize = (12, 7), dpi=1000)  # initiate the figure
f2.subplots_adjust(hspace=0.1, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)
#ax1 = subplotdefi(2,2,1,'Mean error (IRR_meth_limit - OBS)',14)
ax1 = subplotdefi(2,2,1,'',14)
ax1.set_title('IRR_meth_limit - OBS',loc='right',fontsize = 12)
ax1.text(0.01,0.92,'a',color='dimgrey',fontsize=12, transform=ax1.transAxes, weight = 'bold')
#ax2 = subplotdefi(2,2,2,'Mean error (IRR_drai_limit - OBS)',14)
ax2 = subplotdefi(2,2,2,'',14)
ax2.set_title('IRR_drai_limit - OBS',loc='right',fontsize = 12)
ax2.text(0.01,0.92,'b',color='dimgrey',fontsize=12, transform=ax2.transAxes, weight = 'bold')
#ax3 = subplotdefi(2,2,3,'Mean error (IRR_pool_limit - OBS)',14)
ax3 = subplotdefi(2,2,3,'',14)
ax3.set_title('IRR_pool_limit - OBS',loc='right',fontsize = 12)
ax3.text(0.01,0.92,'c',color='dimgrey',fontsize=12, transform=ax3.transAxes, weight = 'bold')
#ax4 = subplotdefi(2,2,4,'Mean error (IRR_satu_limit - OBS)',14)
ax4 = subplotdefi(2,2,4,'',14)
ax4.set_title('IRR_satu_limit - OBS',loc='right',fontsize = 12)
ax4.text(0.01,0.92,'d',color='dimgrey',fontsize=12, transform=ax4.transAxes, weight = 'bold')

h1 = plotmap(boundary, ax1, 'Bias_irr_li', cmap_bias1, norm_bias1,legend_kwds={'label': r"mean error ($km^3$/yr)",'orientation': "horizontal"})
h2 = plotmap(boundary, ax2, 'Bias_drai_l', cmap_bias1, norm_bias1,legend_kwds={'label': r"mean error ($km^3$/yr)",'orientation': "horizontal"})
h3 = plotmap(boundary, ax3, 'Bias_pool_l', cmap_bias1, norm_bias1,legend_kwds={'label': r"mean error ($km^3$/yr)",'orientation': "horizontal"})
h4 = plotmap(boundary, ax4, 'Bias_satu_l', cmap_bias1, norm_bias1,legend_kwds={'label': r"mean error ($km^3$/yr)",'orientation': "horizontal"})
plt.savefig('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\5.png')
#plt.show()

#plot 6
f2 = plt.figure(figsize = (12, 7), dpi=1000)  # initiate the figure
f2.subplots_adjust(hspace=0.1, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)
#ax1 = subplotdefi(2,2,1,'Mean absolute error (MAE) change (IRR_meth_limit - CTL_limit)',12)
ax1 = subplotdefi(2,2,1,'',14)
ax1.set_title('MAE(IRR_meth_limit) - MAE(CTL_limit)',loc='right',fontsize = 12)
ax1.text(0.01,0.92,'a',color='dimgrey',fontsize=12, transform=ax1.transAxes, weight = 'bold')
#ax2 = subplotdefi(2,2,2,'Mean absolute error (MAE) change (IRR_drai_limit - CTL_limit)',12)
ax2 = subplotdefi(2,2,2,'',14)
ax2.set_title('MAE(IRR_drai_limit) - MAE(CTL_limit)',loc='right',fontsize = 12)
ax2.text(0.01,0.92,'b',color='dimgrey',fontsize=12, transform=ax2.transAxes, weight = 'bold')
#ax3 = subplotdefi(2,2,3,'Mean absolute error (MAE) change (IRR_pool_limit - CTL_limit)',12)
ax3 = subplotdefi(2,2,3,'',14)
ax3.set_title('MAE(IRR_pool_limit) - MAE(CTL_limit)',loc='right',fontsize = 12)
ax3.text(0.01,0.92,'c',color='dimgrey',fontsize=12, transform=ax3.transAxes, weight = 'bold')
#ax4 = subplotdefi(2,2,4,'Mean absolute error (MAE) change (IRR_satu_limit - CTL_limit)',12)
ax4 = subplotdefi(2,2,4,'',14)
ax4.set_title('MAE(IRR_satu_limit) - MAE(CTL_limit)',loc='right',fontsize = 12)
ax4.text(0.01,0.92,'d',color='dimgrey',fontsize=12, transform=ax4.transAxes, weight = 'bold')


h1 = plotmap(boundary, ax1, 'AbBias_5', cmap_bias, norm_bias,legend_kwds={'label': r"MAE change ($km^3$/yr)",'orientation': "horizontal"})
h2 = plotmap(boundary, ax2, 'AbBias_6', cmap_bias, norm_bias,legend_kwds={'label': r"MAE change ($km^3$/yr)",'orientation': "horizontal"})
h3 = plotmap(boundary, ax3, 'AbBias_7', cmap_bias, norm_bias,legend_kwds={'label': r"MAE change ($km^3$/yr)",'orientation': "horizontal"})
h4 = plotmap(boundary, ax4, 'AbBias_8', cmap_bias, norm_bias,legend_kwds={'label': r"MAE change ($km^3$/yr)",'orientation': "horizontal"})
plt.savefig('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\6.png')
#plt.show()
