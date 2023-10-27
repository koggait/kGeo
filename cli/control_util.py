from core.analysis.aggregated import aggregation_data
from core.analysis.analize import analizing_data
from core.analysis.merge import merging_data
from core.analysis.combine import combining_data

from core.peeringdb.dive_peeringdb import diving_peeringdb
from core.rir.dive_rir import diving_rir
from core.riswhois.dive_riswhois import diving_riswhois
from core.asnames.dive_asnames import diving_asnames
from core.bgptable.dive_bgptable import diving_bgptable
from core.ip2loc.dive_ip2loc import diving_ip2loc
from core.ipinfo.dive_ipinfo import diving_ipinfo
from core.ipmap.dive_ipmap import diving_ipmap
from core.maxmind.dive_maxmind import diving_maxmind
from core.analysis.dive_analysis import diving_analysis

from core.asnames.backup_asnames import backuping_asnames
from core.asnames.mirror_asnames import mirroring_asnames
from core.asnames.process_asnames import processing_asnames
from core.asnames.serialize_asnames import serialization_asnames

from core.bgptable.backup_bgptable import backuping_bgptable
from core.bgptable.mirror_bgptable import mirroring_bgptable
from core.bgptable.process_bgptable import processing_bgptable
from core.bgptable.serialize_bgptable import serialization_bgptable

from core.ip2loc.backup_ip2loc import backuping_ip2loc
from core.ip2loc.mirror_ip2loc import mirroring_ip2loc
from core.ip2loc.process_ip2loc import processing_ip2loc
from core.ip2loc.serialize_ip2loc import serialization_ip2loc

from core.ipinfo.backup_ipinfo import backuping_ipinfo
from core.ipinfo.mirror_ipinfo import mirroring_ipinfo
from core.ipinfo.process_ipinfo import processing_ipinfo
from core.ipinfo.serialize_ipinfo import serialization_ipinfo

from core.ipmap.backup_ipmap import backuping_ipmap
from core.ipmap.mirror_ipmap import mirroring_ipmap
from core.ipmap.process_ipmap import processing_ipmap
from core.ipmap.serialize_ipmap import serialization_ipmap

from core.maxmind.aggregate_maxmind import aggregation_maxmind
from core.maxmind.backup_maxmind import backuping_maxmind
from core.maxmind.finalize_maxmind import finalization_maxmind
from core.maxmind.merge_maxmind import merging_maxmind
from core.maxmind.mirror_maxmind import mirroring_maxmind
from core.maxmind.process_maxmind import processing_maxmind
from core.maxmind.serialize_maxmind import serialization_maxmind

from core.peeringdb.backup_peeringdb import backuping_peeringdb
from core.peeringdb.mirror_peeringdb import mirroring_peeringdb
from core.peeringdb.process_peeringdb import processing_peeringdb
from core.peeringdb.serialize_peeringdb import serialization_peeringdb

from core.rir.backup_rir import backuping_rir
from core.rir.mirror_rir import mirroring_rir
from core.rir.process_rir import processing_rir
from core.rir.serialize_rir import serialization_rir

from core.riswhois.backup_riswhois import backuping_riswhois
from core.riswhois.mirror_riswhois import mirroring_riswhois
from core.riswhois.process_riswhois import processing_riswhois
from core.riswhois.serialize_riswhois import serialization_riswhois

from core.root import Root
from core.root_util import print_state

def diving_phases():
    mirror_data()
    serialize_data()
    backup_data()
    process_data()
    diving_analysis()


def diving_local():
    serialize_data()
    backup_data()
    process_data()
    diving_analysis()


def diving_data():
    diving_rir()
    diving_asnames()
    diving_bgptable()
    diving_riswhois()
    diving_ipmap()
    diving_ip2loc()
    diving_ipinfo()
    diving_peeringdb()
    diving_maxmind()
    diving_analysis()


def mirror_data():
    mirroring_rir()
    mirroring_asnames()
    mirroring_bgptable()
    mirroring_riswhois()
    mirroring_ipmap()
    mirroring_ip2loc()
    mirroring_ipinfo()
    mirroring_peeringdb()
    mirroring_maxmind()
    print_state(Root.MIRROR, Root.COMPLETE, Root.END)


def serialize_data():
    serialization_rir()
    serialization_asnames()
    serialization_bgptable()
    serialization_riswhois()
    serialization_ipmap()
    serialization_ip2loc()
    serialization_ipinfo()
    serialization_peeringdb()
    serialization_maxmind()
    merging_maxmind()
    print_state(Root.SERIALIZE, Root.COMPLETE, Root.END)


def backup_data():
    backuping_rir()
    backuping_asnames()
    backuping_bgptable()
    backuping_riswhois()
    backuping_ipmap()
    backuping_ip2loc()
    backuping_ipinfo()
    backuping_peeringdb()
    backuping_maxmind()
    print_state(Root.BACKUP, Root.COMPLETE, Root.END)


def process_data():
    processing_rir()
    processing_asnames()
    processing_bgptable()
    processing_riswhois()
    processing_ipmap()
    processing_ip2loc()
    processing_ipinfo()
    processing_peeringdb()
    processing_maxmind()
    aggregation_maxmind()
    finalization_maxmind()
    print_state(Root.PROCESS, Root.COMPLETE, Root.END)


def analize_data():
    merging_data()
    aggregation_data()
    analizing_data()
    combining_data()
    print_state(Root.ANALYSED, Root.COMPLETE, Root.END)
