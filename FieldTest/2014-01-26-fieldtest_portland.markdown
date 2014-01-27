# Field Test Notes

**Sun 26 January 2014**

<https://github.com/psas/DxWiFi>


## Test Description

One team set up a station at Council Crest and one team set up a station
at Rocky Butte. A DxWifi connection was made between each site and tests
were executed to determine QoS between different antenna selections.

![test board](photos/test_board.jpg)

### Abbreviations

 - **CC**: Council Crest Site
 - **RB**: Rocky Butte Site
 - **OMNI**: Omnidirectional Antenna _??_
 - **BBQ**: Grill or Grid Antenna _24dbi_
 - **CPA**: Circular Patch Antenna _??_
 - **Hat**: Stubbed Helical Antenna _13dbi_


# Locations

### Distance between sites: 

 - `12.29 km ± 0.01 km`

![overview map](photos/map.png)


### Rocky Butte Location

![Rocket Butte Setup](photos/rb_setup.jpg)

From cellphote GPS

 - GPS: `45.54708 -122.566162`
 - Elevation<sup>1</sup>: `181 meters` MSL (not from GPS)

### Council Crest Location

 - GPS: `45.54708 -122.566162`
 - Elevation<sup>1</sup>: `322 meters` MSL (not from GPS)
	
**[1] Note:** _elevation from this tool: <http://www.daftlogic.com/sandbox-google-maps-find-altitude.htm>_


# Antenna Description

 - Helical
    - Circularly polarized 
 - CPA 
    - Vertical polarized circular patch antenna
 - BBQ - Grid Dish (Grill)
    - vertical polarized grid antenna
 - OMNI - Omnidirectional Antenna
    - whip style

# Power TX (all tests):

 1 Watt Average Power 3 Watt Peak


# Callsigns

 - CC: `KG7CJT`
 - RB: `KF7RAS`

# Initial setup

 - Time: 19:39 UTC
 - Antennas
    - CC: BBQ
    - RB: Helical
 - RX: -72db       Tx At CC Target
 - RX: -97db       Tx Vertical
 - RX: -inf db     Tx 180 away from CC Target
 - Tx 1W			RX: -72db

At CC Site: BBQ antenna was mounted on an aluminum 6ft ladder

At RB Site: Helical Antenna was clamped to a Al tripod


# First Test (BBQ)

 - Name: 			GRILL_1
 - Time: 			19:43 UTC
 - Setup:			BBQ CC to Helical RB
 - Series:  		5
 - Sendperseries: 	5

## Notes

Test interrupted in series 4 at 20:05 UTC

 - CC Rx: -89db
 - RB Rx: -91db


# Second Test (CPA)

 - Name:         PATCH_1
 - CC Antenna:   CPA 
 - RB Antenna:   Helical
 - Time:         20:19 UTC
 - Setup:        CPA CC to Helical RB
 - Series: 3
 - Sendperseries: 3 	

## Notes

 - CC RX: 97% of packets
 - RB RX: 3% of packets

 - CC Rx: -89db
 - RB Rx: -91db


# Third Test (OMNI)

 - Name:          OMNI
 - CC Antenna:    BBQ Antenna
 - RB Antenna:    Helical
 - Time:          1240PST
 - Setup:         Omnidirectional CC to Helical RB
 - Series:
 - Sendperseries:
 - Firstorsecond:

## Notes

 - CC Rx: -80db
 - RB Rx: -84db

# Antenna Site Survey

?


# Other Photos

![RB antenna](photos/rb_antenna.jpg)
![RB Team](photos/rb_team.jpg)
