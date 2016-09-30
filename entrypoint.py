# module main.
# This serves as the entry point to
# this project.

import sys
import csv
from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup

kBaseUrl = "http://bairwmp.org/projects/archived-projects-2013-plan-update/folder_tabular_view?b_start:int=0&-C"
kSecondPageUrl = "http://bairwmp.org/projects/archived-projects-2013-plan-update/folder_tabular_view?b_start:int=100&-C="
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
    listOfLinks = []
    table = bsObject.find('table', {'class': kTableClassName})
    linkWrappers = table.findAll(kHtmlLink)
    for eachWrapper in linkWrappers:
        listOfLinks.append(eachWrapper.get(kTableHref))
    return listOfLinks

'''
This routine takes in a list of 
valid URLs. It then proceeds to 
collect the needed data from the pages
pointed to by the locators.
'''
def scrapeEachProjectPage(urlList):
    for eachUrl in urlList:
        html = fetchHTML(eachErl)
        bSoupObject = generateBeautifulSoup(html)
        extractDataFromProjectPage(bSoupObject)
'''
Helper routine that does the actual scraping.
'''
def extractDataFromProjectPage(bsObject):
    #    |PART 1|
    title = extractHeading(bsObject)
    abstract = extractAbstract(bsObject)
    deadline = extractDeadline(bsObject)
    projectType = extractProjectType(bsObject)
    projectTypeDescr = extractProjectTypeDescr(bsObject)
    functionalAreas = extractFuncctionalAreas(bsObject)

    #    |PART 2|
    detailedDescr = getDetailedDescr(bsObject)
    parentProject = getParentProject(bsObject)
    relatedDocs = getRelatedDocs(bsObject)
    applicableWaterBodies = getApplicableH20Bodies(bsObject)
    projectNeed = getProjectNeed(bsObject)
    impactsIfNotImpl = getImpactsIfNotImpl(bsObject);
    benefits = getProjectBenefits(bsObject)

    #   |PART 2.2|
    reduceWaterSupply = reduceWaterSupply(bsOject)
    disadvatagedCommunity = disadvantagedCommunity(bsObject)

    '''
    # |Climate Change|
    adaptationToClimateChange = getAdaptationToClimateChange(bsObject)
    reducingGreenhouseGases = getMitigation(bsObject)
    impacts = getClimateChangeImpacts(bsObject)
    '''
    
    # |COSTS|
    costVector = getCostInfo(bsObject)
    stateWidePriorities = getStateWidePriorities(bsObject)
    califWPRMS = getCaliWPRMS(bsObject)
    eligibilityCriteria = getEligibilityCriteria(bsObject)
    prop84 = getMultipleBenefits(bsObject)
    prop1E = getStormWaterFloodManagement(bsObject)
    benefitsAndImpacts = getExpBenefitsAndImpacts(bsObject)

    # |PROJECT TEAM|
    contacts = getContacts(bsObject)
    investigators = getInvestigators(bsObject)
    sponsorAgency = getSponsorAgency(bsObject)
    participants = getParticipatingOrganizations(bsObject)

    # |Files|
    projectBenefitsFile = getProjectBenefitsFile(bsObject)
    
def main():
   firstPageHtml = fetchHTML(kBaseUrl)
   secondPageHtml = fetchHTML(kSecondPageUrl)
   firstPageBsObject = generateBeautifulSoupObject(firstPageHtml)
   secondPageBsObject = generateBeautifulSoupObject(secondPageHtml)
   urlList = getProjectUrls(firstPageBsObject) + getProjectUrls(secondPageBsObject)
   scrapeEachProjectPage(urlList)

if __name__ == "__main__":
    main()
