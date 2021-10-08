import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc

nee_month = np.zeros([13*12])
le_month = np.zeros([13*12])
hs_month = np.zeros([13*12])
gpp_month = np.zeros([13*12])

str_infile = 'D:\Forcing_tower\\NE1.csv'
pd_reader = pd.read_csv(str_infile)
data_forc = np.array(pd_reader)

le = data_forc[:, 40]
le = data_forc[:, 42]
hs = data_forc[:, 46]
nee = data_forc[:, 52] #/ 86400
gpp = data_forc[:, 65] #/ 86400

file_obj_drip = nc.Dataset('D:\Forcing_tower\\Ne1_drip_maize_test.clm2.h3.2001-2013.nc')
EFLX_LH_TOT_drip = file_obj_drip.variables['EFLX_LH_TOT']
var_EFLX_LH_TOT_drip = np.array(EFLX_LH_TOT_drip)
FSH_drip = file_obj_drip.variables['FSH']
var_FSH_drip = np.array(FSH_drip)
NEE_drip = file_obj_drip.variables['NEE']
var_NEE_drip = np.array(NEE_drip)*86400
GPP_drip = file_obj_drip.variables['GPP']
var_GPP_drip = np.array(GPP_drip)*86400

file_obj_sprinkler = nc.Dataset('D:\Forcing_tower\\Ne1_sprinkler_maize_test.clm2.h3.2001-2013.nc')
EFLX_LH_TOT_sprinkler = file_obj_sprinkler.variables['EFLX_LH_TOT']
var_EFLX_LH_TOT_sprinkler = np.array(EFLX_LH_TOT_sprinkler)
FSH_sprinkler = file_obj_sprinkler.variables['FSH']
var_FSH_sprinkler = np.array(FSH_sprinkler)
NEE_sprinkler = file_obj_sprinkler.variables['NEE']
var_NEE_sprinkler = np.array(NEE_sprinkler)*86400
GPP_sprinkler = file_obj_sprinkler.variables['GPP']
var_GPP_sprinkler = np.array(GPP_sprinkler)*86400

gap = 0
j = 0
for year in range(2001, 2014):
    str_year = str(year)
    if (year % 4) == 0:
        day_start = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
        day_end = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
        gap_add = 366
    else:
        day_start = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        day_end = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
        gap_add = 365



    for i in range(12):
        nee_ave = np.mean(nee[gap + day_start[i]: gap + day_end[i]])
        nee_month[j*12 + i] = nee_ave
        le_ave = np.mean(le[gap + day_start[i]: gap + day_end[i]])
        le_month[j*12 + i] = le_ave
        hs_ave = np.mean(hs[gap + day_start[i]: gap + day_end[i]])
        hs_month[j*12 + i] = hs_ave
        gpp_ave = np.mean(gpp[gap + day_start[i]: gap + day_end[i]])
        gpp_month[j*12 + i] = gpp_ave

    gap = gap + gap_add
    j = j + 1

x = range(13*12)
ind = [6-0.5, 18-0.5, 30-0.5, 42-0.5, 54-0.5, 66-0.5, 78-0.5, 90-0.5, 102-0.5, 114-0.5, 126-0.5, 138-0.5, 150-0.5]
f = plt.figure(figsize = (16, 12))  # initiate the figure
f.subplots_adjust(hspace=0.2, wspace=0.2, left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)
ax1 = plt.subplot(2, 2, 1)
plt.title('Monthly latent heat flux')
line1, = ax1.plot(x, le_month, label='Obs', color = 'black', linewidth = 1, marker='o', markerfacecolor='black',markersize=3)
line2, = ax1.plot(x, var_EFLX_LH_TOT_drip, label='CTL', color = 'red', linewidth = 1, marker='^', markerfacecolor='red',markersize=5)
line3, = ax1.plot(x, var_EFLX_LH_TOT_sprinkler, label='IRR', color = 'green', linewidth = 1, marker='*', markerfacecolor='green',markersize=5)
ax1.legend()
ax1.set_ylabel('LE (W/$m^2$)')
ax1.set_xticks(ind)
ax1.set_xticklabels(( '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013'))

ax2 = plt.subplot(2, 2, 2)
plt.title('Monthly sensible heat flux')
line1, = ax2.plot(x, hs_month, label='Obs', color = 'black', linewidth = 1, marker='o', markerfacecolor='black',markersize=3)
line1, = ax2.plot(x, var_FSH_drip, label='CTL', color = 'red', linewidth = 1, marker='^', markerfacecolor='red',markersize=5)
line3, = ax2.plot(x, var_FSH_sprinkler, label='IRR', color = 'green', linewidth = 1, marker='*', markerfacecolor='green',markersize=5)
ax2.legend()
ax2.set_ylabel('HS (W/$m^2$)')
ax2.set_xticks(ind)
ax2.set_xticklabels(( '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013'))

ax3 = plt.subplot(2, 2, 3)
plt.title('Monthly net ecosystem exchange of carbon')
line1, = ax3.plot(x, nee_month, label='Obs', color = 'black', linewidth = 1, marker='o', markerfacecolor='black',markersize=3)
line1, = ax3.plot(x, var_NEE_drip, label='CTL', color = 'red', linewidth = 1, marker='^', markerfacecolor='red',markersize=5)
line3, = ax3.plot(x, var_NEE_sprinkler, label='IRR', color = 'green', linewidth = 1, marker='*', markerfacecolor='green',markersize=5)
ax3.legend()
ax3.set_ylabel('NEE (gC/$m^2$/d)')
ax3.set_xticks(ind)
ax3.set_xticklabels(( '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013'))


