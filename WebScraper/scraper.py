
from bs4 import BeautifulSoup 
import requests 
import re
from fpdf import FPDF
from cfonts import render,say
#https://pyfpdf.readthedocs.io/en/latest/Unicode/index.html
#mirar si pertenece o no un caracter al pdf
def generateTitle():
    output=render('News Recover',colors=['red','yellow'],align='center')
    print(output)

def errataSec():
    pdf=FPDF()
    source= requests.get('https://blog.erratasec.com')
    soup=BeautifulSoup(source.text,'lxml')
    cont=0
    for article in soup.find_all('div',class_='date-outer'):
        try:    
            title=article.h3.a.get_text()
            summary=article.find('div',class_=('post-body entry-content')).get_text()
            link=article.find('div',class_='jump-link').a['href']
            print(title+summary+link)
            print(title.encode('latin-1'))
            pdf.add_page()
            pdf.set_font("Arial",'UI',size=30)
            pdf.multi_cell(0,10,txt=str(title+"hola"))
            pdf.set_font('Arial', '', 14)
            pdf.multi_cell(0,8,txt=summary.encode('latin-1','replace').decode('latin-1'))
            cont=cont+1
            pdf.set_font('Arial','U',size=14)
            pdf.multi_cell(0,8,txt="Link para leer mas"+"\n"+link)
            if(cont==3):
                break
        except Exception as e:
            pass
    pdf.output("errataSec.pdf")

def hackingArticles(palabra):
    print("\nCTF\n")
    CTF= requests.get('https://www.hackingarticles.in/ctf-challenges-walkthrough/')
    soup=BeautifulSoup(CTF.text,'lxml')
    for article in soup.find_all('p',class_='entry-title'):
        titleText=article.a.text
        url=article.a['href']
        if(re.search(palabra,titleText,re.IGNORECASE)):
            print("CTF-->"+titleText+"<---URL---> https:"+url)

    print("\nPENETRATION TESTING\n")
    penetrationTesting= requests.get('https://www.hackingarticles.in/penetration-testing/')
    soup=BeautifulSoup(penetrationTesting.text,'lxml')
    for article in soup.find_all('p',class_='entry-title'):
        titleText=article.a.text
        url=article.a['href']
        if(re.search(palabra,titleText,re.IGNORECASE)):
            print("PT-->"+titleText+"<---URL---> https:"+url)
    
    print("\nWEB PENETRATION TESTING\n")
    webHacking= requests.get('https://www.hackingarticles.in/web-penetration-testing/')
    soup=BeautifulSoup(webHacking.text,'lxml')
    for article in soup.find_all('p',class_='entry-title'):
        titleText=article.a.text
        url=article.a['href']
        if(re.search(palabra,titleText,re.IGNORECASE)):
            print("WH-->"+titleText+"<---URL---> https:"+url)

    print("\nRED TEAMING\n")
    redTeaming= requests.get('https://www.hackingarticles.in/red-teaming/')
    soup=BeautifulSoup(redTeaming.text,'lxml')
    for article in soup.find_all('p',class_='entry-title'):
        titleText=article.a.text
        url = article.a['href']
        if(re.search(palabra, titleText, re.IGNORECASE)):
            print("RT-->"+titleText+"<---URL---> https:"+url)

def krebsOnSecurity():
    pdf=FPDF()
    request= requests.get('https://krebsonsecurity.com/')
    soup=BeautifulSoup(request.text,'lxml')
    for article in soup.find_all('div',class_="post-smallerfont"):
        try:
            print("<--ARTICLE-->")
            title=article.h2.text
            pdf.add_page()
            pdf.set_font("Arial",'UI',size=30)
            pdf.multi_cell(0,10,txt=title.encode('latin-1','replace').decode('latin-1')+"hola")
            print(title+"\n")

            pdf.set_font('Arial', '', 14)
            for paragraph in article.find_all('p'):
                summary=paragraph.text
                pdf.multi_cell(0,8,txt=(summary.encode('latin-1','replace').decode('latin-1')).replace("?",'"'))
                print(summary)
            print("\nLINK TO READ MORE\n")
            pdf.set_font('Arial','U',size=14)
            link=article.find('a',class_="more-link")
            pdf.multi_cell(0,8,txt="Link para leer mas"+"\n"+link['href'])
            print(link['href'])
            print(link)
        except Exception as e:
            print("AAAAAAAAAAAAAA")
            pass
    print("hola")
    pdf.output("krebsOnSecurity.pdf")


        
errataSec()
krebsOnSecurity()



    



