from core.bgptable.backup_bgptable import backuping_bgptable
from core.bgptable.mirror_bgptable import mirroring_bgptable
from core.bgptable.process_bgptable import processing_bgptable
from core.bgptable.serialize_bgptable import serialization_bgptable
from core.root import Root


def diving_bgptable():
    mirroring_bgptable()
    serialization_bgptable()
    processing_bgptable()
    backuping_bgptable()


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    diving_bgptable()
