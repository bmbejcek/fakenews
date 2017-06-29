from summarizer import summarize
import newspaper
from newspaper import Article
from pyteaser import SummarizeUrl
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

url = 'http://www.politifact.com/truth-o-meter/statements/2017/jun/22/antinews/its-fake-news-chinese-lunar-rover-found-no-evidenc/'

a = Article(url)
a.download()
a.parse()

TXT=a.text
TITLE=a.title


def Summarize(title, text):
 summaries = []
 sentences = split_sentences(text)
 keys = keywords(text)
 titleWords = split_words(title)
 
 if len(sentences) <= 1:
    return sentences
 
#score setences, and use the top 5 sentences
 ranks = score(sentences, titleWords, keys).most_common(1)
 for rank in ranks:
    summaries.append(rank[0])
 
 return summaries
 
use=summarize(TITLE,TXT)
print fuzz.ratio(TITLE,use)



