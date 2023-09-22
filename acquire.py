import requests
import pandas as pd
import numpy as np
import os


def grab_swapi_api_df(topic):
    '''specific for swapi api, input people, planets, or starships
    
    return: df'''
    filename = (f'{topic}.csv')
    if os.path.isfile(filename):
        df = pd.read_csv(filename, index_col=[0])

    else:
        # empty list
        total_results = []
        # url
        url = 'https://swapi.dev/api/' + str(topic)
        # grab the search results
        response = requests.get(url)
        data = response.json()
        # Store the first page
        total_results = total_results + data['results']

        while data['next'] is not None:
            response = requests.get(data['next'])
            data = response.json()
            total_results = total_results + data['results']

            df = pd.DataFrame(total_results)
        # convert into csv and save   
        df.to_csv(f'{topic}.csv')

    return df



def grab_power_api_df(url, name):
    '''simple pull from csv format to dataframe'''
    filename = (f'{name}.csv')
    if os.path.isfile(filename):
        df = pd.read_csv(filename, index_col=[0])
    else:
        url = url
        df = pd.read_csv(url)
        df.to_csv(f'{name}.csv')
    return df