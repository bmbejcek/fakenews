from newspaper import Article
url = 'http://www.foxnews.com/politics/2017/06/24/supreme-court-will-justice-kennedy-retire-this-month.html'

a = Article(url)
a.download()
a.parse()

print(a.text)
