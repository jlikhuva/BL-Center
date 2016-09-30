# module main.
# This serves as the entry point to
# this project.

import sys
import csv
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

kBaseUrl = "http://bairwmp.org/projects/archived-projects-2013-plan-update/folder_tabular_view?b_start:int=0&-C"

'''
Fetches the html text stored at url. url
is expected to be a valid location. If not
this procedure ruturns None. The caller must test
to ensure that the returned object is not None.
'''
def fetchHTML(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    return html

'''
provided html is valid html text, this procedure 
converts it to a beautiful soup object that is easy
to parse. None is returned if an excetion is raised. As
such, the caller needs to check that the returned object
is not None.
'''
def generateBeautifulSoupObject(html):
    try:
        bsObject = BeautifulSoup(html) #from the bs4 3rd part library
    except AttributeError as e:
        return None
    return bsObject

