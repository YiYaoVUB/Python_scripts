from Load_data import Data_from_nc
from Calculation_utils import Calculation
import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import numpy as np
import time
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import colors

number_lat = 32 #for cutting the Antarctica

data_SM_C3S = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\Soil_Moisture\C3S_combined_2006-2015_regrid.nc')   #load the data
data_lon = data_SM_C3S.load_variable('lon')
data_lat = data_SM_C3S.load_variable('lat')
data_lat = data_lat[number_lat :]
data_time = data_SM_C3S.load_variable('time')
data_variable_SM_C3S = data_SM_C3S.load_variable('sm')
#data_variable_SM_C3S = data_variable_SM_C3S.swapaxes(2,1)
data_variable_SM_C3S = data_variable_SM_C3S[0, :, :]
data_variable_SM_C3S = data_variable_SM_C3S[number_lat :, :]  #no Anrctatica



data_SM_NOI = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\Soil_Moisture\\NOI_H2OSOI_timmean.nc')   #load the data
data_variable_SM_NOI = data_SM_NOI.load_variable('H2OSOI')
data_variable_SM_NOI[data_variable_SM_NOI >= 10000000000] = None
data_variable_SM_NOI = data_variable_SM_NOI[0,0,  :, :]
data_variable_SM_NOI = data_variable_SM_NOI[number_lat :, :]
var_NOI_C3S = data_variable_SM_NOI - data_variable_SM_C3S

data_SM_CTL = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\Soil_Moisture\\CTL_H2OSOI_timmean.nc')   #load the data
data_variable_SM_CTL = data_SM_CTL.load_variable('H2OSOI')
data_variable_SM_CTL[data_variable_SM_CTL >= 10000000000] = None
data_variable_SM_CTL = data_variable_SM_CTL[0,0, :, :]
data_variable_SM_CTL = data_variable_SM_CTL[number_lat :, :]
var_CTL_NOI = data_variable_SM_CTL - data_variable_SM_NOI
var_CTL_C3S = data_variable_SM_CTL - data_variable_SM_C3S

data_SM_IRR = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\Soil_Moisture\\IRR_H2OSOI_timmean.nc')   #load the data
data_variable_SM_IRR = data_SM_IRR.load_variable('H2OSOI')
data_variable_SM_IRR[data_variable_SM_IRR >= 10000000000] = None
data_variable_SM_IRR = data_variable_SM_IRR[0,0, :, :]
data_variable_SM_IRR = data_variable_SM_IRR[number_lat :, :]
var_IRR_CTL = data_variable_SM_IRR - data_variable_SM_CTL
var_IRR_C3S = data_variable_SM_IRR - data_variable_SM_C3S
var_IRR_NOI = data_variable_SM_IRR - data_variable_SM_NOI

data_SM_DU = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\Soil_Moisture\\DU_H2OSOI_timmean.nc')   #load the data
data_variable_SM_DU = data_SM_DU.load_variable('H2OSOI')
data_variable_SM_DU[data_variable_SM_DU >= 10000000000] = None
data_variable_SM_DU = data_variable_SM_DU[0,0, :, :]
data_variable_SM_DU = data_variable_SM_DU[number_lat :, :]
var_DU_CTL = data_variable_SM_DU - data_variable_SM_CTL
var_DU_C3S = data_variable_SM_DU - data_variable_SM_C3S
var_DU_NOI = data_variable_SM_DU - data_variable_SM_NOI

