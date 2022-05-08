from facebook_scraper import *
from db import cursor,db
import time
import logging

logger = logging.getLogger('facebook_scraper')
logging.basicConfig(level=logging.INFO)

logger.info('Scraping START')

#db
def addFBPostToDB(post_id, post_text, post_img, post_time):
            sql = ("INSERT INTO post_from_fb_poedb(post_id, post_text, post_img, post_time) VALUE(%s, %s, %s, %s)")
            cursor.execute(sql, (post_id, post_text, post_img, post_time))
            db.commit()
            logger.info('\n')
            logger.info('data insert!')
            logger.info('\n')
            logger.info('===================================================')

#facebook scrape
def scrape():
      for post in  get_posts ('poedbtw', pages=4, options={"posts_per_page": 1}): #need add cookies after options
        post_id = post["post_id"]
        post_text = post["text"]
        post_img = post["image"]
        post_time = post["time"]
        logger.info(post_id)
        logger.info(post_text)
        logger.info(post_img)
        logger.info(post_time)
        logger.info("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")  
        
        addFBPostToDB(post_id, post_text, post_img, post_time)  

while True:
  try:

    scrape()

  except Exception as exc:
    logger.error('[!!!] {err}'.format(err=exc))
    time.sleep(10)

#3600  ->1hour
