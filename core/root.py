class Root:
    # --------------------------------------------------
    # PHASES & STATES
    # --------------------------------------------------

    HELP = '-help'

    MIRROR = 'mirror'
    SERIALIZE = 'serialize'

    PREPROCESS = 'preprocess'
    PROCESS = 'process'

    BACKUP = 'backup'

    ORDER = 'order'
    ACCUMULATE = 'accumulate'
    AGGREGATE = 'aggregate'

    MANIPULATE = 'manipulate'
    GROUP = 'group'
    MERGE = 'merge'

    ANALYSE = 'analyse'
    VISUALIZE = 'visualize'

    PHASES = {
        MIRROR: 'mirror',
        SERIALIZE: 'serialize',

        PREPROCESS: 'preprocess',
        PROCESS: 'process',

        BACKUP: 'backup',

        ORDER: 'ordered',
        ACCUMULATE: 'accumulate',
        AGGREGATE: 'aggregate',

        MANIPULATE: 'manipulate',
        GROUP: 'group',
        MERGE: 'merge',

        ANALYSE: 'analyse',
        VISUALIZE: 'visualize'
    }

    BEGIN = 'BEGIN'
    END = 'END'
    COMPLETE = 'COMPLETE'

    STATES = {
        BEGIN: 'START',
        END: 'END',
        COMPLETE: 'COMPLETE'
    }

    # --------------------------------------------------
    # PATHS & DATATYPES
    # --------------------------------------------------

    # data path
    COREDIR = '../core/'
    DATADIR = 'data/'
    HISTORYDIR = 'history/'

    ROOTRUNTIME = 'root_runtime'

    # data directory
    MIRRORED = 'mirrored'
    SERIALIZED = 'serialized'

    PREPROCESSED = 'preprocessed'
    PROCESSED = 'processed'

    HISTORY = 'history'

    ORDERED = 'ordered'
    ACCUMULATED = 'accumulated'
    AGGREGATED = 'aggregated'

    MANIPULATED = 'manipulated'
    MERGED = 'merged'
    GROUPED = 'grouped'

    ANALYSED = 'analysed'
    VISUALIZED = 'visualized'

    FINAL = 'final'
    EVALUATION = 'evaluation'

    # --------------------------------------------------
    # FILETYPES
    # --------------------------------------------------

    TXT = 'txt'
    CSV = 'csv'
    JSON = 'json'
    GZ = 'gz'
    BZ2 = 'bz2'
    ZIP = 'zip'
    PY = 'py'

    # --------------------------------------------------
    # DICTIONARY KEYS
    # --------------------------------------------------

    CC = 'cc'
    COUNTRY = 'country'
    TYPE = 'type'
    START = 'start'
    VALUE = 'value'
    START_VALUE = ['start', 'value']
    ASNAME = 'asname'
    ASNUMBER = 'asnumber'

    # --------------------------------------------------
    # MANIPULATED DATA
    # --------------------------------------------------

    AS_EXTENDED = 'asnames-extended'
    AS_EXTENDED_BY_CC = 'asnames-extended-by-cc'
    AS_BIG_SUM_BY_REG_CC = 'asnames-extended_reg-cc-summary'
    AS_BIG_SUM_BY_ACTIV_CC = 'asnames-extended_activ-cc-summary'
    AS_RATIO = 'as-big_reg-activ-cc-ratio'
    PREFIXRATIO4 = 'rir-max-cc-ratio4'
    PREFIXRATIO6 = 'rir-max-cc-ratio6'

    # --------------------------------------------------
    # RIR DELEGATED STATS
    # --------------------------------------------------

    # DELEGATED STATS
    RIR = 'rir'
    RIR_STATS_FIELDS = ['registry', 'cc', 'type', 'start', 'value', 'date', 'status', 'obaque-id', 'extensions']
    RIR_STATS_REDUCE_FIELDS = ['registry', 'type', 'date', 'status', 'obaque-id', 'extensions']
    RIR_STATS_REDUCE_OBJECTS = 'ZZ'  # cc
    RIR_STATS_DELIMITER = '|'
    IP4 = 'ipv4'
    IP6 = 'ipv6'
    ASN = 'asn'

    # NRO
    NRO = 'nro'
    NRO4 = 'nro_ipv4'
    NRO6 = 'nro_ipv6'
    NROASN = 'nro_asn'
    NRO4BAD = 'bad_nro4'
    NRO6BAD = 'bad_nro6'
    NROASNBAD = 'bad_nro_asn'
    NRO_URL = 'https://ftp.ripe.net/pub/stats/ripencc/nro-stats/latest/nro-delegated-stats'
    NRO_DATA_STARTLINE = 4

    # IANA
    IANA = 'iana'
    IANA_URL = 'https://ftp.ripe.net/pub/stats/ripencc/nro-stats/latest/delegated-iana'
    IANA_DATA_STARTLINE = 33

    # RIPE NCC
    RIPE = 'ripencc'
    RIPE_URL = 'https://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-extended-latest'
    RIPE_DATA_STARTLINE = 4

    # ARIN
    ARIN = 'arin'
    ARIN_URL = 'https://ftp.arin.net/pub/stats/arin/delegated-arin-extended-latest'
    ARIN_DATA_STARTLINE = 4

    # APNIC
    APNIC = 'apnic'
    APNIC_URL = 'https://ftp.apnic.net/stats/apnic/delegated-apnic-extended-latest'
    APNIC_DATA_STARTLINE = 31

    # LACNIC
    LACNIC = 'lacnic'
    LACNIC_URL = 'https://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-extended-latest'
    LACNIC_DATA_STARTLINE = 4

    # AFRINIC
    AFRINIC = 'afrinic'
    AFRINIC_URL = 'https://ftp.afrinic.net/pub/stats/afrinic/delegated-afrinic-extended-latest'
    AFRINIC_DATA_STARTLINE = 4

    # RIR : DATA STARTLINE
    RIR_SET_STARTLINE = {
        NRO: NRO_DATA_STARTLINE,
        IANA: IANA_DATA_STARTLINE,
        AFRINIC: AFRINIC_DATA_STARTLINE,
        APNIC: APNIC_DATA_STARTLINE,
        RIPE: RIPE_DATA_STARTLINE,
        ARIN: ARIN_DATA_STARTLINE,
        LACNIC: LACNIC_DATA_STARTLINE
    }

    # --------------------------------------------------
    # AS NAMES
    # --------------------------------------------------

    ASNAMES = 'asnames'
    ASNAMES_BAD = 'bad_asnames'
    ASNAMES_FIELDS = ['asnumber', 'asname', 'cc']
    ASNAMES_URL = 'https://ftp.ripe.net/ripe/asnames/asn.txt'
    ASNAMES_URL_BAD = 'https://ftp.arin.net/info/asn.txt'

    # --------------------------------------------------
    # ALLOCATION
    # --------------------------------------------------

    ALLOC = 'alloclist'
    ALLOC_URL = 'https://ftp.ripe.net/pub/stats/ripencc/membership/alloclist.txt'

    # --------------------------------------------------
    # IP MAP
    # --------------------------------------------------

    IPMAP = 'ipmap'
    IPMAP_URL = 'https://ftp.ripe.net/ripe/ipmap/geolocations-latest'
    IPMAP_FIELDS = ["ip", "geolocation_id", "city_name", "state_name", "country_name", "cc", "country_code_alpha3",
                    "latitude", "longitude", "score"]
    IPMAP_REDUCE_FIELDS = ["geolocation_id", "city_name", "state_name", "country_name", "country_code_alpha3",
                           "latitude", "longitude", "score"]

    # --------------------------------------------------
    # RIS WHOIS
    # --------------------------------------------------

    RISWHO = 'riswhois'
    RISWHOGOOD = 'good_riswhois'
    RISWHOBAD = 'bad_riswhois'

    RISWHO_STARTLINE = 18
    RISWHO_DELIMITER = '\t'
    RISWHO_FIELDS = ['origin', 'prefix', 'rispeers']
    RISWHO_REDUCE_FIELDS = ['rispeers']

    RISWHO4 = 'riswhois4'
    RISWHO4BAD = 'bad_riswhois4'
    RISWHO4GOOD = 'good_riswhois4'
    RISWHO4_URL = 'https://www.ris.ripe.net/dumps/riswhoisdump.IPv4.gz'
    RISWHO4_REDUCE_OBJECTS = '0.0.0.0/0'

    RISWHO6 = 'riswhois6'
    RISWHO6BAD = 'bad_riswhois6'
    RISWHO6GOOD = 'good_riswhois6'
    RISWHO6_URL = 'https://www.ris.ripe.net/dumps/riswhoisdump.IPv6.gz'
    RISWHO6_REDUCE_OBJECTS = '::/0'

    # --------------------------------------------------
    # RIPE DATABASE
    # --------------------------------------------------

    RIPEDB = 'ripedb'
    RIPEDB_URL = 'ftp://ftp.ripe.net/ripe/dbase/ripe.db.gz'

    # --------------------------------------------------
    # BGP FULL TABLE
    # --------------------------------------------------

    BGPTABLE = 'bgptable'
    BGPTABLE4 = 'bgptable4'
    BGPTABLE6 = 'bgptable6'
    BGPASPATH4 = 'bgpaspath4'
    BGPASPATH6 = 'bgpaspath6'

    FULLPATH = 'full-path'
    ASPATH = 'as-path'

    # scope: CATNIX
    BGPTABLE_URL = 'https://data.ris.ripe.net/rrc18/latest-bview.gz'

    # scope: GLOBAL
    # PROBABLY BEST DATA, BUT SERIALIZED DATA EXPONENTIAL GROWTH > 50GB SPACE NECESSARY
    # BGPTABLE_URL = 'https://data.ris.ripe.net/rrc00/latest-bview.gz'

    # --------------------------------------------------
    # PEERING DB
    # --------------------------------------------------

    PEERINGDB_APIKEY = 'YxHnPDB3.NVbbkAd1FDch1WB8rjMInTeF4fvi0Hmb'

    PEERINGDB = 'peeringdb'
    PEERINGDB_URL = 'https://www.peeringdb.com/api/net'
    PEERINGDB_FIELDS = ["id", "org_id", "org_name", "org", "campus_id", "campus", "name", "aka", "name_long", "website",
                        "clli", "rencode", "npanxx", "notes", "net_count", "ix_count", "sales_email", "sales_phone",
                        "tech_email", "tech_phone", "available_voltage_services", "diverse_serving_substations",
                        "property", "region_continent", "status_dashboard", "created", "updated", "status", "address1",
                        "address2", "city", "country", "state", "zipcode", "floor", "suite", "latitude", "longitude"]
    PEERINGDB_SUB_FIELDS_SOCIAL_MEDIA = ["service", "identifier"]
    PEERINGDB_REDUCE_FIELDS = ["id", "org_id", "org_name", "org", "campus_id", "campus", "aka", "name_long", "website",
                               "clli", "rencode", "npanxx", "notes", "sales_email", "sales_phone", "tech_email",
                               "tech_phone", "available_voltage_services", "diverse_serving_substations", "property",
                               "region_continent", "status_dashboard", "created", "updated", "status", "address1",
                               "address2", "city", "state", "zipcode", "floor", "suite", "latitude", "longitude"]
    PEERINGDB_KEEP_FIELDS = ["asn", "info_type", "info_prefixes4", "info_prefixes6", "ix_count", "fac_count"]

    PEERINGDB_FIELDS_V2 = ["id",
                           "org_id",
                           "name",
                           "aka",
                           "name_long",
                           "website",
                           "social_media",
                           "asn",
                           "looking_glass",
                           "route_server",
                           "irr_as_set",
                           "info_type",
                           "info_prefixes4",
                           "info_prefixes6",
                           "info_traffic",
                           "info_ratio",
                           "info_scope",
                           "info_unicast",
                           "info_multicast",
                           "info_ipv6",
                           "info_never_via_route_servers",
                           "ix_count",
                           "fac_count",
                           "notes",
                           "netixlan_updated",
                           "netfac_updated",
                           "poc_updated",
                           "policy_url",
                           "policy_general",
                           "policy_locations",
                           "policy_ratio",
                           "policy_contracts",
                           "allow_ixp_update",
                           "status_dashboard",
                           "rir_status",
                           "rir_status_updated",
                           "created",
                           "updated",
                           "status"]

    # --------------------------------------------------
    # IP 2 LOCATION
    # --------------------------------------------------

    IP2LOC_TOKEN = '0oNX3BBveGW0jjt18UtEWrQsEjZnR9TZKUk8cgSj74qTKgKs6sg0Sw8ozWaJ9Fsf'

    IP2LOC = 'ip2loc'

    IP2LOC4 = 'ip2loc4'
    IP2LOC4CSV = 'IP2LOCATION-LITE-DB1.CSV'
    IP2LOC4_DBCODE = 'DB1LITECSV'
    IP2LOC4_URL = 'https://www.ip2location.com/download/?token=' + IP2LOC_TOKEN + '&file=' + IP2LOC4_DBCODE

    IP2LOC6 = 'ip2loc6'
    IP2LOC6CSV = 'IP2LOCATION-LITE-DB1.IPV6.CSV'
    IP2LOC6_DBCODE = 'DB1LITECSVIPV6'
    IP2LOC6_URL = 'https://www.ip2location.com/download/?token=' + IP2LOC_TOKEN + '&file=' + IP2LOC6_DBCODE

    IP2LOC_FIELDS = ['start', 'end', 'cc', 'country']
    IP2LOC_REDUCE_FIELDS = ['country']

    IP2PROXY4 = 'ip2proxy4'
    IP2PROXY4_DBCODE = 'PX1LITECSV'
    IP2PROXY4_URL = 'https://www.ip2location.com/download/?token=' + IP2LOC_TOKEN + '&file=' + IP2PROXY4_DBCODE

    IP2PROXY6 = 'ip2proxy6'
    IP2PROXY6_DBCODE = 'PX1LITECSVIPV6'
    IP2PROXY6_URL = 'https://www.ip2location.com/download/?token=' + IP2LOC_TOKEN + '&file=' + IP2PROXY6_DBCODE

    IP2ASN4 = 'ip2asn4'
    IP2ASN4_DBCODE = 'DBASNLITE'
    IP2ASN4_URL = 'https://www.ip2location.com/download/?token=' + IP2LOC_TOKEN + '&file=' + IP2ASN4_DBCODE

    IP2ASN6 = 'ip2asn6'
    IP2ASN6_DBCODE = 'DBASNLITEIPV6'
    IP2ASN6_URL = 'https://www.ip2location.com/download/?token=' + IP2LOC_TOKEN + '&file=' + IP2ASN6_DBCODE

    IP2LOC4_EXTEND = 'ip2loc4_extend'
    IP2LOC4_EXTEND_DBCODE = 'DB11LITECSV'
    IP2LOC4_EXTEND_URL = 'https://www.ip2location.com/download/?token=' + IP2LOC_TOKEN + '&file=' + IP2LOC4_EXTEND_DBCODE

    IP2LOC6_EXTEND = 'ip2loc6_extend'
    IP2LOC6_EXTEND_DBCODE = 'DB11LITECSVIPV6'
    IP2LOC6_EXTEND_URL = 'https://www.ip2location.com/download/?token=' + IP2LOC_TOKEN + '&file=' + IP2LOC6_EXTEND_DBCODE

    IP2PROXY4_EXTEND = 'ip2proxy4_extend'
    IP2PROXY4_EXTEND_DBCODE = 'PX11LITECSV'
    IP2PROXY4_EXTEND_URL = 'https://www.ip2location.com/download/?token=' + IP2LOC_TOKEN + '&file=' + IP2PROXY4_EXTEND_DBCODE

    IP2PROXY6_EXTEND = 'ip2proxy6_extend'
    IP2PROXY6_EXTEND_DBCODE = 'PX11LITECSVIPV6'
    IP2PROXY6_EXTEND_URL = 'https://www.ip2location.com/download/?token=' + IP2LOC_TOKEN + '&file=' + IP2PROXY6_EXTEND_DBCODE

    # --------------------------------------------------
    # IP INFO
    # --------------------------------------------------

    IPINFO = 'ipinfo'
    IPINFO_TOKEN = 'ccc86d52920d96'

    IPINFO_ASN = 'ipinfo_asn'
    IPINFO_ASN_URL = 'https://ipinfo.io/data/free/asn.json.gz?token=' + IPINFO_TOKEN + ''
    IPINFO_ASN_FIELDS = ["start_ip", "end_ip", "asn", "as_name", "as_domain"]

    IPINFO_COUNTRY = 'ipinfo_country'
    IPINFO_COUNTRY_URL = 'https://ipinfo.io/data/free/country.json.gz?token=' + IPINFO_TOKEN + ''
    IPINFO_COUNTRY_FIELDS = ['start_ip', 'end_ip', 'country', 'country_name', 'continent', 'continent_name']

    IPINFO_COUNTRY_ASN = 'ipinfo_country_asn'
    IPINFO_COUNTRY_ASN_URL = 'https://ipinfo.io/data/free/country_asn.json.gz?token=' + IPINFO_TOKEN + ''
    IPINFO_COUNTRY_ASN_FIELDS = ["start_ip", "end_ip", "country", "country_name", "continent", "continent_name", "asn",
                                 "as_name", "as_domain"]

    IPINFO_REDUCE_FIELDS = ["country_name", "continent", "continent_name", "as_domain"]

    STARTIP = 'start_ip'
    IPINFO_FINAL_CC = 'ipinfo_cc'
    IPINFO_FINAL_ASN = 'ipinfo_asn'

    # --------------------------------------------------
    # MAXMIND
    # --------------------------------------------------

    MAXMIND_LICENSE_KEY = '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'

    MAXMIND = 'maxmind'

    MAXMIND4 = 'maxmind4'
    MAXMIND4AS = 'maxmind4as'

    MAXMIND6 = 'maxmind6'
    MAXMIND6AS = 'maxmind6as'

    MAXMINDCCREAL = 'maxmind_real_cc'
    MAXMINDCCREG = 'maxmind_reg_cc'
    MAXMINDCCREP = 'maxmind_rep_cc'

    MAXASN = 'maxasn'
    MAXASN_URL = 'https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-ASN-CSV&license_key=' + MAXMIND_LICENSE_KEY + '&suffix=zip'
    MAXASNFIELDS = ['network', 'autonomous_system_number', 'autonomous_system_organization']
    MAXASN_REDUCE_FIELDS = []

    MAXCITY = 'maxcity'
    MAXCITY_URL = 'https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City-CSV&license_key=' + MAXMIND_LICENSE_KEY + '&suffix=zip'
    MAXCITYFIELDS = ['network', 'geoname_id', 'registered_country_geoname_id', 'represented_country_geoname_id',
                     'is_anonymous_proxy', 'is_satellite_provider', 'postal_code', 'latitude', 'longitude',
                     'accuracy_radius']
    MAXCITY_REDUCE_FIELDS = []

    MAXCITYLOC = 'maxcity_locations'
    MAXCITYLOCFIELDS = ['geoname_id', 'locale_code', 'continent_code', 'continent_name', 'country_iso_code',
                        'country_name', 'subdivision_1_iso_code', 'subdivision_1_name', 'subdivision_2_iso_code',
                        'subdivision_2_name', 'city_name', 'metro_code', 'time_zone', 'is_in_european_union']
    MAXCITYLOC_REDUCE_FIELDS = []

    MAXCOUNTRY = 'maxcountry'
    MAXCOUNTRY_URL = 'https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-Country-CSV&license_key=' + MAXMIND_LICENSE_KEY + '&suffix=zip'
    MAXCOUNTRYFIELDS = ['network', 'geoname_id', 'registered_country_geoname_id', 'represented_country_geoname_id',
                        'is_anonymous_proxy', 'is_satellite_provider']
    MAXCOUNTRYP_REDUCE_FIELDS = ['is_anonymous_proxy', 'is_satellite_provider']

    MAXCOUNTRYLOC = 'maxcountry_locations'
    MAXCOUNTRYLOCFIELDS = ['geoname_id', 'locale_code', 'continent_code', 'continent_name', 'country_iso_code',
                           'country_name', 'is_in_european_union']
    MAXCOUNTRYLOC_REDUCE_FIELDS = ['locale_code', 'country_name', 'continent_code', 'continent_name',
                                   'is_in_european_union']

    MAXMIND_NAME_LIST = ['GeoLite2-ASN-Blocks-IPv4', 'GeoLite2-ASN-Blocks-IPv6', 'GeoLite2-Country-Blocks-IPv4',
                         'GeoLite2-Country-Blocks-IPv6', 'GeoLite2-Country-Locations-de', 'maxmind_real_cc.json',
                         'maxmind_reg_cc.json', 'maxmind_rep_cc.json']

    MAXMIND_MERG_NAME_LIST = ['GeoLite2-Country-Location-IPv4.json', 'GeoLite2-Country-Location-IPv6.json',
                              'Maxmind-ASN-IP-CC-IPv4.json', 'Maxmind-ASN-IP-CC-IPv6.json']

    MAXMIND_AGGREGATED = ['Maxmind_IPv4.json', 'Maxmind_IPv6.json']

    MAXMIND_FINAL_IP4 = ['maxmind_real_cc_ip4.json', 'maxmind_reg_cc_ip4.json', 'maxmind_rep_cc_ip4.json']
    MAXMIND_FINAL_IP6 = ['maxmind_real_cc_ip6.json', 'maxmind_reg_cc_ip6.json', 'maxmind_rep_cc_ip6.json']
    MAXMIND_FINAL_AS = ['maxmind_as_ip4.json', 'maxmind_as_ip6.json']

    # --------------------------------------------------
    # FILENAME : MIRROR URL
    # --------------------------------------------------
    # MIRROR URLS
    MIRROR_URLS = {
        NRO: NRO_URL,

        IANA: IANA_URL,
        RIPE: RIPE_URL,
        ARIN: ARIN_URL,
        AFRINIC: AFRINIC_URL,
        APNIC: APNIC_URL,
        LACNIC: LACNIC_URL,

        ASNAMES: ASNAMES_URL,

        ALLOC: ALLOC_URL,

        IPMAP: IPMAP_URL,

        RISWHO4: RISWHO4_URL,
        RISWHO6: RISWHO6_URL,

        PEERINGDB: PEERINGDB_URL,

        MAXASN: MAXASN_URL,
        MAXCITY: MAXCITY_URL,
        MAXCOUNTRY: MAXCOUNTRY_URL,

        IP2LOC4: IP2LOC4_URL,
        IP2LOC6: IP2LOC6_URL,
        IP2PROXY4: IP2PROXY4_URL,
        IP2PROXY6: IP2PROXY6_URL,
        IP2ASN4: IP2ASN4_URL,
        IP2ASN6: IP2ASN6_URL,

        IP2LOC4_EXTEND: IP2LOC4_EXTEND_URL,
        IP2LOC6_EXTEND: IP2LOC6_EXTEND_URL,
        IP2PROXY4_EXTEND: IP2PROXY4_EXTEND_URL,
        IP2PROXY6_EXTEND: IP2PROXY6_EXTEND_URL,

        IPINFO_ASN: IPINFO_ASN_URL,
        IPINFO_COUNTRY: IPINFO_COUNTRY_URL,
        IPINFO_COUNTRY_ASN: IPINFO_COUNTRY_ASN_URL,

        BGPTABLE: BGPTABLE_URL,

    }

    # --------------------------------------------------
    # END
    # --------------------------------------------------
