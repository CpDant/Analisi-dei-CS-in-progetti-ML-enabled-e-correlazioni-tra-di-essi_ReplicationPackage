# Analisi-dei-Community-Smells-in-progetti-ML-enabled-e-correlazioni-tra-di-essi_ReplicationPackage
Tesi di ricerca realizzata in collaborazione con il SeSaLab.

## Obiettivi
L'obiettivo della tesi è di identificare i Community Smells all'interno di progetti ML-enabled, utilizzando CSDetector (riadattando quello li già presente di [Gianmario Voria](https://github.com/gianwario) e di [Nuri Almarimi](https://github.com/Nuri22). Poi, i dati prodotti dal tool, verranno utilizzati su un modello statistico denominato cross-sectional, che attraverso i valori di Relative Risk e Odds Ratio, stabilisce il tipo di correlazione tra coppie di Community Smells. 

## CSDetector
Il primo step della tesi di ricerca è stato l'utilizzo di CSDetector su un dataset di 50 progetti ML-enabled, denominato "datasetProgetti.xlsx", che ha il compito di rilevare i Community Smells e salvare le informazioni all'interno di un altro dataset, denominato "communitySmellsDataset.xlsx". Entrambi i dataset possono essere visualizzati nella cartella dataset di questo repository. Di seguito andremo a dettagliare i passaggi fondamentali per far funzionare il tool.

### Requisiti
I requisiti fondamentali sono:
* Python 3.8.3
* Java 8.0.231
* Windows 10/11
* [SentiStrength](http://sentistrength.wlv.ac.uk/jkpop/)

### Procedimento
Gli step fondamentali per far funzionare il tool sono:
1. Clonare la repository sul proprio pc come file zip
2. estrarre la cartella csDetector-master
3. creare due cartelle all'interno di csDetector-master una chiamata "out" (dove andrà l'output del tool) e una chiamata senti
4. Inserire Nella cartella "senti" i due file sentiStrength.jar e SentiStrength_Data.zip (attenzione al file zip che va estratto e messo in una cartella chiamata nello stesso modo del file zip)
5. Creare il virtual environment di Python con i seguenti comandi:
    * py -m pip install --user virtualenv
    * py -m pip install --upgrade pip setuptools wheel
    * py -m venv .venv
6. 





