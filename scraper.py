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
    
    #set up variables
    rec_no = 0
    services = []
    
    # get the rec_no
    el = root.cssselect("div#sobi2outer p")[0]  
    rec_no = str( el.text [14:].strip())
    print rec_no
    
    # get services
    for p in root.cssselect ("div#FirstTab p"):
        services [p] = root.cssselect ("div#FirstTab p")[p]
    services = el.text
    print services
    
    return "true"

# lower_rec = 16
# upper_rec = 2402

# for x in range (lower_rec, upper_rec):
#    print scrape_URL (x)  

scrape_URL(103)
