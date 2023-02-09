import argparse
from enum import Enum
import numpy as np
import random


class OrgSize(Enum):
    small = 1
    medium = 2
    large = 3
    xlarge = 4

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(s):
        try:
            return OrgSize[s]
        except KeyError:
            raise ValueError()


class GlintCategories(Enum):
    HybridSupport
    WorkLifeBalance
    TeamCollaboration
    HaveTimeForLearning
    ManagerRespect
    FeelRecognized
    ManagerConfidence
    TeamUnderstandsTopPriorities

class InsightCategories(Enum):
    EmployeeWellBeing
    ManagerConnection
    MeetingEffectiveness

class ValueTypes:
    Hours
    Minutes
    Percentage

class ValueDirection:
    Up
    Down

InsightsList = {
    GlintCategories.HybridSupport: []
}
def main():
    """
    main
    """
    parser = argparse.ArgumentParser(description='Insights Generation')
    # use this flag, or change the default here to use different graph description files
    parser.add_argument('-f', '--InsightsFile', help='Filename for the generated insights',
                        default='insights.txt',
                        dest='insightFileName')
    parser.add_argument('-o', '--numOrgs', help='Number of Organizations', default=5, dest='numOrgs')
    parser.add_argument('-d', '--OrgDepth', help='Max Organization Depth', default=5, dest='maxOrgDepth')
    parser.add_argument('-s', '--OrgSize', type=OrgSize, choices=list(OrgSize.__members__.values()),
                        default=OrgSize.medium)
    parser.add_argument('-s', '--OrgSize', help='Max Organization Depth', default=5, dest='maxOrgDepth')
    parser.add_argument('-c', '--PercentageCorrelation', help='Percentage of correlated insight', default=50,
                        dest='percentCorrelated')

    args = parser.parse_args()


if __name__ == '__main__':
    main()
