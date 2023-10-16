from core.ip2loc.backup_ip2loc import backuping_ip2loc
from core.ip2loc.mirror_ip2loc import mirroring_ip2loc
from core.ip2loc.process_ip2loc import processing_ip2loc
from core.ip2loc.serialize_ip2loc import serialization_ip2loc
from core.root import Root


def diving_ip2loc():
    mirroring_ip2loc()
    serialization_ip2loc()
    backuping_ip2loc()
    processing_ip2loc()


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    diving_ip2loc()
