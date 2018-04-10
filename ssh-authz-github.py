#! /usr/bin/env python3

from github import Github
import sys

API_KEY = 'XXX'
GITHUB_ORG = 'YYY'

g = Github(API_KEY)

def user_belongs_to_org(user, org_name):
    orgs = [org.login for org in user.get_orgs()]
    if org_name in orgs:
        return True
    # We can't only rely on this since user membership may not be public but we
    # may be able to list org members
    org_members = [member.login for member in g.get_organization(GITHUB_ORG).get_members()]
    return user.login in org_members

def get_user_ssh_keys(user):
    return [key.key for key in user.get_keys()]

if __name__ == '__main__':
    username = sys.argv[1]
    user = g.get_user(username)
    if not user_belongs_to_org(user, GITHUB_ORG):
        sys.exit(0)
    for key in get_user_ssh_keys(user):
        print(key)
