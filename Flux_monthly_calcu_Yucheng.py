import pandas as pd
import numpy as np

nee_month = np.zeros([8, 12])
le_month = np.zeros([8, 12])
hs_month = np.zeros([8, 12])
for year in range(2003, 2011):
    str_year = str(year)
    if (year % 4) == 0:
        day_start = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
        day_end = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
        gap_add = 366
    else:
        day_start = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        day_end = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
        gap_add = 365

    str_infile = 'D:\Forcing_tower\YCA_F_DAILY\YCA_F_DAILY_YCA_F_daily\data\\' + str_year + '.csv'
    pd_reader = pd.read_csv(str_infile)
    print(pd_reader)
    data_forc = np.array(pd_reader)
    nee = data_forc[:, 3] / 86400
    le = data_forc[:, 6] * 11.574
    hs = data_forc[:, 7] * 11.574

    for i in range(12):
        nee_ave = np.mean(nee[day_start[i]: day_end[i]])
        nee_month[year-2003, i] = nee_ave
        le_ave = np.mean(le[day_start[i]: day_end[i]])
        le_month[year - 2003, i] = le_ave
        hs_ave = np.mean(hs[day_start[i]: day_end[i]])
        hs_month[year - 2003, i] = hs_ave

f = open('D:\Forcing_tower\YCA_F_DAILY\YCA_F_DAILY_YCA_F_daily\data\\nee.txt','w')
for i in range(8):
    for j in range(12):
        f.write(str(nee_month[i,j]) + ' ')
    f.write('\n')
f.close()

f = open('D:\Forcing_tower\YCA_F_DAILY\YCA_F_DAILY_YCA_F_daily\data\\le.txt','w')
for i in range(8):
    for j in range(12):
        f.write(str(le_month[i,j]) + ' ')
    f.write('\n')
f.close()

f = open('D:\Forcing_tower\YCA_F_DAILY\YCA_F_DAILY_YCA_F_daily\data\\hs.txt','w')
for i in range(8):
    for j in range(12):
        f.write(str(hs_month[i,j]) + ' ')
    f.write('\n')
f.close()
print('test')