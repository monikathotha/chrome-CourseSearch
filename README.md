# course-extension
Chrome Extension – Search Campuswire and Coursera

The project uses crawlers to scrape Coursera and Campuswire website for CS410. This enables an easier search and lets user view results from both websites on one page.
A chrome extension UI is used to enter search query and it displays links to both sites.

BeautifulSoup algo is used to parse the HTML of the webpages.
BM25OKapi is used to rank the search results.

The code can be easily enhanced and modified to show a combined view of search results from both sites.
This can also be extended for other courses by changing the URLs.
Note: The data file has used campuswire crawler to crawl only ~200 posts as it takes lot of time and resources to crawl 1000+ posts.

Steps to install the code:

pip install -U flask-cors
pip install Flask

If you want to scrape the data again. Follow steps 1 to 5, else skip to step 6
Note: The campuswire data in this file has only ~200 documents

****************************
Preparing Data
****************************
Step 1:
Clean below data files:
CourseraURLs.txt
AlldataFileCoursera.txt
AllURLFileCoursera.txt
AlldataFileCampuswire.txt
AllURLFileCampuswire.txt
CleanDataFileCoursera
CleanDataFileCampuswire

Step 2:
Run GetCourseraURL.py
Use breakpoint and manually enter userName and password for the website.

Step 3:
Run Scraper_Campuswire.py
Use breakpoint and manually enter userName and password for the website.

Step 4:
Run Scraper_Coursera.py
Use breakpoint and manually enter userName and password for the website.

Step 5:
Run CleanupData.py

****************************
Data is ready
****************************

Step 6:
Run below commands on the terminal to start the server:
export FLASK_APP=app.py
flask run

Step 7:
Load Chrome Extension

Step 8:
Login to coursera and campuswire on the browser instance and launch the chrome extension to start running searches!!

Youtube demo link: https://youtu.be/wpiCSEEQ25g

		
