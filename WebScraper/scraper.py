from bs4 import BeautifulSoup 
import requests 
from fpdf import FPDF


def errataSec():
    pdf=FPDF()
    #pdf.cell(100,100,txt="Esto es una",ln=2,align="C")
    
    source= requests.get('https://blog.erratasec.com')
    soup=BeautifulSoup(source.text,'lxml')
    for article in soup.find_all('div',class_='date-outer'):
        try:
            
            #title=article.find('div',class_=('date-outer')).h3.a.text
            title=article.h3.a.text
            summary=article.find('div',class_=('post-body entry-content')).text
            link=article.find('div',class_='jump-link').a['href']
            #print(title+summary+link)
            #print("ESTO ES OTRO ARTICULO")
            print(title.encode('latin-1'))
            pdf.add_page()
            pdf.set_font("Arial",'UI',size=30)
            pdf.cell(100,40,txt=title.decode('latin-1'),align="C")
            pdf.ln()
            pdf.set_font("Arial",size=12)
            pdf.multi_cell(0,5,txt=summary.decode('latin-1'))
            #pdf.cell(100,100,txt="Esto es una",ln=2,align="C")
            pdf.ln()
        
        except Exception as e:
            pass
    pdf.output("prueba.pdf")

errataSec()
 

