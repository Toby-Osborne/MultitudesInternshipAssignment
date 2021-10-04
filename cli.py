from github import Github
import time

#introduction
print ("========================================")
print ("Welcome to the Multitudes CLI!  Time to dig some data... ")
print ("                       .-'~~~-.\n                     .'o  oOOOo`.\n                    :~~~-.oOo   o`.\n                     `. \ ~-.  oOOo.\n                       `.; / ~.  OO:\n                       .'  ;-- `.o.'\n                      ,'  ; ~~--'~\n                      ;  ;\n_______\|/__________\\;_\\//___\|/________")
print ("========================================")

#initially define variable
g = Github()

#checking rate limit, before searching
print (f"You have {g.rate_limiting[0]} queries out of {g.rate_limiting[1]} per hour") #prints remaining queries 
remSec = int(g.rate_limiting_resettime-time.time()) #prints time to reset adjusted from Epoch to relative time in min/sec

print (f"{str(remSec/60).split('.')[0]} minutes {remSec%60} seconds remaining till rate limit reset") #
print ("========================================")


#exception handling with warnings
while(1):
    print ("Who's the repo-wner'?")
    username = input()
    print ("========================================")
    
    try:
        user = g.get_user(username) #attempts to get username
        break
    except:
        if g.rate_limiting[0] > 0:
            print("This is not a valid username") #other exception could be a 404 exception
            print (f"You have {g.rate_limiting[0]} queries out of {g.rate_limiting[1]} per hour") #prints remaining queries 
        else:
            print("You have 0 remaining queries for this hour, exiting ...") #if remaining time is zero then this exception is thrown
            exit()

while(1):
    print ("Whats the repo's name?")
    repository = input()
    print ("========================================")
    try:
        repo = user.get_repo(repository)
        break
    except:
        if g.rate_limiting[0] > 0:
            print(f"This is not a valid repository for user {username}")
            print (f"You have {g.rate_limiting[0]} queries out of {g.rate_limiting[1]} per hour") #prints remaining queries 
        else:
            print("You have 0 remaining queries for this hour, exiting ...")
            exit()


print("Digging for Data...")
print ("========================================")

pulls = repo.get_pulls(state='open') #gets a list of pulls in the omicrosoftpen state using the state argument

print(f"Found a total of {pulls.totalCount} open pull requests at {username}/{repository}.")
print("See you next time :)")
print ("========================================")


