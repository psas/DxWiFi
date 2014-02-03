#!/bin/sh

# Prints a single NMEA sentence containing the greatest latitude
# ./$0 [input.pcap [*.pcap]]

files=("$@")
[ -z "$files" ] && files=(*.pcap)

{
    for F in "${files[@]}"; do
	tcpdump -nAr "$F"
    done
} \
    | sed -nr 's/^.*(-[0-9]+dB).*$/\1/p;s/^.*(\$GPG.*)\r$/\1/p' \
    | awk -F, 'BEGIN{n=0}$1~/^-/{r=$1}/^\$/{if ($3~/^[0-9][0-9][0-9][0-9]\.[0-9]+$/&&$3>n){n=$3;p=$0","r};r=""}END{print p}'
