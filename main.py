import asyncio
import toml
from functions import scraper, html_parser, slack, date_parser
import logging

config = toml.load('config.toml')

#------------#
#Logging setup
#------------#
log_level = getattr(logging, config['logging']['level'])
logging.basicConfig(level=log_level,
                     filename='log/log.log',
                     filemode='w', 
                     format='%(asctime)s - %(levelname)s - %(message)s')

#------------#
#スラック通知条件
#------------#

def get_latest_article(articles):
    for article in articles:
        article['parsed_time'] = date_parser.parse_datetime(article['time'])
    
    latest_article = max(articles, key=lambda x: x['parsed_time'])
    return latest_article['parsed_time']


#------------#
#main script
#------------#

def main():
    
    #html取得
    asyncio.get_event_loop().run_until_complete(scraper.openURL(config['scrape']['target_url']))


    #html解析
    articles = html_parser.phraser("temp/temp_page.html")

    #Slack通知
    slack_webhook_key = config['slack']['webhook_url']
    latest_date = get_latest_article(articles)
    for article in articles:
        if article['parsed_time'] == latest_date:
            slack.send_to_slack(slack_webhook_key, article)

if __name__ == '__main__':
    main()