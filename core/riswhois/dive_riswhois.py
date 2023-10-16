from core.riswhois.backup_riswhois import backuping_riswhois
from core.riswhois.mirror_riswhois import mirroring_riswhois
from core.riswhois.process_riswhois import processing_riswhois
from core.riswhois.serialize_riswhois import serialization_riswhois
from core.root import Root


def diving_riswhois():
    mirroring_riswhois()
    serialization_riswhois()
    backuping_riswhois()
    processing_riswhois()


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    diving_riswhois()
