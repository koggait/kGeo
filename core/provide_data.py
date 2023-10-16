from core.mirror_util import copy_to_evaluation
from core.root import Root


def providing_data():
    for file in Root.BERNDSET.values():
        copy_to_evaluation(file)


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    providing_data()
    exit()
