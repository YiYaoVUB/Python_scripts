import netCDF4 as nc
import numpy
import os

str_scenario = 'hotdry'

str_output_raw = 'E:\Forcings\\' + str_scenario + '\\'

str_input_lwd_raw = 'D:\Forcings\\' + str_scenario + '_lwd\\' + str_scenario + '_lwd_'
str_input_swd_raw = 'D:\Forcings\\' + str_scenario + '_swd\\' + str_scenario + '_swd_'
str_input_pr_raw = 'D:\Forcings\\' + str_scenario + '_pr\\' + str_scenario + '_pr_'
str_input_Qair_raw = 'D:\Forcings\\' + str_scenario + '_Qair\\' + str_scenario + '_Qair_'
str_input_tas_raw = 'D:\Forcings\\' + str_scenario + '_tas\\' + str_scenario + '_tas_'
str_input_uas_raw = 'D:\Forcings\\' + str_scenario + '_uas\\' + str_scenario + '_uas_'
str_input_vas_raw = 'D:\Forcings\\' + str_scenario + '_vas\\' + str_scenario + '_vas_'

file_obj = nc.Dataset('D:\Forcings\\' + str_scenario + '_lwd\\' + str_scenario + '_lwd_063.nc')

lon = file_obj.variables['lon']
var_lon = numpy.array(lon)

lat = file_obj.variables['lat']
var_lat = numpy.array(lat)

file_obj.close()

