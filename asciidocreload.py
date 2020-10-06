import os
import platform
import sys, getopt
import time
from selenium import webdriver
from pathlib import Path

def ultima_modifica(path_file):
    # funziona solo in windows
    return os.path.getmtime(path_file)

def main(argv):
    print('script in esecuzione!')
    print('per terminare CTRL + C')

    pathfile = ''
    command = ''
    # ricezione parametri --------------------------------------------
    # -f path del file da controllare
    # -c path del comando da eseguire
    opts, args = getopt.getopt(argv,"f:c:",["pathfile","pathcommand"])
    for opt, arg in opts:
        if opt == "-f":
            pathfile = arg
        if opt == "-c":
            command = arg
    # fine ricezione parametri ---------------------------------------

    # creazione stringa di comando da eseguire quando il file è modificato
    # aggiunto 'python' per eseguire lo script passato come parametro .py
    comando = "python " + command + " " + pathfile

    # preparazione file da aprire con firefox
    # cambio estensione del file: lo script da eseguire converte from .adoc to .html
    # firefox per aprire un file locale vuole come prefisso url 'file:///'
    url = pathfile
    url = str(Path(pathfile).with_suffix('.html'))
    url = 'file://' + url
    
    # carico e preparazione driver firefox
    driver = webdriver.Firefox(executable_path = 'geckodriver')
    driver.get(url)
    
    # primo avvio controlla data ultima modifica del file
    um = ultima_modifica(pathfile)
    
    # fino a quando non si chiude il programma
    # controlla ogni tot secondi l'ultima modifica al file
    # se modificato esegui script passato come argomento ( -c ) 
    # ed effettua il refresh del file aperto con firefox
    while True:
        if um != ultima_modifica(pathfile):
            um = ultima_modifica(pathfile)
            # esegui comando
            os.system(comando)
            driver.refresh()
            print('file aggiornato!')
        time.sleep(5)

if __name__ == "__main__":
    main(sys.argv[1:])
