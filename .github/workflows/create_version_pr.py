#!/usr/bin/env python3
import json
import sys
import re
from tempfile import TemporaryDirectory
from subprocess import check_call
from difflib import unified_diff

from os import environ as env, path
from typing import NamedTuple, cast
from github import Github
from github.ContentFile import ContentFile
from github.GitCommit import GitCommit
from github.GithubException import GithubException
from github.Repository import Repository

API_TOKEN = env["GITHUB_API_TOKEN"]
REPOSITORY = env["GITHUB_REPOSITORY"]
BASE_BRANCH = env.get("GITHUB_BASE_BRANCH", "master")
DRY_RUN = bool(env.get("GITHUB_DRY_RUN", False))


def main():
    if API_TOKEN:
        github = Github(API_TOKEN)
    else:
        print("GITHUB_API_TOKEN is required")
        sys.exit(1)

    repo = github.get_repo(REPOSITORY)
    #head = repo.get_branch(BASE_BRANCH).commit.sha


    p=repo.get_pull(2)
    p.merge(merge_method='rebase')

if __name__ == "__main__":
    main()
