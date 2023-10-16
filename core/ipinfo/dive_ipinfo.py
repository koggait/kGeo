from core.ipinfo.backup_ipinfo import backuping_ipinfo
from core.ipinfo.mirror_ipinfo import mirroring_ipinfo
from core.ipinfo.process_ipinfo import processing_ipinfo
from core.ipinfo.serialize_ipinfo import serialization_ipinfo
from core.root import Root


def diving_ipinfo():
    mirroring_ipinfo()
    serialization_ipinfo()
    backuping_ipinfo()
    processing_ipinfo()


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    diving_ipinfo()
