# Controlla e verifica i dati

La sezione **Elaborazione dell'albero genealogico** delle [impostazioni di amministrazione](settings.md) contiene due strumenti che controllano l'albero genealogico: uno per problemi tecnici nel database e uno per dati implausibili.

## Controlla e Ripara il Database

Questo strumento controlla il database di Gramps per incoerenze interne e ripara quelle che può – analogo allo strumento [Controlla e Ripara il Database](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) in Gramps Desktop.

Clicca su **Controlla e Ripara** e attendi che l'indicatore di progresso completi. Il risultato è mostrato sotto il pulsante:

- Se non sono stati trovati errori, viene visualizzato un messaggio di conferma.
- Se sono stati trovati errori, viene mostrato un riepilogo delle riparazioni applicate.

Esegui questo strumento se incontri errori o comportamenti inaspettati che potrebbero essere causati da incoerenze nel database, come relazioni mancanti tra oggetti.

## Verifica i Dati

Mentre [Controlla e Ripara il Database](#check-and-repair-database) cerca incoerenze *tecniche*, questo strumento cerca dati *implausibili* – analogo allo strumento [Verifica i Dati](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) in Gramps Desktop. Riporta cose che non sono impossibili ma sono abbastanza improbabili da meritare un secondo sguardo, come una madre di 12 anni o una persona che ha vissuto fino a 130 anni.

Sotto **Opzioni** puoi regolare le soglie utilizzate dai test – età massima, età minima e massima per sposarsi o avere figli, numero massimo di figli, e così via – così come se stimare date mancanti o imprecise e se segnalare date non valide come il 31 febbraio. Le opzioni che cambi vengono ricordate nel tuo browser per la prossima esecuzione; **Ripristina** ripristina le impostazioni predefinite.

Clicca su **Verifica i Dati** per iniziare. Il controllo viene eseguito come un'attività in background, e i risultati vengono quindi elencati sotto **Risultati della Verifica dei Dati**. Niente viene cambiato da questo strumento: riporta solo ciò che trova.

!!! nota
    Un risultato non è prova di un errore. Vite lunghe e ampie differenze di età si verificano, quindi tratta i risultati come un elenco di cose da controllare piuttosto che un elenco di cose da correggere.
