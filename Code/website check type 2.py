from urllib2 import Request, urlopen, HTTPError, URLError

user_agent = 'Mozilla/20.0.1 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent':user_agent }
link = "http://www.politifact.com/truth-o-meter/statements/2017/jun/22/antinews/its-fake-news-chinese-lunar-rover-found-no-evidenc/"
req = Request(link, headers = headers)
try:
        page_open = urlopen(req)
except HTTPError, e:
        print e.code
except URLError, e:
        print e.reason
else:
        print 'ok'