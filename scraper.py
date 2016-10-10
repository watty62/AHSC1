#!/usr/bin/python

# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page

def scrape_URL (url_no):
    scrape_add = "http://www.grampiancaredata.gov.uk/home?catid=" & cstr (url_no)
    html = scraperwiki.scrape(scrap_add)

for x in range (1, 10):
    print scrape_URL (x) 
    

    
