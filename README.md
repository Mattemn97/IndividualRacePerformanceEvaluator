# IndividualRacePerformanceEvaluator
This repository aims to be an example of the application of the statistical-objective evaluation of basketball matches to the competitions of individual motorsport drivers and in particular F1

# Individuazione delle variabili
Iniziando con l'individuazione delle variabili si entra subito in contatto con il primo problema: cosa è una variabile all'interno di una gara?

## Definizione di variabile
Andando per negazione, possiamo ciecamente dire che non è una variabilw all'interno della singola gara il mezzo utilizzato utilizzato per correre: in quanto non cambia durante la gara. Essendo lo stesso dall'inizio alla fine della gara non può essere una varibile di cui tenere conto.

Quindi una variabile è una qualcosa di quantificabile può cambiare durante il corso della gare e che descrive, anche parzialmente, una gara di un pilota

## Caratteristiche delle variabili
Le variabili devono avere le seguenti caratteristiche:
* Nome univoco
* Unità di misura ben precisa
* Individuali del singolo pilota


## Possibili variabili
| Variabile                                             | Codice | Unità     | Tipologia | Descrizione                                                                              |
|-------------------------------------------------------|--------|-----------|-----------|------------------------------------------------------------------------------------------|
| Posizione partenza                                    | PP     | Pos       | Posizioni | Posizione in cui si trovava il pilota alla partenza del granpremio                       |
| Posizione arrivo                                      | PA     | Pos       | Posizioni | Posizione in cui si trovava il pilota alla fine del granpremio                           |
| Posizioni guadagnate                                  | PG     | Delta Pos | Posizioni | Posizioni guadagnate dal pilota --> PP - PA                                              |
| Sorpassi effettuati                                   | SE     | Sorp      | Sorpassi  | Totale dei sorpassi effettuati dal pilota                                                |
| Sorpassi subiti                                       | SS     | Sorp      | Sorpassi  | Totale dei sorpassi subiti dal pilota                                                    |
| Sorpasso effettuato con Under-Cut                     | UC     | Sorp      | Sorpassi  | Punto aggiuntivo in caso di Under Cut effettuato correttamente                           |
| Contatti causati                                      | CC     | Cont      | Contatti  | Totale dei contatti con altri piloti causati dal pilota                                  |
| Contatti subiti                                       | CS     | Cont      | Contatti  | Totale dei contatti con altri piloti subiti dal pilota                                   |
| Ritiri causati                                        | RC     | Rit       | Ritiri    | Punteggio negativo in caso di ritiro causato da un errore del pilota                     |
| Ritiri subiti                                         | RS     | Rit       | Ritiri    | Punteggio negativo in caso di ritiro non causato da un errore del pilota                 |
| Giri alla guida del granpremio                        | GG     | Giri      | Giri      | Totale giri effettuati al comando del granpremio dal pilota                              |
| Giri alla guida del granpremio/totale giri completati | GG%    | %Giri     | Giri      | Percentuale dei giri effettuati al comando del granpremio sul totale dei giri effettuati |
| Giri completati del granpremio                        | GC     | Giri      | Giri      | Totale giri effettuati nel granpremio dal pilota                                         |
| Giri completati del granpremio/totale giri granpremio | GC%    | %Giri     | Giri      | Percentuale dei giri effettuati dal pilota sul totale dei giri del granpremio            |
| Pit Stop effettuati oltre la media                    | PSE    | Pit       | PitStop   |                                                                                          |
| Penalità ottenute                                     | PO     | Pen       | Penalità  |                                                                                          |
| Penalità ottenute in secondi                          | POS    | sec       | Penalità  |                                                                                          |

## Applicazioni nelle formule
### Formula "Valutazione di Lega"
La formula utilizzata attualmente dalla FIP è detta "Valutazione di Lega". Andando a convertire i codici delle variabili del basket con quelle precedentemente indentificate la formula diventa:

```
Valutazione di Lega = SE - SS + UC - CC + CS - RC - RS + GG + GC
```

La formula creata è una pura riscrittura della "Valutazione di Lega" e non tiene conto della proporzionalità sui giri effettuati, non del fatto che ogni tipo di contatto è ritenibile come negativo o della posizione di partenza e di arrivo.

### Formula "Valutazione di Lega" ponderata

```
Valutazione di Lega = (PP * 0.75 + PG) + (SE - SS + UC) - (CC * 1.25 - PP + RO + RD + AS - FF + FS + SD - SS
```
