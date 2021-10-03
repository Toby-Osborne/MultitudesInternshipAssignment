from github import Github
import time
import math

from github.GithubObject import GithubObject

print ("=======================================")
print ("Welcome to the Multitudes CLI!  Time to dig some data... ")
print ("=======================================")
#checking rate limit, before searching
g = Github()

print (f"You have {g.rate_limiting[0]} queries out of {g.rate_limiting[1]} per hour")
remSec = int(g.rate_limiting_resettime-time.time())

print (f"{str(remSec/60).split('.')[0]} minutes {remSec%60} seconds remaining till rate limit reset")
print ("=======================================")


#exception handling with warnings
while(1):
    print ("Who's the repo-wner'?")
    username = input()
    print ("=======================================")
    
    try:
        user = g.get_user(username)
        break
    except:
        if g.rate_limiting[0] > 0:
            print("This is not a valid username")
        else:
            print("You have 0 remaining queries for this hour")

while(1):
    print ("Whats the repo's name?")
    repository = input()
    print ("=======================================")
    try:
        repo = user.get_repo(repository)
        break
    except:
        if g.rate_limiting[0] > 0:
            print("This is not a valid repository")
        else:
            print("You have 0 remaining queries for this hour")

    
print("Digging for Data...")
print ("=======================================")

pulls = repo.get_pulls(state='open')

print("Found a total of "+ str(pulls.totalCount) +" open pull requests at "+ username+"/"+repository+".")
print("See you next time :)")
print ("=======================================")

