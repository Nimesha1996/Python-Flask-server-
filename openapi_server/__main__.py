#!/usr/bin/env python

import connexion

from openapi_server import encoder
from openapi_server import appConfig

def main():
#    app = connexion.App(__name__, specification_dir='./openapi/')
    app = appConfig.connex_app
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Swagger Petstore - OpenAPI 3.0'},
                pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()

