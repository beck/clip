# ---------------------------------------------------------------------------
# clip.py
# Created on: 2013-01-31 
# Description: Clip imagery to a specified vector boundary. 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
arcpy.env.workspace = 'C:\\Users\\90000000000\\Documents\\landSanFran\\'

# Local variables:
boundary = 'C:\\Users\\90000000000\\Documents\\landSanFran\\Vector\\sanFranciscoBoundary.shp'
NLCD = 'C:\\Users\\90000000000\\Documents\\landSanFran\\NLCD\\NLCD.img'
output = 'C:\\Users\\90000000000\\Documents\\landSanFran\\imagery\\20100719\\processing\\071910'

# Process: Clip
arcpy.Clip_management(NLCD, '9538.187689 4171021.935430 31781.231270 4201388.824867', output, boundary, "", "ClippingGeometry")

##Usage: Clip_management in_raster rectangle out_raster {in_template_dataset} {nodata_value} {NONE | ClippingGeometry}

##try:
  ##  import arcpy
  ##  arcpy.env.workspace = r"C:/Workspace"
    
    ##Clip Raster Dataset by known extent - Left Bottom Right Top
  ##  arcpy.Clip_management("image.tif","1952602.23 294196.279 1953546.23 296176.279","clip.gdb/clip", "#", "#", "NONE")
    
    ##Clip Raster Dataset with feature geometry
  ##  arcpy.Clip_management("image.tif", "#", "clip.tif","feature.shp", "0", "ClippingGeometry")
##except:
   ## print "Clip example failed."
   ## print arcpy.GetMessages()
