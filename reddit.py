#!/usr/bin/env python3
__author__ = "Leon Wetzel"
__copyright__ = "Copyright 2021, Leon Wetzel"
__credits__ = ["Leon Wetzel"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Leon Wetzel"
__email__ = "post@leonwetzel.nl"
__status__ = "Production"


import praw
from nltk import sent_tokenize


def main():
    with open("reddit_secret.txt", "r", encoding='utf-8') as F:
        secret = F.read()
    with open("reddit_id.txt", "r", encoding='utf-8') as F:
        identifier = F.read()
    with open("reddit_user_id.txt", "r", encoding='utf-8') as F:
        user_id = F.read()

    reddit = praw.Reddit(
        client_id=identifier,
        client_secret=secret,
        user_agent="Ashleigh Dev Team",
    )

    subject = reddit.redditor(name=user_id)
    comments = [comment.body for comment
                in subject.comments.new(limit=None)]
    sentences_per_comment = [sent_tokenize(comment)
                             for comment in comments]
    sentences= [comment.replace("\n", "").strip() for sentence
                in sentences_per_comment for comment in sentence]

    with open("quips.txt", "w", encoding='utf-8') as F:
        for sentence in sentences:
            F.write(f"{sentence}\n")


if __name__ == '__main__':
    main()