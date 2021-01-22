"""
Module structures
"""
import pandas as pd


class Structures:
    """
    Class Structures
    """

    def __init__(self):
        """
        The constructor
        """

    @staticmethod
    def wide(blob: pd.DataFrame):
        """
        Via a pivot function, each institution's data series is assigned to a
        distinct column, i.e., a reverse wide format. Subsequently, datetime
        formatting & epoch calculations.

        :param blob:
        :return:
        """

        data = blob.pivot_table(columns=['code'],
                                values=blob.columns.drop(labels=['code']))

        data.reset_index(drop=False, inplace=True)
        data.rename(columns={'index': 'date'}, inplace=True)

        return data

    @staticmethod
    def narrow(blob: pd.DataFrame):
        """

        :param blob:
        :return:
        """

        data = blob.drop(columns=['epoch']).melt(id_vars=['date'],
                                                 var_name='code',
                                                 value_name='value')

        return data
