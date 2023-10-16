from core.analysis.merge import merging_data
from core.analysis.aggregated import aggregation_data
from core.analysis.analize import analizing_data
from core.analysis.combine import combining_data
from core.root import Root


def diving_analysis():
    merging_data()
    aggregation_data()
    analizing_data()
    combining_data()


if __name__ == "__main__":
    Root.DATADIR = '../data/'
    Root.HISTORYDIR = '../history/'
    diving_analysis()
    exit()
