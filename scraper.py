#!/usr/bin/python

# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("http://www.grampiancaredata.gov.uk/home?catid=2")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)

for el in root:
    #print el.tag
    for el2 in el:
        if el2.tag == "<script type='text/javascript'>:
            print "TRUE"
        print "--", el2.tag, el2.attrib
    
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
