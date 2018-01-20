import json
import urllib2
import platform
import socket
import sys
import time;





hostnameStr = 'Hostname'
processorStr = 'Processor'
ipStr = 'IP'
dateStr = 'CreationDate'
consoleAddressStr = "ConsoleAddress"

consoleAddress = sys.argv[1]
print consoleAddress

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("9.9.9.9", 80))
ip = s.getsockname()[0]
s.close()

localtime = time.asctime( time.localtime(time.time()) )
hostname = socket.gethostname()

processor = platform.processor()
info = {
        hostnameStr: hostname,
        dateStr: localtime,
        processorStr: processor,
        ipStr: ip
        }



# data = {
#         'ids': [12, 3, 4, 5, 6]
# }

req = urllib2.Request(consoleAddress + '/Assets/post')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(info))




file = open(ip +'.properties', 'w')
file.write(consoleAddressStr + '=' + consoleAddress + '\n')
file.write(hostnameStr + '=' + hostname + '\n')
file.write(dateStr + '=' + localtime + '\n')
file.write(processorStr + '=' + processor + '\n')
file.write(ipStr + '=' + ip + '\n')
file.close()
