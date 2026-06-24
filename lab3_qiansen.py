#Qiansen | Lab 3 | Hustle
#TICKET 1A
username = 'qqiho'
#predict: 5 characters 
print (len(username))
#explain: Yes len() counted every character 
#TICKET 2A 
print (username[0])
print (username[4])
#predict: q and o
#explain: The last index is len(username)-1 because the first index starts at zero not one
#TICKET 3A
print ('Welcome to loop @' + username)
print (f'Welcome to loop @{username}')
#predict: I think both lines will look the same
#explain: I thought the first method was easier because you type around the same amount of characters but its more similar to JavaScript
#TICKET 4A
#username [0] = 'X'
#predict:I think there will be an error because at index 0 its q and not x 
# File "/Users/qiansenhuang/Desktop/hustle-summer26/lab3_qiansen.py", line 18, in <module>
    #username [0] = 'X'
    #~~~~~~~~~^^^
    #TypeError: 'str' object does not support item assignment
print (username.upper())
#explain: I think immutable means that it can't be changed or altered
#TICKET 5B
feed = ["caption1", "caption2", "caption3"]
print (len(feed))
print (feed[0])
#predict: 3 and caption1 prints 
#explain: I used index 0 
#TICKET 6B
feed.append("caption4")
#predict: I think it will have 3 as the index
#explain: It's at 3 because the index starts at 0
#TICKET 7B
feed.pop(0)
feed.sort()
print (feed)
#predict: caption1 gets reoved and the rest will end up in alphabetical order
#explain: Pop removes things based on index and sort puts things in alphabetical order
#TICKET 8C
profile = {"username": "qqiho", "followers": "50", "verified": "False"}
print (profile ["followers"])
#profile [0]
#  File "/Users/qiansenhuang/Desktop/hustle-summer26/lab3_qiansen.py", line 45, in <module>
   # profile [0]
   # ~~~~~~~~^^^
#KeyError: 0
#predict: 50 is printed, I think profile [0] tries to find the first index
#explain: Dictionaries use keys instead of indexes because they aren't in order
#TICKET 9C 
profile ["followers"] = "100" 
profile ["bio"] = "hi"
print (profile)
profile.get("datejoined")
print (profile.get("datejoined"))
#predict: I think it'll just print error or key not found
#explain: It's safer because it allows you to check without crashing if it's missing 
#TICKET 10D
print (f '@{username} has {profile["followers"]} followers and {len(feed)} posts. Top post: {feed[0]}' )
#predict: @qqiho has 100 followers and 3 posts. Top post: caption2 (<- caption one was removed)
#explain: Strings, lists, and dictionaries