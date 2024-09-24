from pyppeteer import launch
import logging

async def openURL(url:str) -> str:
    browser = await launch(options={'args': ['--no-sandbox']})
    logging.info(f"Opening URL: {url}")
    try:
        page = await browser.newPage()
        response = await page.goto(url)
        logging.info(f"Status code: {response.status}")
        if response.status == 200:
            htmlContent = await page.content()
            logging.info(f"HTML content received from {url}")
            with open('temp/temp_page.html', 'w', encoding='utf-8') as file:
                file.write(htmlContent)
            logging.info(f"HTML content saved to temp/temp_page.html")
            return htmlContent
        else:
            logging.error(f"Error: Received status code {response.status} from {url}")
        
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
    
    finally:
        await browser.close()
        logging.info("Browser closed.")