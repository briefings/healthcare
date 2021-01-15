"""
Module formatting
"""
import collections

import pandas as pd

import phe.baselines.structures
import phe.baselines.timeseries


# noinspection PyUnresolvedReferences,PyProtectedMember
class Formatting:
    """
    Class Formatting
    """

    def __init__(self):
        """
        The constructor
        """

        Attributes = collections.namedtuple(typename='Attributes', field_names=['names'])
        self.attributes = Attributes._make([['date', 'epoch']])

        self.timeseries = phe.baselines.timeseries.TimeSeries()
        self.structures = phe.baselines.structures.Structures()

    def inspect(self, wide: pd.DataFrame, narrow: pd.DataFrame):
        """

        :param wide:
        :param narrow:
        :return:
        """

        assert narrow.shape[0] == wide.shape[0] * (
                    wide.shape[1] - len(self.attributes.names)), "The ... must have an equal number of ..."

    def exc(self, blob: pd.DataFrame):
        """

        :param blob:
        :return:
        """

        wide = self.structures.wide(blob=blob.copy())
        wide = self.timeseries.exc(blob=wide.copy())
        narrow = self.structures.narrow(blob=wide.copy())

        return wide, narrow
