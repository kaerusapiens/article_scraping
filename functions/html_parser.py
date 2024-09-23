from bs4 import BeautifulSoup

def phraser(htmlContent:str) -> str :
    soup = BeautifulSoup(htmlContent, 'html.parser')
    articles = soup.select('#latest > article > div > div.col-12.col-lg-7.col-xl-8 > div')
    return articles
