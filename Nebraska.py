import netCDF4 as nc
import numpy as np
import os
import time
import pandas as pd
import math
gap = 0

str_obsfile = 'D:\Forcing_tower\\NE1.csv'
pd_reader = pd.read_csv(str_obsfile, encoding= 'unicode_escape')
data_forc = np.array(pd_reader)
lh_obs = data_forc[:, 40] #C
sh_obs = data_forc[:, 46] #%
#gpp_obs = data_forc[:, 20]
#sf_obs = data_forc[:, 46] * 100
sm_obs = data_forc[:, 36] / 100
lw_obs = data_forc[:, 30]
nee_obs = data_forc[:, 52]  * 12 / 1000000
sw_obs = data_forc[:, 28]

str_simfile1 = 'D:\Tower_result\\'
site_name = 'Nebraska'

bias_noirr = np.zeros([5,1])
bias_drip = np.zeros([5,1])
bias_flood = np.zeros([5,1])
rmse_noirr = np.zeros([5,1])
rmse_drip = np.zeros([5,1])
rmse_flood = np.zeros([5,1])

index = 0
for str_var in ['EFLX_LH_TOT', 'FSH', 'NEE', 'SWup', 'LWup']:

    str_file_noirr = 'D:\Tower_result\\' + site_name + '_noirr\\' + site_name + '_noirr_' + str_var
    str_file_drip = 'D:\Tower_result\\' + site_name + '_drip\\' + site_name + '_drip_' + str_var
    str_file_flood = 'D:\Tower_result\\' + site_name + '_sprinkler\\' + site_name + '_sprinkler_' + str_var

    file_obj_noirr = nc.Dataset(str_file_noirr)
    file_obj_drip = nc.Dataset(str_file_drip)
    file_obj_flood = nc.Dataset(str_file_flood)

    var_noirr = file_obj_noirr.variables[str_var]
    var_drip = file_obj_drip.variables[str_var]
    var_flood = file_obj_flood.variables[str_var]

    noirr = np.array(var_noirr)
    drip = np.array(var_drip)
    flood = np.array(var_flood)

    if str_var == 'H2OSOI':
        noirr = noirr[:,0,:]
        drip = drip[:, 0, :]
        flood = flood[:, 0, :]

    if str_var == 'EFLX_LH_TOT':
        obs = lh_obs
    if str_var == 'FSH':
        obs = sh_obs
    if str_var == 'H2OSOI':
        obs = sm_obs
    if str_var == 'NEE':
        obs = nee_obs
    if str_var == 'SWup':
        obs = sw_obs
    if str_var == 'LWup':
        obs = lw_obs

    bias_noirr_sum = 0
    bias_drip_sum = 0
    bias_flood_sum = 0

    rmse_noirr_sum = 0
    rmse_drip_sum = 0
    rmse_flood_sum = 0

    num = 0
    threshold = -1000
    if str_var == 'H2OSOI':
        threshold = -1
    if str_var == 'NEE':
        threshold = -0.1
    if str_var == 'H2OSFC':
        threshold = 0
    for i in range(len(noirr) - 1):
        if obs[i] > threshold:
            bias_noirr_temp = noirr[i] - obs[i]
            bias_drip_temp = drip[i] - obs[i]
            bias_flood_temp = flood[i] - obs[i]

            bias_noirr_sum = bias_noirr_sum + bias_noirr_temp
            bias_drip_sum = bias_drip_sum + bias_drip_temp
            bias_flood_sum = bias_flood_sum + bias_flood_temp

            rmse_noirr_sum = rmse_noirr_sum + bias_noirr_temp**2
            rmse_drip_sum = rmse_drip_sum + bias_drip_temp**2
            rmse_flood_sum = rmse_flood_sum + bias_flood_temp**2

            num = num + 1
    if num == 0:
        index = index + 1
        continue

    else:
        bias_noirr[index] = bias_noirr_sum/num
        bias_drip[index] = bias_drip_sum/num
        bias_flood[index] = bias_flood_sum/num
        rmse_noirr[index] = math.sqrt(rmse_noirr_sum/num)
        rmse_drip[index] = math.sqrt(rmse_drip_sum/num)
        rmse_flood[index] = math.sqrt(rmse_flood_sum/num)

        index = index + 1

        print('test')

bias = np.hstack((bias_noirr, bias_drip, bias_flood))
rmse = np.hstack((rmse_noirr, rmse_drip, rmse_flood))

np.savetxt("E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\Nebraska_Bias.csv", bias, delimiter=',')
np.savetxt("E:\Data_Evaluation\Data_for_evaluation\Irrigation_amount\Fig\\Nebraska_Rmse.csv", rmse, delimiter=',')

print('test')


