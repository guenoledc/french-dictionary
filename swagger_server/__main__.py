#!/usr/bin/env python3

import connexion
import os
import flask
import waitress

from swagger_server import encoder


def root(app, api):
    def func():
        #print(app, api)
        return flask.redirect(api.base_path+app.options.openapi_console_ui_path)
    return func

def beforeRequest():
    with flask.request as r:
        print(r.method, r.url, r.environ["REMOTE_ADDR"], dict(r.headers))

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    
    app.app.before_request(beforeRequest)

    app.app.json_encoder = encoder.JSONEncoder
    api = app.add_api('swagger.yaml', arguments={'title': 'French Dictionary'}, pythonic_params=True)
    app.add_url_rule("/", None, root(app, api))
    port = int(os.environ.get("PORT", 8080))
    #app.run(port=port, host="0.0.0.0")
    waitress.serve(app, port=port, host="*")


if __name__ == '__main__':
    main()
