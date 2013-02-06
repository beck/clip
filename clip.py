# ---------------------------------------------------------------------------
# clip.py
# Created on: 2013-01-31 
# Description: Clip imagery to a specified vector boundary. 
# ---------------------------------------------------------------------------

import arcpy
import os

workspace = os.path.expanduser('~/Documents/landSanFran')
arcpy.env.workspace = workspace

# Local variables:
boundary = os.path.join(workspace, 'Vector/sanFranciscoBoundary.shp')
NLCD = os.path.join(workspace, 'NLCD/NLCD.img')
output = os.path.join(workspace, 'imagery/20100719/processing/071910')

# Process: Clip
arcpy.Clip_management(
    NLCD, 
    '9538.187689 4171021.935430 31781.231270 4201388.824867', 
    output, 
    boundary, 
    '', 
    'ClippingGeometry')

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
