
	


#!/usr/local/bin/python2.7

import dpkt

counter=0
ipcounter=0
tcpcounter=0
udpcounter=0

filename='groundstation12.pcap'

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
    string = string[:20] + string[21:]
    string = string[:18] + '.' + string[18:]
    
    
    string = string[:33] + string[34:]
    string = string[:31] + '.' + string[31:]
    string = string[:25] + string[26:]
    string = string[:37] + string[38:]
    print string
    #print ip[0]

#    if ip.p==dpkt.ip.IP_PROTO_TCP: 
 #      tcpcounter+=1

  #  if ip.p==dpkt.ip.IP_PROTO_UDP:
   #    udpcounter+=1



print "Total number of packets in the pcap file: ", counter
print "Total number of ip packets: ", ipcounter
print "Total number of tcp packets: ", tcpcounter
print "Total number of udp packets: ", udpcounter
