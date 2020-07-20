from flask import Flask
from flask_bootstrap import Bootstrap

from config import config

bootstrap = Bootstrap()


def create_app(configuration_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[configuration_name])

    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    @app.cli.command()
    def test():
        import unittest
        tests = unittest.TestLoader().discover('tests')
        unittest.TextTestRunner(verbosity=2).run(tests)

    return app
