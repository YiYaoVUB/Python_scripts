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


data_R_NOI = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\QRUNOFF\\NOI_QRUNOFF_timmean.nc')   #load the data
data_variable_R_NOI = data_R_NOI.load_variable('QRUNOFF')
data_lon = data_R_NOI.load_variable('lon')
data_lat = data_R_NOI.load_variable('lat')
data_lat = data_lat[29 :]
data_time = data_R_NOI.load_variable('time')
data_variable_R_NOI[data_variable_R_NOI >= 10000000000] = None
data_variable_R_NOI = data_variable_R_NOI[0, :, :]
data_variable_R_NOI = data_variable_R_NOI[29 :, :]


data_R_CTL = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\QRUNOFF\\CTL_QRUNOFF_timmean.nc')   #load the data
data_variable_R_CTL = data_R_CTL.load_variable('QRUNOFF')
data_variable_R_CTL[data_variable_R_CTL >= 10000000000] = None
data_variable_R_CTL = data_variable_R_CTL[0, :, :]
data_variable_R_CTL = data_variable_R_CTL[29 :, :]
var_CTL_NOI = data_variable_R_CTL - data_variable_R_NOI

data_I_CTL = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\QRUNOFF\\CTL_QIRRIG_timmean.nc')   #load the data
data_variable_I_CTL = data_I_CTL.load_variable('QIRRIG_FROM_SURFACE')
data_variable_I_CTL[data_variable_I_CTL >= 10000000000] = None
data_variable_I_CTL = data_variable_I_CTL[0, :, :]
data_variable_I_CTL = data_variable_I_CTL[29 :, :]
var_CTL_NOI_new = (data_variable_R_CTL + data_variable_I_CTL - data_variable_R_NOI)/data_variable_I_CTL


data_R_IRR = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\QRUNOFF\\IRR_QRUNOFF_timmean.nc')   #load the data
data_variable_R_IRR = data_R_IRR.load_variable('QRUNOFF')
data_variable_R_IRR[data_variable_R_IRR >= 10000000000] = None
data_variable_R_IRR = data_variable_R_IRR[0, :, :]
data_variable_R_IRR = data_variable_R_IRR[29 :, :]
var_IRR_CTL = data_variable_R_IRR - data_variable_R_CTL
var_IRR_NOI = data_variable_R_IRR - data_variable_R_NOI

data_I_IRR = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\QRUNOFF\\IRR_QIRRIG_timmean.nc')   #load the data
data_variable_I_IRR = data_I_IRR.load_variable('QIRRIG_FROM_SURFACE')
data_variable_I_IRR[data_variable_I_IRR >= 10000000000] = None
data_variable_I_IRR = data_variable_I_IRR[0, :, :]
data_variable_I_IRR = data_variable_I_IRR[29 :, :]
var_IRR_NOI_new = (data_variable_R_IRR + data_variable_I_IRR - data_variable_R_NOI)/data_variable_I_IRR
var_IRR_CTL_new = (data_variable_I_IRR+data_variable_R_IRR - data_variable_I_CTL - data_variable_R_CTL)/data_variable_I_IRR


data_R_DU = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\QRUNOFF\\DU_QRUNOFF_timmean.nc')   #load the data
data_variable_R_DU = data_R_DU.load_variable('QRUNOFF')
data_variable_R_DU[data_variable_R_DU >= 10000000000] = None
data_variable_R_DU = data_variable_R_DU[0, :, :]
data_variable_R_DU = data_variable_R_DU[29 :, :]
var_DU_CTL = data_variable_R_DU - data_variable_R_CTL
var_DU_NOI = data_variable_R_DU - data_variable_R_NOI

data_I_DU = Data_from_nc('E:\Data_Evaluation\Data_for_evaluation\QRUNOFF\\DU_QIRRIG_timmean.nc')   #load the data
data_variable_I_DU = data_I_DU.load_variable('QIRRIG_FROM_SURFACE')
data_variable_I_DU[data_variable_I_DU >= 10000000000] = None
data_variable_I_DU = data_variable_I_DU[0, :, :]
data_variable_I_DU = data_variable_I_DU[29 :, :]
var_DU_NOI_new = (data_variable_R_DU + data_variable_I_DU - data_variable_R_NOI)/data_variable_I_DU
var_DU_CTL_new = (data_variable_R_DU + data_variable_I_DU - data_variable_I_CTL - data_variable_R_CTL)/data_variable_I_DU


