# HyDAMO-validatiemodule

De HyDAMO-validatiemodule is het rekenhart van de HyDAMO-validatietool. De module valideert een dataset, aangeleverd als GeoPackage, conform het HyDAMO-datamodel en de bijbehorende [validatieregels](../Introductie%20tool/02%20Validatieregels.md). Een volledige validatie bestaat uit syntaxvalidatie, logische validatie en topologische validatie.

Binnen de validatiecloudservice wordt de module aangestuurd via de API, maar de module kan ook zelfstandig als Python-module worden uitgevoerd. De broncode is open source beschikbaar op [GitHub](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule){:target="_blank"}. De validatiemodule is ook beschikbaar als [Python-package](https://pypi.org/project/hydamo-validation){:target="_blank"}.

Deze pagina beschrijft het lokaal installeren en uitvoeren van een validatie met de validatiemodule binnen een Python-omgeving:

1. **Installatie:** een Python-omgeving opzetten en de validatiemodule installeren.
2. **Invoergegevens:** datasets en validatieregels klaarzetten.
3. **Commandline:** validaties uitvoeren zonder tussenkomst van de API of webclient.
4. **Python:** de validatiemodule aanroepen vanuit eigen Python-code.
5. **Validatieresultaten:** de uitvoerbestanden bekijken en interpreteren.

## 1. Installatie van de validatiemodule

Voor lokaal gebruik installeren we de HyDAMO-validatiemodule in een virtuele Python-omgeving met [uv](https://docs.astral.sh/uv/){:target="_blank"}, met vastgepinde versies van de ondersteunende Python-packages. In dit voorbeeld gebruiken we versie `1.6.0` van de validatiemodule.

### Python-omgeving aanmaken

Installeer zo nodig [uv](https://docs.astral.sh/uv/getting-started/installation/){:target="_blank"} en open een opdrachtprompt (cmd) of PowerShell in de gewenste werkmap.

Maak een virtuele Python-omgeving aan:

```console
uv venv --python 3.12
```

Uv kan de benodigde Python-versie automatisch downloaden wanneer deze nog niet beschikbaar is. De ondersteunde Python-versie staat in het [projectdefinitiebestand](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule/blob/v1.6.0/pyproject.toml){:target="_blank"}.

Activeer de omgeving in de opdrachtprompt (cmd):

```console
.venv\Scripts\activate.bat
```

Of in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Als PowerShell het uitvoeren van scripts blokkeert, kun je ook zonder activatie werken door de Python-interpreter rechtstreeks aan te roepen, bijvoorbeeld met `.venv\Scripts\python.exe`.

### Validatiemodule installeren

Download [requirements.lock](https://raw.githubusercontent.com/HetWaterschapshuis/HyDAMOValidatieModule/v1.6.0/requirements.lock) van release `v1.6.0` en sla het bestand op in de werkmap.

Installeer de vastgepinde packageversies uit `requirements.lock` en vervolgens de bijbehorende versie van de validatiemodule:

```console
uv pip sync requirements.lock
uv pip install --no-deps hydamo-validation==1.6.0
```

Controleer de installatie:

```console
uv pip show hydamo-validation
```

De validatiemodule is nu klaar voor gebruik.

### Ontwikkelaarsinstallatie

Wil je de broncode aanpassen, tests draaien of bijdragen aan de ontwikkeling? Clone dan de [GitHub-repository](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule){:target="_blank"} en gebruik `requirements-dev.lock` voor de ontwikkelomgeving. Zie de [ontwikkelaarsdocumentatie](https://hetwaterschapshuis.github.io/HyDAMOValidatieModule/){:target="_blank"} voor meer informatie.

## 2. Invoergegevens voorbereiden

Voor een validatie zijn minimaal één GeoPackage met HyDAMO-gegevens en een JSON-bestand met validatieregels nodig. De gegevens mogen op een willekeurige locatie staan. In dit voorbeeld gebruiken we `D:\validatiemap`, met de volgende structuur:

```text
validatiemap/
├── datasets/
│   └── hydamo.gpkg
└── validationrules.json
```

De map `datasets` bevat één of meer GeoPackages met HyDAMO-objectlagen. Het bestand `validationrules.json` bevat de uit te voeren validatieregels en de te gebruiken versie van het HyDAMO-datamodel.

### Voorbeeldgegevens

Voor een eerste validatie gebruiken we de [WRIJ-testdataset](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule/tree/v1.6.0/tests/data/tasks/test_wrij){:target="_blank"} uit de GitHub-repository. Deze bevat zowel een GeoPackage als bijbehorende validatieregels.

De dataset gebruikt ook AHN-hoogtemodellen voor een aantal validatieregels. Deze zijn beschikbaar in de [AHN-testgegevens](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule/tree/v1.6.0/tests/data/dtm){:target="_blank"}.

Download de bestanden uit beide mappen. Je kunt hiervoor ook de [broncode van release v1.6.0](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule/archive/refs/tags/v1.6.0.zip){:target="_blank"} als ZIP downloaden en de benodigde bestanden daaruit kopiëren.

Plaats de validatieset in `D:\validatiemap` en de AHN-hoogtemodellen afzonderlijk in `D:\data\ahn`:

```text
D:\validatiemap\
├── datasets\
│   └── HyDAMO.gpkg
└── validationrules.json

d:\data\ahn\
├── 34HN1_CM.tif
├── 34HN2_CM.tif
├── 41EN1_CM.tif
├── 41EN2_CM.tif
├── 41EZ1_CM.tif
├── 41EZ2_CM.tif
├── index.dbf
├── index.prj
├── index.shp
└── index.shx
```

Neem alle AHN-bestanden over, inclusief de indexbestanden. Deze zijn nodig om de AHN-bestanden correct te gebruiken. De coverages hoeven niet in dezelfde map te staan als de validatieset, je kunt immers meerdere sets valideren aan dezelfde AHN coverage.

## 3. Validatie uitvoeren via de commandline

Activeer de Python-omgeving en voer de validatie uit met:

```console
python -m hydamo_validation D:\validatiemap --coverages AHN=D:\data\ahn
```

Hierbij geven we de projectmap met de GeoPackage en validatieregels op, en met `--coverages` afzonderlijk de locatie van de AHN-hoogtemodellen.

De module doorloopt achtereenvolgens:

1. Initialisatie en inlezen van gegevens
2. Vaststellen van het HyDAMO-datamodel
3. Syntaxvalidatie
4. Logische en topologische validatie
5. Samenvatten en exporteren van resultaten

De voortgang wordt in de opdrachtprompt getoond.

### Aanvullende opties

Met onderstaande argumenten kun je de uitvoering aanpassen:

| Argument | Beschrijving |
| --- | --- |
| `--log-level` | Logniveau `INFO` (standaard) of `DEBUG` voor uitgebreidere logging. |
| `--output-types` | Uitvoerformaten: `geopackage` (standaard), `csv` en `geojson`. Meerdere formaten zijn mogelijk. |
| `--coverages` | Locatie van externe rastergegevens, opgegeven als `NAAM=PAD`. Deze mag buiten de projectmap staan, zoals `AHN=D:\data\ahn`. |
| `--raise-error` | Geeft Python-exceptions direct door, bijvoorbeeld voor foutopsporing. |

Voorbeeld met meerdere uitvoerformaten en uitgebreide logging:

```console
python -m hydamo_validation D:\validatiemap --coverages AHN=D:\data\ahn --output-types geopackage csv geojson --log-level DEBUG
```

Met `--help` krijg je een overzicht van alle argumenten:

```console
python -m hydamo_validation --help
```

## 4. Validatie uitvoeren vanuit Python

De validatiemodule kan ook rechtstreeks vanuit Python worden aangeroepen, bijvoorbeeld vanuit een eigen script of Jupyter Notebook.

Onderstaand voorbeeld voert dezelfde validatie uit als de commandline:

```python
from pathlib import Path
from hydamo_validation import validator

# Configureer de validator
run_validation = validator(
    output_types=["geopackage"],
    log_level="INFO",
    coverages={"AHN": Path(r"D:\data\ahn")},
)

# Voer de validatie uit
datamodel, layer_summary, result_summary = run_validation(
    directory=Path(r"D:\validatiemap"),
    raise_error=True,
)
```

De functie geeft bij een geslaagde uitvoering drie objecten terug:

- `datamodel`: het ingelezen HyDAMO-datamodel met de gevalideerde gegevens.
- `layer_summary`: de validatieresultaten per objectlaag.
- `result_summary`: de samenvatting van de validatie, inclusief status en eventuele fouten.

Via de parameters `output_types`, `log_level` en `coverages` kun je de validator op dezelfde manier configureren als via de commandline.

Bij `raise_error=True` wordt een Python-exception direct doorgegeven wanneer tijdens de uitvoering een technische fout optreedt.

## 5. Validatieresultaten

De validatiemodule maakt in de opgegeven projectmap automatisch een map `results` aan. Bij de standaardinstellingen bevat deze onder andere:

```text
validatiemap\
├── datasets\
│   └── HyDAMO.gpkg
├── validationrules.json
└── results\
    ├── results.gpkg
    ├── validation_result.json
    └── validator.log
```

De bestanden bevatten:

- **results.gpkg**: de resultaten per objectlaag, inclusief de beoordelingen van de uitgevoerde validatieregels.
- **validation_result.json**: een samenvatting van de validatie, inclusief status, uitgevoerde controles en eventuele fouten.
- **validator.log**: het logbestand met de voortgang en meldingen tijdens de validatie.

Bij gebruik van `--output-types` kunnen de resultaten ook als CSV of GeoJSON worden weggeschreven.

### Controleren van de resultaten

Controleer na afloop of de validatie volledig is uitgevoerd. Bekijk hiervoor de status en eventuele foutmeldingen in `validation_result.json` en `validator.log`.

Let op het onderscheid tussen:

- **Validatiefouten:** gegevens die niet voldoen aan de HyDAMO-validatieregels.
- **Technische fouten:** validatieregels die niet konden worden uitgevoerd, bijvoorbeeld door ontbrekende rastergegevens.

In versie 1.6.0 kunnen technische fouten voorkomen terwijl `validation_result.json` toch `success: true` en `status: "finished"` vermeldt. Controleer daarom ook de foutmeldingen in `error` of `errors` en het logbestand. De aanwezigheid van uitvoerbestanden betekent niet automatisch dat alle validatieregels zijn uitgevoerd.

**Let op:** bij een nieuwe validatie wordt de bestaande map `results` verwijderd en opnieuw aangemaakt. Bewaar eerdere resultaten daarom buiten deze map als je ze wilt behouden.

Voor meer informatie over de betekenis van de validatieresultaten en de individuele controles, zie [Validatieregels](../Introductie%20tool/02%20Validatieregels.md).
