import sys, os

from src.barcode_utils import get_codes, get_barcodes, create_bardode_images
from src.pdf_printer import print_pdf

if not os.path.exists('barcodes'):
    os.makedirs('barcodes')

if not os.path.exists('outputs'):
    os.makedirs('outputs')

cmd_type, codes = get_codes(sys.argv)
# print(cmd_type, codes)

if cmd_type is not None and len(codes) > 0:
    print('Lettura dati degli articoli ' + ', '.join(codes))
    data = get_barcodes(codes)

    print('Generazione di {0} barcodes'.format(str(len(data))))
    create_bardode_images(data)

    print('Generazione barcode completata :D')

else:
    print('Nessun articolo da elaborare :c\nPer elaborare i dati devi specificare un codice articolo o il percorso di un file .csv\n\n\n')

# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Gestione della stampa del documento con i barcode :/            
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

dir_content = os.listdir('barcodes')

if len(dir_content) > 0:
    print(f'Desideri generare un file .pdf con i barcode nella cartella barcodes? [y/n]')
    confirm = input()

    if confirm == 'y' or confirm == 'Y':
        print_pdf(dir_content)
        print('Stampa completata :3')

if codes is not None or len(dir_content) > 0:
    print('Ho finitooo :P')