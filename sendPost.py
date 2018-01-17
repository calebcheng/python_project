import json
import urllib2

data = {
        'ids': [12, 3, 4, 5, 6]
}

req = urllib2.Request('http://localhost:3000/AssetInfo')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))


# import urllib2
# urllib2.urlopen("http://localhost:3000").read()
