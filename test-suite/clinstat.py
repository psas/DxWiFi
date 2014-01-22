import argparse
import subprocess
import os
import time
import ConfigParser


dev = “wlan4”
clickfile = “test.click”
ip = “192.168.0.10”
essid = “rockettest1”

    subprocess.call(["stop", "network-manager"])
    subprocess.call(["ifconfig", dev, "down"])

    subprocess.call(["iwconfig", dev, "mode", "ad-hoc", "essid", essid])
    
    subprocess.call(["ifconfig", dev, ip])

    time.sleep(10)

    subprocess.call(["click-install", clickfile])

    time.sleep(15)

    subprocess.call(["click-uninstall"])
