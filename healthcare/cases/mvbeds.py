import collections

import numpy as np
import pandas as pd

import healthcare.algorithms.patterns


# noinspection PyUnresolvedReferences,PyProtectedMember
class MVBeds:

    def __init__(self, uri):
        """

        :param uri:
        """

        self.uri = uri
        Dimensions = collections.namedtuple(typename='Dimensions', field_names=['all', 'descriptive'])
        self.dimensions = Dimensions._make((['region', 'code', 'institution'], ['region', 'institution']))

        Data = collections.namedtuple(typename='Data', field_names=['sheet_name', 'cells', 'start', 'end'])
        self.data = Data._make(('MV Beds Occupied', 'C:JZ', 24, 515))

        FieldNames = collections.namedtuple(typename='FieldNames', field_names=['cells', 'row'])
        self.fieldnames = FieldNames._make(('F:JZ', 13))

        self.notes = "Provider Level Data - Mechanical Ventilation beds - occupied (as at 08:00)"

    def dataset(self) -> pd.DataFrame:
        """

        :return:
        """

        try:
            return pd.read_excel(io=self.uri, sheet_name=self.data.sheet_name, header=None,
                                 skiprows=np.arange(self.data.start - 1), usecols=self.data.cells,
                                 nrows=(self.data.end - self.data.start + 1))
        except OSError as err:
            raise Exception(err.strerror) from err

    def fields(self) -> list:
        """

        :return:
        """

        try:
            names = pd.read_excel(
                io=self.uri, sheet_name=self.data.sheet_name, header=None, skiprows=self.fieldnames.row - 1,
                usecols=self.fieldnames.cells, nrows=1, parse_dates=True)
        except OSError as err:
            raise Exception(err.strerror) from err

        return self.dimensions.all + names.astype(str).values.tolist()[0]

    def institutions(self, blob) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        frame = blob[self.dimensions.all]
        assert frame.shape[0] == frame.drop_duplicates().shape[0]
        frame = healthcare.algorithms.patterns.Patterns().exc(blob=frame.copy())

        return frame

    def exc(self) -> (pd.DataFrame, pd.DataFrame, str):
        """

        :return:
        """

        # Bare minimum checks
        assert self.data.cells.rsplit(':')[1] == self.fieldnames.cells.rsplit(':')[1], \
            "The last column of the data cells must be the same as the last column " + \
            "of the fields names"

        # Data
        data = self.dataset()
        data = data.set_axis(labels=self.fields(), axis=1)

        # Hence
        series = data[data.columns.drop(labels=self.dimensions.descriptive)].copy()
        series.fillna(0, inplace=True)
        institutions = self.institutions(blob=data)

        return series, institutions, self.notes
