from typing import List, Dict
from pyppeteer import launch
import requests
import toml
import logging

config = toml.load('config.toml')
print("config loaded")

SLACK_WEBHOOK_URL = config['slack']['webhook_url']

Article = Dict[str, str]

# Function to scrape data from the website
async def scrape_ppc_news() -> List[Article]:
    browser = await launch(headless=True)
    page = await browser.newPage()
    
    # Navigate to the page
    await page.goto('https://searchengineland.com/library/ppc')
    
    # Wait for the content to load (adjust the selector if needed)
    await page.waitForSelector('article h3')
    
    # Extract the article titles, links, and content
    articles = await page.evaluate('''() => {
        const data = [];
        document.querySelectorAll('article').forEach(article => {
            const title = article.querySelector('h3').innerText;
            const link = article.querySelector('a').href;
            const content = article.querySelector('p').innerText;
            data.push({title, link, content});
        });
        return data;
    }''')
    
    await browser.close()
    return articles

# Function to send results to Slack
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
