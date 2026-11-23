# XBvPC — presentazione in italiano

**Laboratorio sperimentale C++17 per l'esecuzione controllata di codice x64 guest e l'analisi di immagini PE32+.**

> **Non è un emulatore Xbox Series X|S funzionante.** Non sono stati avviati giochi commerciali, non esiste ancora un loader di produzione, e non si rivendica compatibilità con titoli reali.

## Risultati verificati al 23 novembre 2026

- **P6-R4:** 102/102 controlli; IAT con due provider.
- **P7-R3:** 74/74 controlli; coordinamento fra CPU guest e ciclo di vita del grafo.
- **P8-S1-R3:** 16/16; due funzioni x64 da PE esterno eseguite con risultati `42` e `23`.
- **P9-S1:** 25/25; import PE per nome e ordinale, 2/2 chiamate annidate.
- **P10-S1-R1:** operatore preparato, ma **nessun PASS confermato** nei log disponibili alla stesura.

Sono risultati di test **sintetici e locali**, non build CI o dimostrazioni di giochi reali. Il codice storico e i binari non si pubblicano automaticamente: si selezionano i file che si è autorizzati a distribuire e si costruisce un percorso di compilazione riproducibile.

Consulta [stato dettagliato](STATUS.md), [architettura](ARCHITECTURE.md), [roadmap](ROADMAP.md) e [istruzioni GitHub](GITHUB_SETUP_IT.md).
