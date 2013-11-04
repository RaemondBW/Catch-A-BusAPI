from resources import agencies
import urllib2
import xml.etree.ElementTree as ET
import time

for agency in [item['agency'] for item in agencies]:
    minLat = float('inf')
    maxLat = -float('inf')
    minLon = float('inf')
    maxLon = -float('inf')
    routesPage = urllib2.urlopen("http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a="\
        + agency).read()
    root = ET.fromstring(routesPage)
    for routeTag in [route.attrib['tag'] for route in root.iter('route')]:
        # get the longitude and latitude from the route page to develop and idea of where the transit agencies are
        routePage = urllib2.urlopen("http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a="\
            +agency+"&r="+routeTag).read()
        routeRoot = ET.fromstring(routePage)
        latmin = float(routeRoot[0].attrib['latMin'])
        latmax = float(routeRoot[0].attrib['latMax'])
        lonmin = float(routeRoot[0].attrib['lonMin'])
        lonmax = float(routeRoot[0].attrib['lonMax'])
        if latmin < minLat:
            minLat = latmin
        if latmax > maxLat:
            maxLat = latmax
        if lonmin < minLon:
            minLon = lonmin
        if lonmax > maxLon:
            maxLon = lonmax
        time.sleep(.2)
    print "'minLat':'" +str(minLat) + "','maxLat':'" + str(maxLat) +"','minLon':'"+ str(minLon) +"','maxLon':'"+ str(maxLon)+"'"
    time.sleep(3)

