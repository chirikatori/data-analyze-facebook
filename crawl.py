from lib.facebook_scraper import *
from dotenv import load_dotenv
import pandas as pd
import os
import time
from random import randint

load_dotenv()

PAGE_NUMBER=100

post_list = []
start_url = None

#save url of the last post crawled if error 
def handle_pagination_url(url):
    global resume_url
    resume_url = url
    if post_list:
        print(f"{len(post_list)}: {post_list[-1]['time']}: {resume_url}")

#save url to a file 
def save_url(resume_url):
  f = open(os.getenv("RESUME_URL_SAVE_FILE"), "w")
  f.write(resume_url)
  f.close()
  
#read the url crawled since last ban
def read_resume_url():
  try:
    f = open(os.getenv("RESUME_URL_SAVE_FILE"), "r")
    resume_url = f.read()
    f.close()
    return resume_url
  except:
    return None
  

resume_url = read_resume_url()

#crawl function
try:
    for post in get_posts(os.getenv("FACEBOOK_FANPAGE_ID"),
                      options={"reactions": True, 
                               "allow_extra_requests": True,
                               "comments": True,
                               "reactors": "generator",
                               "shares": True,
                               "sharers": "generator",
                               "comments": "generator"
                               },
                      # unbind below if you want to use credential
                      #credential=[os.getenv("FACEBOOK_USERNAME"), os.getenv("FACEBOOK_PASSWORD")]
                      #then bind below
                      cookies=os.getenv("FACEBOOK_COOKIES_FILE_PATH"),
                      start_url=resume_url,
                      request_url_callback=handle_pagination_url,
                      timeout=300,
                      pages=PAGE_NUMBER):
        print(post)
        post_list.append(post)
    
        time.sleep(randint(5, 10))
        
except exceptions.TemporarilyBanned:
    print("Temporarily Banned")

except Exception as e:
  print(e)

save_url(resume_url)

post_df_full = pd.DataFrame(columns=post_list[0].keys(), index=range(len(post_list)), data=post_list)

post_df_full.to_csv(f"{os.getenv('FOLDER_PATH_RAW')}{os.getenv('FACEBOOK_FANPAGE_ID')}1.csv", mode="a", index=False)
