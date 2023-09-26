import csv
import collections
import sys


def sortFunction(dict: dict):
    return {k: v for k, v in sorted(
        dict.items(), key=lambda item: item[1])}


def sorting(pageName):
    try:
        analysis_file = open("{}.csv".format(pageName), "r", newline="")
    except FileNotFoundError:
        print("file not found error")
        sys.exit()
    fieldNames = ["date", "likes", "comments", "shares", "score"]
    analysis_file = csv.DictReader(analysis_file, fieldNames)
    data = {}
    sorted_shares = {}
    sorted_comments = {}
    sorted_likes = {}
    for row in analysis_file:
        if row["date"] != "date":
            data[row["date"]] = int(row["score"])
            sorted_shares[row["date"]] = int(row["shares"])
            sorted_comments[row["date"]] = int(row["comments"])
            sorted_likes[row["date"]] = int(row["likes"])

    soretedScore = sortFunction(data)
    soretedShares = sortFunction(sorted_shares)
    sorted_comments = sortFunction(sorted_comments)
    sorted_likes = sortFunction(sorted_likes)
    soretedScore = collections.OrderedDict(sorted(soretedScore.items()))
    sorted_likes = collections.OrderedDict(sorted(sorted_likes.items()))
    sorted_comments = collections.OrderedDict(sorted(sorted_comments.items()))
    sorted_shares = collections.OrderedDict(sorted(sorted_shares.items()))
    return [soretedShares, sorted_comments, sorted_likes,soretedScore]
