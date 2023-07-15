import urllib.request #Handling URL

from bs4 import BeautifulSoup #Handling or parsing html files

import nltk #NLP toolkit
nltk.download('stopwords') #or is was extracted

from nltk.corpus import stopwords


#get the info from website
#response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/Natural_language_processing')
#html = response.read()

#...read from text file instead...
request=open("C://Users//USER//OneDrive//Documents//pantechAssign//titleGen//doc3.txt",'r')
html=request.read()
#..reading end

soup = BeautifulSoup(html,'html5lib')#decode html5 
text = soup.get_text(strip = True)#remove html tags..simple text with keywords

tokens = [t for t in text.split()]#tokenised


sr= stopwords.words('english')#a, of, by. may etc
clean_tokens = tokens[:]#remove stopwords
for token in tokens:#count of freq of keywords and plot
    if token in stopwords.words('english'):
        
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)

