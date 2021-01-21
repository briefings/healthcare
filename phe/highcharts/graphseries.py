"""
Module graphseries
"""

import glob
import json
import os

import dask
import pandas as pd


class GraphSeries:
    """
    Class GraphSeries

    Creates the most appropriate data structure for HighCharts graphing
    """

    def __init__(self, blob: pd.DataFrame, institutions: pd.DataFrame, path: str):
        """
        
        :param blob: A summary of the time series per institution; reversed wide format
        :param institutions: The distinct institutions
        :param path: The data will be saved here
        """

        self.blob = blob
        self.institutions = institutions
        self.path = path
        self.branch = self.getbranch()

    def getbranch(self):
        """

        :return:
        """

        branch = os.path.join(self.path, 'highcharts')

        if not os.path.exists(branch):
            os.makedirs(branch)

        return branch

    def series(self, code, institution, region):
        """

        :param code: Institution code
        :param institution: Institution name
        :param region: Institution region
        :return:
        """

        excerpt = self.blob[['epoch', code]].rename(columns={code: 'admissions'})
        dictionary = excerpt.to_dict(orient='records')

        data = {'code': code, 'institution': institution,
                'region': region, 'data': dictionary}

        with open(os.path.join(self.branch, code + '.json'), 'w') as disk:
            json.dump(data, disk)

    def inspect(self):
        """
        Inspect: Distinct institutions & distinct files

        """

        files = glob.glob(os.path.join(self.branch, '*.json'))
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
