from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd

startURL = "https://www.trekbikes.com/us/en_US/bikes/c/B100/?q=:relevance&page=4&pageSize=24"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(startURL)
time.sleep(30)
tempList = []
def scrape():
    headers = ["Price"]
    planetData = []
    for i in range(1,14):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for li_tag in soup.find_all("li",attrs ={"class","cell productListItem product-list__item"}):
            #article_tags = li_tag.find("article", attrs={"class", "product-tile"})
            #div_tags = article_tags.find("div", attrs={"class", "product-tile__wrap"})
            #a_tags = div_tags.find_all("a", attrs ={"class", "product-tile__link"})
            #print(len(a_tags))
            #div4_tags = div_tags.find_all("div", attrs={"class", "product-tile__info"})
            #p_tags = div4_tags.find("p")
            for bob in li_tag.find_all("span", attrs={"class","product-tile__saleprice"}):
                tempList.append(bob.get_text())
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
        try: 
            browser.find_element(By.XPATH, value='/html/body/div[5]/div[2]/div/div[2]/main/section/div/div[2]/div/div[3]/div[1]/nav/div[2]/a').click()
            print(f"page{i} scraping completed")
        except:
            df = pd.DataFrame(tempList)
            df.to_csv("TrekBikesPrices.csv", index = False)
            print(df.head())
scrape()            
    
    
    #with open("EbizTestPrices.csv","w") as f:
    #    csvWriter = csv.writer(f)
    #    csvWriter.writerow(headers)
    #    csvWriter.writerow(tempList)
    #df = pd.DataFrame(tempList)
    #df.to_csv("TrekBikesPrices.csv", index = False)
    #print(df.head())
#scrape()            
