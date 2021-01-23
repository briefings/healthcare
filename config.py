import os


class Config:

    def __init__(self):
        """
        The constructor
        """

        self.source = 'https://www.england.nhs.uk/statistics/wp-content/uploads/' \
                      'sites/2/2021/01/Covid-Publication-14-01-2021.xlsx'

        self.warehouse = os.path.join(os.getcwd(), 'warehouse')
        self.uri = os.path.join(os.getcwd(), 'data', 'Covid-Publication-14-01-2021.xlsx')
