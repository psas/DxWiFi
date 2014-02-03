#!/bin/sh

# ./$0 [input.pcap [*.pcap]] > output.nmea

files=("$@")
[ -z "$files" ] && files=(*.pcap)

{
    for F in "${files[@]}"; do
	tcpdump -nAr "$F"
    done
} \
    | sed -nr 's/^.*(-[0-9]+dB).*$/\1/p;s/^.*(\$GPG.*)\r$/\1/p' \
    | awk -F, '$1~/^-/{r=$1}/^\$/{print$0","r;r=""}'
