
from pyppeteer import launch

async def openURL(url:str) -> str:
    browser = await launch(executablePath='/usr/bin/google-chrome',
                           headless=False,
                           args=['--no-sandbox', '--headless', '--disable-gpu'])
    try:
        page = await browser.newPage()
        response = await page.goto(url)
        
        if response.status == 200:
            htmlContent = await page.content()
            return htmlContent
        else:
            print(f"Error: Received status code {response.status} from {url}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    
    finally:
        await browser.close()


