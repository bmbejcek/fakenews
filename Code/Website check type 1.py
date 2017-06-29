import requests
request = requests.get('http://www.politifact.com/truth-o-meter/statements/2017/jun/22/antinews/its-fake-news-chinese-lunar-rover-found-no-evidenc/')
if request.status_code == 200:
    print('Web site exists')
else:
    print('Web site does not exist') 
    
    
