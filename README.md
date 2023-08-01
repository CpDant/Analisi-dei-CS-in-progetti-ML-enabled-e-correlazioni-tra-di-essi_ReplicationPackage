# Analisi-dei-Community-Smells-in-progetti-ML-enabled-e-correlazioni-tra-di-essi_ReplicationPackage
Tesi di ricerca realizzata in collaborazione con il SeSaLab.

## Obiettivi
L'obiettivo della tesi è di identificare i Community Smells all'interno di progetti ML-enabled, utilizzando CSDetector (riadattando quello li già presente di [Gianmario Voria](https://github.com/gianwario) e di [Nuri Almarimi](https://github.com/Nuri22)). Poi, i dati prodotti dal tool, verranno utilizzati su un modello statistico denominato cross-sectional, che, attraverso i valori di Relative Risk e Odds Ratio, stabilisce il tipo di correlazione tra coppie di Community Smells. 

## CSDetector
Il primo step della tesi di ricerca è stato l'utilizzo di CSDetector su un dataset di 50 progetti ML-enabled, denominato "datasetProgetti.xlsx", che ha il compito di rilevare i Community Smells e salvare le informazioni all'interno di un altro dataset, denominato "communitySmellsDataset.xlsx". Entrambi i dataset possono essere visualizzati nella cartella dataset di questo repository. Di seguito andremo a dettagliare i passaggi fondamentali per far funzionare il tool e i risultati prodotti.

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
4. Inserire Nella cartella "senti" i due file sentiStrength.jar e SentiStrength_Data.zip (attenzione al file zip che va estratto e messo in una cartella chiamata nello stesso modo del file zip). Il link per scaricare i file si trova nella sezione dei requisiti.
5. Creare il virtual environment di Python con i seguenti comandi:
    * <i>py -3.8 -m pip install --user virtualenv</i>
    * <i>py -3.8 -m pip install --upgrade pip setuptools wheel</i>
    * <i>py -3.8 -m venv .venv</i>
6. installare i moduli (con l'env attivo) utilizzando il comando <i>py -3.8 -m pip install -r .\requirements.txt</i>
7. installare spacy (con il comando <i>py -3.8 -m pip install spacy</i>) e eseguire il seguente comando <i>py -3.8 -m spacy download en_core_web_sm</i>
8. Aprire una console con il comando "python -3.8" ed eesguire i seguenti comandi:
    * <i>import nltk</i>;
    * <i>nltk.download('punkt')</i>;

Se tutti gli step sono stati eseguiti correttamente, il tool CSDetector potrà essere utilizzato per analizzare i progetti, con il comando <i>py -3.8 .\devNetwork.py -p "GitHubToken" -r "linkGitHubProgetto" -s "./senti" -o "./out"</i>, dove i campi "GitHubToken" e "linkGithubProgetto" devono essere riempiti rispettivamente con il token, creato da GitHub, che permette di accedere alle GitHub API (l'accesso alle GitHub API è necessario per il funzionamento del tool) e il link della repository del progetto. Su alcuni progetti potrebbe non funzionare, però se viene rieseguito più volte potrebbe poi funzionare, se l'errore non accade all'inizio dell'esecuzione, altrimenti è un errore che non può essere risolto e quindi quel progetto non sarà analizzabile.

### Risultati
Il tool è stato eseguito sui progetti salvati nel dataset denominato "datasetProgetti.xlsx" e i risultati dell'esecuzione hanno permesso di determinare gli smell associati ad ogni singolo progetto. L'output del tool stampa sul prompt uno o più acronimi, che identificano gli smell associati a quel progetto. CSDetector ha la possibilità di identificare 10 tipi di Community Smells, che sono:

<code>Organizational Silo Effect (OSE)</code>: Questo Community Smell è associato a problemi di coordinamento delle attività. Le attività di sviluppo del software, a volte, non sono interconnesse tra loro. Questo smell pone sfide per verificare le dipendenze delle attività e le condizioni non favorevoli, per una comunicazione efficace tra i compagni di squadra che eseguono le attività. Questo scenario mette a rischio la congruenza socio-tecnica.

<code>Black-Cloud Effect (BCE)</code> : Questo smell è presente quando le organizzazioni non forniscono le condizioni per le interazioni sociali e una comunicazione efficace tra i compagni di squadra. Pertanto, le condizioni non supportano lo scambio di conoscenze durante i processi di sviluppo del software, ad esempio esperienza professionale o comprensione dei progetti in corso.

<code>Prima-Donnas Effect (PDE)</code> : Questo smell indica la presenza di compagni di squadra che lavorano in isolamento. Non sono disposti ad accogliere con favore il cambiamento di prodotti legacy e il supporto di altri compagni di squadra. Questi compagni di squadra impediscono all'organizzazione soluzioni o processi innovativi ed un'efficace comunicazione e collaborazione.

<code>Sharing Villainy (SV)</code> : Questo Community Smell descrive ambienti di lavoro in cui l'obiettivo di condividere conoscenze o informazioni affidabili è una sfida. Le organizzazioni non forniscono le condizioni previste per la condivisione delle conoscenze, come opportunità di incontri e incentivi. Pertanto, alcuni compagni di squadra non vedono la condivisione delle conoscenze come un'attività produttiva per il completamento dei progetti.

<code>Organizational Skirmish (OS)</code> : Una schermaglia organizzativa è uno scenario in cui i team hanno differenze rispetto alle loro culture organizzative. Rende difficile il lavoro dei project manager. L'impatto è noto sulla produttività, ad esempio i ritardi del progetto.

<code>Solution Defiance (SD)</code> : Questo smell descrive i conflitti tra le squadre. I compagni di squadra con fattori di livello simili (ad esempio, background tecnico) e convinzioni culturali organizzative (ad esempio, valori e norme) creano sottoteam. Quindi entrano in conflitto nelle riunioni decisionali, poiché ogni gruppo sostiene le proprie opinioni su potenziali soluzioni.

<code>Radio Silence (RS)</code> : È uno scenario in cui leader e compagni di squadra svolgono compiti in organizzazioni molto formali e complesse. In queste condizioni, le strutture di comunicazione del team non favoriscono la diffusione efficiente delle informazioni tra i team. Ad esempio, una persona che lavora come intermediario di informazioni unico per diversi team, porta a un sovraccarico di comunicazione e enormi ritardi.

<code>Truck Factor (TF)</code> : La maggior parte delle informazioni e delle conoscenze sul progetto sono concentrate
in uno o pochi sviluppatori. Porta a una significativa perdita di conoscenza, a causa del turnover degli sviluppatori.

<code>Unhealthy Interaction (UI)</code> : Le discussioni tra gli sviluppatori sono lente, leggere, brevi e/o contengono conversazioni scadenti. Risulta esserci una bassa partecipazione degli sviluppatori alle discussioni del progetto (ad esempio, pull requests, problemi, ecc.), con lunghi ritardi tra le comunicazioni dei messaggi.

<code>Toxic Communication (TC)</code> : Le comunicazioni tra gli sviluppatori sono soggette a conversazioni tossiche e sentimenti negativi contenenti opinioni spiacevoli, di rabbia o addirittura contrastanti su vari argomenti di cui le persone discutono. Dunque, gli sviluppatori possono avere interazioni interpersonali negative con i loro coetanei,
che possono portare a frustrazione e stress. Queste interazioni negative possono alla fine portare gli sviluppatori ad abbandonare i progetti.

I risultati sono stati salvati nel dataset "communitySmellsDataset.xlsx", andando a modificare il codice <i>devNetwork.py</i>, in modo tale che appena il tool ci restituisce l'output, esso viene salvato automaticamente nel dataset.

## Modello cross-sectional
il modello \textit{cross-sectional} è un modello statistico in cui si raccolgono dati da molti individui diversi in un punto nel tempo. Esso risulta essere un modello semplice ed economico per la raccolta dei dati e l'identificazione di correlazioni. Inoltre, consente solo di descrivere una variabile e non misurarla.
Di seguito verranno riportati gli step fondamentali per far funzionare il modello e i risultati prodotti.

### Procedimento
Il primo passo è stato quello di calcolare gli elementi chiave del modello cross-sectional, cioé il Relative Risk (la probabilità che un soggetto, appartenente ad un gruppo esposto a determinati fattori, sviluppi la malattia, rispetto alla probabilità che un soggetto, appartenente ad un gruppo non esposto, sviluppi la stessa malattia) e l'Odds Ratio (dato statistico che misura il grado di correlazione tra due fattori). Per calcolare questi fattori, è stato utilizzato uno script di Python, denominato "correlationDetection.py", che in input riceve gli acronimi della coppia di smell che si vuole confrontare e in output fornisce, attraverso una serie di calcoli, proprio i due elementi citati in precedenza.

### Risultati
Dopo aver calcolato, per ogni coppia di smell, i valori di Relative RIsk e Odds Ratio, i dati sono stati salvati in un dataset, denominato "correlationCSDataset.xlsx". Poi, ho realizzato due tabelle in formato excel, che permettono di visualizzare, in maniera grafica, i risultati ottenuti e renderli più comprensibili. Le tabelle sono delle matrici diagonali, aventi entrambe le stesse regole, elencate di seguito:
* <code>Valore della cella = 1</code>, la cella assume un colore grigio;
* <code>Valore della cella > 1</code>, la cella passa dal colore grigio, al colore verde indicando, in questo modo, che sono positivamente correlate;
* <code>Valore della cella < 1 </code>, la cella passa dal colore grigio al colore rosso indicando, in questo modo, che sono negativamente correlate.

Le due matrici diagonali sono state denominate "relativeRiskMatrix.xlsx" e "oddsRatioMatrix.xlsx" e si possono visualizzare nella cartella matrix di questa repository. Rappresentano rispettivamente i valori di Relative Risk e Odds Ratio. Osservando le due matrici, quello che si può dedurre è che i valori di \textit{Relative Risk} e \textit{Odds Ratio}, indicano più o meno le stesse informazioni per ogni coppia. Una delle coppie più interessanti è la coppia <code>BCE/RS</code>. Come possiamo vedere dai grafici, il valore del \textit{Relative Risk} è uguale a 10.6 e quello dell'\textit{Odds Ratio} è uguale a 31.6 ed entrambe le celle sono colorate di un verde molto scuro, poiché sono molto distanti dal punto di centro che è il valore 1. Da ciò si può dedurre che i due smell sono fortemente correlati in maniera positiva, cioé la presenza dello smell BCE, implica molto spesso la presenza anche di RS.





