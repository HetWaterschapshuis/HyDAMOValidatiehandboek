# HyDAMO-validatiemodule

De HyDAMO-validatiemodule is het rekenhart van de HyDAMO validatietool. De module valideert een dataset, aangeleverd als GeoPackage, conform het HyDAMO-datamodel en de bijbehorende [validatieregels](../Introductie%20tool/02%20Validatieregels.md). Een volledige validatie bestaat uit syntaxvalidatie, logische validatie en topologische validatie.

Binnen de validatiecloudservice wordt de module aangestuurd via de API, maar de module kan ook zelfstandig als Python-module worden uitgevoerd. De broncode is open source beschikbaar op [GitHub](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule){:target="_blank"}. Elke release wordt gepubliceerd als [Python-package](https://pypi.org/project/hydamo-validation){:target="_blank"}.

Deze pagina beschrijft het lokaal installeren en uitvoeren van een validatie met de validatiemodule:

1. **Installatie:** een Python-omgeving opzetten en de validatiemodule installeren.
2. **Invoergegevens:** datasets en validatieregels klaarzetten.
3. **Commandline:** validaties uitvoeren zonder tussenkomst van de API of webclient.
4. **Python:** de validatiemodule aanroepen vanuit eigen Python-code.
5. **Validatieresultaten:** de uitvoerbestanden bekijken en interpreteren.

## 1. Installatie van de validatiemodule

Voor lokaal gebruik installeren we de HyDAMO-validatiemodule in een virtuele Python-omgeving met [uv](https://docs.astral.sh/uv/){:target="_blank"} met vastgepinde versies van ondersteunende Python-packages.

### Python-omgeving aanmaken

Installeer zo nodig [uv](https://docs.astral.sh/uv/getting-started/installation/){:target="_blank"} en open een opdrachtprompt (cmd) of PowerShell in de gewenste werkmap.

Maak een virtuele Python-omgeving aan:

```console
uv venv --python 3.12
```

Uv kan de benodigde Python-versie automatisch downloaden wanneer deze nog niet beschikbaar is. De ondersteunde Python-versie staat in het [projectdefinitiebestand](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule/blob/main/pyproject.toml){:target="_blank"}.

Activeer de omgeving in de opdrachtprompt:

```console
.venv\Scripts\activate
```

### Validatiemodule installeren

Download [requirements.lock](https://raw.githubusercontent.com/HetWaterschapshuis/HyDAMOValidatieModule/main/requirements.lock){:target="_blank"} en sla het bestand op in de werkmap.

Installeer de vastgepinde package-versies uit `requirements.lock` en vervolgens de validatiemodule:

```console
uv pip sync requirements.lock
uv pip install --no-deps hydamo-validation
```

Controleer de installatie:

```console
uv pip show hydamo-validation
```

De validatiemodule is nu klaar voor gebruik.

### Ontwikkelaarsinstallatie

Wil je de broncode aanpassen, tests draaien of bijdragen aan de ontwikkeling? Clone dan de [GitHub-repository](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule){:target="_blank"} en gebruik `requirements-dev.lock` voor de ontwikkelomgeving. Zie de [ontwikkelaarsdocumentatie](https://hetwaterschapshuis.github.io/HyDAMOValidatieModule/){:target="_blank"} voor meer informatie.

## 2. Invoergegevens voorbereiden

Voor een validatie zijn minimaal één GeoPackage met HyDAMO-gegevens en een JSON-bestand met validatieregels nodig. Deze mag op een willekeurige locatie staan, we gaan voor de rest van dit voorbeeld uit van `D:\validatiemap`. Maak deze aan in de volgende structuur

```text
validatiemap/
├── datasets/
│   └── hydamo.gpkg
└── validationrules.json
```

De map `datasets` bevat één of meer GeoPackages met HyDAMO-objectlagen. Het bestand `validationrules.json` bevat de uit te voeren validatieregels en de te gebruiken versie van het HyDAMO-datamodel.

Voor een eerste validatie kun je de [testdataset](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule/tree/main/tests/data/tasks/test_wrij){:target="_blank"} uit de GitHub-repository gebruiken. Neem zowel de map `datasets` als het bestand `ValidationRules.json` over.

Sommige validatieregels gebruiken externe rastergegevens, zoals AHN-hoogtemodellen. Deze gegevens moeten afzonderlijk beschikbaar zijn en kunnen bij de uitvoering worden opgegeven via de optie `coverages`.

## 3. Validatie uitvoeren via de commandline

Activeer de Python-omgeving en voer de validatie uit met:

```console
python -m hydamo_validation D:\validatiemap
```

Geef hierbij het pad op naar de projectmap met de map `datasets` en het bestand `validationrules.json`.

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
| `--coverages` | Locatie van externe rastergegevens, opgegeven als `NAAM=PAD`, bijvoorbeeld voor AHN. |
| `--raise-error` | Geeft Python-exceptions direct door, bijvoorbeeld voor foutopsporing. |

Voorbeeld met meerdere uitvoerformaten en uitgebreide logging:

```console
python -m hydamo_validation D:\validatiemap --output-types geopackage csv geojson --log-level DEBUG
```

Voorbeeld met een lokaal AHN-hoogtemodel:

```console
python -m hydamo_validation D:\validatiemap --coverages AHN=D:\data\ahn
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
)

# Voer de validatie uit
datamodel, layer_summary, result_summary = run_validation(
    directory=Path(r"D:\validatiemap"),
    raise_error=True,
)
```

De functie geeft drie objecten terug:

- `datamodel`: het ingelezen HyDAMO-datamodel met de gevalideerde gegevens.
- `layer_summary`: de validatieresultaten per objectlaag.
- `result_summary`: de samenvatting van de validatie, inclusief status en eventuele fouten.

Via de parameters `output_types`, `log_level` en `coverages` kun je de validator op dezelfde manier configureren als via de commandline.

Voor het gebruik van externe rastergegevens kun je bijvoorbeeld meegeven:

```python
run_validation = validator(
    output_types=["geopackage", "csv"],
    log_level="INFO",
    coverages={"AHN": Path(r"D:\data\ahn")},
)
```

## 5. Validatieresultaten

De validatiemodule maakt in de opgegeven projectmap automatisch een map `results` aan. Bij de standaardinstellingen bevat deze onder andere:

```text
project_map/
└── results/
    ├── results.gpkg
    ├── validation_result.json
    └── validator.log
```

De bestanden bevatten:

- **results.gpkg**: de resultaten per objectlaag, inclusief de beoordelingen van de uitgevoerde validatieregels.
- **validation_result.json**: een samenvatting van de validatie, inclusief status, uitgevoerde controles en eventuele fouten.
- **validator.log**: het logbestand met de voortgang en meldingen tijdens de validatie.

Bij gebruik van `--output-types` kunnen de resultaten ook als CSV of GeoJSON worden weggeschreven.

**Let op:** bij een nieuwe validatie wordt de bestaande map `results` verwijderd en opnieuw aangemaakt. Bewaar eerdere resultaten daarom buiten deze map als je ze wilt behouden.

Voor meer informatie over de betekenis van de validatieresultaten en de individuele controles, zie [Validatieregels](../Introductie%20tool/02%20Validatieregels.md).
