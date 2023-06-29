import requests
from bs4 import BeautifulSoup
import json
from datetime import date
from os import path

COOKIE_FILE = path.dirname(path.realpath(__file__)) + "/../../cookies.txt"

# Functions declaration
def GenerateUrl():
    today = date.today()
    url_date = today.strftime("%Y-%m-%d")
    url = "https://intra.epitech.eu/planning/load?format=json&start=" + url_date + "&end=" + url_date
    return url

def GetCookies():
    file = open(COOKIE_FILE, "r")
    cookies = dict()
    for line in file:
        line = line.split()
        if len(line) == 2:
            cookies[line[0]] = line[1]
        else:
            print("Error: cookies.txt is not well formated.")
            print("\"" + line + "\"")
    return cookies

def GetJson(url, cookies):
    page = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = json.loads(soup.text)
    return content

def ExtractData(content):
    roomsPlanning = dict()

    for activity in content:
        if (activity == None):
            continue
        if (type(activity) == str):
            print("Error: " + content[activity])
            continue
        titleModule = activity.get("titlemodule")

        if (activity.get("room") is None or activity["room"].get("code") is None):
            print(f"Error: activity [{titleModule}] has no room.")
            continue
        room = activity["room"]["code"]

        if (room not in roomsPlanning):
            roomsPlanning[room] = list()
        roomsPlanning[room].append([activity["start"], activity["end"]])
        print(f"activity [{titleModule}] added to room [{room}].")
    return roomsPlanning

def GetActivities():
    url = GenerateUrl()
    cookies = GetCookies()

    content = GetJson(url, cookies)
    roomsPlanning = ExtractData(content)
    print(roomsPlanning)
    return roomsPlanning

# main function
def main():
    roomsPlanning = GetActivities()
    print(roomsPlanning)

if __name__ == "__main__":
    main()
