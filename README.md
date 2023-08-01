# Analisi-dei-Community-Smells-in-progetti-ML-enabled-e-correlazioni-tra-di-essi_ReplicationPackage
Tesi di ricerca realizzata in collaborazione con il SeSaLab.

## Obiettivi
L'obiettivo della tesi è di identificare i Community Smells all'interno di progetti ML-enabled, utilizzando CSDetector (riadattando quello li già realizzato da [Gianmario Voria](https://github.com/gianwario) e da [Nuri Almarimi](https://github.com/Nuri22)). Poi, i dati prodotti dal tool, verranno utilizzati su un modello statistico denominato cross-sectional, che, attraverso delle metriche di correlazione (*Relative Risk* e *Odds Ratio*), stabilisce il tipo di correlazione tra coppie di Community Smells. 

## Modello cross-sectional
il modello *cross-sectional* è un modello statistico in cui si raccolgono dati da molti individui diversi in un punto nel tempo. Esso risulta essere un modello semplice ed economico per la raccolta dei dati e l'identificazione di correlazioni. Inoltre, consente solo di descrivere una variabile e non misurarla. Le metriche di correlazione che sono state utilizzate sono il *Relative Risk* e l'*Odds Ratio*. Di seguito vengono descritte nel dettaglio.

### Relative Risk
il *Relative Risk (RR)* è la probabilità che un soggetto, appartenente ad un gruppo esposto a determinati fattori, sviluppi la malattia, rispetto alla probabilità che un soggetto, appartenente ad un gruppo non esposto, sviluppi la stessa malattia. Si potrebbe riassumere ciò che è stato definito in precedenza con la seguente formula matematica:

$$RR=I(esposti)/I(non esposti)$$

dove I rappresenta l'incidenza, cioé il rapporto tra i nuovi casi di malattia durante un periodo di tempo e le persone a rischio all'inizio del periodo. Il *RR* può assumere tre significati differenti:

<code>RR = 1</code>, il fattore di rischio è ininfluente sulla comparsa della malattia;

<code>RR > 1</code>, il fattore di rischio è implicato nel manifestarsi della malattia;

<code>RR < 1</code>, il fattore di rischio difende dalla malattia (fattore di difesa).

### Odds Ratio
l'*Odds Ratio* è un dato statistico che misura il grado di correlazione tra due fattori. A differenza del *RR* che è uno studio prospettico, l'*Odds Ratio* viene utilizzato negli studi caso-controllo, cioé quelli che identificano fattori che possono contribuire a una condizione, quindi non è necessaria la raccolta dei dati nel tempo. Per calcolare gli *OR* si utilizza la seguente formula: 

$$OR=\frac{odds_E}{odds_{\neg E}}$$
dove il numeratore indica l'odds (rapporto tra la probabilità P di un evento e la probabilità che tale evento non accada) della malattia tra soggetti esposti e il denominatore indica l'odds della malattia tra soggetti non esposti. Anche l'OR assume tre significati differenti:

<code>OR = 1</code>, l'odds di esposizione nei sani è uguale all'odds di esposizione nei malati, cioè il fattore in esame è ininfluente sulla comparsa della malattia;

<code>OR > 1</code>, il fattore in esame può essere implicato nella comparsa della malattia (fattore di rischio);

<code>OR < 1</code>, il fattore in esame è una difesa contro la malattia (fattore protettivo).
### Procedimento
Dopo aver calcolato i Community Smells all'interno del dataset di progetti ML-enabled "datasetProgetti.xlsx" (grazie al tool open-source CSDetector), sono stati salvati i risultati nel dataset "communitySmellsDataset.xlsx". Per poter riuscire ad applicare il modello statistico a questo dataset è necessario seguire con precisione i seguenti step:
1. Effettuare il download della repository;
2. Aprire il prompt dei comandi (sia su Mac che su Windows);
3. Posizionarsi sulla cartella appena scaricata (dopo aver estratto i file dal .zip)
4. Eseguire il comando *py -3.8 correlationDetection.py*;
5. Inserire da tastiera gli acronimi dei Community Smells cosi come viene chiesto dallo script (gli acronimi devono essere in caps lock e devono corrispondere a come vengono salvati nel dataset "communitySmellsDataset.xlsx".

Se gli step sono stati eseguiti nel modo giusto e non sono stati riscontrati errori, allora lo script calcolerà i valori di *Relative Risk* e *Odds Ratio* in maniera corretta. 

### Risultati
Dopo aver calcolato, per ogni coppia di smell (senza ripetizioni), i valori di *Relative Risk* e *Odds Ratio*, questi sono stati salvati nel dataset "correlationCSDataset.xlsx". Poi, ho realizzato due tabelle in formato excel, che permettono di visualizzare, in maniera grafica, i risultati ottenuti e renderli più comprensibili. Le tabelle sono delle matrici diagonali, aventi entrambe le stesse regole, elencate di seguito:
* <code>Valore della cella = 1</code>, la cella assume un colore grigio;
* <code>Valore della cella > 1</code>, la cella passa dal colore grigio, al colore verde indicando, in questo modo, che sono positivamente correlate;
* <code>Valore della cella < 1 </code>, la cella passa dal colore grigio al colore rosso indicando, in questo modo, che sono negativamente correlate.

Le due matrici diagonali sono state denominate "relativeRiskMatrix.xlsx" e "oddsRatioMatrix.xlsx" e si possono visualizzare nella cartella matrix di questa repository. Rappresentano rispettivamente i valori di Relative Risk e Odds Ratio, per ogni coppia di smell. Osservando le due matrici, quello che si può dedurre è che i valori di *Relative Risk e *Odds Ratio, indicano più o meno le stesse informazioni per ogni coppia. Una delle coppie più interessanti è la coppia <code>BCE/RS</code>. Come possiamo vedere dai grafici, il valore del *Relative Risk* è uguale a 10.6 e quello dell'*Odds Ratio* è uguale a 31.6 ed entrambe le celle sono colorate di un verde molto scuro, poiché sono molto distanti dal punto di centro che è il valore 1. Da ciò si può dedurre che i due smell sono fortemente correlati in maniera positiva, cioé la presenza dello smell BCE, implica molto spesso la presenza anche di RS.
