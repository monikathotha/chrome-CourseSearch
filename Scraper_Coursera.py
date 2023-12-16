import time
import requests
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.by import By

home_url = 'https://www.coursera.org/learn/cs-410/home/'
courseraURLfile = 'courseraURLs.txt'
dataFile = 'AlldataFile.txt'
allURLFile = 'AllURLFile.txt'


def get_html():
    '''
    This method gets HTML of the coursera page for URLs in a text file
    '''
    driver = webdriver.Chrome()
    urlList = []
    driver.get('https://www.coursera.org/degrees/master-of-computer-science-illinois?authMode=login')

    cURLfile = open(courseraURLfile, "r")
    df = open(dataFile, 'a')
    for url in cURLfile:

        driver.get(url)
        time.sleep(15)
        
        try:
            #Page with video, the code will read and store only transcript.
            res_html = driver.execute_script('return document.getElementsByClassName("rc-Transcript")[0].innerHTML')
            soup = BeautifulSoup(res_html, 'html.parser')

            #print(soup.get_text(separator=' '))
            df.write(soup.get_text(separator=' ').replace("\n", " ").replace("\r", " "))
            df.write('\n')
            urlList.append(url)
        except:
            try:
                #Page with instructions and no video, the code will read and store instructions.
                res_html = driver.execute_script('return document.getElementsByClassName("rc-ReadingItem")[0].innerHTML')
                soup = BeautifulSoup(res_html, 'html.parser')

                #print(soup.get_text(separator=' ').replace("\n", "").replace("\r", " "))
                df.write(soup.get_text(separator=' ').replace("\n", " ").replace("\r", " "))
                df.write('\n')
                urlList.append(url)
            except:
                try:
                    res_html = driver.execute_script('return document.getElementsByClassName("item-page-content")[0].innerHTML')
                    soup = BeautifulSoup(res_html, 'html.parser')

                    #print(soup.get_text(separator=' ').replace("\n", "").replace("\r", " "))
                    df.write(soup.get_text(separator=' ').replace("\n", " ").replace("\r", " "))
                    df.write('\n')
                    urlList.append(url)
                except:
                    print("Could not get HTML of this URL: ", url)
    
    driver.close()
    df.close()
    cURLfile.close()

    with open(allURLFile, 'a') as f:
        for u in urlList:
            f.write(u)


get_html()