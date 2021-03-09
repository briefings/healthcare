"""
Module patterns
"""
import pandas as pd


class Patterns:
    """
    Class Patterns
    """

    def __init__(self):
        """
        The constructor
        """

    @staticmethod
    def dictionary():
        """

        :return:
        """

        return {'Bmi': 'BMI', 'Nhs': 'NHS', 'Cic': 'C.I.C.', "Andrew'S": "Andrew's",
                "King'S": "King's", "Anthony'S": "Anthony's", "Guy'S": "Guy's",
                "George'S": "George's", "Augustine'S": "Augustine's", "Women'S": "Women's",
                "Children'S": "Children's", "Mary'S": "Mary's", "Peter'S": "Peter's",
                "Hugh'S": "Hugh's", "(Loc)": "(LOC)", "Vii'S": "VII's",
                "Citycare": "CityCare", "Hca": "HCA"}

    def format(self, blob: pd.DataFrame):
        """

        :param blob:
        :return:
        """

        for key, value in self.dictionary().items():

            blob.loc[:, 'institution'] = blob['institution'].str.replace(
                pat=key, repl=value, case=True, regex=False)

        return blob

    def exc(self, blob: pd.DataFrame):
        """

        :param blob:
        :return:
        """

        blob.loc[:, 'institution'] = blob['institution'].str.title()
        blob = self.format(blob=blob.copy())

        return blob
