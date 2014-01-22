// udpgen.click
 
// This file is a simple, fast UDP/IP load generator, meant to be used in the
// Linux kernel module. It sends UDP/IP packets from this machine to another
// machine at a given rate. See 'udpcount.click' for a packet counter
// compatible with udpgen.click.
 
// The relevant address and rate arguments are specified as parameters to a
// compound element UDPGen.
 
// UDPGen($device, $rate, $limit, $seth, $sip, $sport, $deth, $dip, $dport);
//
//	$device		name of device to generate traffic on
//	$rate		rate to generate traffic (packets/s)
//	$limit		total number of packets to send
//      $size		bytes per packet
//	$seth		source eth addr
//	$sip		source ip addr
//	$sport		source port
//      $deth		destination eth addr
//	$dip		destination ip addr
//	$dport		destination port
 
elementclass UDPGen {
  $device, $rate, $limit, $size, $ethtype,
  $seth, $sip, $sport, $deth, $dip, $dport |
 
  source :: RevSerialSource($size, $limit);
  encap_one :: EtherEncap($ethtype, $seth, $deth);
  encap_two :: UDPIPEncap($sip, $sport, $dip, $dport);
  source -> encap_two -> encap_one -> td :: ToDevice($device);
  
}
 
u :: UDPGen(wlan2, 1250, 10000, 100, 0x0800,
	    wlan2, 192.168.0.5, 12121,
	    ff:ff:ff:ff:ff:ff, 192.168.0.255, 12121);
