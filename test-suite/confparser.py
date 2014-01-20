

import ConfigParser, os

config = ConfigParser.RawConfigParser()
config.read('test.cfg')
dev = config.get('interface', 'dev')
ip = config.get('interface', 'ip')
essid = config.get('interface', 'essid')
dumpfile = config.get('iofiles', 'dumpfile')
clickfile = config.get('iofiles', 'clickfile')
series = config.getint('test', 'series')
sendsperseries = config.getint('test', 'sendsperseries')

print dev
print ip
print essid
print clickfile
print dumpfile
print series
print sendsperseries




