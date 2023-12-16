import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#base_url = 'https://www.coursera.org/learn/cs-410/home/week/'
home_url = 'https://www.coursera.org/learn/cs-410/home/'
courseraURLfile = 'courseraURLs.txt'

def get_course_coursera_urls():
    '''
    This method stores all URLs of the course in a courseURLs.txt file
    '''
    
    driver = webdriver.Chrome()
    driver.get(home_url)
    time.sleep(3)

    total_weeks = len(driver.find_elements(By.CLASS_NAME, "css-q89akd")) + 1

    cs410urls = []
    
    #nbr of weeks 
    for wk in range(total_weeks):
        url = home_url + "week/" + str(wk+1)

        driver.get(url)
        time.sleep(10)
        try:
            h2_element = driver.find_elements(By.CLASS_NAME, "css-e6lsmr")
            # Get all the elements available with tag name 'p'
            for h2_e in h2_element:
                #print("H2E TEXT:  ", h2_e.text)
                if (h2_e.text.lower().find("quiz") == -1):
                    elements = h2_e.find_elements(By.TAG_NAME, 'li')
                    for e in elements:
                        #print("TEXT:  ", e.text)
                        href_e = e.find_elements(By.TAG_NAME, 'a')
                        for hr_e in href_e:
                            #print("HREF:  ", hr_e.get_attribute('href'))
                            cs410urls.append(hr_e.get_attribute('href'))
        except:
            print("Program ran into some issue with this URL: ", url)
    driver.close()

    with open(courseraURLfile, 'w') as f:
        for u in cs410urls:
            f.write(u)
            f.write('\n')


get_course_coursera_urls()