data_lon = np.roll(data_lon, int(len(data_lon)/2))      #move the 0 degree to the center
data_lon[data_lon>= 180] = data_lon[data_lon>= 180] - 360
data_variable_SM_C3S = np.roll(data_variable_SM_C3S, int(len(data_lon)/2))
var_NOI_C3S  = np.roll(var_NOI_C3S , int(len(data_lon)/2))
var_CTL_NOI  = np.roll(var_CTL_NOI , int(len(data_lon)/2))
var_CTL_C3S  = np.roll(var_CTL_C3S , int(len(data_lon)/2))
var_IRR_C3S  = np.roll(var_IRR_C3S , int(len(data_lon)/2))
var_IRR_CTL  = np.roll(var_IRR_CTL , int(len(data_lon)/2))
var_SM_C3S  = np.roll(var_IRR_C3S , int(len(data_lon)/2))
var_DU_CTL  = np.roll(var_DU_CTL , int(len(data_lon)/2))
var_DU_C3S  = np.roll(var_DU_C3S , int(len(data_lon)/2))
var_IRR_NOI  = np.roll(var_IRR_NOI , int(len(data_lon)/2))
var_DU_NOI  = np.roll(var_DU_NOI , int(len(data_lon)/2))
data_variable_SM_NOI = np.roll(data_variable_SM_NOI , int(len(data_lon)/2))
data_variable_SM_CTL = np.roll(data_variable_SM_CTL , int(len(data_lon)/2))
data_variable_SM_IRR = np.roll(data_variable_SM_IRR , int(len(data_lon)/2))
data_variable_SM_DU = np.roll(data_variable_SM_DU , int(len(data_lon)/2))

for i in range(np.size(data_variable_SM_DU,0)):
    for j in range(np.size(data_variable_SM_DU,1)):
        if data_variable_SM_C3S[i,j] < 0:
            var_NOI_C3S[i,j] = float('NaN')
            var_CTL_NOI[i, j] = float('NaN')
            var_CTL_C3S[i, j] = float('NaN')
            var_IRR_C3S[i, j] = float('NaN')
            var_IRR_CTL[i, j] = float('NaN')
            var_DU_CTL[i, j] = float('NaN')
            var_DU_C3S[i, j] = float('NaN')
            var_IRR_NOI[i, j] = float('NaN')
            var_DU_NOI[i, j] = float('NaN')


f = plt.figure(figsize = (12, 8))  # initiate the figure
f.subplots_adjust(hspace=0.15, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)
ax1 = plt.subplot(1, 2, 1, projection=ccrs.PlateCarree())
ax1.coastlines(linewidth=0.5)

cmap='Blues'
divider = make_axes_locatable(ax1)
norms = colors.DivergingNorm(vmin=0,
                                vcenter=0.25,
                             vmax=0.5)
