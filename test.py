from github import Github
import datetime
import config

github_obj = Github(config.access_token)

repo_name = input("input repo name: ")

repo_obj = github_obj.get_user().get_repo(repo_name)

branch_name = input("branch_name: ")

commits = repo_obj.get_commits(sha = branch_name, since = datetime.datetime.now() - datetime.timedelta(days = 7), until = datetime.datetime.now())

for cm in commits:
	print(cm.sha)
	print(cm.commit.message)
	print("\n")