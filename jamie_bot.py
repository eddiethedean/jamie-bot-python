import praw
import re

#request_re = r'((young )?(jamie (pull up|find|get|search) ))(\w|, | )+'
request_re = r'lee'
keyword_re = r'(?<=(pull up|find|get|search) )[\w, ]+(?=(\.| )?)'

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("all")
i = 0
for comment in subreddit.stream.comments():
    if re.search(request_re, comment.body.lower()):
        print(comment.body)
        print(comment.id)
        comment.reply('Me too!!!')
        i += 1
    if i > 5:break

#for submission in subreddit.hot(limit=10):
    #for comment in submission.comments:
        #if type(comment) == praw.models.reddit.comment.Comment:
            #if re.search(request_re, comment.body.lower()):
                #print(comment.body)



