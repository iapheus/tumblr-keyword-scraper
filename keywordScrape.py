from bs4 import BeautifulSoup
import requests

linkList = [] #This is where you paste your blog links

print("Enter the keyword: ")
keyword = input()
blogList = []


# In this section, we get the usernames in the notes section of the links we get from linkList
for link in range(len(linkList)):
    linkURL = requests.get(linkList[link] + "#notes")
    linkUrlSoup = BeautifulSoup(linkURL.text, "html.parser")
    span = linkUrlSoup.find_all(class_="action")
    for tag in span:
        a = tag.find_all("a", {"rel": "nofollow"})
        for tag in a:
            for i in tag:
                if i not in blogList: # We check not to get the same username multiple times
                    blogList.append(i)

# In this section, we search for our keyword among the blogs with the usernames we got from the blogList
for length in range(len(blogList)):
    blogURL = requests.get("https://" + blogList[length] + ".tumblr.com")
    if keyword.lower() in blogURL.text.lower():
        print ('Found, blog name is: ' + blogList[length])
        with open("blogNames.txt", "a") as blogNameText:
            blogNameText.write("The name of the blog with the " + keyword + " in it: " + blogList[length] + "\n")
    else:
        print("Not found, blog counter: " + str(length+1))
        continue
blogNameText.close()
