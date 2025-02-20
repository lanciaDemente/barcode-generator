import os, pyodbc, requests, shutil, csv

from pylibdmtx.pylibdmtx import encode
from PIL import Image

from dotenv import load_dotenv
load_dotenv()

def get_codes(input_argv):
    cmd_type = None
    codes = []

    if '-l' in input_argv:
        cmd_type = 'l'
        codes = ' '.join(input_argv[2:]).split('.')
    
    elif '-f' in input_argv:
        cmd_type = 'f'
        
        csv_path = ' '.join(input_argv[2:])
        if os.path.isfile(csv_path) and csv_path[-3:] == 'csv':
            with open(csv_path, encoding='utf-8-sig') as csv_file:
                reader = csv.reader(csv_file, delimiter=";")
                codes = [(line[0].strip()) for line in reader]
        else:
            raise ValueError("file specificato non trovato :c")

    else:
        cmd_type = 'a'
        if '-a' in input_argv:
            codes = [' '.join(input_argv[2:])]
        else:
            codes = [' '.join(input_argv[1:])]

    return cmd_type, list(map(str.strip, codes))

def get_barcodes(codes):
    data = {}

    if len(codes) > 0:
        connection_string = os.environ['CONNECTION_STRING']

        query = ''
        with open('query.sql', 'r') as f:
            query = f.read()
        
        query = query.format('\'' + '\',\''.join(codes) + '\'')
        # print(query)

        # Establishing a connection to the SQL Server
        cnxn = pyodbc.connect(connection_string)
        cursor = cnxn.cursor()
        cursor.execute(query)
        
        rows = cursor.fetchall()
        for row in rows:
            barcode = row[1]
            data[barcode] = {}
            data[barcode]['rowcode'] = row[0]
            data[barcode]['codetype'] = row[2]
        
        cursor.close()

    return data

def create_bardode_images(data):
    # TODO: aggiungere supporto per altri barcode (per ora solo datamatrix)
    for key in data:
        rowcode = data[key].get('rowcode')
        encoded = encode(key.encode('utf8'))
        img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
        img.save('barcodes\{0}.png'.format(rowcode))