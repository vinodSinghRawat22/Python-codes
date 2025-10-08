# 49. Write a script that extracts hashtags from a tweet. 

tweet = input("Enter a tweet: ")

words = tweet.split()

hashtags = []
for word in words: 
    if word[0] == '#'and len(word)>1 :
        hashtags.append(word)

if hashtags: 
    print("\nHashtags present in tweet is/are: ")
    for word in hashtags:
        print( f"   {word}", end = ' ')
else: 
    print("No hashtag present in the tweet.")