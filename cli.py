from github import Github
import time
import math

print ("=======================================")
print ("Welcome to the Multitudes CLI!  Time to dig some data... ")
print ("=======================================")
#checking rate limit, before searching
g = Github()

print ("You have "+str(g.rate_limiting[0])+" queries out of "+str(g.rate_limiting[1])+" per hour")
remSec = int(g.rate_limiting_resettime-time.time())

print (str(remSec/60).split(".")[0] + " minutes " + str(remSec%60) + " seconds remaining till rate limit reset")
print ("=======================================")

print ("Who's the repo-wner'?")
username = input()
print ("=======================================")
print ("Whats the repo's name?")
repository = input()
print ("=======================================")
print("Digging for Data...")
print ("=======================================")


#very nice
user = g.get_user(username)
repo = user.get_repo(repository)
pulls = repo.get_pulls(state='open')
print("Found a total of "+ str(pulls.totalCount) +" open pull requests at "+ username+"/"+repository+".")
print("See you next time :)")
print ("=======================================")

#print(g)