
	


#!/usr/local/bin/python2.7

import dpkt

counter=0
ipcounter=0
tcpcounter=0
udpcounter=0

filename='data.pcap'

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
    print str(rssi) + "," + ip[2]
    #print ip[0]

#    if ip.p==dpkt.ip.IP_PROTO_TCP: 
 #      tcpcounter+=1

  #  if ip.p==dpkt.ip.IP_PROTO_UDP:
   #    udpcounter+=1



print "Total number of packets in the pcap file: ", counter
print "Total number of ip packets: ", ipcounter
print "Total number of tcp packets: ", tcpcounter
print "Total number of udp packets: ", udpcounter
