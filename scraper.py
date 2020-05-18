from newspaper import Article
from newspaper import ArticleException
import newspaper



def scrape_news_links(url):
    '''
        Scrapes links : not only google but any online vendor.
        set url while calling the function
    '''
    print('scraping_links')
    paper = newspaper.build(url, memoize_articles=False)
    links = []
    for article in paper.articles:
        links.append(article.url)
    
    # print(links)
    return links

def clean_text(text):
    '''
        To clean text
    '''
    print('cleaning_text')
    # text = text.strip()
    # text = text.lower()
    # for punct in string.punctuation:
    #     text = text.replace(punct, '')
    string = text.split('\n')
    text = " ".join(string)
    text.replace('\\', '')
    return text

def get_content(links):
    '''
        get headlines and news content
    '''
    print('getting content')
    content = []
    try:
        for url in links:
            article = Article(url, language='en')
            article.download()
            article.parse()
            title = clean_text(article.title)
            news = clean_text(article.text)
            if title != None:
                if news != None: 
                    if news != ' ': 
                        if news != '':      # for sites which news content cannot be scraped
                            content.append([title, news])
    except ArticleException as ae:
        if 'Article \'download()\' failed' in ae:
            print('Could not get article')
    finally:    
        return content
    

def scraper(link='https://timesofindia.indiatimes.com/'):
    '''
        aggregator function
    '''
    print('scraper_main')
    return get_content(scrape_news_links(link))

# if __name__ == "__main__":
    # links = scrape_google_links()
    # print(get_content(links[:15]))