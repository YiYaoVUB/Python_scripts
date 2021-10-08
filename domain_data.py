import netCDF4 as nc
import numpy

file_obj = nc.Dataset('D:\domain\\domain.lnd.360x720_cruncep.100429.nc')

mask = file_obj.variables['mask']
var_mask = numpy.array(mask)

frac = file_obj.variables['frac']
var_frac = numpy.array(frac)

area = file_obj.variables['area']
var_area = numpy.array(area)

ncfile = nc.Dataset('D:\domain\\domain.lnd.180x360.2106151.nc', 'w', format='NETCDF4')
ncfile.createDimension('ni', 360)
ncfile.createDimension('nj', 180)
ncfile.createDimension('nv', 4)

xc = ncfile.createVariable('xc', 'f8', ('nj', 'ni'))
xc.long_name = 'longitude of grid cell center'
xc.units = 'degrees_east'
xc.bounds = 'xv'

yc = ncfile.createVariable('yc', 'f8', ('nj', 'ni'))
yc.long_name = 'latitude of grid cell center'
yc.units = 'degrees_north'
yc.bounds = 'yv'

xv = ncfile.createVariable('xv', 'f8', ('nv', 'nj', 'ni'))
xv.long_name = 'longitude of grid cell vertices'
xv.units = 'degrees_east'

yv = ncfile.createVariable('yv', 'f8', ('nv', 'nj', 'ni'))
yv.long_name = 'latitude of grid cell vertices'
yv.units = 'degrees_north'


lat_range = numpy.arange(-89.5, 90.5, 1)
lat_range = numpy.reshape(lat_range, (180, -1))
lat_data = numpy.tile(lat_range, (1, 360))
lat_bound1 = lat_data - 0.5
lat_bound2 = lat_data + 0.5

lon_range = numpy.arange(0.5, 360.5, 1)
lon_data = numpy.tile(lon_range, (180, 1))
lon_data = numpy.roll(lon_data, 180, axis=1)
lon_bound1 = lon_data - 0.5
lon_bound2 = lon_data + 0.5

yc[:, :] = lat_data
xc[:, :] = lon_data

xv[0, :,:] = lon_bound1
xv[3, :,:] = lon_bound1
xv[1, :,:] = lon_bound2
xv[2, :,:] = lon_bound2

yv[0,:,:] = lat_bound1
yv[1,:,:] = lat_bound1
yv[2,:,:] = lat_bound2
yv[3,:,:] = lat_bound2

out_mask = numpy.zeros([180, 360])
for i in range(180):
    for j in range(360):
        if ((var_mask[2*i,2*j] + var_mask[2*i+1,2*j] + var_mask[2*i,2*j+1] + var_mask[2*i+1,2*j+1])>0):
            out_mask[i,j]= 1
        else:
            out_mask[i, j] = 0

out_frac = numpy.zeros([180, 360])
out_area = numpy.zeros([180, 360])
for i in range(180):
    for j in range(360):
        out_area[i, j] = var_area[2*i,2*j] + var_area[2*i+1,2*j] + var_area[2*i,2*j+1] + var_area[2*i+1,2*j+1]
        out_frac[i, j] = (var_mask[2 * i, 2 * j]*var_area[2*i,2*j] + var_mask[2 * i + 1, 2 * j]*var_area[2*i+1,2*j] + var_mask[2 * i, 2 * j + 1]*var_area[2*i,2*j+1] + var_mask[2 * i + 1, 2 * j + 1]*var_area[2*i+1,2*j+1]) / out_area[i, j]

mask = ncfile.createVariable('mask', 'int', ('nj', 'ni'))
mask.long_name = 'land domain mask'
mask.units = 'unitless'
mask.coordinate = 'xc yc'

frac = ncfile.createVariable('frac', 'f8', ('nj', 'ni'))
frac.long_name = 'fraction of grid cell that is active'
frac.units = 'unitless'
frac.coordinate = 'xc yc'

area = ncfile.createVariable('area', 'f8', ('nj', 'ni'))
area.long_name = 'area of grid cell in radians squared'
area.units = 'unitless'
area.coordinate = 'xc yc'

out_mask = numpy.roll(out_mask, 180, axis=1)
out_frac = numpy.roll(out_frac, 180, axis=1)
out_area = numpy.roll(out_area, 180, axis=1)

mask[:,:] = out_mask
frac[:,:] = out_frac
area[:,:] = out_area


file_obj.close()