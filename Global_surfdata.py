import netCDF4 as nc
import numpy

ncfile = nc.Dataset('D:\domain\\surfdata_1x1_hist_78pfts_CMIP6_simyr2000_c210608.nc', 'a', format='NETCDF4')

pct_natveg = ncfile.variables['PCT_NATVEG']
pct_natveg_data = numpy.array(pct_natveg)

pct_crop = ncfile.variables['PCT_CROP']
pct_crop_data = numpy.array(pct_crop)
pct_natveg_data = pct_natveg_data + pct_crop_data
pct_natveg[:,:] = pct_natveg_data

pct_crop_data = numpy.zeros([180, 360])
pct_crop[:,:] = pct_crop_data

ncfile.close()