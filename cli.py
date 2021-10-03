from github import Github
import argparse as ap

print ("Welcome to the Multitudes CLI!  Time to dig some data... ")
print ("Who's the repo-wner'?")
username = input()
print ("Whats the repo's name?")
repository = input()
print("Digging for Data...")
g = Github()

#very nice
user = g.get_user(username)
repo = user.get_repo(repository)
pulls = repo.get_pulls(state='open')
print("Found a total of "+ str(pulls.totalCount) +" open pull requests at "+ username+"/"+repository+".")
print("See you next time :)")

#print(g)