data_lon = np.roll(data_lon, int(len(data_lon)/2))      #move the 0 degree to the center
data_lon[data_lon>= 180] = data_lon[data_lon>= 180] - 360


var_CTL_NOI  = np.roll(var_CTL_NOI , int(len(data_lon)/2))
var_CTL_NOI_new  = np.roll(var_CTL_NOI_new , int(len(data_lon)/2))
var_IRR_CTL  = np.roll(var_IRR_CTL , int(len(data_lon)/2))
var_IRR_CTL_new  = np.roll(var_IRR_CTL_new , int(len(data_lon)/2))
var_IRR_NOI_new  = np.roll(var_IRR_NOI_new , int(len(data_lon)/2))
var_DU_CTL  = np.roll(var_DU_CTL , int(len(data_lon)/2))
var_DU_CTL_new  = np.roll(var_DU_CTL_new , int(len(data_lon)/2))
var_DU_NOI_new  = np.roll(var_DU_NOI_new , int(len(data_lon)/2))
var_IRR_NOI  = np.roll(var_IRR_NOI , int(len(data_lon)/2))
var_DU_NOI  = np.roll(var_DU_NOI , int(len(data_lon)/2))
data_variable_R_NOI = np.roll(data_variable_R_NOI , int(len(data_lon)/2))
data_variable_R_CTL = np.roll(data_variable_R_CTL , int(len(data_lon)/2))
data_variable_R_IRR = np.roll(data_variable_R_IRR , int(len(data_lon)/2))
data_variable_R_DU = np.roll(data_variable_R_DU , int(len(data_lon)/2))
data_variable_I_CTL = np.roll(data_variable_I_CTL , int(len(data_lon)/2))
data_variable_I_IRR = np.roll(data_variable_I_IRR , int(len(data_lon)/2))
data_variable_I_DU = np.roll(data_variable_I_DU , int(len(data_lon)/2))

f = plt.figure(figsize = (12, 8))  # initiate the figure
f.subplots_adjust(hspace=0.15, wspace=0.1, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)


ax3 = plt.subplot(2, 2, 1, projection=ccrs.PlateCarree())
ax3.coastlines(linewidth=0.5)
ax3.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='Blues'
divider = make_axes_locatable(ax3)
norms = colors.DivergingNorm(vmin=0,
                             vcenter=0.5,
                             vmax=1)
h = ax3.pcolormesh(data_lon,data_lat,var_CTL_NOI_new, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax3, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='neither', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Runoff loss / Irrigation water (mm/mm)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('CTL')



ax4 = plt.subplot(2, 2, 3, projection=ccrs.PlateCarree())
ax4.coastlines(linewidth=0.5)
ax4.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='Blues'
divider = make_axes_locatable(ax4)
norms = colors.DivergingNorm(vmin=0,
                             vcenter=0.5,
                             vmax=1)
h = ax4.pcolormesh(data_lon,data_lat,var_IRR_NOI_new, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax4, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='neither', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Runoff loss / Irrigation water (mm/mm)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('IRR')


ax4 = plt.subplot(2, 2, 4, projection=ccrs.PlateCarree())
ax4.coastlines(linewidth=0.5)
ax4.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
cmap='Blues'
divider = make_axes_locatable(ax4)
norms = colors.DivergingNorm(vmin=0,
                             vcenter=0.5,
                             vmax=1)
h = ax4.pcolormesh(data_lon,data_lat,var_DU_NOI_new, cmap=cmap, rasterized=True, norm=norms)
cbar   = f.colorbar(h, ax=ax4, cmap=cmap,
                               spacing='uniform',
                               orientation='horizontal',
                               extend='neither', shrink = 1, pad = 0, aspect = 50)
cbar.set_label('Runoff loss / Irrigation water (mm/mm)',fontsize = 8)
ticklabs = cbar.ax.get_xticklabels()
cbar.ax.set_xticklabels(ticklabs, fontsize=8)
plt.title('DU')


plt.show()



