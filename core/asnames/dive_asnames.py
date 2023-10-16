from core.asnames.backup_asnames import backuping_asnames
from core.asnames.mirror_asnames import mirroring_asnames
from core.asnames.process_asnames import processing_asnames
from core.asnames.serialize_asnames import serialization_asnames
from core.root import Root


def diving_asnames():
    mirroring_asnames()
    serialization_asnames()
    backuping_asnames()
    processing_asnames()


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    diving_asnames()
    exit()
