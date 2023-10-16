from core.ipmap.backup_ipmap import backuping_ipmap
from core.ipmap.mirror_ipmap import mirroring_ipmap
from core.ipmap.process_ipmap import processing_ipmap
from core.ipmap.serialize_ipmap import serialization_ipmap
from core.root import Root


def diving_ipmap():
    mirroring_ipmap()
    serialization_ipmap()
    backuping_ipmap()
    processing_ipmap()


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    diving_ipmap()
