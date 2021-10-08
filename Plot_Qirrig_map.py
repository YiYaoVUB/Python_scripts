import pandas as pd
import numpy as np
import geopandas as gp
import matplotlib.pyplot as plt
import scipy.io as scio
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
from matplotlib import colors
import matplotlib.gridspec as gridspec
import cartopy.crs as ccrs
projection = ccrs.PlateCarree()
f = plt.figure(figsize = (12, 10))  # initiate the figure
f.subplots_adjust(hspace=0.15, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)

ax1 = plt.subplot(2, 2, 1)
plt.title('Mean observed irrigation water withdrawal')
right_side1 = ax1.spines['right']
#right_side1.set_visible(False)
left_side1 = ax1.spines['left']
#left_side1.set_visible(False)
top_side1 = ax1.spines['top']
#top_side1.set_visible(False)
bottom_side1 = ax1.spines['bottom']
#bottom_side1.set_visible(False)
ax1.set_xticks([])
ax1.set_yticks([])

ax2 = plt.subplot(2, 2, 2)
plt.title('Mean error (CTL - OBS)')
right_side1 = ax1.spines['right']
#right_side1.set_visible(False)
left_side1 = ax1.spines['left']
#left_side1.set_visible(False)
top_side1 = ax1.spines['top']
#top_side1.set_visible(False)
bottom_side1 = ax1.spines['bottom']
#bottom_side1.set_visible(False)
ax2.set_xticks([])
ax2.set_yticks([])

ax3 = plt.subplot(2, 2, 3)
plt.title('Mean error (IRR - OBS)')
right_side1 = ax1.spines['right']
#right_side1.set_visible(False)
left_side1 = ax1.spines['left']
#left_side1.set_visible(False)
top_side1 = ax1.spines['top']
#top_side1.set_visible(False)
bottom_side1 = ax1.spines['bottom']
#bottom_side1.set_visible(False)
ax3.set_xticks([])
ax3.set_yticks([])

ax4 = plt.subplot(2, 2, 4)
plt.title('Mean absolute error (MAE) change (IRR - CTL)')
right_side1 = ax1.spines['right']
#right_side1.set_visible(False)
left_side1 = ax1.spines['left']
#left_side1.set_visible(False)
top_side1 = ax1.spines['top']
#top_side1.set_visible(False)
bottom_side1 = ax1.spines['bottom']
#bottom_side1.set_visible(False)
ax4.set_xticks([])
ax4.set_yticks([])

#ax5 = plt.subplot(3, 2, 5)
#plt.title('Mean absolute error (MAE) change (IRR - CTL)')
#right_side5 = ax5.spines['right']
#right_side5.set_visible(False)
#left_side5 = ax5.spines['left']
#left_side5.set_visible(False)
#top_side5 = ax5.spines['top']
#top_side5.set_visible(False)
#bottom_side5 = ax5.spines['bottom']
#bottom_side5.set_visible(False)
#ax5.set_xticks([])
#ax5.set_yticks([])

#ax6 = plt.subplot(3, 2, 6)
#plt.title('Mean absolute error (MAE) change (DU - IRR)')
#right_side5 = ax5.spines['right']
##right_side5.set_visible(False)
#left_side5 = ax5.spines['left']
##left_side5.set_visible(False)
#top_side5 = ax5.spines['top']
##top_side5.set_visible(False)
#bottom_side5 = ax5.spines['bottom']
##bottom_side5.set_visible(False)
#ax6.set_xticks([])
#ax6.set_yticks([])

boundary = gp.GeoDataFrame.from_file('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\\Example.shp', encoding = 'gb18030')
data_geod = gp.GeoDataFrame.from_file('E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\\Example.shp', encoding = 'gb18030')

base1 = boundary.boundary.plot(ax = ax1, edgecolor='lightgrey', linewidth=0.2)
vmax = data_geod.Obs.max()
vmin = data_geod.Obs.min()
norms1 = colors.DivergingNorm(vmin=vmin,
                             vcenter=0.01,
                             vmax=vmax)
cmap1='Blues'
divider = make_axes_locatable(ax1)
cax = divider.append_axes("bottom", size="5%", pad=0.1)
h = data_geod.plot(column='Obs',cmap=cmap1,ax=base1,norm=norms1, alpha=10, legend=True,cax=cax, legend_kwds={'label': r"water withdrawal ($km^3$/yr)",'orientation': "horizontal"}, missing_kwds={"color": "lightgrey","edgecolor": "white","label": "Missing values"})



base2 = boundary.boundary.plot(ax = ax2, edgecolor='lightgrey', linewidth=0.2)
colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']
cmap2 = mpl.colors.ListedColormap(colors)
bounds = [-15, -10, -5, -0.001, 0.001, 5, 10, 15]
norm2 = mpl.colors.BoundaryNorm(bounds,cmap2.N,extend='both')
divider = make_axes_locatable(ax2)
cax = divider.append_axes("bottom", size="5%", pad=0.1)
h = data_geod.plot(column='Bias_ctl',cmap=cmap2,ax=base2,norm=norm2, alpha=10, legend=True,cax=cax, legend_kwds={'label': r"mean error ($km^3$/yr)",'orientation': "horizontal"}, missing_kwds={"color": "lightgrey","edgecolor": "white","label": "Missing values"})





