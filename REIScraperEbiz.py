from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd

startURL = "https://www.rei.com/c/bikes?ir=category%3Amountain-bikes&r=category%3Acycling%7Cbikes"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(startURL)
time.sleep(10)
tempList = []
def scrape():
    headers = ["Price"]
    planetData = []
    for i in range(1,6):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for li_tag in soup.find_all("li",attrs ={"class","pPe0GNuagvmEFURs1Q_vm"}):
            div_tags = li_tag.find("div", attrs={"class", "_2_c4c8sdaRnQ6CTAsAlQLM _2gicqyVSZCnmQ7-YrmbwIl"})
            div2_tags = div_tags.find("div", attrs={"class", "_1zwqhlCzOK-xETXwFg_-iZ"})
            tempList.append(div2_tags.find("span"))
            #print(tempList)
            #print(div2_tags)
            #tempList = []
            #for index,div2_tag in enumerate(div2_tags):
            #    if index == 0:
            #        tempList.append(div2_tag.find_all("span")[0].contents[0])
            #        
            #    else:
            #        try:
            #            tempList.append(div2_tag.contents[0])
            #        except:
            #            tempList.append("")
            planetData.append(tempList) 
            #browser.find_element(By.XPATH, value='//*[@id="app-main"]/div/div/div[2]/div[2]/div[3]/div[2]/nav/a[1]').click()
            #print(f"page{i} scraping completed")
    #with open("EbizTestPrices.csv","w") as f:
    #    csvWriter = csv.writer(f)
    #    csvWriter.writerow(headers)
    #    csvWriter.writerow(tempList)
    df = pd.DataFrame(tempList)
    df.to_csv("REIBikePrices.csv", index = False)
    print(df.head())
scrape()            
