import requests
import json
from operator import itemgetter
from django.http import HttpResponse


def sort_by_key(key, list_of_dict, reverse=True):
    return sorted(list_of_dict, key = itemgetter(key), reverse=reverse)


def get_repos(request, org_name):
    try:
        m = int(request.GET.get("m", 5))
        n = int(request.GET.get("n", 5))
    except ValueError:
        return HttpResponse("m and n should be integers", content_type="text/plain")
    repo_list_org = json.loads(requests.get("https://api.github.com/orgs/{}/repos".format(org_name)).content)
    top_n_repos = sort_by_key("forks_count", repo_list_org)[:n]
    for repo in top_n_repos:
        repo_contributors = json.loads(requests.get(repo['contributors_url']).content)
        top_m_contributors = sort_by_key("contributions", repo_contributors)[:m]
        repo["top_" + str(m) + "_contributors"] = top_m_contributors
    return HttpResponse(top_n_repos, content_type="text/json")