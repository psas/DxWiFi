
	


#!/usr/local/bin/python2.7

import dpkt
import re


counter=0
ipcounter=0
tcpcounter=0
udpcounter=0
comp = "a"

for i in range (1, 42):
	filename='ground' + str(i) + '.pcap'

	for ts, pkt in dpkt.pcap.Reader(open(filename,'r')):

	    counter+=1
	    eth=dpkt.ethernet.Ethernet(pkt) 
	   # if eth.type!=dpkt.ethernet.ETH_TYPE_IP:
	      # continue
	     
	    tag = "*"

	    tap=dpkt.radiotap.Radiotap(pkt)

	    rssi = -(256-tap.ant_sig.db)


	    ip=eth.data
	    ipcounter+=1
	    ip = ip.partition(tag)
	    ip = ip[0].partition("GPGGA")
	    string =  str(rssi) + "," + ip[2]
	  
	    #match = re.findall(r'[\w. ,-]+', string)
	    #print match[0]
   
	    #string = string[:20] + string[21:]
	    string = string[:18] + ' ' + string[18:]
	    
	    
	    #string = string[:33] + string[34:]
	    string = string[:32] + ' ' + string[32:]
	    string = string[:26] + string[27:]
	    string = string[:39] + string[40:]
	    latlon = string[16:27] + ' ' + string[28:40]
	    DDD = string[16:26] + ' ' + string[28:39]
	    try:
	       lat = float(DDD[3:10])/60
	    except:
	       lat = "0000000"
	    try:
	       lon = float(DDD[14:22])/60
	    except:
	       lon = "0000000"
	    #print str(lat)[1:8] + " " + str(lon)[1:8]
	    DDD = DDD[:2] + str(lat)[1:8] + "N " + DDD[11:14]+ str(lon)[1:8] + "W"
            string = string[:77] + ',' + DDD   
	  #  print latlon
	 
	    match = re.findall(r'[\w. ,-]+', string)
	    if comp != latlon:
	    	print match[0]
	    comp = latlon
	    #print ip[0]

	#    if ip.p==dpkt.ip.IP_PROTO_TCP: 
	 #      tcpcounter+=1

	  #  if ip.p==dpkt.ip.IP_PROTO_UDP:
	   #    udpcounter+=1



print "Total number of packets in the pcap file: ", counter
print "Total number of ip packets: ", ipcounter
print "Total number of tcp packets: ", tcpcounter
print "Total number of udp packets: ", udpcounter
