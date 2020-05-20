from newspaper import Article
from newspaper import ArticleException
import newspaper
from progress.bar import IncrementalBar
import time
import string


def scrape_news_links(url):
    '''
        Scrapes links : not only google but any online vendor.
        set url while calling the function
    '''
    paper = newspaper.build(url, memoize_articles=False)
    links = []
    bar = IncrementalBar('Scraping Links', max=len(paper.articles), suffix='%(percent)d%%')
    for article in paper.articles:
        links.append(article.url)
        bar.next()
        time.sleep(0.1)
    bar.finish()
    
    # print(links)
    return links

def clean_text(text):
    '''
        To clean text
    '''
    # print('cleaning_text')
    # text = text.strip()
    # text = text.lower()
    # for punct in string.punctuation:
    #     text = text.replace(punct, '')
    text = text.lower()
    strin = text.split('\n')
    text = " ".join(strin)
    # text.replace('\\', '')
    exclude = set(string.punctuation)
    text = ''.join(ch for ch in text if ch not in exclude)
    return text

def get_content(links):
    '''
        get headlines and news content
    '''
    # print('getting content')
    content = []
    # next_bar = IncrementalBar('Getting Content', max=)
    bar = IncrementalBar('Getting content & Cleaning text', max=len(links), suffix='%(percent)d%%' )
    for url in links:
        try:
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
            bar.next()
    
        except ArticleException as ae:
            # if 'Article \'download()\' failed' in ae:
            continue
    
    bar.finish()
    return content
    

def scraper(link='https://timesofindia.indiatimes.com/'):
    '''
        aggregator function
    '''
    # print('scraper_main')5
    return get_content(scrape_news_links(link))

# if __name__ == "__main__":
    # links = scrape_google_links()
    # print(get_content(links[:15]))