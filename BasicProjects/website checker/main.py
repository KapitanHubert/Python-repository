from websites import *
import os, sys
import threading, time
import requests

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

websites = Websites("websites.txt")
#print(websites.getNextWebsiteToCheck())
websites.putWebsiteData({"index" : 0, "website": "duckduckgo.pl","statusCode": 200})
websites.saveReport()
