
from bs4 import BeautifulSoup 
import requests 
from fpdf import FPDF
#https://pyfpdf.readthedocs.io/en/latest/Unicode/index.html
#mirar si pertenece o no un caracter al pdf
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
    
    pdf.output("cosa.pdf")

errataSec()
 

