import netCDF4 as nc
import numpy




file_obj = nc.Dataset('E:\Forcings\\nitrogen_forcings\\ndep_NHx_NOy_2011_1x1deg.nc')
ndep = file_obj.variables['NHx_NOy']
var_ndep = numpy.array(ndep)
var_ndep = numpy.roll(var_ndep, 180, axis=1)
file_obj.close()

ncfile = nc.Dataset('D:\domain\\ndep_clm_2011_1x1_c04062021.nc', 'w', format='NETCDF4')
ncfile.createDimension('lon', 360)
ncfile.createDimension('lat', 180)
ncfile.createDimension('time', size=None)

lon = ncfile.createVariable('lon', 'f8', ('lon'))
lon.long_name = 'Longitude'
lon.units = 'degrees_east'

lat = ncfile.createVariable('lat', 'f8', ('lat'))
lat.long_name = 'Latitude'
lat.units = 'degrees_north'

time = ncfile.createVariable('time', 'f8', ('time'))
time.long_name = 'time'
time.units = 'days since 2011-01-01 00:00'
time.calendar = 'noleap'

ndep_year = ncfile.createVariable('NDEP_year', 'f8', ('time', 'lat', 'lon'), fill_value = -999)
ndep_year.long_name = 'annual nitrogen deposition'
ndep_year.units = 'g(N)/m2/yr'
ndep_year.cell_method = 'average'


lat_range = numpy.arange(-89.5, 90.5, 1)

lon_range = numpy.arange(0.5, 360.5, 1)
#lon_range = numpy.roll(lon_range, 180, axis=0)

lon[:] = lon_range
lat[:] = lat_range
time[0] = 0
#var_ndep = numpy.roll(var_ndep, 180, axis=1)
ndep_year[0, :,:] = var_ndep
ncfile.close()

