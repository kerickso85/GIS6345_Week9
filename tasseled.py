

import arcpy
from arcpy.ia import *
#from osgeo import gdal, gdal_array
import numpy as np
#b2 = Raster("p012r030_7t20000927_z19_nn20.tif")
#b3 = Raster("p012r030_7t20000927_z19_nn30.tif")
#b4 = Raster("p012r030_7t20000927_z19_nn40.tif")
#b5 = Raster("p012r030_7t20000927_z19_nn50.tif")
#b6 = Raster("p012r030_7k20000927_z19_nn62.tif") #actually importing SWIR 2 as band 6
#b7 = Raster("p012r030_7t20000927_z19_nn70.tif")

#array2 = b2.ReadAsArray()
#array3 = b3.ReadAsArray()
#array4 = b4.ReadAsArray()
#array5 = b5.ReadAsArray()
#array6 = b6.ReadAsArray()
#array7 = b7.ReadAsArray()


#compband_raster = np.stack([array2,array3,array4,array5,array6,array7])


#compband_raster = arcpy.ia.CompositeBand(["p012r030_7t20000927.met"]) #create a composite raster of LS8 bands 2-7
#print(type(compband_raster)) #sanity check
#compband_raster.save('C:/Users/krisw/OneDrive/Desktop/GIS 6345 Local/Week 9/LS7_composite.tif')

#print('Composite raster has been saved to the active directory') #to let me know when it's done :)
#print('The sensor name is',arcpy.GetRasterProperties_management("LS7_composite.tif","SENSORNAME"))

TasseledCap_raster = arcpy.ia.TasseledCap("Multispectral_p012r0_1.tif")

TasseledCap_raster.save('C:/imagery folder/TS_raster')

print('Tasseled-cap transformation raster has been saved to the active directory') #to let me know when it's done :)
