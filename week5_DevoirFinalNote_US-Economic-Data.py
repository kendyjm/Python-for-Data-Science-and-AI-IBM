'''
Instructions
Gross domestic product (GDP) is a measure of the market value of all the final goods and services produced in a period. GDP is an indicator of how well the economy is doing. A drop in GDP indicates the economy is producing less; similarly an increase in GDP suggests the economy is performing better. In this assignment you will examine how changes in GDP impact the unemployment rate. You will take screen shots of every step. You will share the notebook via a URL.


Review criteria
In this assignment, you will be marked on your ability to apply Python programming concepts that would commonly be used to load, analyze and share your data.
'''

import pandas as pd
from bokeh.plotting import figure, output_file, show, output_notebook


# output_notebook()

def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)


# The dictionary links contain the CSV files with all the data.
# The value for the key GDP is the file that contains the GDP data.
# The value for the key unemployment contains the unemployment data.
links = {
    'GDP': 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv', \
    'unemployment': 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}


# Question 1: Create a dataframe that contains the GDP data and display the first five rows of the dataframe.
## Use the dictionary links and the function pd.read_csv to create a Pandas dataframes that contains the GDP data.
## Hint: links["GDP"] contains the path or name of the file.
def create_dataframe(link_key):
    '''
    Create a Pandas data frame from a key found in 'links'
    TODO handle failing cases (key not found in links, csv_read failed for any reasons etc

    :param link_key: key to find from 'links' and retrieve corresponding data path
    :return: Pandas data frame
    '''
    data_path = get_url(link_key)
    data_frame = pd.read_csv(data_path)
    data_rows = data_frame.shape[0];
    print('Read {} rows from {} data file'.format(data_rows, link_key))
    return data_frame


def get_url(link_key):
    '''
    Get data url from 'links'
    :param link_key: key to find from 'links' and retrieve corresponding data path
    :return: link value
    '''
    file_path = links[link_key]
    print("File path for {} data : {}".format(link_key, file_path))
    return file_path


gdp_link_key = 'GDP'
gdp_data_frame = create_dataframe(gdp_link_key)
## Use the method head() to display the first five rows of the GDP data, then take a screen-shot.
print(gdp_data_frame.head())
