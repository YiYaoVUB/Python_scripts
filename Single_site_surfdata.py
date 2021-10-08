import netCDF4 as nc
import numpy

ncfile = nc.Dataset('D:\domain\\surfdata_0.47x0.63_Castellaro_flood.nc', 'a', format='NETCDF4')

irrigation_method = ncfile.createVariable('irrigation_method', 'int', ('cft', 'lsmlat', 'lsmlon'))
irrigation_method.long_name = 'irrigation method'
irrigation_method.units = 'unitless'

irrigation_method = ncfile.variables['irrigation_method']
irrigation_data = numpy.ones([64, 1, 1]) * 3
irrigation_method[:, :, :] = irrigation_data

pct_urban = ncfile.variables['PCT_URBAN']
pct_urban_data = numpy.zeros([3, 1, 1])
pct_urban[:, :, :] = pct_urban_data

pct_natveg = ncfile.variables['PCT_NATVEG']
pct_natveg_data = numpy.zeros([1, 1])
pct_natveg[:,:] = pct_natveg_data

pct_crop = ncfile.variables['PCT_CROP']
pct_crop_data = numpy.ones([1, 1]) * 100
pct_crop[:,:] = pct_crop_data

pct_lake = ncfile.variables['PCT_LAKE']
pct_lake_data = numpy.zeros([1, 1])
pct_lake[:,:] = pct_lake_data

pct_cft = ncfile.variables['PCT_CFT']
pct_cft_data = numpy.zeros([64, 1, 1])
pct_cft[:,:,:] = pct_cft_data
pct_cft[3,:,:] = 100

ncfile.close()