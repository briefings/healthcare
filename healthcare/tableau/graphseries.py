"""
Module graphseries
"""
import os

import pandas as pd


class GraphSeries:
    """
    Class GraphSeries

    Creates the most appropriate data structure for Tableau graphing
    """

    def __init__(self, blob: pd.DataFrame, institutions: pd.DataFrame, path: str):
        """

        :param blob: A summary of the time series per institution; narrow format
        :param institutions: The distinct institutions
        :param path: The data will be saved here
        """

        self.blob = blob
        self.institutions = institutions
        self.path = path

    def getbranch(self):
        """

        :return:
        """

        branch = os.path.join(self.path, 'tableau')

        if not os.path.exists(branch):
            os.makedirs(branch)

        return branch

    def write(self, branch):
        """

        :param branch:
        :return:
        """

        self.blob.to_csv(path_or_buf=os.path.join(branch, 'series.csv'),
                         header=True, index=False, encoding='UTF-8')

        self.institutions.to_csv(path_or_buf=os.path.join(branch, 'institutions.csv'),
                                 header=True, index=False, encoding='UTF-8')

    def exc(self):
        """

        :return:
        """

        branch = self.getbranch()
        self.write(branch=branch)
