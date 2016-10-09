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


start_str = "<!-- Start of SOBI2 Menu Module -->"
end_str = "<!--End of SOBI2 Menu Module -->"
start_index = html.find(start_str) + len( start_str)
end_index = html.find (end_str)

short_html = html [start_index : end_index]

start_str = "sobi2Cats.icon.nlMinus = 'http://www.grampiancaredata.gov.uk/components/com_sobi2/images/nolines_minus.gif';"
start_index = short_html.find (start_str) + len(start_str)

end_str = "document.write(sobi2Cats);" 
end_index = short_html.find (end_str)
shorter_html = short_html [start_index + 1: end_index]

# print shorter_html

split_lines = shorter_html.splitlines()

print split_lines [470]

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
