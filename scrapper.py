import os
from facebook_scraper import get_posts
import datetime
from getpass import getpass
import csv


def scraping():
    username, passw = ["", ""]
    if "userinfo.txt" in os.listdir():
        updateInfo = input("Do you want to update your credintials? y/n: ")
        if updateInfo == "y":
            username = input("Enter your FB account mail: ")
            passw = getpass("Enter your FB account password: ")
            with open("userinfo.txt","w",encoding="utf-8") as f:
                f.write(username+"\n")
                f.write(passw+"\n")
        else:
            readFile = open("userinfo.txt", "r", encoding="utf-8").readlines()
            username = readFile[0].replace("\n", "")
            passw = readFile[1].replace("\n", "")
    else:
        print("[INFO]: Enter valid information")
        username = input("Enter your FB account mail: ")
        passw = getpass("Enter your FB account password: ")
        with open("userinfo.txt","w",encoding="utf-8") as f:
            f.write(username+"\n")
            f.write(passw+"\n")

    pageName = input("Enter the page name: ")
    analysis_file = open("{}.csv".format(pageName), "a", newline="")
    fieldNames = ["date", "likes", "comments", "shares", "score"]
    analysis_file = csv.DictWriter(analysis_file, fieldNames)
    analysis_file.writeheader()
    for post in get_posts('{}'.format(pageName), credentials=(username, passw)):
        likes = post["likes"]
        shares = post["shares"]
        comments = post["comments"]
        date = post["time"]
        score = likes+shares+comments
        analysis_file.writerow({"date": date, "likes": likes,
                                "comments": comments, "shares": shares, "score": score})
    return pageName
