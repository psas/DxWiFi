#!/bin/sh

# ./$0 [input.pcap [*.pcap]] > output.nmea

files=("$@")
[ -z "$files" ] && files=(*.pcap)

{
    for F in "${files[@]}"; do
	tcpdump -nAr "$F"
    done
} | sed -nr 's/^.*(\$GPG.*)\r$/\1/p'
