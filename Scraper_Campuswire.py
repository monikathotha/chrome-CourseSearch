import time
import requests
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = 'https://campuswire.com/c/G4A2F7542/feed'
dataFile = 'AlldataFileCampuswire.txt'
allURLFile = 'AllURLFileCampuswire.txt'


def get_campuswireHTML():

    driver = webdriver.Chrome()
    driver.get(base_url)
    urlList = []

    #Get total count of posts
    time.sleep(10)
    total_feeds = int(driver.execute_script('return document.getElementsByClassName("post-ref")[0].innerHTML')[1:])

    df = open(dataFile, 'a')
    urlFile = open(allURLFile, 'a')

    #total_feeds = 1
    for feed in range(total_feeds):
        url = base_url + "/" + str(feed+1)

        driver.get(url)
        time.sleep(20)
        try:
            res_html = driver.execute_script('return document.getElementsByClassName("modal-body")[0].innerHTML')
            soup = BeautifulSoup(res_html, 'html.parser')

            #print(soup.get_text(separator=' '))
            df.write(soup.get_text(separator=' ').replace("\n", " ").replace("\r", " "))
            df.write('\n')
            
            urlFile.write(url)
            urlFile.write('\n')
        except:
            print("Could not get HTML of this URL: ", url)
    
    driver.close()
    df.close()
    urlFile.close()


get_campuswireHTML()