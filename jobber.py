import os
from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import get_jobs
from freelancersdk.resources.projects.projects import search_projects
from freelancersdk.resources.projects.helpers import create_search_projects_filter, create_get_projects_user_details_object, create_get_projects_project_details_object


def load_text(filename, mode='r', encoding='utf-8'):
    with open(filename, mode, encoding=encoding) as f:
        txt = f.read()
    return txt


token = load_text('token.txt')

session = Session(oauth_token=token)

