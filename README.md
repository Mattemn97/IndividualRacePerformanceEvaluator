# IndividualRacePerformanceEvaluator

Il progetto **IndividualRacePerformanceEvaluator** propone un sistema di valutazione statistica per i piloti di motorsport (con particolare focus su Formula 1), ispirato alla formula "Valutazione di Lega" utilizzata nel basket. L’obiettivo è fornire un indicatore oggettivo delle prestazioni dei piloti gara per gara.

## 🎯 Obiettivi
✅ Applicare un sistema di valutazione oggettivo alle prestazioni individuali dei piloti.  
✅ Automatizzare la raccolta dati e il calcolo dei punteggi.  
✅ Generare report settimanali tramite pipeline (GitHub Actions).  

## 🏎️ Variabili considerate

| Variabile | Codice | Unità | Descrizione |
|------------|--------|--------|-------------|
| Posizione partenza | PP | Pos | Posizione in griglia |
| Posizione arrivo | PA | Pos | Posizione finale |
| Posizioni guadagnate | PG | ΔPos | PP - PA |
| Sorpassi effettuati | SE | Sorp | **(Non disponibile direttamente in Fast-F1)** |
| Sorpassi subiti | SS | Sorp | **(Non disponibile direttamente in Fast-F1)** |
| Under-Cut riusciti | UC | Sorp | **(Non disponibile direttamente)** |
| Contatti causati | CC | Cont | **(Non disponibile)** |
| Contatti subiti | CS | Cont | **(Non disponibile)** |
| Ritiri causati | RC | Rit | **(Stimabile solo manualmente o da note extra)** |
| Ritiri subiti | RS | Rit | **(Stimabile solo manualmente o da note extra)** |
| Giri al comando | GG | Giri | Numero giri al comando |
| % giri al comando | GG% | % | GG / totale giri gara |
| Giri completati | GC | Giri | Numero giri completati |
| % giri completati | GC% | % | GC / totale giri gara |
| Pit stop oltre media | PSE | Pit | **(Possibile confronto con media pit stop evento)** |
| Penalità (numero) | PO | Pen | Numero penalità |
| Penalità (sec) | POS | sec | Secondi di penalità totali |

## ℹ️ Note sui dati
Le seguenti variabili **non sono direttamente ottenibili da Fast-F1**:
- Sorpassi effettuati/subiti (SE, SS)
- Under-Cut riusciti (UC)
- Contatti (CC, CS)
- Ritiri causati/subiti (RC, RS)

👉 **Approccio**: Queste metriche potranno essere aggiunte manualmente o con fonti esterne (es. FIA race notes). Il sistema è progettato per integrarle successivamente.

## 📈 Formula di valutazione (prima versione)

```python
Valutazione = (PP * 0.75 + PG) + (SE - SS + UC) - (CC * 1.25) \
              - (RC + RS) + GG + GC - (PO + POS/10)
```
👉 Nota: La formula verrà calibrata in base alle variabili effettivamente disponibili.

⚙️ Architettura
- Python + Fast-F1: per scaricare e analizzare i dati
- Jinja2 + pdfkit / WeasyPrint: per creare i report
- GitHub Actions: per pipeline automatizzate (update settimanale e report)

🚀 Come iniziare
1️⃣ Installa i requisiti:

```python
pip install -r requirements.txt
```
2️⃣ Esegui l’analisi per un gran premio:

```python
python -m src.evaluator --year 2024 --gp "Monaco"
```
3️⃣ Genera un report:

```python
python -m src.report_generator --year 2024 --gp "Monaco"
```
🤖 Pipeline automatica
GitHub Actions esegue settimanalmente:

- Aggiornamento dei dati dell'ultima gara
- Calcolo valutazioni
- Generazione e upload del report

📄 Licenza
Questo progetto è distribuito sotto licenza MIT.

---

## 🛠️ Requisiti (requirements.txt)

```txt
fastf1
pandas
jinja2
weasyprint
matplotlib
```