ax4 = plt.subplot(2, 2, 4)
plt.title('Monthly gross primary production')
line1, = ax4.plot(x, gpp_month, label='Obs', color = 'black', linewidth = 1, marker='o', markerfacecolor='black',markersize=3)
line1, = ax4.plot(x, var_GPP_drip, label='CTL', color = 'red', linewidth = 1, marker='^', markerfacecolor='red',markersize=5)
line3, = ax4.plot(x, var_GPP_sprinkler, label='IRR', color = 'green', linewidth = 1, marker='*', markerfacecolor='green',markersize=5)
ax4.legend()
ax4.set_ylabel('GPP (gC/$m^2$/d)')
ax4.set_xticks(ind)
ax4.set_xticklabels(( '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013'))




le_calcu_obs = le_month[12: -12]
hs_calcu_obs = hs_month[12: -12]
nee_calcu_obs = nee_month[12: -12]
gpp_calcu_obs = gpp_month[12: -12]

le_calcu_drip = var_EFLX_LH_TOT_drip[12: -12]
hs_calcu_drip = var_FSH_drip[12: -12]
nee_calcu_drip = var_NEE_drip[12: -12]
gpp_calcu_drip = var_GPP_drip[12: -12]

le_calcu_sprinkler = var_EFLX_LH_TOT_sprinkler[12: -12]
hs_calcu_sprinkler = var_FSH_sprinkler[12: -12]
nee_calcu_sprinkler = var_NEE_sprinkler[12: -12]
gpp_calcu_sprinkler = var_GPP_sprinkler[12: -12]

le_bias_drip = 0
le_bias_sprinkler = 0
le_rmse_drip = 0
le_rmse_sprinkler = 0

hs_bias_drip = 0
hs_bias_sprinkler = 0
hs_rmse_drip = 0
hs_rmse_sprinkler = 0

nee_bias_drip = 0
nee_bias_sprinkler = 0
nee_rmse_drip = 0
nee_rmse_sprinkler = 0

gpp_bias_drip = 0
gpp_bias_sprinkler = 0
gpp_rmse_drip = 0
gpp_rmse_sprinkler = 0
for i in range(11*12):
    le_bias_drip = le_bias_drip + le_calcu_drip[i] - le_calcu_obs[i]
    le_bias_sprinkler = le_bias_sprinkler + le_calcu_sprinkler[i] - le_calcu_obs[i]
    le_rmse_drip = le_rmse_drip + (le_calcu_drip[i] - le_calcu_obs[i])**2
    le_rmse_sprinkler = le_rmse_sprinkler + (le_calcu_sprinkler[i] - le_calcu_obs[i]) ** 2

    hs_bias_drip = hs_bias_drip + hs_calcu_drip[i] - hs_calcu_obs[i]
    hs_bias_sprinkler = hs_bias_sprinkler + hs_calcu_sprinkler[i] - hs_calcu_obs[i]
    hs_rmse_drip = hs_rmse_drip + (hs_calcu_drip[i] - hs_calcu_obs[i]) ** 2
    hs_rmse_sprinkler = hs_rmse_sprinkler + (hs_calcu_sprinkler[i] - hs_calcu_obs[i]) ** 2

    nee_bias_drip = nee_bias_drip + nee_calcu_drip[i] - nee_calcu_obs[i]
    nee_bias_sprinkler = nee_bias_sprinkler + nee_calcu_sprinkler[i] - nee_calcu_obs[i]
    nee_rmse_drip = nee_rmse_drip + (nee_calcu_drip[i] - nee_calcu_obs[i]) ** 2
    nee_rmse_sprinkler = nee_rmse_sprinkler + (nee_calcu_sprinkler[i] - nee_calcu_obs[i]) ** 2

    gpp_bias_drip = gpp_bias_drip + gpp_calcu_drip[i] - gpp_calcu_obs[i]
    gpp_bias_sprinkler = gpp_bias_sprinkler + gpp_calcu_sprinkler[i] - gpp_calcu_obs[i]
    gpp_rmse_drip = gpp_rmse_drip + (gpp_calcu_drip[i] - gpp_calcu_obs[i]) ** 2
    gpp_rmse_sprinkler = gpp_rmse_sprinkler + (gpp_calcu_sprinkler[i] - gpp_calcu_obs[i]) ** 2

le_bias_drip = le_bias_drip /11/12
le_bias_sprinkler = le_bias_sprinkler /11/12
le_rmse_drip = (le_rmse_drip/11/12)**(1/2)
le_rmse_sprinkler = (le_rmse_sprinkler/11/12)**(1/2)

hs_bias_drip = hs_bias_drip /11/12
hs_bias_sprinkler = hs_bias_sprinkler /11/12
hs_rmse_drip = (hs_rmse_drip/11/12)**(1/2)
hs_rmse_sprinkler = (hs_rmse_sprinkler/11/12)**(1/2)

nee_bias_drip = nee_bias_drip /11/12
nee_bias_sprinkler = nee_bias_sprinkler /11/12
nee_rmse_drip = (nee_rmse_drip/11/12)**(1/2)
nee_rmse_sprinkler = (nee_rmse_sprinkler/11/12)**(1/2)

gpp_bias_drip = gpp_bias_drip /11/12
gpp_bias_sprinkler = gpp_bias_sprinkler /11/12
gpp_rmse_drip = (gpp_rmse_drip/11/12)**(1/2)
gpp_rmse_sprinkler = (gpp_rmse_sprinkler/11/12)**(1/2)

plt.show()