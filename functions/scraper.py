
from pyppeteer import launch
from pyppeteer.launcher import Launcher
test = ' '.join(Launcher().cmd)
print(test)
async def openURL(url:str) -> str:
    browser = await launch(executablePath='/usr/bin/google-chrome',headless=False,args=['--no-sandbox', '--headless', '--disable-gpu'])
    page = await browser.newPage()
    await page.goto(url)
    htmlContent = await page.content()
    await browser.close()
    return htmlContent

