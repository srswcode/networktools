import pygeoip

rawdata = pygeoip.GeoIP('/pywork/geoipdb/GeoLiteCity.dat')

def ipquery(ip):
    data = rawdata.record_by_name(ip)
    country = data['country_name']
    city = data['city']
    longi = data['longitude']
    lat = data['latitude']
    print ('[x] '+str(city)+',' +str(country))
    print ('[x] Latitude: '+str(lat)+ ', Longitude: '+ str(longi))

#optional

ip = input("What's your ip? ")
print (ipquery(ip))
