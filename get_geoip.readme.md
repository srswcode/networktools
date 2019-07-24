How To Geolocate an IP Address with Python - May 18, 2014
Python 2.7.3

In order to geolocate an IP address with Python you will need a database to match an IP to a location. 
I am using the Maxmind database, which is available for free.

wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
gunzip GeoLiteCity.dat.gz

Next, we install the Pure Python API for Maxmind's GeoIP databases (https://github.com/appliedsec/pygeoip)

sudo pip install pygeoip
-----------------------------------------------------
UPDATE - PYTHON 3 (Ubuntu 16.04)

sudo pip3 install pygeoip

Download Maxmind location-data

user@user:~$ cd Desktop
user@user:~/Desktop$ mkdir geolocate
user@user:~/Desktop$ cd geolocate
user@user:~/Desktop/geolocate$ wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
user@user:~/Desktop/geolocate$ gunzip GeoLiteCity.dat.gz

-----------------------------------------------------
Run the code

user@user:~/Desktop/geolocate$ python3 geo.py
What's your ip? 207.38.138.230
[x] New York,United States
[x] Latitude: 40.7449, Longitude: -73.9782

-----------------------------------------------------
-----------------------------------------------------
-----------------------------------------------------
Gnarlodious18 May 2014 at 08:42

Groovy! Except for OSX I had to say:

cd /usr/local/
sudo curl -O http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
sudo gunzip /usr/local/GeoLiteCity.dat.gz

sudo pip install pygeoip

python2.7
import pygeoip
rawdata = pygeoip.GeoIP('/usr/local/GeoLiteCity.dat')

def ipquery(ip):
data = rawdata.record_by_name(ip)
country = data['country_name']
city = data['city']
longi = data['longitude']
lat = data['latitude']
print '[x] '+str(city)+',' +str(country)
print '[x] Latitude: '+str(lat)+ ', Longitude: '+ str(longi)

ip='207.38.138.230'
ipquery(ip)

[x] New York,United States
[x] Latitude: 40.7143, Longitude: -74.006

Reply
Thanga Rajan8 September 2015 at 04:04

its not working for me
Reply

    Mike M25 June 2016 at 08:49

    it's still working...

Daniel23 June 2016 at 08:47

Neither for me...
Reply

    Mike M25 June 2016 at 08:49

    Just tried the code and it is still working. What problems did you have?

Martina1 December 2017 at 07:27

The benefit of this plan is that it can deal with a substantial number of addresses, in particular 4.3 billion myip info
Reply
Unknown30 April 2019 at 03:23

Various IP geolocation API services are providing free geolocation information, 
e.g: http://ipgeolocaion.io, IPStack, IP2Location, IP-API, DB-IP, IP info, etc. 
Each service has different features. You can select a service according to your demand.

Among these services, You can easily find the geolocation information of an IP address 
freely by using ipgeolocation.io. ipgeolocation.io provides 45000 free requests per month / 1500 per day.

You can use it by following these simple steps:

Just go to https://ipgeolocation.io/ and signup here.
Then sign in and select a free plan.
After signing in, go to the Dashboard and copy the API key.
Use this API key to locate the IP address.
In order to find geolocation information about an IP address, pass it as a query parameter like below. 
Note that apiKey is also passed as a query parameter for authorization.

# Get geolocation for an IPv4 IP Address = 8.8.8.8
$ curl 'https://api.ipgeolocation.io/ipg...'

The JSON response will be as follows:
{
"ip": "8.8.8.8",
"hostname": "http://google-public-dns-a.googl...",
"continent_code": "NA",
"continent_name": "North America",
"country_code2": "US",
"country_code3": "USA",
"country_name": "United States",
"country_capital": "Washington",
"state_prov": "California",
"district": "",
"city": "Mountain View",
"zipcode": "94043",
"latitude": "37.4229",
"longitude": "-122.085",
"is_eu": false,
"calling_code": "+1",
"country_tld": ".us",
"languages": "en-US,es-US,haw,fr",
"country_flag": "
",

"isp": "Level 3 Communications",
"connection_type": "",
"organization": "Google Inc.",
"geoname_id": "5375480",
"currency": {
"code": "USD",
"name": "US Dollar",
"symbol": "$"
},
"time_zone": {
"name": "America/Los_Angeles",
"offset": -8,
"current_time": "2019-01-14 03:30:00.135-0800",
"current_time_unix": 1547465400.135,
"is_dst": false,
"dst_savings": 1
}
}

The geolocation information for an IP address from the IP Geolocation API can be retrieved in the following languages:
English (en)
German (de)
Russian (ru)
Japanese (ja)
French (fr)
Chinese Simplified (cn)
Spanish (es)
Czech (cs)
Italian (it)
Disclaimer: I am working for http://ipgeolocaion.io