h = ax1.pcolormesh(data_lon,data_lat,data_variable_SM_C3S, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax1, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='max', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Soil moisture ($m^3$/$m^3$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('ESA CCI')

ax1 = plt.subplot(1, 2, 2, projection=ccrs.PlateCarree())
ax1.coastlines(linewidth=0.5)

cmap='Blues'
divider = make_axes_locatable(ax1)
norms = colors.DivergingNorm(vmin=0,
                                vcenter=0.25,
                             vmax=0.5)
h = ax1.pcolormesh(data_lon,data_lat,data_variable_SM_NOI, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax1, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='max', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Soil moisture ($m^3$/$m^3$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('NOI')
plt.show()

f = plt.figure(figsize = (12, 8))  # initiate the figure
f.subplots_adjust(hspace=0.15, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)
ax2 = plt.subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax2.coastlines(linewidth=0.5)

cmap='bwr_r'
divider = make_axes_locatable(ax2)
norms = colors.DivergingNorm(vmin=-0.2,
                             vcenter=0,
                             vmax=0.2)
h = ax2.pcolormesh(data_lon,data_lat,var_NOI_C3S, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax2, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Soil moisture ($m^3$/$m^3$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('NOI - ESA CCI')
plt.show()

f = plt.figure(figsize = (12, 8))  # initiate the figure
f.subplots_adjust(hspace=0.15, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)
ax3 = plt.subplot(1, 2, 1, projection=ccrs.PlateCarree())
ax3.coastlines(linewidth=0.5)

cmap='bwr_r'
divider = make_axes_locatable(ax3)
norms = colors.DivergingNorm(vmin=-0.05,
                             vcenter=0,
                             vmax=0.05)
h = ax3.pcolormesh(data_lon,data_lat,var_CTL_NOI, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax3, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Soil moisture ($m^3$/$m^3$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('CTL - NOI')

ax3 = plt.subplot(1, 2, 2, projection=ccrs.PlateCarree())
ax3.coastlines(linewidth=0.5)

cmap='bwr_r'
divider = make_axes_locatable(ax3)
norms = colors.DivergingNorm(vmin=-0.2,
                             vcenter=0,
                             vmax=0.2)
h = ax3.pcolormesh(data_lon,data_lat,var_CTL_C3S, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax3, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Soil moisture ($m^3$/$m^3$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('CTL - ESA CCI')
plt.show()

f = plt.figure(figsize = (12, 8))  # initiate the figure
f.subplots_adjust(hspace=0.15, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)

ax4 = plt.subplot(1, 2, 1, projection=ccrs.PlateCarree())
ax4.coastlines(linewidth=0.5)

cmap='bwr_r'
divider = make_axes_locatable(ax4)
norms = colors.DivergingNorm(vmin=-0.05,
                             vcenter=0,
                             vmax=0.05)
h = ax4.pcolormesh(data_lon,data_lat,var_IRR_CTL, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax4, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Soil moisture ($m^3$/$m^3$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('IRR - CTL')


ax4 = plt.subplot(1, 2, 2, projection=ccrs.PlateCarree())
ax4.coastlines(linewidth=0.5)

cmap='bwr_r'
divider = make_axes_locatable(ax4)
norms = colors.DivergingNorm(vmin=-0.05,
                             vcenter=0,
                             vmax=0.05)
h = ax4.pcolormesh(data_lon,data_lat,var_DU_CTL, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax4, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Soil moisture ($m^3$/$m^3$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('DU - CTL')


plt.show()




















ax1 = plt.subplot(2, 2, 2, projection=ccrs.PlateCarree())
ax1.coastlines(linewidth=0.5)
ax1.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='Blues'
divider = make_axes_locatable(ax1)
norms = colors.DivergingNorm(vmin=0,
                                vcenter=0.25,
                             vmax=0.5)
h = ax1.pcolormesh(data_lon,data_lat,data_variable_SM_CTL, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax1, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='max', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Soil moisture',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('CTL')









f = plt.figure(figsize = (12, 12))  # initiate the figure
f.subplots_adjust(hspace=0.15, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)

ax4 = plt.subplot(3, 2, 1, projection=ccrs.PlateCarree())
ax4.coastlines(linewidth=0.5)
ax4.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='bwr_r'
divider = make_axes_locatable(ax4)
norms = colors.DivergingNorm(vmin=-0.2,
                             vcenter=0,
                             vmax=0.2)
h = ax4.pcolormesh(data_lon,data_lat,var_IRR_C3S, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax4, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Soil moisture',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('IRR - C3S')

ax4 = plt.subplot(3, 2, 3, projection=ccrs.PlateCarree())
ax4.coastlines(linewidth=0.5)
ax4.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='bwr_r'
divider = make_axes_locatable(ax4)
norms = colors.DivergingNorm(vmin=-0.05,
                             vcenter=0,
                             vmax=0.05)
h = ax4.pcolormesh(data_lon,data_lat,var_IRR_NOI, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax4, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Soil moisture',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('IRR - NOI')



ax4 = plt.subplot(3, 2, 2, projection=ccrs.PlateCarree())
ax4.coastlines(linewidth=0.5)
ax4.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='bwr_r'
divider = make_axes_locatable(ax4)
norms = colors.DivergingNorm(vmin=-0.2,
                             vcenter=0,
                             vmax=0.2)
h = ax4.pcolormesh(data_lon,data_lat,var_DU_C3S, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax4, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Soil moisture',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('DU - C3S')

ax4 = plt.subplot(3, 2, 4, projection=ccrs.PlateCarree())
ax4.coastlines(linewidth=0.5)
ax4.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='bwr_r'
divider = make_axes_locatable(ax4)
norms = colors.DivergingNorm(vmin=-0.05,
                             vcenter=0,
                             vmax=0.05)
h = ax4.pcolormesh(data_lon,data_lat,var_DU_NOI, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax4, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Soil moisture',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('DU - NOI')

ax4 = plt.subplot(3, 2, 6, projection=ccrs.PlateCarree())
ax4.coastlines(linewidth=0.5)
ax4.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='bwr_r'
divider = make_axes_locatable(ax4)
norms = colors.DivergingNorm(vmin=-0.05,
                             vcenter=0,
                             vmax=0.05)
h = ax4.pcolormesh(data_lon,data_lat,var_DU_CTL, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax4, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Soil moisture',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('DU - CTL')


