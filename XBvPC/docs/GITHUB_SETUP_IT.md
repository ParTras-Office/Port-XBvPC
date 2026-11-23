# Pubblicazione GitHub — XBvPC

## 1. Prima di pubblicare

- Determina il link al tuo repository (`https://github.com/<utente>/<repository>`).
- Non esportare direttamente la cartella privata `build-linux`, le directory di esecuzione WSL o i PE binari sperimentali.
- Scegli una licenza solo dopo verifica di proprietà del codice e dipendenze.
- Decidi se il repository deve essere pubblico: la pubblicazione è irreversibile per copie già clonate.

## 2. Copia questo scaffold nel clone Git locale

**Non sovrascrivere file già esistenti senza esaminarne le differenze.** Se hai creato un repository vuoto sul sito GitHub, clonalo localmente e poi copia qui i file; in alternativa usa una cartella di lavoro separata.

## 3. Esegui il preflight

```bash
python3 tools/check_repository.py
python3 tools/generate_status.py --check
python3 -m unittest discover -s tests -p 'test_*.py' -v

git status --short
# Prima di fare un commit, esaminare:
git diff --cached --stat
git diff --cached --check
```

## 4. Pubblica soltanto dopo verifica

Esempio per un repository vuoto, dopo aver sostituito i segnaposto e controllato contenuti e branch:

```bash
# Eseguire dalla directory locale dello scaffold curato:
git init
git branch -M main
git add README.md docs data tools tests .github .gitignore .gitattributes CONTRIBUTING.md SECURITY.md CHANGELOG.md src
python3 tools/check_repository.py
git diff --cached --stat
git commit -m 'docs: initialize research repository'
REPO_URL="https://github.com/USERNAME/XBvPC.git"
git remote add origin "$REPO_URL"
# Solo quando sei certo del contenuto: git push -u origin main
```

Se il repository ha già un README o una cronologia, **non eseguire `git init` né sovrascrivere**: integra sul clone, lavora su branch e usa una pull request. Verifica il remote con `git remote -v` prima di operare.

## 5. Impostazioni consigliate sul sito GitHub

- About: `Experimental x86-64 / PE32+ compatibility research lab — synthetic fixtures only; not a working Xbox emulator`.
- Topics: `cpp`, `x86-64`, `pe32`, `emulation-research`, `wsl`, `systems-programming`.
- Attiva Issues / Discussions se vuoi accogliere contributi.
- Imposta protezioni su `main`: pull request obbligatorie, controlli CI e nessun push forzato.
- Evita la creazione di Release eseguibili finché non esiste una build pubblica riproducibile e chiaramente licenziata.

## 6. Quando aggiungere i sorgenti veri

Creare un sottoinsieme autonomo in `src/`, dopo una revisione file per file; rimuovere percorsi assoluti e include verso cartelle private. Aggiungere `CMakeLists.txt`, test automatici reali, fixture riproducibili (sorgenti, non binari), istruzioni verificate da un clone pulito e CI con GCC/Clang. Non dichiarare verde la compilazione C++ finché quella job non è presente.

## Nome del repository

Il nome pubblico scelto è **XBvPC**; il repository GitHub dovrebbe chiamarsi `XBvPC`. Non cambiare i nomi tecnici dei file C++, gli identificativi dei gate, i percorsi WSL e gli SHA-256 storici: servono alla tracciabilità delle verifiche già eseguite. La rinomina pubblica non modifica automaticamente una repository GitHub esistente.
