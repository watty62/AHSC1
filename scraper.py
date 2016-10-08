from bs4 import BeautifulSoup 
import urllib

def getit(pagetext):
  soup = BeautifulSoup(pagetext)
  
  for ln in soup:
    if ln == "<!-- Start of SOBI2 Menu Module -->": 
        print "true"
  
  
  '''
  results = []
  dls = soup.findAll('dl')
  for adl in dls:
    thedt = adl.dt
    while thedt:
      thea = thedt.a
      if thea:
        print 'SUBJECT:', thea.string
      thedd = thedt.findNextSibling('dd')
      if thedd:
        print 'CONTENT:',
        while thedd:
          for x in thedd.findAll(text=True):
            print x,
          thedd = thedd.findNextSibling('dd')
        print
      howmany -= 1
      if not howmany: return
      print
      thedt = thedt.findNextSibling('dt')
'''
theurl = ('http://www.grampiancaredata.gov.uk/home?catid=2')
thepage = urllib.urlopen(theurl).read()
getit(thepage)
