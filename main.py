# This is a research program that use wikipidia api to get you a snippet of the thing
# you want to research on. Included selenium to get you to wikipidia itself and research
# what you are looking for

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

# regex for html cleaning
CLEANR = re.compile('<.*?>')
# chrome driver
CHROME_PATH = "/Users/adama/Desktop/chromedriver"
# wiki endpoint
WIKI_ENDPOINT = "https://en.wikipedia.org/w/api.php"


#  just function to rerun program
def ask():
    if input("press 'r' to re-launch research program:") == "r":
        find_me_something_about()


# html tag cleaner function
def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext


# research function
def find_me_something_about():
    # thing you are looking for
    SEARCHPAGE = input("what do you want to research on wikipedia: ")
    # fetching data
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": SEARCHPAGE,
        "srprop": "snippet"
    }

    response = requests.get(url=WIKI_ENDPOINT, params=params)

    data = response.json()
    research_result = data["query"]["search"]

    # printing all data
    for snippets in research_result:
        print(cleanhtml(snippets["snippet"]))

    # option to get to wikipidia for a better research
    if input(f"\n\nsnippet not talking about '{SEARCHPAGE}' accurately type 'more' to go to wikipidia: ") == "more":
        driver = webdriver.Chrome(executable_path=CHROME_PATH)
        driver.get("https://www.wikipedia.org/")
        time.sleep(2)
        driver.find_element(By.XPATH, value="//*[@id='searchInput']").send_keys(SEARCHPAGE)
        driver.find_element(By.XPATH, value="//*[@id='search-form']/fieldset/button").click()

    # calling the function that help re-run research
    ask()


# initializer
if input("press 'r' to launch research") == "r":
    find_me_something_about()
