#!/usr/bin/env python
from __future__ import print_function
from contextlib import contextmanager
import socket
import struct
import time

# Defines:
SEND_IP = b'192.168.0.255'
SEND_PORT = 12121
FROM_IP = b'0.0.0.0'
FROM_PORT = 21212

# Number packets to send
PACKET_N = 1000     # packets
PACKET_S = 1000     # bytes

# Send rate [Mbit/second]
RATE = 1e6 # 1 million Mbit/s

# Packet definition
PACKET = [
    {'fourcc': 'SEQN', 'struct': struct.Struct("!4sL"), 'data': lambda: s},
    {'fourcc': 'TMST', 'struct': struct.Struct("!4sQ"), 'data': lambda: int(time.time()*1000)},
]

# calculate leftover size
size = 0
for m in PACKET:
    size += m['struct'].size
leftovers = chr(0)*(PACKET_S-size)

# rate calc
timepass = (PACKET_N*PACKET_S*8)/RATE
delay = timepass/PACKET_N


@contextmanager
def udp():
    """UDP Socket creator as a context."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind((FROM_IP, FROM_PORT))
    sock.settimeout(0.1)
    yield sock
    sock.close()


def send(msg):
    with udp() as sock:
        sock.sendto(msg, (SEND_IP, SEND_PORT))

if __name__ == '__main__':

    # Sequence counter
    s = 0
    while s < PACKET_N:
        data = ''
        for m in PACKET:
            data += m['struct'].pack(m['fourcc'], m['data']())
        data += leftovers
        send(data)
        s += 1
        time.sleep(delay)
