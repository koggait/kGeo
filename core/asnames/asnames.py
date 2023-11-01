from core.asnames.backup_asnames import backuping_asnames
from core.asnames.mirror_asnames import mirroring_asnames
from core.asnames.process_asnames import processing_asnames
from core.asnames.serialize_asnames import serialization_asnames
from core.root import Root

from core.mirror_util import mirror_file
from core.root import Root
from core.root_util import log_begin, log_end

MIRROR = 'MIRRORING'

SERIALIZE = 'serialize'

PREPROCESS = 'preprocess'
PROCESS = 'process'

BACKUP = 'backup'

NAME = 'asnames'
FIELDS = ['asnumber', 'asname', 'cc']
URL = 'https://ftp.ripe.net/ripe/asnames/asn.txt'


class Asnames:

    __attrs__ = [
        'name'
        'fields'
        'json_data',
    ]

    def __init__(self):
        super().__init__()

    def mirror(self):
        log_begin(action=MIRROR, entity=NAME)
        mirror_file(filename=NAME)
        log_end(action=MIRROR, entity=NAME)


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
