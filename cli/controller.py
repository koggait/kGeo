import argparse

from cli.control_util import diving_peeringdb
from cli.control_util import diving_rir
from cli.control_util import diving_riswhois
from cli.control_util import diving_asnames
from cli.control_util import diving_bgptable
from cli.control_util import diving_ip2loc
from cli.control_util import diving_ipinfo
from cli.control_util import diving_ipmap
from cli.control_util import diving_maxmind
from cli.control_util import diving_local_peeringdb
from cli.control_util import diving_local_rir
from cli.control_util import diving_local_riswhois
from cli.control_util import diving_local_asnames
from cli.control_util import diving_local_bgptable
from cli.control_util import diving_local_ip2loc
from cli.control_util import diving_local_ipinfo
from cli.control_util import diving_local_ipmap
from cli.control_util import diving_local_maxmind

from cli.control_util import diving_analysis
from cli.control_util import diving_local
from cli.control_util import diving_data
from cli.control_util import mirror_data
from cli.control_util import serialize_data
from cli.control_util import backup_data

def control(argv):
    parser = argparse.ArgumentParser(prog='kGeo v0.1.5',
                                     add_help='Run kGeo.py with arguments to specify which operations will be executed.'
                                              'Running it without arguments will lead to execution of all core functions.'
                                              'To run the Daily-Mirror use --daily or handle specific dataset with other arguments.'
                                              'Executing scripts from within the core package is also possible,'
                                              'except for utility files. Keep in Mind, that some scripts need other pre-executed scripts,'
                                              'if you are running kGeo for the first time.',
                                     description='Data-Driven AS & IP Geolocation Tool')

    # Add operation arguments
    parser.add_argument('-a', '--analysis', action='store_true', help='Run analysis related functions.')
    parser.add_argument('-d', '--daily', action='store_true', help='Run all mirroring, serialization and backup related functions.')
    parser.add_argument('-l', '--local', action='store_true', help='Skip mirroring and run all functions on local mirrored files.')

    # Add specific option arguments
    parser.add_argument('-as', '--asnames', action='store_true', help='Operate on asnames data.')
    parser.add_argument('-bgp', '--bgptable', action='store_true', help='Operate on BGP table data.')
    parser.add_argument('-ip2', '--ip2loc', action='store_true', help='Operate on IP2Loc data.')
    parser.add_argument('-ipi', '--ipinfo', action='store_true', help='Operate on IPInfo data.')
    parser.add_argument('-max', '--maxmind', action='store_true', help='Operate on MaxMind data.')
    parser.add_argument('-pee', '--peeringdb', action='store_true', help='Operate on PeeringDB data.')
    parser.add_argument('-ris', '--riswhois', action='store_true', help='Operate on RIS WHOIS data.')
    parser.add_argument('-map', '--ipmap', action='store_true', help='Operate on IPMap data.')
    parser.add_argument('-r', '--rir', action='store_true', help='Operate on RIR data.')

    args = parser.parse_args(argv[1:])

    # Handling argument operations
    if len(argv) == 1:
        diving_data()
    else:
        if args.analysis: diving_analysis()
        if args.daily:
            mirror_data(), serialize_data(), backup_data()
        if args.local:
            if len(argv) == 2:
                diving_local()
            if args.asnames:
                diving_local_asnames()
            if args.ip2loc:
                diving_local_ip2loc()
            if args.ipinfo:
                diving_local_ipinfo()
            if args.riswhois:
                diving_local_riswhois()
            if args.ipmap:
                diving_local_ipmap()
            if args.rir:
                diving_local_rir()
            if args.bgptable:
                diving_local_bgptable()
            if args.maxmind:
                diving_local_maxmind()
            if args.peeringdb:
                diving_local_peeringdb()
        else:
            if args.asnames: diving_asnames()
            if args.ip2loc: diving_ip2loc()
            if args.ipinfo: diving_ipinfo()
            if args.riswhois: diving_riswhois()
            if args.ipmap: diving_ipmap()
            if args.rir: diving_rir()
            if args.bgptable: diving_bgptable()
            if args.maxmind: diving_maxmind()
            if args.peeringdb: diving_peeringdb()