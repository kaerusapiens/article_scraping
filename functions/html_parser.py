from bs4 import BeautifulSoup

def phraser(filePath:str) -> dict:
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            htmlContent = file.read()
            soup = BeautifulSoup(htmlContent, 'html.parser')         
            
            global_content_stream = soup.find('section', class_='global-content-stream')
            if global_content_stream:
                article_content=[]
                articles = global_content_stream.find_all('div', class_='article-text')
                for article in articles:
                    #category_name
                    category_name = article.find('p', class_='category-name').get_text(strip=True)

                    #headline
                    tag_headline = article.find('h2', class_='headline').find('a')
                    tag_headline_link = tag_headline['href']
                    tag_headline_text = tag_headline.get_text(strip=True)

                    #description
                    tag_dek = article.find('p', class_='dek').get_text(strip=True)

                    #author and time
                    tag_byline = article.find('span', class_='byline')
                    author_and_time = tag_byline.get_text(strip=True).split('|')
                    author = author_and_time[0].strip()
                    time = author_and_time[1].strip()
                    article_content.append({
                        'category_name': category_name,
                        'headline': tag_headline_text,
                        'headline_link': tag_headline_link,
                        'description': tag_dek,
                        'author': author,
                        'time': time
                    })
                return article_content
            else: 
                print("global-content-stream not found")

    except Exception as e:
        print(f"An error occurred: {e}")