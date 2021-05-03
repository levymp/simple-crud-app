from marshmallow import Schema
from marshmallow.fields import Email, Int, Str, Url, 

class GithubRepoSchema(Schema):
    id = Int(required=True)
    repo_name = Str()
    full_name = Str()
    language = Str()
    description = Str()
    repo_url = Url()

class KudoSchema(Schema):
    user_id = Email(required=True)
    