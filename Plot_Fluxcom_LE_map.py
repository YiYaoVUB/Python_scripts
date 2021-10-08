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

data_E_GLEAM = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\FLUXCOM\LE.RS.EBC-ALL.MLM-ALL.METEO-NONE.720_360.monthly.2006-2015_remap_W_m2_timmean.nc')   #load the data
data_lon = data_E_GLEAM.load_variable('lon')
data_lat = data_E_GLEAM.load_variable('lat')
data_lat = data_lat[29 :]
data_time = data_E_GLEAM.load_variable('time')
data_variable_E_GLEAM = data_E_GLEAM.load_variable('LE')

data_variable_E_GLEAM = data_variable_E_GLEAM[0, :, :]
data_variable_E_GLEAM = data_variable_E_GLEAM[29 :, :]  #no Anrctatica



data_E_NOI = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\FLUXCOM\\NOI_EFLX_LH_TOT_monmean_timmean.nc')   #load the data
data_variable_E_NOI = data_E_NOI.load_variable('EFLX_LH_TOT')
data_variable_E_NOI[data_variable_E_NOI >= 10000000000] = None
data_variable_E_NOI = data_variable_E_NOI[0, :, :]
data_variable_E_NOI = data_variable_E_NOI[29 :, :]
var_NOI_GLEAM = data_variable_E_NOI - data_variable_E_GLEAM

data_E_CTL = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\FLUXCOM\\CTL_EFLX_LH_TOT_monmean_timmean.nc')   #load the data
data_variable_E_CTL = data_E_CTL.load_variable('EFLX_LH_TOT')
data_variable_E_CTL[data_variable_E_CTL >= 10000000000] = None
data_variable_E_CTL = data_variable_E_CTL[0, :, :]
data_variable_E_CTL = data_variable_E_CTL[29 :, :]
var_CTL_NOI = data_variable_E_CTL - data_variable_E_NOI
var_CTL_GLEAM = data_variable_E_CTL - data_variable_E_GLEAM

data_E_IRR = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\FLUXCOM\\IRR_EFLX_LH_TOT_monmean_timmean.nc')   #load the data
data_variable_E_IRR = data_E_IRR.load_variable('EFLX_LH_TOT')
data_variable_E_IRR[data_variable_E_IRR >= 10000000000] = None
data_variable_E_IRR = data_variable_E_IRR[0, :, :]
data_variable_E_IRR = data_variable_E_IRR[29 :, :]
var_IRR_CTL = data_variable_E_IRR - data_variable_E_CTL
var_IRR_GLEAM = data_variable_E_IRR - data_variable_E_GLEAM
var_IRR_NOI = data_variable_E_IRR - data_variable_E_NOI

data_E_DU = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\FLUXCOM\\DU_EFLX_LH_TOT_monmean_timmean.nc')   #load the data
data_variable_E_DU = data_E_DU.load_variable('EFLX_LH_TOT')
data_variable_E_DU[data_variable_E_DU >= 10000000000] = None
data_variable_E_DU = data_variable_E_DU[0, :, :]
data_variable_E_DU = data_variable_E_DU[29 :, :]
var_DU_CTL = data_variable_E_DU - data_variable_E_CTL
var_DU_GLEAM = data_variable_E_DU - data_variable_E_GLEAM
var_DU_NOI = data_variable_E_DU - data_variable_E_NOI

data_lon = np.roll(data_lon, int(len(data_lon)/2))      #move the 0 degree to the center
data_lon[data_lon>= 180] = data_lon[data_lon>= 180] - 360
data_variable_E_GLEAM = np.roll(data_variable_E_GLEAM, int(len(data_lon)/2))
var_NOI_GLEAM  = np.roll(var_NOI_GLEAM , int(len(data_lon)/2))
var_CTL_NOI  = np.roll(var_CTL_NOI , int(len(data_lon)/2))
var_CTL_GLEAM  = np.roll(var_CTL_GLEAM , int(len(data_lon)/2))
var_IRR_CTL  = np.roll(var_IRR_CTL , int(len(data_lon)/2))
var_IRR_GLEAM  = np.roll(var_IRR_GLEAM , int(len(data_lon)/2))
var_DU_CTL  = np.roll(var_DU_CTL , int(len(data_lon)/2))
var_DU_GLEAM  = np.roll(var_DU_GLEAM , int(len(data_lon)/2))
var_IRR_NOI  = np.roll(var_IRR_NOI , int(len(data_lon)/2))
var_DU_NOI  = np.roll(var_DU_NOI , int(len(data_lon)/2))
data_variable_E_NOI = np.roll(data_variable_E_NOI , int(len(data_lon)/2))
data_variable_E_CTL = np.roll(data_variable_E_CTL , int(len(data_lon)/2))
data_variable_E_IRR = np.roll(data_variable_E_IRR , int(len(data_lon)/2))
data_variable_E_DU = np.roll(data_variable_E_DU , int(len(data_lon)/2))

