import os
import sys

import yaml

baseDirectory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(baseDirectory)

with open('configuration.yaml') as file:
    configuration = yaml.safe_load(file)


class Configuration:
    SECRET_KEY = configuration['SECRET_KEY']

    def __init__(self):
        pass


class DevelopmentConfiguration(Configuration):
    DEBUG = True


class TestingConfiguration(Configuration):
    Testing = True


class ProductionConfiguration(Configuration):
    pass


config = {
    'development': DevelopmentConfiguration,
    'testing': TestingConfiguration,
    'production': ProductionConfiguration,
    'default': DevelopmentConfiguration
}