base3 = boundary.boundary.plot(ax = ax3, edgecolor='lightgrey', linewidth=0.2)
colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']
cmap3 = mpl.colors.ListedColormap(colors)
bounds = [-15, -10, -5, -0.001, 0.001, 5, 10, 15]
norm3 = mpl.colors.BoundaryNorm(bounds,cmap3.N,extend='both')
divider = make_axes_locatable(ax3)
cax = divider.append_axes("bottom", size="5%", pad=0.1)
h = data_geod.plot(column='Bias_irr',cmap=cmap3,ax=base3,norm=norm3, alpha=10, legend=True,cax=cax, legend_kwds={'label': r"mean error ($km^3$/yr)",'orientation': "horizontal"}, missing_kwds={"color": "lightgrey","edgecolor": "white","label": "Missing values"})


#base4 = boundary.boundary.plot(ax = ax4, edgecolor='lightgrey', linewidth=0.2)
#colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']
#cmap4 = mpl.colors.ListedColormap(colors)
#bounds = [-15, -10, -5, -0.001, 0.001, 5, 10, 15]
#norm4 = mpl.colors.BoundaryNorm(bounds,cmap4.N,extend='both')
#divider = make_axes_locatable(ax4)
#cax = divider.append_axes("bottom", size="5%", pad=0.1)
#h = data_geod.plot(column='Bias_du',cmap=cmap4,ax=base4,norm=norm4, alpha=10, legend=True,cax=cax, legend_kwds={'label': r"mean error ($km^3$/yr)",'orientation': "horizontal"}, missing_kwds={"color": "lightgrey","edgecolor": "white","label": "Missing values"})


colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']
cmap = mpl.colors.ListedColormap(colors)

bounds = [-15, -10, -5, -0.001, 0.001, 5, 10, 15]
norm = mpl.colors.BoundaryNorm(bounds,cmap.N,extend='both')


base5 = boundary.boundary.plot(ax = ax4, edgecolor='lightgrey', linewidth=0.2)


#vmax = data_geod.AbBias.max()
#vmin = data_geod.AbBias.min()
#vmax = 25
#vmin = -25
#norms = colors.DivergingNorm(vmin=vmin,
#                             vcenter=0,
#                             vmax=vmax)
divider = make_axes_locatable(ax4)
cax = divider.append_axes("bottom", size="5%", pad=0.1)
h = data_geod.plot(column='AbBias_irr_',cmap=cmap,ax=base5,norm=norm, alpha=10, legend=True,cax=cax, legend_kwds={'label': "MAE(IRR) - MAE(CTL) ($km^3$/yr)",'orientation': "horizontal"}, missing_kwds={"color": "lightgrey","edgecolor": "white","label": "Missing values"})


#base6 = boundary.boundary.plot(ax = ax6, edgecolor='lightgrey', linewidth=0.2)
##colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']
#cmap = mpl.colors.ListedColormap(colors)

#bounds = [-15, -10, -5, -0.001, 0.001, 5, 10, 15]
#norm = mpl.colors.BoundaryNorm(bounds,cmap.N,extend='both')
#divider = make_axes_locatable(ax6)
#cax = divider.append_axes("bottom", size="5%", pad=0.1)
#h = data_geod.plot(column='AbBias_du_c',cmap=cmap,ax=base6,norm=norm, alpha=10, legend=True,cax=cax, legend_kwds={'label': "MAE(NEW) - MAE(OLD) ($km^3$/yr)",'orientation': "horizontal"}, missing_kwds={"color": "lightgrey","edgecolor": "white","label": "Missing values"})

plt.show()

f = plt.figure(figsize = (6, 6))  # initiate the figure
f.subplots_adjust(hspace=0.15, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)

ax1 = plt.subplot(1, 1, 1)
plt.title('Relative error ((CTL - OBS) / CTL)')
right_side1 = ax1.spines['right']
#right_side1.set_visible(False)
left_side1 = ax1.spines['left']
#left_side1.set_visible(False)
top_side1 = ax1.spines['top']
#top_side1.set_visible(False)
bottom_side1 = ax1.spines['bottom']
#bottom_side1.set_visible(False)
ax1.set_xticks([])
ax1.set_yticks([])

base2 = boundary.boundary.plot(ax = ax1, edgecolor='lightgrey', linewidth=0.2)
colors = ['darkgreen', 'forestgreen', 'limegreen', 'lime', 'white', 'plum', 'violet', 'fuchsia', 'purple']
cmap2 = mpl.colors.ListedColormap(colors)
bounds = [-3, -1, -0.5, -0.001, 0.001, 0.5, 1, 3]
norm2 = mpl.colors.BoundaryNorm(bounds,cmap2.N,extend='both')
divider = make_axes_locatable(ax1)
cax = divider.append_axes("bottom", size="5%", pad=0.1)
h = data_geod.plot(column='Bias_ctl',cmap=cmap2,ax=base2,norm=norm2, alpha=10, legend=True,cax=cax, legend_kwds={'label': r"relative error",'orientation': "horizontal"}, missing_kwds={"color": "lightgrey","edgecolor": "white","label": "Missing values"})
plt.show()