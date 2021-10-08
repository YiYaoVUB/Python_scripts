import pandas as pd
import numpy as np

nee_month = np.zeros([13, 12])
le_month = np.zeros([13, 12])
hs_month = np.zeros([13, 12])
gpp_month = np.zeros([13, 12])

str_infile = 'D:\Forcing_tower\Cheorwon\\Cheorwon.csv'
pd_reader = pd.read_csv(str_infile)
print(pd_reader)
data_forc = np.array(pd_reader)

le = data_forc[:, 30]
hs = data_forc[:, 29]
nee = data_forc[:, 28] / 86400
gpp = data_forc[:, 24] / 86400

gap = 0
for year in range(2016, 2019):
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
        nee_month[year-2016, i] = nee_ave
        le_ave = np.mean(le[gap + day_start[i]: gap + day_end[i]])
        le_month[year - 2016, i] = le_ave
        hs_ave = np.mean(hs[gap + day_start[i]: gap + day_end[i]])
        hs_month[year - 2016, i] = hs_ave
        gpp_ave = np.mean(gpp[gap + day_start[i]: gap + day_end[i]])
        gpp_month[year - 2016, i] = gpp_ave
    gap = gap + gap_add

f = open('D:\Forcing_tower\\C_nee.txt','w')
for i in range(13):
    for j in range(12):
        f.write(str(nee_month[i,j]) + ' ')
    f.write('\n')
f.close()

f = open('D:\Forcing_tower\\C_le.txt','w')
for i in range(13):
    for j in range(12):
        f.write(str(le_month[i,j]) + ' ')
    f.write('\n')
f.close()

f = open('D:\Forcing_tower\\C_hs.txt','w')
for i in range(13):
    for j in range(12):
        f.write(str(hs_month[i,j]) + ' ')
    f.write('\n')
f.close()

f = open('D:\Forcing_tower\\C_gpp.txt','w')
for i in range(13):
    for j in range(12):
        f.write(str(gpp_month[i,j]) + ' ')
    f.write('\n')
f.close()

print('test')