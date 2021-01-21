"""
Module directories
"""

import os

import config


class Directories:
    """
    Class Directories
    """

    def __init__(self):
        """
        The constructor
        """

        self.configurations = config.Config()

    def cleanup(self):
        """
        Empties the data warehouse

        :return:
        """

        [os.remove(os.path.join(base, file))
         for base, directories, files in os.walk(self.configurations.warehouse)
         for file in files]

        [os.removedirs(os.path.join(base, directory))
         for base, directories, files in os.walk(self.configurations.warehouse, topdown=False)
         for directory in directories
         if os.path.exists(os.path.join(base, directory))]

    def exc(self):
        """

        :return:
        """

        # Empty the data warehouse
        self.cleanup()

        # Re-create the warehouse
        if not os.path.exists(self.configurations.warehouse):
            os.makedirs(self.configurations.warehouse)
