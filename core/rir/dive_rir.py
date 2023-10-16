from core.rir.backup_rir import backuping_rir
from core.rir.mirror_rir import mirroring_rir
from core.rir.process_rir import processing_rir
from core.rir.serialize_rir import serialization_rir
from core.root import Root


def diving_rir():
    mirroring_rir()
    serialization_rir()
    backuping_rir()
    processing_rir()


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    diving_rir()
    exit()
