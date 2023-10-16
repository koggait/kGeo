##### kGeo 1.3 RC - Data-Driven AS & IP Geolocation

*****************************************************************************

###### after running kgeo the data can be found in core/data/...
###### backuped files are archived in core/history/...
###### evaluation data described in the coordination document in core/evaluation/...

*****************************************************************************

## About kGeo 1.3 RC

This repository aims at getting started with an analytical database for geolocation of internet autonomous systems.
*****************************************************************************

## Where is the data from?

The database is built using the following datasets:

RIPE FTP:

- Latest Delegated Stats from NRO, RIPENCC, ARIN , AFRINIC , APNIC , LACNIC

- Latest AS Names List
- Latest IP MAP Geolocation Dump

RIPE RIS:

- RIPE RIS WhoisDumps IPv4
- RIPE RIS WhoisDumps IPv6

MAXMIND:

- GeoLite2 ASN
- GeoLite2 City
- GeoLite2 Country

IP2Location

- ip2proxy4_extend
- ip2proxy6_extend
- ip2loc4_extend
- ip2loc6_extend
- ip2asn4
- ip2asn6
- ip2proxy4
- ip2proxy6
-

IPINFO

- ipinfo_country_asn
- ipinfo_country
- ipinfo_asn

FULL BGP TABLE DUMP

- BGP Table

PEERINGDB

- PeeringDB Dataset

*****************************************************************************

## Getting started

To run all scripts simply run kGeo.py.

The script will download all datasets, serialize them and begin to build the json datasets.
For selective use, execute the scripts directly or use arguments when running kGeo.py.
*****************************************************************************

Run kGeo.py with arguments to specify which operations will be executed.
Running it without arguments will lead to execution of all core functions.
To run the Daily-Mirror use --daily or handle specific dataset with other arguments.
Executing scripts from within the core package is also possible,
except for utility files. Keep in Mind, that some scripts need other pre-executed scripts,
if you are running kGeo for the first time.

Arguments: | -d, --daily | -a, --analysis | -as,  --asnames | -bgp, --bgptable | -ip2, --ip2loc | -ipi, --ipinfo | -max, --maxmind | -pee, --peeringdb | -ris, --riswhois | -map, --ipmap | -r,   --rir |

*****************************************************************************

##### Notes

| Thesis |                             University of Kassel, Distributed Systems                              |
|--------|:--------------------------------------------------------------------------------------------------:|
| Title  | Data-Driven Analysis of Registry and IP Information for Geolocation of Internet Autonomous Systems |
| Author |                                          Sebastian Kogga                                           

*****************************************************************************