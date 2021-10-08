import netCDF4 as nc
import numpy

str_simu = '1x1_control'
str_out = 'control'
str_var_daily = ['lai_pft','gpp_pft','npp_pft']

for str_var in str_var_daily:
    str_in = '/data/brussel/vo/000/bvo00012/vsc10154/output/archive/' + str_simu + '/lnd/hist/' + str_simu + '.clm2.h2.2037-01-01-00000.nc'
    ncfile_in = nc.Dataset(str_in, 'a', format='NETCDF4')

    str_in2 = '/data/brussel/vo/000/bvo00012/vsc10154/output/archive/' + str_simu + '/lnd/hist/' + str_simu + '.clm2.h3.2100-01-01-00000.nc'
    ncfile_in2 = nc.Dataset(str_in2, 'a', format='NETCDF4')
    lon = ncfile_in.variables['lon']
    var_lon = numpy.array(lon)
    lat = ncfile_in.variables['lat']
    var_lat = numpy.array(lat)

    pfts1d_ixy = ncfile_in2.variables['pfts1d_ixy']
    var_pfts1d_ixy = numpy.array(pfts1d_ixy)
    pfts1d_jxy = ncfile_in2.variables['pfts1d_jxy']
    var_pfts1d_jxy = numpy.array(pfts1d_jxy)
    pfts1d_itype_veg = ncfile_in2.variables['pfts1d_itype_veg']
    var_pfts1d_itype_veg = numpy.array(pfts1d_itype_veg)

    for year in range(2000,2100):
        str_in1 = '/data/brussel/vo/000/bvo00012/vsc10154/output/archive/' + str_simu + '/lnd/hist/' + str_var + '_' + str_out + '_' + str(year) +'.nc'
        print(str_in1)
        ncfile_in1 = nc.Dataset(str_in1, 'a', format='NETCDF4')
        totvegc = ncfile_in1.variables[str_var]
        var_totvegc = numpy.array(totvegc)

        time = ncfile_in1.variables['time']
        var_time = numpy.array(time)


        str_outfile = '/data/brussel/vo/000/bvo00012/vsc10154/output/archive/' + str_simu + '/lnd/hist/' + 'CLM_' + str_var + '_' + str_out + '_' + str(year) + '.nc'
        print(str_outfile)
        ncfile_out = nc.Dataset(str_outfile, 'w', format='NETCDF4')
        ncfile_out.createDimension('lon', len(var_lon))
        ncfile_out.createDimension('lat', len(var_lat))
        ncfile_out.createDimension('time', size = None)
        ncfile_out.createDimension('pft', size = 14)

        var_TOTVEGC = numpy.ones((14, 365, len(var_lat), len(var_lon))) * -9999
        totvegc_out = ncfile_out.createVariable(str_var, 'f8', ('pft', 'time', 'lat', 'lon'))
        totvegc_out.long_name = str_var
        if str_var == 'lai_pft':
            totvegc_out.units = 'm^2/m^2'
        else:
            totvegc_out.units = 'kgCm^-2s^-1'
        totvegc_out.mode = 'time-dependent'

        var_Time = ncfile_out.createVariable('time', 'f8', ('time'))
        var_Time.units = 'days since 2000-01-01 00:00:00'
        var_Time = var_time


        for g in range(137630):
            print(g)
            if var_pfts1d_itype_veg[g] > 0:
                var_TOTVEGC[var_pfts1d_itype_veg[g]-1,0:365,pfts1d_jxy[g]-1,pfts1d_ixy[g]-1] = var_totvegc[0:365,g]

        totvegc_out[:,:,:,:] = var_TOTVEGC[:,:,:,:]
        ncfile_out.close()
