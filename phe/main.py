import os
import sys
import logging


def main():

    # Clean-up
    phe.algorithms.directories.Directories().exc()

    # Get the data, and structure it for graphing
    interface = phe.cases.interface.Interface()

    for tab in ['admissionstotal', 'admissions85']:

        logger.info('Analysing: \'{}\'\n'.format(tab))

        # Retrieving
        series, institutions, notes = interface.exc(tab=tab)
        logger.info('Sample\n{}\n\n'.format(series.head()))
        logger.info('Institutions\n{}\n\n'.format(institutions))

        # Structuring
        wide, narrow = phe.baselines.formatting.Formatting().exc(blob=series)
        logger.info('\n\nwide:\n')
        logger.info(wide.info())
        logger.info('\n\nnarrow:\n')
        logger.info(narrow.info())

        # Finally, graphing data ...
        # Note: phe.highcharts.graphseries involves parallel processing
        path = os.path.join(configurations.warehouse, tab)
        phe.tableau.graphseries.GraphSeries(blob=narrow, institutions=institutions, path=path).exc()
        phe.highcharts.graphseries.GraphSeries(blob=wide, institutions=institutions, path=path).exc()


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    import phe.cases.interface
    import phe.baselines.formatting
    import phe.algorithms.directories
    
    import phe.highcharts.graphseries
    import phe.tableau.graphseries

    import config
    configurations = config.Config()

    main()
