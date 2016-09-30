# module main.
# This serves as the entry point to
# this project.

import sys
import csv
from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup

kBaseUrl = "http://bairwmp.org/projects/archived-projects-2013-plan-update/folder_tabular_view?b_start:int=0&-C"
kTableEntryClass = "contenttype-irwmpproject"
kTableClassName = "listing"
kTableHref = "href"
kHtmlLink = "a"

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
        bsObject = BeautifulSoup(html, 'html.parser') #from the bs4 3rd part library
    except AttributeError as e:
        return None
    return bsObject

'''
This routine takes the beautiful soup object generated above
and gathers from it links to the listed projects. The links are packaged
into a list that is returned to the caller.
'''

#This is how a single url element looks like in html.
'''
<tr class="even"> |class= "odd" if odd|
  <td>
    <span
      class="contenttype-irwmpproject">
        <img width="16"
          height="16" src="http://bairwmp.org/proj.gif" alt="Project" />
            <a href="http://bairwmp.org/projects/archived-projects-2013-plan-update/mount-diablo-state-park-comprehensive-stock-pond"
            class="state-published" title="">Mount Diablo State Park:  Comprehensive Stock Pond Evaluation and Sedimentation Remediation</a>
    </span>
  </td>
  <td>Project</td>
</tr>
'''
def getProjectUrls(bsObject):
    table = bsObject.find('table', {'class': kTableClassName})
    links = table.findAll(kHtmlLink)
    for linkWrapper in links:
        print linkWrapper.get(kTableHref)
        
'''
<td>
<span class="contenttype-irwmpproject">
<img alt="Project" height="16" src="http://bairwmp.org/proj.gif" width="16"/>
<a class="state-published" href="http://bairwmp.org/projects/archived-projects-2013-plan-update/mount-diablo-state-park-comprehensive-stock-pond" title="">text</a>
</span>
</td>

def extractURL(string):
    miniSoup = generateBeautifulSoupObject(string)
    return miniSoup.findAll(class_ = kTableDataClass)

'''

def main():
    html = fetchHTML(kBaseUrl)
    bsObject = generateBeautifulSoupObject(html)
    getProjectUrls(bsObject)

if __name__ == "__main__":
    main()
