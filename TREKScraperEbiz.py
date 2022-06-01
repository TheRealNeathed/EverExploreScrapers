# Hello, and welcome to our TREK scraper. This scraper scrapes bike price data from the TREK website and uploads it to TrekBikesPrices.csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
# this is just QOL for the webdriver - making it easier to use and adding in a sleep statement so no bugs happen if the website is slow to load
browser = webdriver.Chrome("chromedriver.exe")
tempList = []
# the main function that will gather the price data
def scrape():
    headers = ["Price"]
    planetData = []
    # There are 14 pages of data, so we have the code iterate through each page
    for i in range(1,14):
        # Inside the loop, we add the trek bikes URL. This shows 24 bikes per page, and there are around 300.
        startURL = f"https://www.trekbikes.com/us/en_US/bikes/c/B100/?q=:relevance&page={i}&pageSize=24"
        browser.get(startURL)
        time.sleep(30)
        # BeautifulSoup is a library that will parse the website to make data more readable
        soup = BeautifulSoup(browser.page_source, "html.parser")
        # The code goes through each list tag in the website...
        for li_tag in soup.find_all("li",attrs ={"class","cell productListItem product-list__item"}):
            # ... and then through each span tag, which contain the prices
            for span in li_tag.find_all("span", attrs={"class","product-tile__saleprice"}):
                tempList.append(span.get_text())
            planetData.append(tempList)
        # just a print statement to check if the scraping finished
        print(f"page{i} scraping completed")
        # going to the next page
        i = i+1
    # adding the prices into a spreadsheet
    df = pd.DataFrame(tempList)
    df.to_csv("TrekBikesPrices.csv", index = False)
    print(df.head())
scrape()              
# Tada! The spreadsheet is called TrekBikesPrices.csv and contains all the bike prices.
