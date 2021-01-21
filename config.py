import os


class Config:

    def __init__(self):
        self.url = 'https://www.england.nhs.uk/statistics/wp-content/uploads/' \
                   'sites/2/2021/01/Covid-Publication-14-01-2021.xlsx'

        self.warehouse = os.path.join(os.getcwd(), 'warehouse')
