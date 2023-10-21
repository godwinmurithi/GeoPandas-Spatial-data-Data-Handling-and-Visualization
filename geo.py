#import library
import geopandas as gpd
import contextily

#read data

url = url = 'https://raw.githubusercontent.com/jcanalesluna/bcn-geodata/master/districtes/districtes.geojson'
districts = gpd.read_file(url)
districts

#save the district GeoDataFrame into a geoJSON file:
districts.to_file("district.json", driver="GeoJSON")

#Exploring GeoDataFrames
'''You may have noticed that the GeoDataFrame 
in the previous section resembles a traditional 
pandas dataframe. The similarity makes sense, as 
GeoDataFrame is a subclass of pandas.DataFrame. 
That means it inherits many of the methods and 
attributes of pandas dataframe. What's new in GeoDataFrame 
is that it can store geometry columns (also known as 
GeoSeries) and perform spatial operations. 

The geometry column can contain any type of vector 
data, such as points, lines, and polygons. Further, 
its important to note that although a GeoDataFrame can 
have multiple GeoSeries, only one column is considered 
the active geometry, meaning that all the spatial 
operations will be based on that column. '''


#In GeoPandas, the CRS information is stored in the crs attribute:
districts.crs

districts.to_crs(epsg=2026, inplace=True)
districts.crs

#Exploring the attributes of a spatial dataset
#Area
districts['area'] = districts.area / 1000000
districts

#Centroid
districts['centroid']=districts.centroid
districts

#Boundary
districts['boundary']=districts.boundary

#Distance
from shapely.geometry import Point

sagrada_fam = Point(2.1743680500855005, 41.403656946781304)
sagrada_fam = gpd.GeoSeries(sagrada_fam, crs=4326)
sagrada_fam= sagrada_fam.to_crs(epsg=2062)
districts['sagrada_fam_dist'] = [float(sagrada_fam.distance(centroid)) / 1000 for centroid in districts.centroid]

#Plotting with GeoPandas
'''The spatial operations we have performed provide insightful information for our study.
However, visualising your geometries in space is a great way to improve your analysis.
Fortunately, creating a GeoPandas plot is super easy. You just have to call the
GeoDataFrame.plot() function, built upon Pythons matplotlib package.'''

ax= districts.plot(figsize=(10,6))
contextily.add_basemap(ax, crs=districts.crs.to_string())

'''We can make our GeoPandas plot more informative by coloring each district. 
Setting the legend to 'True' creates a legend to help interpret the colors.'''

'''
Finally, we can add the centroids of the districts and the Sagrada Familia to our map, 
as well as a title. Equally, to make the plot more compelling, we can use the nice contextily 
package to add a tile map of the actual city of Barcelona.
'''

ax= districts.plot(column='DISTRICTE', figsize=(10,6), alpha=0.3, edgecolor='black', legend=True)
contextily.add_basemap(ax, crs=districts.crs.to_string())