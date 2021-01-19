import glob
import json
import os

import dask
import pandas as pd


class GraphSeries:

    def __init__(self, blob: pd.DataFrame, institutions: pd.DataFrame, path: str):
        """
        
        :param blob: A dataframe of institutions data; reversed wide format
        :param institutions: The distinct health institutions
        :param path: The data will be saved here
        """

        self.blob = blob
        self.institutions = institutions
        self.path = path

    def series(self, code, institution, region):
        """
        
        """

        excerpt = self.blob[['epoch', code]].rename(columns={code: 'admissions'})
        dictionary = excerpt.to_dict(orient='records')

        data = {'code': code, 'institution': institution,
                'region': region, 'data': dictionary}

        with open(os.path.join(self.path, code + '.json'), 'w') as disk:
            json.dump(data, disk)

    def inspect(self):
        """
        Inspect: Distinct institutions & distinct files

        """

        files = glob.glob(os.path.join(self.path, '*.json'))
        assert len(files) == self.institutions.shape[0]

    def exc(self):
        """
        
        """

        computations = [dask.delayed(self.series)(
            code=c['code'], institution=c['institution'], region=c['region'])
            for c in self.institutions.to_dict(orient='records')]

        dask.visualize(computations, filename='highcharts', format='pdf')
        dask.compute(computations, scheduler='processes')
        self.inspect()
