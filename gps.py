# Make sure that the route.csv file is available in the current dir

# Make sure that the route.csv contain lat and long separated by comma in each
# row

# You need to do a pip install for gmplot
import csv
from gmplot import gmplot

gmap = gmplot.GoogleMapPlotter(22.1231,55.3242,13)
gmap.coloricon = "https://www.googlemapsmarkers.com/v1/%s"

with open('route.csv','r') as f:
	reader = csv.reader(f)
	for row in reader:
		lat = float(row[0])
		long = float(row[1])
		gmap.marker(lat,long,'red')
gmap.draw('delete.html')
