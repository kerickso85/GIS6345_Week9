

import arcpy
from arcpy.ia import *
import rasterio
from rasterio.plot import show

TasseledCap_raster = arcpy.ia.TasseledCap("Multispectral_p012r0_1.tif") #using the composite image I created with bands 2-7

TasseledCap_raster.save('C:/imagery folder/TS_raster') #this is the directory that the results of the TC transformation were saved in

print('Tasseled-cap transformation raster has been saved to the active directory.') #to let me know when it's done :)

Greenness = rasterio.open('C:/imagery folder/ts_rasterc2/w001001.adf') #access the directory containing the Band2 raster pertaining to greenness

rasterio.plot.show(Greenness) #display the greenness raster
