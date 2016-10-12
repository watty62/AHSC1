#!/usr/bin/python

# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
# scrape_add = ""

def scrape_URL (url_no):
    scrape_add = "http://www.grampiancaredata.gov.uk/home?sobi2Task=sobi2Details&sobi2Id=" + str(url_no)
    html = scraperwiki.scrape(scrape_add)
    root = lxml.html.fromstring(html)

    # for el in root:
    for el in root.cssselect("div.tab-page a"):           
         print lxml.html.tostring(el)
    
    return "true"

# lower_rec = 16
# upper_rec = 2402

# for x in range (lower_rec, upper_rec):
#    print scrape_URL (x)  

scrape_URL(103)
