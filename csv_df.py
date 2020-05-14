import csv
import pandas as pd
from scraper import scraper

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


def create_csv(links):
    '''
        aggregator function of this module
    '''
    for link in links:
        print('create_csv_main')
        content_lst = scraper(link)
        df_to_csv(create_df(content_lst))
