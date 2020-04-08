import logging, coloredlogs


logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')


coloredlogs.install()

logging.info('an info messge')
