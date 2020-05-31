import requests
from bs4 import BeautifulSoup
import html
import time
import os

def generateCookie(header):
    genCookie = {}
        
    for x in header['Set-Cookie'].split(", "):
        genCookie[x.split('=')[0]] = x.split('=')[1]
        
    return genCookie

def pollWebadvisor(getURL, postURL, fields, interval):
    while 1:
        print('\nChecking Webadvisor...\n')
        r = requests.get(getURL)
        cookie = generateCookie(r.headers)
        r = requests.get(getURL, cookies=cookie)
        cookie = generateCookie(r.headers)

        r = requests.post(postURL, data=fields, cookies=cookie)
        obj = BeautifulSoup(r.text, features="lxml")
        
        table = obj.find('table', attrs={'class':'mainTable'})
        rows = table.findAll('tr')[5:]

        courseAvailabilityMap = {}

        for row in rows:
            cols = row.findAll('td')

            if len(cols) < 8:
                print(r.text)
                print('Invalid request or webadvisor is down... Dumped raw response')
                exit()

            if cols[3].find('a') is None:
                print(r.text)
                print('Invalid request or webadvisor is down... Dumped raw response')
                exit()

            title = html.unescape(cols[3].find('a').contents[0])
            spotsOpen = int(cols[7].find('p').contents[0].split('/')[0])

            if title in courseAvailabilityMap:
                courseAvailabilityMap[title] = courseAvailabilityMap[title] + spotsOpen
            else:
                courseAvailabilityMap[title] = spotsOpen

        courses = courseAvailabilityMap.keys()
        for course in courses:
            print('The course ' + course + ' has ' + str(courseAvailabilityMap[course]) + ' spots open')
            if courseAvailabilityMap[course] != 0:
                os.system("afplay " + "notify.mp3")
            time.sleep(1)
        print('\nSleeping...')
        time.sleep(interval)
    
term = ""
course1 = ""
course2 = ""
course3 = ""
course4 = ""
course5 = ""
courseCode1 = ""
courseCode2 = ""
courseCode3 = ""
courseCode4 = ""
courseCode5 = ""
courseSection1 = ""
courseSection2 = ""
courseSection3 = ""
courseSection4 = ""
courseSection5 = ""
courseCount = 0
getURL = 'https://webadvisor.uoguelph.ca/WebAdvisor/WebAdvisor?CONSTITUENCY=WBST&type=P&pid=ST-WESTS12A&TOKENIDX=1'
postURL = 'https://webadvisor.uoguelph.ca/WebAdvisor/WebAdvisor?TOKENIDX=1&SS=1&APP=ST&CONSTITUENCY=WBST'

interval = int(input('Please enter a time inverval, in seconds. Webadvisor will be checked based on this interval: '))
print('\n')
term = input('Please enter the term (Summer 2020 -> S20): ').upper()
print('\n')
courses = input('Please enter a comma seperated list of course subjects (For example: CIS,CHEM,BIOC): ').upper().split(',')
print('\n')
courseCount = len(courses)

if courseCount < 1:
    print('Must enter atleast 1 course subject')
    exit()
if courseCount > 0:
    course1 = courses[0]
if courseCount > 1:
    course2 = courses[1]
if courseCount > 2:
    course3 = courses[2]
if courseCount > 3:
    course4 = courses[3]
if courseCount > 4:
    course5 = courses[4]
if courseCount > 5:
    print('Max of 5 course subjects may be entered')
    exit()

courseCodes = input('Please enter a comma seperated list of course codes (For example: 3760,2500). Enter these in an order to match with the previously entered subjects: ').upper().split(',')
print('\n')

if len(courseCodes) < 1:
    print('Must enter atleast 1 course code')
    exit()
if len(courseCodes) != courseCount:
    print('Must enter the same number of course subjects and codes')
    exit()

if courseCount > 0:
    courseCode1 = courseCodes[0]
if courseCount > 1:
    courseCode2 = courseCodes[1]
if courseCount > 2:
    courseCode3 = courseCodes[2]
if courseCount > 3:
    courseCode4 = courseCodes[3]
if courseCount > 4:
    courseCode5 = courseCodes[4]
if courseCount > 5:
    print('Max of 5 course codes may be entered')
    exit()

courseSections = input('Please optionally enter a comma seperated list of course sections (For example: 101,102). Enter these in an order to match with the previously entered subjects/codes, if you are skipping a section just enter a empty string (For example: 101,,102): ').upper().split(',')
print('\n')

courseSectionsCount = len(courseSections)
if courseSectionsCount > 0:
    courseSection1 = courseSections[0]
if courseSectionsCount > 1:
    courseSection2 = courseSections[1]
if courseSectionsCount > 2:
    courseSection3 = courseSections[2]
if courseSectionsCount > 3:
    courseSection4 = courseSections[3]
if courseSectionsCount > 4:
    courseSection5 = courseSections[4]
if courseSectionsCount > 5:
    print('Max of 5 course sections may be entered')
    exit()

fields = {"VAR1":term, "VAR10":"", "VAR11":"","VAR12":"", "VAR13":"", "VAR14":"", "VAR15":"", "VAR16":"", "DATE.VAR1":"", "DATE.VAR2":"", "LIST.VAR1_CONTROLLER":"LIST.VAR1", "LIST.VAR1_MEMBERS":"LIST.VAR1*LIST.VAR2*LIST.VAR3*LIST.VAR4", "LIST.VAR1_MAX":"5", "LIST.VAR2_MAX":"5", "LIST.VAR3_MAX":"5", "LIST.VAR4_MAX":"5", "LIST.VAR1_1":course1, "LIST.VAR2_1":"", "LIST.VAR3_1":courseCode1, "LIST.VAR4_1":courseSection1, "LIST.VAR1_2":course2, "LIST.VAR2_2":"", "LIST.VAR3_2":courseCode2, "LIST.VAR4_2":courseSection2, "LIST.VAR1_3":course3, "LIST.VAR2_3":"", "LIST.VAR3_3":courseCode3, "LIST.VAR4_3":courseSection3, "LIST.VAR1_4":course4, "LIST.VAR2_4":"", "LIST.VAR3_4":courseCode4, "LIST.VAR4_4":courseSection4, "LIST.VAR1_5":course5, "LIST.VAR2_5":"", "LIST.VAR3_5":courseCode5, "LIST.VAR4_5":courseSection5, "VAR7":"", "VAR8":"", "VAR3":"", "VAR6":"", "VAR21":"", "VAR9":"", "SUBMIT_OPTIONS":""}

pollWebadvisor(getURL, postURL, fields, interval)