from github import Github
import datetime
import config

# login github and get the github object
# learn more about Github Objects in PyGithub
# http://pygithub.readthedocs.io/en/latest/github_objects.html
github_obj = Github(config.access_token)

# get repo_name from user

# repo_name = input("input repo name: ")
repo_name = "pygithub-test"

# get the Repository Object matches the user's input
# learn more about Repository in PyGithub
# http://pygithub.readthedocs.io/en/latest/github_objects/Repository.html

# get_user()
# get_repo()
# learn more about Main class: Github in PyGithbb
# http://pygithub.readthedocs.io/en/latest/github.html
repo_obj = github_obj.get_user().get_repo(repo_name)

# branch_name = input("branch_name: ")
branch_name = "master"

# learn more about get_commits()
# http://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.get_commits
# learn more about timedelta
# https://docs.python.org/3/library/datetime.html#timedelta-objects
all_commits = repo_obj.get_commits(sha = branch_name, since = datetime.datetime.now() - datetime.timedelta(days = 7), until = datetime.datetime.now())

for a_commit in all_commits:
	print(a_commit.sha)
	print(a_commit.commit.message)
	print("\n")
