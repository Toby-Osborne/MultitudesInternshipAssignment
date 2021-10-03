from pprint import pprint
from github import Github


username = 'microsoft'
repository = "TypeScript"

g = Github()

user = g.get_user(username)
repo = user.get_repo(repository)
pulls = repo.get_pulls(state='all')
print(pulls.totalCount)


#print(g)