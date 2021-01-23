import pandas as pd

import config
import phe.cases.admissions85
import phe.cases.admissionstotal
import phe.cases.mvbeds
import phe.cases.mvbedscovid
import phe.cases.totalbeds
import phe.cases.totalbedscovid


class Interface:

    def __init__(self):
        """

        """

        configurations = config.Config()
        uri = configurations.uri

        self.admissionstotal = phe.cases.admissionstotal.AdmissionsTotal(uri=uri)
        self.admissions85 = phe.cases.admissions85.Admissions85(uri=uri)
        self.mvbeds = phe.cases.mvbeds.MVBeds(uri=uri)
        self.mvbedscovid = phe.cases.mvbedscovid.MVBedsCOVID(uri=uri)
        self.totalbeds = phe.cases.totalbeds.TotalBeds(uri=uri)
        self.totalbedscovid = phe.cases.totalbedscovid.TotalBedsCOVID(uri=uri)

    def exc(self, tab: str) -> (pd.DataFrame, pd.DataFrame, str):
        """

        :param tab:
        :return:
        """

        return {
            'admissionstotal': self.admissionstotal.exc(),
            'admissions85': self.admissions85.exc(),
            'mvbeds': self.mvbeds.exc(),
            'mvbedscovid': self.mvbedscovid.exc(),
            'totalbeds': self.totalbeds.exc(),
            'totalbedscovid': self.totalbedscovid.exc()
        }.get(tab, LookupError(tab + ' is not a valid tab option'))
