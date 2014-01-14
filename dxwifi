#!/bin/bash
#TODO test or warn about click installation

#Checks whether click is installed.  Exits if not
#Automatically calls click-uninstall for safety
test_click()
{
	click --version > /dev/null 2>&1
	if [ "$?" -eq 127 ] ; then
		echo "You must have click installed to use $0."
		exit 1
	fi
	click-uninstall #The only truly necessary call to this
}

#Exits if not run as root
test_root()
{
	if [[ $UID -ne 0 ]]; then
		echo "$0 must be run as root"
		exit 1
	fi
}

#Turns on network manager, which should revert
#any crazy settings
set_internet()
{
	click-uninstall #Redundant-- for safety!
	start network-manager > /dev/null 2>&1
	echo "Network manager started."
	exit 0
}

#Locates the and click-installs the .click file located in $2
set_click()
{
	if [ -z $2 ]; then
		echo "Please enter a .click file to load"
		exit 1
	fi

	#Only configures the wireless environment if a device is specified
	if [ ! -z $3 ]; then

		click-uninstall #Redundant-- for safety!

		stop network-manager > /dev/null 2>&1

		#Bring down and configure the interface
		ifconfig $3 down
		if [[ $? -ne 0 ]]; then exit; fi
		iwconfig $3 mode ad-hoc
		if [[ $? -ne 0 ]]; then exit; fi
	
		#Set interface ip
		if [ ! -z $4 ]; then
			if [[ $4 == *.*.*.* ]]
			then
				ifconfig $3 $4
			else
				ifconfig $3 192.168.0.$4
			fi
			if [[ $? -ne 0 ]]; then exit; fi
		else
			ifconfig $3 up
		fi
	fi

	#Installs the click file if found
	if [ -e ./$2 ] #Current directory
		then
			click-install $2
			if [[ $? -ne 0 ]]; then exit; fi
			echo "$(pwd)/$2 loaded."
		else
			if [ -e $HOME/Click-Configs/$2 ] #Click-Configs directory
				then
					click-install $HOME/Click-Configs/$2
					if [[ $? -ne 0 ]]; then exit; fi
					echo "$HOME/Click-Configs/$2 loaded." 
				else
					echo "Unable to locate $2."
					exit 1
			fi
	fi
	echo "Remember to run dxwifi stop"
	exit 0
}

#Sets configuration for non-click applications
set_test()
{
	click-uninstall #Redundant-- for safety!

	stop network-manager > /dev/null 2>&1

	#Configures interface
	ifconfig $2 down
	if [[ $? -ne 0 ]]; then exit; fi
	iwconfig $2 mode ad-hoc
	if [[ $? -ne 0 ]]; then exit; fi

	#Sets ip if the user specified one
	if [ ! -z $3 ]; then
		if [[ $3 == *.*.*.* ]]
		then
			ifconfig $2 $3
		else
			ifconfig $2 192.168.0.$3
	
			if [[ $? -ne 0 ]]
			then
				echo "Invalid IP address: $3"
				exit
			fi
		fi
	else
	ifconfig $2 up
	fi
}

test_click
test_root

case "$@" in
	"") echo "Usage: $0 [internet]"
		 echo "       $0 [click <clickfile.click> <iface (optional)>"
		 echo "                          <ip (optional, and default is 192.168.0.INPUT)>]"
		 echo	"       $0 [test <iface> <ip (as above)>]"
		 echo "       $0 [stop]"
		;;
	i*) set_internet	
		;;
	c*) set_click $@
		;;
	t*) set_test $@
		;;
	s*) click-uninstall
		 echo "Click uninstalled"
		;;
	*)		echo "Please use a valid option."
		;;
esac
