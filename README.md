# barcode-generator
A python script that can generate barcode 🐍

## Prerequisiti
Per utilizzare correttamente lo script occorre aver installato:
- Python 3.0+
- wkhtmltopdf

## Configurazione
Creare un file .env in questa cartella. Nel file .env vanno impostate le seguenti chiavi:
- CONNECTION_STRING: La stringa di connessione utilizzata per connettersi al db e ricavare i dati tramite query.sql
- PDF_LIB_PATH: Il percorso per richiamare il programma wkhtmltopdf

Esempio di file .env:
```
CONNECTION_STRING='DRIVER={ODBC Driver 17 for SQL Server};SERVER=my-server;DATABASE=my-db;Trusted_Connection=yes;'
PDF_LIB_PATH='C:\\PathTo\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
```

Creare un file query.sql contenente la query per ricavare i valori dei barcode dal database a cui ci si sta collegando. Vedi query.example.sql per avere le istruzioni su come scrivere la query correttamente.

La primissima volta va configurato il virtual env utilizzato da questo script.
Utilizzare i seguenti comandi:
- ```python -m venv venv``` (verrà creato un venv chiamato venv)
- ```.\venv\Scripts\activate``` (verrà attivato il venv e entreremo nel suo contesto)
- ```pip install -r requirements.txt``` (verranno installate le dipendenze dello script)
- ```deactivate``` (verrà disattivato il venv)

## Utilizzo
Per utilizzare lo script va attivato il venv con il comando ```venv\Scripts\activate```.

Per lanciare lo script utilizzare ```python generator.py```. Si possono usare i seguenti comandi:
- ```python generator.py <cod articolo>``` oppure ```python generator.py -a <cod articolo>``` per generare i barcode di un solo articolo.
- ```python generator.py -l <cod articolo 1>.<cod articolo 2>.<cod articolo n>``` per generare i barcode di una lista di articoli. I codici devono essere separati dal carattere punto (.).
- ```python generator.py -f <percorso csv>``` per generare i barcode da un file csv. Il file csv deve essere formattato in modo da avere un codice articolo per ogni riga (non separati da nessun tipo di carattere).

Ad ogni esecuzione dello script, se ci sono dati nella cartella barcodes, verrà chiesto se si vuole generare il report pdf.

Al termine dell'utilizzo disattivare il venv attivato per utilizzare lo script con il comando ```deactivate```.
