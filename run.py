import requests
from bs4 import BeautifulSoup

def generateCookie(header):
    cookie = {}
    
    keySections = header['Set-Cookie'].split(", ")
    
    for x in keySections:
        cookie[x.split('=')[0]] = x.split('=')[1]
        
    return cookie

TERM = ""
COURSE1 = ""
COURSE2 = ""
COURSE3 = ""
COURSE4 = ""
COURSE5 = ""
COURSECODE1 = ""
COURSECODE2 = ""
COURSECODE3 = ""
COURSECODE4 = ""
COURSECODE5 = ""
COURSESECTION1 = ""
COURSESECTION2 = ""
COURSESECTION3 = ""
COURSESECTION4 = ""
COURSESECTION5 = ""


getURL = 'https://webadvisor.uoguelph.ca/WebAdvisor/WebAdvisor?CONSTITUENCY=WBST&type=P&pid=ST-WESTS12A&TOKENIDX=1'
r = requests.get(getURL)
cookie = generateCookie(r.headers)
getURL = 'https://webadvisor.uoguelph.ca/WebAdvisor/WebAdvisor?CONSTITUENCY=WBST&type=P&pid=ST-WESTS12A&TOKENIDX=1'
r = requests.get(getURL, cookies=cookie)
cookie = generateCookie(r.headers)

postURL = 'https://webadvisor.uoguelph.ca/WebAdvisor/WebAdvisor?TOKENIDX=1&SS=1&APP=ST&CONSTITUENCY=WBST'
fields = {"VAR1":TERM, "VAR10":"", "VAR11":"","VAR12":"", "VAR13":"", "VAR14":"", "VAR15":"", "VAR16":"", "DATE.VAR1":"", "DATE.VAR2":"", "LIST.VAR1_CONTROLLER":"LIST.VAR1", "LIST.VAR1_MEMBERS":"LIST.VAR1*LIST.VAR2*LIST.VAR3*LIST.VAR4", "LIST.VAR1_MAX":"5", "LIST.VAR2_MAX":"5", "LIST.VAR3_MAX":"5", "LIST.VAR4_MAX":"5", "LIST.VAR1_1":COURSE1, "LIST.VAR2_1":"", "LIST.VAR3_1":COURSECODE1, "LIST.VAR4_1":COURSESECTION1, "LIST.VAR1_2":COURSE2, "LIST.VAR2_2":"", "LIST.VAR3_2":COURSECODE2, "LIST.VAR4_2":COURSESECTION2, "LIST.VAR1_3":COURSE3, "LIST.VAR2_3":"", "LIST.VAR3_3":COURSECODE3, "LIST.VAR4_3":COURSESECTION3, "LIST.VAR1_4":COURSE4, "LIST.VAR2_4":"", "LIST.VAR3_4":COURSECODE4, "LIST.VAR4_4":COURSESECTION4, "LIST.VAR1_5":COURSE5, "LIST.VAR2_5":"", "LIST.VAR3_5":COURSECODE5, "LIST.VAR4_5":COURSESECTION5, "VAR7":"", "VAR8":"", "VAR3":"", "VAR6":"", "VAR21":"", "VAR9":"", "SUBMIT_OPTIONS":""}


r = requests.post(postURL, data=fields, cookies=cookie)

print(r.text)



