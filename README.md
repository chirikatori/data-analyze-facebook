
# Data-analyze-facebook  
This is a student project which use [facebook-scaper](https://github.com/kevinzg/facebook-scraper), [pandas](https://pandas.pydata.org/docs/index.html), [seaborn](https://seaborn.pydata.org/index.html), [matplotlib](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html), [numpy](https://numpy.org/doc/stable/).  

# Table of contents  
1. [Features](#feature)  
2. [Lesson](#lesson)    
3. [Run locally](#run)  
4. [Environment Variables](#var)

<a name="feature"></a>
## Features  

- Crawl data from a facebook page
- Preprocess the data
- Visualize the data  
 
<a name="lesson"></a>
## Lessons Learned  

- How to build a project
- How to Preprocess the data and Visualize it
- What exactly Data Analysis do 
- How to write a Readme

<a name="run"></a>
## Run Locally  

Clone the project  

~~~bash  
  git clone https://github.com/chirikatori/data-analyze-facebook.git
~~~

Go to the project directory  

~~~bash  
  cd data-analyze-facebook
~~~

Install dependencies  

~~~bash  
pip install -r requirement.txt
~~~

Start to scrape data  

~~~bash  
python crawl.py
~~~
Preprocess data: [Preprocess.ipynb](Preprocess.ipynb)

Visualize data: [Analyzes.ipynb](Analyzes.ipynb)

<a name="var"></a>
## Environment Variables  

To run this project, you will need to add the following environment variables to your .env file  
`FACEBOOK_USERNAME, 
FACEBOOK_PASSWORD` if you use credentials

`FACEBOOK_COOKIES_FILE_PATH` if you use cookies

`FACEBOOK_FANPAGE_ID`: id of the page you scrape

`RESUME_URL_SAVE_FILE`

`FOLDER_PATH_RAW`

`FOLDER_PATH_CLEAN`  


## Acknowledgements  
- [FACEBOOK_SCRAPER](https://github.com/kevinzg/facebook-scraper)
- [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

## Feedback  

If you have any feedback, please reach out to us at https://github.com/chirikatori/data-analyze-facebook/issues

