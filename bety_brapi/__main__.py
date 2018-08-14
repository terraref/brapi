#!/usr/bin/env python3

import connexion

from bety_brapi import encoder, database
from flask_sqlalchemy import SQLAlchemy
import logging
import sys


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'BrAPI'})
    app.run(port=8080)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)

    app.app.logger.addHandler(handler)
    app.app.logger.setLevel(logging.DEBUG)

    app.run(port=8080)


if __name__ == '__main__':
    main()
