from scraper import *
def main():
    generateTitle()
    salir=False
    while(not(salir)):
        print('a-Generar PDF de articulos de ErrataSec()')
        print('b-Busqueda de articulso de la pagina de hackingArticles')
        resultado=input()
        if(resultado=='a'):
            errataSec()
        if(resultado=='b'):
            print("Introduce palabra para ver si existe algun articulo en Hacking Articles")
            palabra=input()
            hackingArticles(palabra)
        else:
            print("no se ha reconocido operacion")
        print("Pulse '1' para salir sino pulse cualquiera")
        salida=input()
        salir=salida=='1'

main()

    