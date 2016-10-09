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
# root = lxml.html.fromstring(html)


start_str = "sobi2Cats.icon.nlMinus = 'http://www.grampiancaredata.gov.uk/components/com_sobi2/images/nolines_minus.gif';"
start_index = html.find(start_str)

short_html = html [start_index + len( start_str):]
print short_html

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
