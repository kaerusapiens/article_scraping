
import requests
from typing import List, Dict
import logging

def send_to_slack(articles: List[Article]) -> None:
    message = "📰 PPC News from Search Engine Land:\n"
    
    for article in articles:
        message += f"*Title:* {article['title']}\n"
        message += f"*Link:* {article['link']}\n"
        message += f"*Content:* {article['content']}\n\n"
    
    response = requests.post(SLACK_WEBHOOK_URL, json={'text': message})
    
    if response.status_code != 200:
        logging.error(f"Failed to send to Slack: {response.text}")
    else:
        logging.info("Message sent to Slack successfully.")

# Main function to run the scraper and send data to Slack
async def main() -> None:
    try:
        articles = await scrape_ppc_news()
        send_to_slack(articles)
    except Exception as e:
        logging.info(e)
