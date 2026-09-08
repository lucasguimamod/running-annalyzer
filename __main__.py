from functions import *
import json

def main():
    arquivo = open('historico.json', 'r')
    hist = json.load(arquivo)
    arquivo.close()
    menu(hist)
    save_history(hist)

if __name__ == '__main__':
    main()