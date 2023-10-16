from core.maxmind.aggregate_maxmind import aggregation_maxmind
from core.maxmind.backup_maxmind import backuping_maxmind
from core.maxmind.finalize_maxmind import finalization_maxmind
from core.maxmind.merge_maxmind import merging_maxmind
from core.maxmind.mirror_maxmind import mirroring_maxmind
from core.maxmind.process_maxmind import processing_maxmind
from core.maxmind.serialize_maxmind import serialization_maxmind
from core.root import Root


def diving_maxmind():
#    mirroring_maxmind()
    serialization_maxmind()
    processing_maxmind()
    merging_maxmind()
    backuping_maxmind()
    aggregation_maxmind()
    finalization_maxmind()


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    diving_maxmind()
    exit()
