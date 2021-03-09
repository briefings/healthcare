"""
Module time
"""
import numpy as np
import pandas as pd


class TimeSeries:
    """
    Class Time -> This class converts a field of date strings - named 'date' - to datetime, and
    creates an epoch (milliseconds) field.
    """

    def __init__(self):
        """

        """

    @staticmethod
    def epoch(series: pd.Series):
        """
        Either
            (series - pd.Timestamp('1970-01-01')) // pd.Timedelta('1ms')
              -> floor divide by unit
        or
            (series.astype(np.int64) / (10 ** 6)).astype(np.longlong)
              -> explicitly converting nanoseconds to milliseconds

        :param series: The series that will be converted to epoch time (milliseconds)
        """

        return (series.astype(np.int64) / (10 ** 6)).astype(np.longlong)

    def exc(self, blob: pd.DataFrame):
        """

        :param blob:
        :return:
        """

        blob.loc[:, 'date'] = pd.to_datetime(blob['date'])
        blob.loc[:, 'epoch'] = self.epoch(series=blob['date'])

        return blob
