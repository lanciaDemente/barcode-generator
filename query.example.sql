-- NON CANCELLARE QUESTI COMMENTI!!

-- La query deve tornare i seguenti campi:
-- RowCode: un codice univoco che identifica il record (verrà usato come nome del file)
--          non deve contenere caratteri speciali (sarà il nome di un file quindi evitare spazi (e robe tipo %&/!?) ok?)
-- Barcode: codice a barre che verrà generato

-- Parametri:
-- {0}: Codice articolo (lo {0} verrà sostituito nell'esecuzione dello script con i codici da prendere)

-- Per utilizzare la query creare un file query.sql che la contiene, questo file query.example.sql è solo un esempio.

select
    'codice-univoco-per-barcode-articolo' as RowCode,
    'valore-barcode-0101' as Barcode
from Articoli
where CodiceArticolo in ({0})