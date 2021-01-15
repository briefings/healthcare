import json
import os

import dask
import pandas as pd


class GraphSeries:

    def __init__(self, blob: pd.DataFrame, institutions: pd.DataFrame, path: str):
        self.blob = blob
        self.institutions = institutions
        self.path = path

    def series(self, code):
        excerpt = self.blob[['epoch', code]].rename(columns={code: 'admissions'})
        dictionary = excerpt.to_dict(orient='records')

        data = {'code': code, 'data': dictionary}

        return data

    def write(self, data):
        """
        filestring = os.path.join(self.path, 'admissions.json')
        if os.path.isfile(filestring):
            os.remove(filestring)

        :param data: The data that would be written into a file
        :return:
        """

        with open(os.path.join(self.path, 'admissions.json'), 'w') as disk:
            json.dump(data, disk)

    def exc(self):
        computations = [dask.delayed(self.series)(code=c['code'])
                        for c in self.institutions.to_dict(orient='records')]

        dask.visualize(computations, filename='tableau', format='pdf')

        self.write(dask.compute(computations, scheduler='processes')[0])
