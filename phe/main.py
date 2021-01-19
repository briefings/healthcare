import os
import sys
import logging


def main():

    sample, institutions, notes = phe.cases.admissionstotal.AdmissionsTotal(url=configurations.url).exc()
    logger.info('\n{}\n\n'.format(sample.head()))

    wide, narrow = phe.baselines.formatting.Formatting().exc(blob=sample)
    logger.info('\n{}\n\n'.format(wide.head()))
    logger.info('\n{}\n\n'.format(narrow.head()))

    logger.info('\n{}\n\n'.format(institutions))


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    import config

    configurations = config.Config()

    import phe.cases.admissionstotal
    import phe.baselines.formatting

    main()
