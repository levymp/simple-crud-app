from ..kudo.service import Service as Kudo
from ..kudo.schema import GithubRepoSchema
from json import dumps, loads


def create_repo(data, email):
    github_repo = GithubRepoSchema().load(loads(data))

    if github_repo.errors:
        return json_response({"error": github_repo.errors}, 422)
    
    kudo = Kudo(email).create_kudo_for(github_repo)
    return json_response(kudo)

def get_kudo(repo_id, email):
    kudo = Kudo(email).find_kudo(repo_id)
    status = 200 if kudo else 422
    response = kudo or {"error": "kudo not found"}
    return json_response(response, status=status)

def update(repo_id, data, email):
    github_repo = GithubRepoSchema().load(loads(data))

    if github_repo.errors:
        return json_response({"error": github_repo.errors}, 422)
    
    kudo_service = Kudo(email)

    if kudo_service.update_kudo_with(repo_id, github_repo):
        return json_response(github_repo.data)
    else:
        return json_response({"error": "kudo not found"})


def delete(repo_id, email):
    kudo_service = Kudo(email)
    if kudo_service.delete_kudo_for(repo_id):
        return json_response({})
    else:
        return json_response({"error": "kudo not found"}, 404)


def json_response(payload, status=200):
    return (dumps(payload), status, {"content-type": "application/json"})
