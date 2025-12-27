# 🎭 Playwright – automatizované testy (Testing Akademie)

Tento repozitář obsahuje ukázkové automatizované testy napsané v Pythonu pomocí **Playwright** a **pytest-playwright** v rámci úkolu z kurzu Testing Akademie.

Testy ověřují základní funkčnost dvou reálných webových stránek:

- https://www.primokulist.cz
- https://vaspraktikpraha.cz

---

## 🛠️ Použité technologie

- Python 3.10+
- pytest
- Playwright
- pytest-playwright (plugin)

---

## ⚙️ Instalace

1. Vytvoření a aktivace virtuálního prostředí:

```bash
python3 -m venv venv    # macOS
source venv/bin/activate   # macOS / Linux
```

2. Instalace závislostí:

```bash
python3 -m pip install pytest playwright pytest-playwright    #macOS
```

3. Instalace prohlížečů:

```bash
python3 -m playwright install    # macOS
```

## Spuštění testů

1. Spuštění všech testů v projektu:

```bash
pytest
```

2. Spuštění konkrétního testovacího souboru:

```bash
pytest tests/test_primokulist.py
pytest tests/test_vaspraktik.py
```

## 🧪 Přehled testů

### tests/test_primokulist.py

- přesměrování na stránku Oční centrum Dejvice
- navigace v hlavním menu (O nás, Objednání)
- validace kontaktního formuláře při chybně vyplněných údajích

### tests/test_vaspraktik.py

- přijetí cookies a skrytí cookies banneru
- navigace mezi jednotlivými ordinacemi
- vyplnění registračního formuláře
- výběr zdravotní pojišťovny
- otevření externího odkazu (Instagram) v nové záložce

## 🌳 Struktura projektu

ENGETO-Playwright/
├── tests/
│ ├── test_primokulist.py
│ └── test_vaspraktik.py
├── .gitignore
├── README.md
└── requirements.txt

## ℹ️ Poznámka

Projekt slouží ke studijním účelům v rámci kurzu Testing Akademie a ukazuje základní práci s Playwrightem, pytestem a pytest-playwright pluginem.
