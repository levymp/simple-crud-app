from flask import Flask
from flask_cors import CORS
from flask_oidc import OpenIDConnect

app = Flask(__name__)

from . import routes

app.config.update({
    'OIDC_CLIENT_SECRETS': './../../../../client_secrets.json',
    'OIDC_RESOURCE_SERVER_ONLY': True,
    })

oidc = OpenIDConnect(app)

CORS(app)
