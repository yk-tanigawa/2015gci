import urllib2, sys
import xml.etree.ElementTree as etree

try: zipcode = sys.argv[1]
except: zipcode = '1700003'
resp = urllib2.urlopen('http://zip.cgis.biz/xml/zip.php?zn=%s'%zipcode).read()

output = {}
tree = etree.fromstring(resp)

for e in tree[-1]:
    output[e.attrib.keys()[0]] = e.attrib.values()[0]

print output
print output['state'] + output['city'] + output['address']
