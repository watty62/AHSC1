#!/usr/bin/python

# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
# import lxml.html
#
# # Read in a page
# scrape_add = ""

def scrape_URL (url_no):
    scrape_add = "http://www.grampiancaredata.gov.uk/home?catid=" + str(url_no)
    html = scraperwiki.scrape(scrape_add)
    return html

for x in range (1, 5):
    print scrape_URL (x) 
    

    
