from core.peeringdb.backup_peeringdb import backuping_peeringdb
from core.peeringdb.mirror_peeringdb import mirroring_peeringdb
from core.peeringdb.process_peeringdb import processing_peeringdb
from core.peeringdb.serialize_peeringdb import serialization_peeringdb
from core.root import Root


def diving_peeringdb():
    mirroring_peeringdb()
    serialization_peeringdb()
    backuping_peeringdb()
    processing_peeringdb()


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    diving_peeringdb()
    exit()