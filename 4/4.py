import re
import urllib

search = re.compile("(\d*)$")
search_html = re.compile("\.html$")

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "12345"

for i in xrange(400):
    line = urllib.urlopen(url + nothing).read()
    print str(i)+line
    match = search.findall(line)
    print match
    if search_html.findall(line):
        break
    if match:
        nothing = match[0]
    else:
        nothing = str(int(match) / 2)