#!/usr/bin/perl
# Only lines with valid NMEA sentences will be printed.
# validate.pl [file.nmea [file.nmea [*.nmea]]] > output.nmea

use strict;
use warnings;

my($fail_checksum, $fail_regex, $lines); # counters

while (<>) {
    if (m/^\$(GPGGA,\d{6}\.\d{3},\d{4}\.\d{4},N,\d{5}\.\d{4},W,\d,\d{1,2},\d\.\d{2},\d{3,4}\.\d,M,-\d{2}\.\d,M,0000,0000)\*([0-9A-F]{2})(,-\d{2}dB)?$/) {
	my $calculated_checksum;
	my $parsed_checksum = $2;
	map {$calculated_checksum^=$_} $1=~m/./sg;
	$calculated_checksum = uc(sprintf("%x", ord($calculated_checksum)));
	if ($calculated_checksum eq $parsed_checksum) {
	    print;
	} else {
	    $fail_checksum++;
	}
    } else {
	$fail_regex++;
    }
    $lines++;
}

warn "Processed $lines lines.",
    $fail_regex?sprintf("  Parse errors: %i (%.3f%%).", $fail_regex, $fail_regex/$lines*100):"",
    $fail_checksum?sprintf("  Checksum errors: %i (%.3f%%).", $fail_checksum, $fail_checksum/$lines*100):"",
    "\n";
