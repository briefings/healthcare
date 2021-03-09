import os
import sys
import logging


def main():

    # Unload data
    logger.info(' {}\n'.format('Unloading data ...'))
    healthcare.algorithms.unload.Unload().exc()

    # Clean-up
    logger.info(' {}\n'.format('Preparing warehouse ...'))
    healthcare.algorithms.directories.Directories().exc()

    # Get the data, and structure it for graphing
    interface = healthcare.cases.interface.Interface()

    for tab in ['admissionstotal', 'totalbeds']:

        # In focus
        logger.info(' Analysing -> \'{}\'\n'.format(tab))

        # Retrieving
        series, institutions, notes = interface.exc(tab=tab)

        # Structuring
        wide, narrow = healthcare.baselines.formatting.Formatting().exc(blob=series)

        # Finally, graphing data ...
        # Note: phe.highcharts.graphseries involves parallel processing
        path = os.path.join(configurations.warehouse, tab)
        healthcare.tableau.graphseries.GraphSeries(blob=narrow, institutions=institutions, path=path).exc()
        healthcare.highcharts.graphseries.GraphSeries(blob=wide, institutions=institutions, path=path).exc()


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    import healthcare.cases.interface
    import healthcare.baselines.formatting

    import healthcare.algorithms.unload
    import healthcare.algorithms.directories
    
    import healthcare.highcharts.graphseries
    import healthcare.tableau.graphseries

    import config
    configurations = config.Config()

    main()
