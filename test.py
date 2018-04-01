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
	# get_commits Return  type:github.PaginatedList.PaginatedList of github.Commit.Commit
	# learn more about commit
	# http://pygithub.readthedocs.io/en/latest/github_objects/Commit.html#github.Commit.Commit.commit
	# learn more about message
	# http://pygithub.readthedocs.io/en/latest/github_objects/GitCommit.html#github.GitCommit.GitCommit.message
	print(a_commit.commit.message)
	print("\n")

# learn more about get_issues_comments
# http://pygithub.readthedocs.io/en/latest/github_objects/IssueComment.html#github.IssueComment.IssueComment.updated_at
all_issues = repo_obj.get_issues_comments(since = datetime.datetime.now() - datetime.timedelta(days = 7))

for an_issue in all_issues:
	# learn more about body
	# http://pygithub.readthedocs.io/en/latest/github_objects/IssueComment.html#github.IssueComment.IssueComment.updated_at
	print(an_issue.body)
	print("updated at")
	# learn more about updated_at
	# http://pygithub.readthedocs.io/en/latest/github_objects/IssueComment.html#github.IssueComment.IssueComment.updated_at
	print(an_issue.updated_at)
	print("\n")