for yr in range(1, 101):
    year = 1999 + yr


    day_start = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    day_end = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

    stryear = str(int(yr))
    if yr < 10:
        str_input_lwd = str_input_lwd_raw + '00' + stryear + '.nc'
        str_input_swd = str_input_swd_raw + '00' + stryear + '.nc'
        str_input_pr = str_input_pr_raw + '00' + stryear + '.nc'
        str_input_Qair = str_input_Qair_raw + '00' + stryear + '.nc'
        str_input_tas = str_input_tas_raw + '00' + stryear + '.nc'
        str_input_uas = str_input_uas_raw + '00' + stryear + '.nc'
        str_input_vas = str_input_vas_raw + '00' + stryear + '.nc'
    elif yr < 100:
        str_input_lwd = str_input_lwd_raw + '0' + stryear + '.nc'
        str_input_swd = str_input_swd_raw + '0' + stryear + '.nc'
        str_input_pr = str_input_pr_raw + '0' + stryear + '.nc'
        str_input_Qair = str_input_Qair_raw + '0' + stryear + '.nc'
        str_input_tas = str_input_tas_raw + '0' + stryear + '.nc'
        str_input_uas = str_input_uas_raw + '0' + stryear + '.nc'
        str_input_vas = str_input_vas_raw + '0' + stryear + '.nc'
    else:
        str_input_lwd = str_input_lwd_raw + stryear + '.nc'
        str_input_swd = str_input_swd_raw + stryear + '.nc'
        str_input_pr = str_input_pr_raw + stryear + '.nc'
        str_input_Qair = str_input_Qair_raw + stryear + '.nc'
        str_input_tas = str_input_tas_raw + stryear + '.nc'
        str_input_uas = str_input_uas_raw + stryear + '.nc'
        str_input_vas = str_input_vas_raw + stryear + '.nc'

    file_obj_lwd = nc.Dataset(str_input_lwd)
    lwd = file_obj_lwd.variables['lwd']
    var_lwd = numpy.array(lwd)
    var_lwd = numpy.roll(var_lwd, 180, axis=2)
    var_lwd[var_lwd<=0] = 0.01
    file_obj_lwd.close()


    file_obj_swd = nc.Dataset(str_input_swd)
    swd = file_obj_swd.variables['swd']
    var_swd = numpy.array(swd)
    var_swd = numpy.roll(var_swd, 180, axis=2)
    file_obj_swd.close()

    file_obj_pr = nc.Dataset(str_input_pr)
    pr = file_obj_pr.variables['pr']
    var_pr = numpy.array(pr)
    var_pr = numpy.roll(var_pr, 180, axis=2)
    file_obj_pr.close()


    file_obj_Qair = nc.Dataset(str_input_Qair)
    Qair = file_obj_Qair.variables['Qair']
    var_Qair = numpy.array(Qair)
    var_Qair = numpy.roll(var_Qair, 180, axis=2)
    file_obj_Qair.close()

    file_obj_tas = nc.Dataset(str_input_tas)
    tas = file_obj_tas.variables['tas']
    var_tas = numpy.array(tas)
    var_tas = numpy.roll(var_tas, 180, axis=2)
    file_obj_tas.close()

    file_obj_uas = nc.Dataset(str_input_uas)
    uas = file_obj_uas.variables['uas']
    var_uas = numpy.array(uas)
    var_uas = numpy.roll(var_uas, 180, axis=2)
    var_uas_sq = numpy.power(var_uas, 2)
    file_obj_uas.close()

    file_obj_vas = nc.Dataset(str_input_vas)
    vas = file_obj_vas.variables['vas']
    var_vas = numpy.array(vas)
    var_vas = numpy.roll(var_vas, 180, axis=2)
    var_vas_sq = numpy.power(var_vas, 2)
    file_obj_vas.close()

    var_was_sq = var_uas_sq + var_vas_sq
    var_was = numpy.power(var_was_sq, 0.5)
    #var_was[numpy.isnan(var_was)] = 0

    for month in range(1, 13):
        if month < 10:
            str_output = str_output_raw + str(int(year)) + '-0' + str(month) + '.nc'
        else:
            str_output = str_output_raw + str(int(year)) + '-' + str(month) + '.nc'

        ncfile = nc.Dataset(str_output, 'w', format='NETCDF4')

        ncfile.createDimension('lon', len(var_lon))
        ncfile.createDimension('lat', len(var_lat))
        ncfile.createDimension('time', size = None)
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

        zbot = ncfile.createVariable('ZBOT', 'f8', ('lat', 'lon'))
        zbot.long_name = 'observational height'
        zbot.units = 'm'
        zbot.mode = 'time-invariant'

        Time = ncfile.createVariable('time', 'f8', ('time'))
        Time.long_name = 'observation time'
        Time.units = 'days since 2000-01-01 00:00:00'
        Time.calendar = 'noleap'

        flds = ncfile.createVariable('FLDS', 'f8', ('time', 'lat', 'lon'))
        flds.long_name = 'incident longwave (FLDS)'
        flds.units = 'W/m2'
        flds.mode = 'time-dependent'

        fsds = ncfile.createVariable('FSDS', 'f8', ('time', 'lat', 'lon'))
        fsds.long_name = 'incident shortwave (FSDS)'
        fsds.units = 'W/m2'
        fsds.mode = 'time-dependent'

        prectmms = ncfile.createVariable('PRECTmms', 'f8', ('time', 'lat', 'lon'))
        prectmms.long_name = 'precipitation (PRECTmms)'
        prectmms.units = 'mm/s'
        prectmms.mode = 'time-dependent'

        shum = ncfile.createVariable('SHUM', 'f8', ('time', 'lat', 'lon'))
        shum.long_name = 'specific humidity at the lowest atm level'
        shum.units = 'kg/kg'
        shum.mode = 'time-dependent'

        tbot = ncfile.createVariable('TBOT', 'f8', ('time', 'lat', 'lon'))
        tbot.long_name = 'temperature at the lowest atm level (TBOT)'
        tbot.units = 'K'
        tbot.mode = 'time-dependent'

        wind = ncfile.createVariable('WIND', 'f8', ('time', 'lat', 'lon'))
        wind.long_name = 'wind at the lowest atm level (WIND)'
        wind.units = 'm/s'
        wind.mode = 'time-dependent'

        lat_range = numpy.arange(-89.5, 90.5, 1)
        lat_range = numpy.reshape(lat_range, (180, -1))
        lat_data = numpy.tile(lat_range, (1, 360))

        lon_range = numpy.arange(0.5, 360.5, 1)
        lon_data = numpy.tile(lon_range, (180, 1))

        zbot_data = numpy.ones((len(var_lat), len(var_lon))) * 10

        edgew[0] = 0
        edgee[0] = 360
        edgen[0] = 90
        edges[0] = -90

        latixy[:, :] = lat_data
        longxy[:, :] = lon_data
        zbot[:, :] = zbot_data

        day = range(365*(yr-1) + day_start[month-1], 365*(yr-1) + day_end[month-1])
        Time[:] = day
        flds[0:day_end[month-1] - day_start[month-1], :, :] = var_lwd[day_start[month-1]:day_end[month-1], :, :]
        fsds[0:day_end[month-1] - day_start[month-1], :, :] = var_swd[day_start[month-1]:day_end[month-1], :, :]
        prectmms[0:day_end[month-1] - day_start[month-1], :, :] = var_pr[day_start[month-1]:day_end[month-1], :, :]
        shum[0:day_end[month-1] - day_start[month-1], :, :] = var_Qair[day_start[month-1]:day_end[month-1], :, :]
        tbot[0:day_end[month-1] - day_start[month-1], :, :] = var_tas[day_start[month-1]:day_end[month-1], :, :]
        wind[0:day_end[month-1] - day_start[month-1], :, :] = var_was[day_start[month-1]:day_end[month-1], :, :]
        ncfile.close()
