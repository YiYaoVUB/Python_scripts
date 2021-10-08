import netCDF4 as nc
import numpy as np
import os
import time
import pandas as pd

gap = 0

str_infile = 'D:\Forcing_tower\Japan\\Japan.csv'
pd_reader = pd.read_csv(str_infile, encoding= 'unicode_escape')
data_forc = np.array(pd_reader)
temp = data_forc[:, 44] #C
humi = data_forc[:, 42] #%
wids = data_forc[:, 47] #m/s
pres = data_forc[:, 43] * 1000
sola = data_forc[:, 35]
prec = data_forc[:, 45] / 86400
long = data_forc[:, 37]

for year in range(2012, 2013):
    str_year = str(year)
    if (year % 4) == 0:
        day_start = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
        day_end = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
        gap_add = 366
    else:
        day_start = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        day_end = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
        gap_add = 365

    for month in range(1, 13):
        str_month = str(month)
        if month < 10:
            strfile = 'D:\Forcing_tower\\Japan\\' + str_year + '-0' + str_month + '.nc'
        else:
            strfile = 'D:\Forcing_tower\\Japan\\' + str_year + '-' + str_month + '.nc'

        ncfile = nc.Dataset(strfile, 'w', format='NETCDF4')
        ncfile.createDimension('lon', 1)
        ncfile.createDimension('lat', 1)
        ncfile.createDimension('time', size=None)
        ncfile.createDimension('scalar', 1)

        edgew = ncfile.createVariable('EDGEW', 'f8', ('scalar',))
        edgew.long_name = 'western edge in atmospheric data'
        edgew.units = 'degrees E'
        edgew.mode = 'time-invariant'

        edgee = ncfile.createVariable('EDGEE', 'f8', ('scalar',))
        edgee.long_name = 'Eastern edge in atmospheric data'
        edgee.units = 'degrees E'
        edgee.mode = 'time-invariant'

        longxy = ncfile.createVariable('LONGXY', 'f8', ('lat', 'lon'))
        longxy.long_name = 'longitude'
        longxy.units = 'degrees E'
        longxy.mode = 'time-invariant'

        edgen = ncfile.createVariable('EDGEN', 'f8', ('scalar',))
        edgen.long_name = 'northern edge in atmospheric data'
        edgen.units = 'degrees N'
        edgen.mode = 'time-invariant'

        edges = ncfile.createVariable('EDGES', 'f8', ('scalar',))
        edges.long_name = 'southern edge in atmospheric data'
        edges.units = 'degrees N'
        edges.mode = 'time-invariant'

        latixy = ncfile.createVariable('LATIXY', 'f8', ('lat', 'lon'))
        latixy.long_name = 'latitude'
        latixy.units = 'degrees N'
        latixy.mode = 'time-invariant'

        edgew[0] = 139.6875
        edgee[0] = 140.3125
        longxy[0, 0] = 140.0000
        edgen[0] = 36.187989556135730
        edges[0] = 35.718015665796300
        latixy[0, 0] = 35.953002610966020

        Time = ncfile.createVariable('time', 'f8', ('time'))
        Time.long_name = 'observation time'
        Time.units = 'days since 2012-01-01 00:00:00'
        Time.calendar = 'gregorian'



        fsds = ncfile.createVariable('FSDS', 'f8', ('time', 'lat', 'lon'))
        fsds.long_name = 'incident solar (FSDS)'
        fsds.units = 'W/m2'
        fsds.mode = 'time-dependent'

        flds = ncfile.createVariable('FLDS', 'f8', ('time', 'lat', 'lon'))
        flds.long_name = 'incident longwave (FLDS)'
        flds.units = 'W/m2'
        flds.mode = 'time-dependent'

        prectmms = ncfile.createVariable('PRECTmms', 'f8', ('time', 'lat', 'lon'))
        prectmms.long_name = 'precipitation (PRECTmms)'
        prectmms.units = 'mm/s'
        prectmms.mode = 'time-dependent'

        psrf = ncfile.createVariable('PSRF', 'f8', ('time', 'lat', 'lon'))
        psrf.long_name = 'pressure at the lowest atm level (PSRF)'
        psrf.units = 'Pa'
        psrf.mode = 'time-dependent'

        rh = ncfile.createVariable('RH', 'f8', ('time', 'lat', 'lon'))
        rh.long_name = 'relative humidity at the lowest atm level (RH)'
        rh.units = '%'
        rh.mode = 'time-dependent'


        tbot = ncfile.createVariable('TBOT', 'f8', ('time', 'lat', 'lon'))
        tbot.long_name = 'temperature at the lowest atm level (TBOT)'
        tbot.units = 'C'
        tbot.mode = 'time-dependent'

        # tdew = ncfile.createVariable('TDEW', 'f4', ('time', 'lat', 'lon'))
        wind = ncfile.createVariable('WIND', 'f8', ('time', 'lat', 'lon'))
        wind.long_name = 'wind at the lowest atm level (WIND)'
        wind.units = 'm/s'
        wind.mode = 'time-dependent'


        days = range(gap + day_start[month-1], gap + day_end[month-1])
        Time[0:day_end[month-1] - day_start[month-1]] = days
        print(len(sola[day_start[month-1]:day_end[month-1]]))
        fsds[0:day_end[month-1] - day_start[month-1],0,0] = sola[gap + day_start[month-1]:gap + day_end[month-1]]
        flds[0:day_end[month - 1] - day_start[month - 1], 0, 0] = long[gap + day_start[month - 1]:gap + day_end[month - 1]]
        prectmms[0:day_end[month-1] - day_start[month-1],0,0] = prec[gap + day_start[month-1]:gap + day_end[month-1]]
        wind[0:day_end[month-1] - day_start[month-1],0,0] = wids[gap + day_start[month-1]:gap + day_end[month-1]]
        rh[0:day_end[month-1] - day_start[month-1],0,0] = humi[gap + day_start[month-1]:gap + day_end[month-1]]
        psrf[0:day_end[month-1] - day_start[month-1],0,0] = pres[gap + day_start[month-1]:gap + day_end[month-1]]
        tbot[0:day_end[month-1] - day_start[month-1],0,0] = temp[gap + day_start[month-1]:gap + day_end[month-1]]

        ncfile.close()
    gap = gap + gap_add








