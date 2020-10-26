"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""
import requests


#this is a variable named "addresses"
addresses = []

#this is a variable named "more" that requires a value to be assigned by the user
more = input("Do you have an email address to enter (y/n)? ")

#if "more" is equal to "y", then the user will input their address into the "email" variable
while more == "y":
    email = input("Enter the address: ")
    
    #append the value "email" to existing values of "addresses"
    addresses.append(email)
    
    #if user has more email addresses to input, loop code
    more = input("Do you have another address(y/n)? ")
    
    #loop here
    while more != "y":
        
        #break here
        if more == "n":
            break
        
        #error check here
        else:
            more = input("Please enter a y or n: ")

#print "addresses" value
print(addresses)

response = addresses
response = requests.post("https://webexapis.com/v1/messages", roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vMjZhMDNlMDAtMTcxNS0xMWViLTk2ZGYtZWY4YWY4YTU5ZmZl")