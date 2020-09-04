from bs4 import BeautifulSoup 
import requests 
import csv 
source= requests.get('https://blog.erratasec.com')

soup=BeautifulSoup(source.text,'lxml')
csv_file=open('csm_scrape.csv','w')

csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Title','Summary','FullArticleLink'])
for article in soup.find_all('div',class_='date-outer'):
    try:
        #title=article.find('div',class_=('date-outer')).h3.a.text
        title=article.h3.a.text
        summary=article.find('div',class_=('post-body entry-content')).text
        link=article.find('div',class_='jump-link').a['href']
        print(title+summary+link)
        print("ESTO ES OTRO ARTICULO")
    except Exception as e:
        pass
    csv_writer.writerow([title,summary,link])

csv_file.close()