for i in range(np.size(data_variable_E_DU,0)):
    for j in range(np.size(data_variable_E_DU,1)):
        if data_variable_E_GLEAM[i,j] < 0:
            var_NOI_GLEAM[i,j] = float('NaN')
            var_CTL_NOI[i, j] = float('NaN')
            var_CTL_GLEAM[i, j] = float('NaN')
            var_IRR_GLEAM[i, j] = float('NaN')
            var_IRR_CTL[i, j] = float('NaN')
            var_DU_CTL[i, j] = float('NaN')
            var_DU_GLEAM[i, j] = float('NaN')
            var_IRR_NOI[i, j] = float('NaN')
            var_DU_NOI[i, j] = float('NaN')

f = plt.figure(figsize = (12, 8))  # initiate the figure
f.subplots_adjust(hspace=0.15, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)

ax1 = plt.subplot(4, 4, 1, projection=ccrs.PlateCarree())
ax1.coastlines(linewidth=0.5)
ax1.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='Blues'
divider = make_axes_locatable(ax1)
norms = colors.DivergingNorm(vmin=0,
                             vcenter=50,
                             vmax=100)
h = ax1.pcolormesh(data_lon,data_lat,data_variable_E_GLEAM, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax1, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Latent heat flux (W/$m^2$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('FLUXCOM')

ax1 = plt.subplot(4, 4, 2, projection=ccrs.PlateCarree())
ax1.coastlines(linewidth=0.5)
ax1.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='Blues'
divider = make_axes_locatable(ax1)
norms = colors.DivergingNorm(vmin=0,
                                vcenter=50,
                             vmax=100)
h = ax1.pcolormesh(data_lon,data_lat,data_variable_E_NOI, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax1, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Latent heat flux (W/$m^2$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('NOI')

ax1 = plt.subplot(4, 4, 5, projection=ccrs.PlateCarree())
ax1.coastlines(linewidth=0.5)
ax1.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='Blues'
divider = make_axes_locatable(ax1)
norms = colors.DivergingNorm(vmin=0,
                             vcenter=50,
                             vmax=100)
h = ax1.pcolormesh(data_lon,data_lat,data_variable_E_CTL, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax1, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Latent heat flux (W/$m^2$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('CTL')

ax1 = plt.subplot(4, 4, 9, projection=ccrs.PlateCarree())
ax1.coastlines(linewidth=0.5)
ax1.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='Blues'
divider = make_axes_locatable(ax1)
norms = colors.DivergingNorm(vmin=0,
                             vcenter=50,
                             vmax=100)
h = ax1.pcolormesh(data_lon,data_lat,data_variable_E_IRR, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax1, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Latent heat flux (W/$m^2$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('IRR')

ax1 = plt.subplot(4, 4, 13, projection=ccrs.PlateCarree())
ax1.coastlines(linewidth=0.5)
ax1.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='Blues'
divider = make_axes_locatable(ax1)
norms = colors.DivergingNorm(vmin=0,
                             vcenter=50,
                             vmax=100)
h = ax1.pcolormesh(data_lon,data_lat,data_variable_E_DU, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax1, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Latent heat flux (W/$m^2$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('DU')


ax2 = plt.subplot(4, 4, 3, projection=ccrs.PlateCarree())
ax2.coastlines(linewidth=0.5)
ax2.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='bwr_r'
divider = make_axes_locatable(ax2)
norms = colors.DivergingNorm(vmin=-30,
                             vcenter=0,
                             vmax=30)
h = ax2.pcolormesh(data_lon,data_lat,var_NOI_GLEAM, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax2, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Latent heat flux (W/$m^2$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('NOI - FLUXCOM')

ax3 = plt.subplot(4, 4, 6, projection=ccrs.PlateCarree())
ax3.coastlines(linewidth=0.5)
ax3.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='bwr_r'
divider = make_axes_locatable(ax3)
norms = colors.DivergingNorm(vmin=-30,
                             vcenter=0,
                             vmax=30)
h = ax3.pcolormesh(data_lon,data_lat,var_CTL_GLEAM, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax3, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Latent heat flux (W/$m^2$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('CTL - FLUXCOM')

ax3 = plt.subplot(4, 4, 7, projection=ccrs.PlateCarree())
ax3.coastlines(linewidth=0.5)
ax3.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='bwr_r'
divider = make_axes_locatable(ax3)
norms = colors.DivergingNorm(vmin=-10,
                             vcenter=0,
                             vmax=10)
h = ax3.pcolormesh(data_lon,data_lat,var_CTL_NOI, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax3, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Latent heat flux (W/$m^2$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('CTL - NOI')

ax4 = plt.subplot(4, 4, 10, projection=ccrs.PlateCarree())
ax4.coastlines(linewidth=0.5)
ax4.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='bwr_r'
divider = make_axes_locatable(ax4)
norms = colors.DivergingNorm(vmin=-30,
                             vcenter=0,
                             vmax=30)
h = ax4.pcolormesh(data_lon,data_lat,var_IRR_GLEAM, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax4, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Latent heat flux (W/$m^2$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('IRR - FLUXCOM')

ax4 = plt.subplot(4, 4, 11, projection=ccrs.PlateCarree())
ax4.coastlines(linewidth=0.5)
ax4.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='bwr_r'
divider = make_axes_locatable(ax4)
norms = colors.DivergingNorm(vmin=-10,
                             vcenter=0,
                             vmax=10)
h = ax4.pcolormesh(data_lon,data_lat,var_IRR_NOI, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax4, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Latent heat flux (W/$m^2$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('IRR - NOI')

ax4 = plt.subplot(4, 4, 12, projection=ccrs.PlateCarree())
ax4.coastlines(linewidth=0.5)
ax4.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='bwr_r'
divider = make_axes_locatable(ax4)
norms = colors.DivergingNorm(vmin=-5,
                             vcenter=0,
                             vmax=5)
h = ax4.pcolormesh(data_lon,data_lat,var_IRR_CTL, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax4, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Latent heat flux (W/$m^2$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('IRR - CTL')

ax4 = plt.subplot(4, 4, 14, projection=ccrs.PlateCarree())
ax4.coastlines(linewidth=0.5)
ax4.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='bwr_r'
divider = make_axes_locatable(ax4)
norms = colors.DivergingNorm(vmin=-30,
                             vcenter=0,
                             vmax=30)
h = ax4.pcolormesh(data_lon,data_lat,var_DU_GLEAM, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax4, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Latent heat flux (W/$m^2$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('DU - FLUXCOM')

ax4 = plt.subplot(4, 4, 15, projection=ccrs.PlateCarree())
ax4.coastlines(linewidth=0.5)
ax4.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='bwr_r'
divider = make_axes_locatable(ax4)
norms = colors.DivergingNorm(vmin=-10,
                             vcenter=0,
                             vmax=10)
h = ax4.pcolormesh(data_lon,data_lat,var_DU_NOI, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax4, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Latent heat flux (W/$m^2$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('DU - NOI')

ax4 = plt.subplot(4, 4, 16, projection=ccrs.PlateCarree())
ax4.coastlines(linewidth=0.5)
ax4.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='bwr_r'
divider = make_axes_locatable(ax4)
norms = colors.DivergingNorm(vmin=-5,
                             vcenter=0,
                             vmax=5)
h = ax4.pcolormesh(data_lon,data_lat,var_DU_CTL, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax4, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='both', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Latent heat flux (W/$m^2$)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('DU - CTL')

plt.show()



