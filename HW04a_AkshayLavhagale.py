''' Akshay Lavhagale
    Homework 04a - Develop with the Perspective of the Tester in mind '''

import requests
import json


def github_handle(userid):
    res = requests.get(f'https://api.github.com/users/{userid}/repos')

    # Executed if GitHub username is invalid
    if '"message":"Not Found"' in res.text:
        return "The user ID does not exist"
    else:
        repository = {}
        res_json = json.loads(res.text)
        for repo in res_json:
            repository[repo['name']] = 0

        if len(repository.keys()) == 0:
            return "This user has no repository"
        else:
            # Returning a list of names of repositories of a GitHub account
            for item in repository.keys():
                repository[item] = len(json.loads((requests.get(f'https://api.github.com/repos/'
                                                                f'{userid}/{item}/commits')).text))
            # Returning number of commits for a repository
            for repo, commit_count in repository.items():
                print(f"Repo: {repo} Number of commits: {commit_count}")
        return repository
