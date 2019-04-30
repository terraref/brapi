#!/usr/bin/env python

import logging

import connexion
from connexion.resolver import RestyResolver


def token_auth(token, required_scopes):
    print("token_auth")
    return {'user': 'admin'}


def bearer_auth(token):
    print("bearer_auth")
    return {'user': 'admin'}


def basic_auth(username, password, required_scopes=None):
    print("basic_auth")
    return {'user': 'admin'}


if __name__ == '__main__':
    debug = True

    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    app = connexion.FlaskApp(__name__, debug=debug)

    app.add_api('brapi.yaml',
                arguments={'title': 'TERRA-REF BRAPI'},
                resolver=RestyResolver('api'),
                resolver_error=501)

    # app.run(port=5000, host=None, server='flask', debug=debug, use_reloader=False)
    app.run(port=5000, host=None, server='flask', debug=debug)
