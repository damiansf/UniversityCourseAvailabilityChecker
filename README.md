# UniversityCourseAvailabilityChecker

Simple messy python script that polls Webadvisor (University of Guelph's course selection system) for you to get course availabilities. A notification sound is played when a course has open spots. This script helps automate the process of waiting for spots to open up in courses.

Simply run the script with python3 and it will prompt you for any required information. The script is by no means polished and is pretty rough around the edges so it may crash if you give it invalid data and Webadvisor responds with an error.

This script is designed for Mac. If you are on any other platform you may have issues. Comment out lines 5, 47 and, 58 to attempt to avoid
any issues. Also make sure you have bs4, requests, html, time and (on mac) os libraries installed.

The program will continously run until you kill it.

* NOTE, If you choose to attempt to use this script for malicious purposes to spam the University with requests I do not take any responsibility for your actions nor do I condone them.