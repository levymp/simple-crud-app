from . import app, oidc
from flask import request, g, 
from json import loads, dumps
from .kudo.service import Service as Kudo
from .kudo.schema import GithubRepoSchema
from .utils.api_utils import json_response, create_repo, update, delete, get_kudo


@app.route("/kudos", methods=["GET", "POST"])
@oidc.accept_token(True)
def index():
    if request.method == "GET":
        return json_response(Kudo(g.oidc_token_info['sub']).find_all_kudos())
    else:
        return create_repo(request.data, g.oidc_token_info["sub"])

@app.route("/kudo/<int:repo_id>", methods=["GET", "PUT", "DELETE"])
@oidc.accept_token(True)
def kudo(repo_id):
    if request.method == "GET":
        return get_kudo(repo_id, g.oidc_token_info["sub"])
    elif request.method == "PUT":
        return update(repo_id, request.data, g.oidc_token_info["sub"])
    else:
        return delete(repo_id, g.oidc_token_info["sub"])


