
import requests
import logging

def send_to_slack(webhook_key:str,article: dict):
    if article['category_name'] == "SEO":
        message = f"📰`{article['category_name']}` "
    elif article['category_name'] == "PPC":
        message = f":moneybag:`{article['category_name']}` "
    else:
        message = f":paperclip:`{article['category_name']}` "
    message += f"*<{article['headline_link']}|{article['headline']}>*\n"
    message += f"```{article['description']}```\n"
    message += "\n"
    
    response = requests.post(webhook_key, json={'text': message})
    logging.info(f"Status code: {response.status_code}")
    if response.status_code != 200:
        logging.error(f"Failed to send to Slack: {response.text}")
    else:
        logging.info("Message sent to Slack successfully.")

