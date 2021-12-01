# Author MB 12/01/2021

def party_invite(lst):
    for name in lst:
        print("Hi {0}, You're invited to my party on Friday!".format(name))

party_invite(["Jason", "Mateo", "Jordan"])
