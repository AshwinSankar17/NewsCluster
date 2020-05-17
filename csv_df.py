import csv
import pandas as pd
from scraper import scraper


LINKS = ['https://timesofindia.indiatimes.com/', 'https://www.thehindu.com/', 'https://www.bbc.com/news', 'https://www.theguardian.co.uk/']

def create_df(content_list):
    '''
        To write the data to csv file
        takes a list of list where the inner list contains ['headline', 'news']
    '''
    title = []
    news = []
    print('creating_dataFrame')

    for content in content_list:
        title.append(content[0])
        news.append(content[1])

    data = {'Title' : title, 'News' : news}
    df = pd.DataFrame(data, columns=['Title', 'News'])
    return df


def df_to_csv(df, filename='NewsCluster.csv'):
    '''
        writes dataframe to csv
    '''
    print('writing_to_csv')
    df.to_csv('./data/' + filename)


def create_csv():
    '''
        aggregator function of this module
    '''
    print('create_csv_main')
    content_list = []
    for link in LINKS:
        content_list.append(scraper(link))

    content_lst = []
    for content in content_list:
        for cont in content:
            content_lst.append(cont)
    # content_lst = scraper()
    # print(content_lst)
    try:
        num = int(input('Enter the number of articles to be stored : '))
        if num < 15:
            raise ValueError('Provide a larger number for dataset')
        df_to_csv(create_df(content_lst[:num]))
    except ValueError as ve:
        df_to_csv(create_df(content_lst))
