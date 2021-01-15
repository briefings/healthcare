import collections

import numpy as np
import pandas as pd


# noinspection PyUnresolvedReferences,PyProtectedMember
class AdmissionsTotal:

    def __init__(self, url):

        self.url = url
        Dimensions = collections.namedtuple(typename='Dimensions', field_names=['all', 'descriptive'])
        self.dimensions = Dimensions._make((['region', 'code', 'institution'], ['region', 'institution']))

        self.datacells = 'C:KM'  # type='Data', field_names=['cells', 'start', 'end']
        self.dataend = 515
        self.datastart = 24

        self.fieldnames = 'F:KM'  # type='FieldNames', field_names=['cells', 'row']
        self.fieldrow = 13

        self.notes = "Provider Level Data - Admissions - Number of patients admitted with COVID-19 (Last 24hrs)"

    def readings(self) -> pd.DataFrame:

        try:
            return pd.read_excel(io=self.url, sheet_name='Admissions Total', header=None,
                                 skiprows=np.arange(self.datastart - 1), usecols=self.datacells,
                                 nrows=(self.dataend - self.datastart + 1))
        except OSError as err:
            raise Exception(err.strerror) from err

    def fields(self) -> list:

        try:
            names = pd.read_excel(
                io=self.url, sheet_name='Admissions Total', header=None, skiprows=self.fieldrow - 1,
                usecols=self.fieldnames, nrows=1, parse_dates=True)
        except OSError as err:
            raise Exception(err.strerror) from err

        return self.dimensions.all + names.astype(str).values.tolist()[0]

    def institutions(self, blob) -> pd.DataFrame:

        frame = blob[self.dimensions.all]
        assert frame.shape[0] == frame.drop_duplicates().shape[0]

        return frame

    def exc(self) -> (pd.DataFrame, pd.DataFrame, str):

        # Bare minimum checks
        assert self.datacells.rsplit(':')[1] == self.fieldnames.rsplit(':')[1], \
            "The last column of the data cells must be the same as the last column " + \
            "of the fields names"

        # Data
        data = self.readings().set_axis(labels=self.fields(), axis=1)

        # Hence
        sample = data[data.columns.drop(labels=self.dimensions.descriptive)].copy()
        sample.fillna(0, inplace=True)
        institutions = self.institutions(blob=data)

        return sample, institutions, self.notes
