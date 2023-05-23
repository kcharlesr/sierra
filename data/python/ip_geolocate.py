import geocoder
from matplotlib.cbook import ls_mapper
with open("ip.txt") as filp:
    contents = filp.read()
    ip_add = contents.split()

# ip_add = '135.125.190.144'
for i in ip_add:
    g = geocoder.ip(i)
    # print(i, g.city, g.latlng)
    print(i, g.lat, g.lng, g.city, g.postal)