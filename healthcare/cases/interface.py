import pandas as pd

import config
import healthcare.cases.admissions85
import healthcare.cases.admissionstotal
import healthcare.cases.mvbeds
import healthcare.cases.mvbedscovid
import healthcare.cases.totalbeds
import healthcare.cases.totalbedscovid


class Interface:

    def __init__(self):
        """

        """

        configurations = config.Config()
        uri = configurations.uri

        self.admissionstotal = healthcare.cases.admissionstotal.AdmissionsTotal(uri=uri)
        self.admissions85 = healthcare.cases.admissions85.Admissions85(uri=uri)
        self.mvbeds = healthcare.cases.mvbeds.MVBeds(uri=uri)
        self.mvbedscovid = healthcare.cases.mvbedscovid.MVBedsCOVID(uri=uri)
        self.totalbeds = healthcare.cases.totalbeds.TotalBeds(uri=uri)
        self.totalbedscovid = healthcare.cases.totalbedscovid.TotalBedsCOVID(uri=uri)

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
