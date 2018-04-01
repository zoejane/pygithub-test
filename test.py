from github import Github
import config

g = Github(config.github_token)

for repo in g.get_user().get_repos():
	print(repo.name)