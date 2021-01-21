import pandas as pd

import config
import phe.cases.admissions85
import phe.cases.admissionstotal


class Interface:

    def __init__(self):
        """

        """

        configurations = config.Config()

        self.admissionstotal = phe.cases.admissionstotal.AdmissionsTotal(url=configurations.url)
        self.admissions85 = phe.cases.admissions85.Admissions85(url=configurations.url)

    def exc(self, tab: str) -> (pd.DataFrame, pd.DataFrame, str):
        """

        :param tab:
        :return:
        """

        return {
            'admissionstotal': self.admissionstotal.exc(),
            'admissions85': self.admissions85.exc()
        }.get(tab, LookupError(tab + ' is not a valid tab option'))
