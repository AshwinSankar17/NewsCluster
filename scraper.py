from newspaper import Article, ArticleException
import newspaper

def scrape_google_links(url='http://cnn.com'):
    '''
        Scrapes links : not only google but any online vendor.
        set url while calling the function
    '''
    print('scraping_links')
    paper = newspaper.build(url)
    links = []
    for article in paper.articles:
        links.append(article.url)
    # resp = requests.get(url)
    # soup = BeautifulSoup(resp.text, 'lxml')
    # g_links = soup.find_all('a')
    # links = []
    # for link in g_links:
    #     l = link.get('href')
    #     if l == None:
    #         continue
    #     elif l.startswith('./articles'):
    #         uri = url + l.split('.')[1]
    #         if uri not in links:
    #             links.append(uri)
    return links

def clean_text(text):
    '''
        To clean text
    '''
    print('cleaning_text')
    string = text.split('\n')
    text = " ".join(string)
    text.replace('\\', '')
    return text

def get_content(links):
    '''
        get headlines and news content
    '''
    print('getting content')
    try:
        content = []
        for url in links:
            article = Article(url)
            article.parse()
            article.download()
            title = article.title
            news = clean_text(article.text)
            if title != None or news != None or news != ' ' or news != '':      # for sites which news content cannot be scraped
                content.append([title, news])
    except ArticleException:
        pass
    finally:    
        return content
    

def scraper(link):
    '''
        aggregator function
    '''
    print('scraper_main')
    return get_content(scrape_google_links(link)[:200])

# if __name__ == "__main__":
    # links = scrape_google_links()
    # print(get_content(links[:15]))