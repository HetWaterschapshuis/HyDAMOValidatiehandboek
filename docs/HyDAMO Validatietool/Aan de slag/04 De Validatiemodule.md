# HyDAMO Validatiemodule

De HyDAMO Validatiemodule is als rekenhart het werkpaard van de validatietool. Hij voert - op de achtergrond - de daadwerkelijke validatie van een of meerdere datasets uit aan de hand van het opgegeven HyDAMO-datamodel en set validatieregels. De HyDAMO Validatiemodule voert drie soorten [validaties](TODO hier nog een link plaatsen) uit: de syntaxvalidatie, de logische validatie en de topologische validatie. 

De Validatiemodule is integraal onderdeel van de validatie-cloudservice en wordt als deze door de Webclient of de Validatie-API aangestuurd. Daarnaast is de module ook als los rekenhart beschikbaar op een openbare [GitHub repository](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule){:target="_blank"} of als gepubliceerde [Python-module](https://pypi.org/project/hydamo-validation){:target="_blank"}. Hiermee kan je een validatie ook zonder interface op een lokaal systeem doorvoeren en de validatie-module zelf mee-ontwikklen en delen (zie afsluitende paragraaf).

Hieronder vind je informatie over het lokale gebruik van de validatie module.

## Lokale versie van de HyDAMO Validatiemodule

### De code clonen
1. Kies een plek op je lokale computer om de repository naar toe te kloonen (bijvoorbeeld ‘C:\repos\HyDAMOValidatieModule’). Voer onderstaand bevel uit in Git Bash of gebruik alternatief git-functionaliteit in bijv. Visual Studio Code.
```bash
git clone https://github.com/HetWaterschapshuis/HyDAMOValidatieModule.git
```

### De omgeving opzetten
1. Installeer zo nodig Python van de [officiële site](https://www.python.org/downloads/){:target="_blank"} in de benodigde versie. Inspecteer hiervoor de parameter 'requires-python' in het [projectdefinitie-bestand 'project.toml'](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule/blob/main/pyproject.toml){:target="_blank"}: op GitHub. Kies bijvoorbeeld de C-schrijf als installatielocatie (bijv. 'C:\Python312').
2. Maak een Python-environment aan voor je lokale installatie. Voer in de opdrachtprompt (alternatief powershell) voor het voorbeeld van een lokale repository in ‘C:\repos\HyDAMOValidatieModule’ en Python-installatie in 'C:\Python312' uit:
```console
C:\Python312\python -m venv C:\repos\HyDAMOValidatieModule\.venv
```
3. Activeer het aangemaakte environment in de opdrachtpromt:
```console
C:\repos\HyDAMOValidatieModule\.venv\Scripts\activate
```
4. Update pip (opdrachtpromt met geactiveerd venv):
```console
python -m pip install --upgrade pip
```
5. Installeer de library- en projectmanagement-module 'uv' globaal (opdrachtpromt met geactiveerd venv):
```console
pipx install uv
```
6. Alle libraries installeren die in het requirements-bestand (ontwikkel-versie) zijn vastgelegd (opdrachtpromt met geactiveerd venv):
```console
uv pip sync requirements-dev.lock
```

## De module runnen

Om de module te kunnen runnen is het nodig om tenminste een GeoPackage-invoerdataset en validatieregel-JSON in de juiste mappenstructuur aan te bieden:

```tree
project_map/
├── datasets/
│   └──  <datasetnaam>.gpkg
└── validationrules.json
```
Voor een eerste run kan je bijvoorbeeld een [testdataset](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule/tree/main/tests/data/tasks/test_wrij){:target="_blank"} van de GitHub-repository downloaden en lokaal neerzetten.

Met de opdracht-prompt kan je vervolgens de validatie uitvoeren.

1. Activeer het aangemaakte environment in de opdrachtpromt:
```console
C:\repos\HyDAMOValidatieModule\.venv\Scripts\activate
```
2. Roep de rekenmodule aan in de opdrachtpromt en geef het pad op waarin zich de map 'datasets' bevindt:
```console
(.venv) C:\repos\HyDAMOValidatieModule>python -m hydamo_validation <pad naar directory met daarin 'dataset'-map>
```

De rekenmodule begint vervolgens aan de hand van de standaard-instellingen de validatie en koppelt in de opdrachtpromt de vooruitgang terug. Hij doorlopt grofweg de volgende fases:

1. Voorbereiding en initialisatie
2. Datamodel vaststellen
3. Syntaxvalidatie
4. De inhoudelijke validatie (algemeene, logische, toplogische regels)
5. Samenvatten en exporteren

Aan het einde van het proces maakt de module in de projectmap de map 'results' aan en schrijft standaardmatig de volgende uitvoerbestanden weg: results.gpkg, validatieon_result.json, validator.log.

In plaats van de standaardinstellingen te gebruiken kan je bij de uitvoering een aantal aanvullende argumenten specificeeren:

- **log-level**: je hebt de optie om '--log-level DEBUG' mee te geven om uitgebreidere logging te zien (standaard log-level: INFO).
- **output-types**: geef hier de gewensde uitvoer-formaten mee. Je hebt de keuze uit 'geopackage' (standaard), 'csv' en 'geojson' en alle mogelijke selecties en combinaties. Voorbeeld voor alle formaten: '--output-types geopackage, csv, geojson'.
- **coverages**: geeft hier een directory met lokale hoogtemodel-bestanden mee, standaard wordt geen locatie opgegeven.
- **raise-error**:  geef '--raise-error' mee om bij het optreden van een exception een foutmelding te zien te krijgen. 


## De module mee-ontwikkelen

De validatiemodule is bewust opgezet als opensource software onder MIT licensie. Het is dus zonder meer mogelijk om dieper in de structuur, werkwijze, gebruikte classes en validatiefuncties in te duiken. Hiervoor is het mogelijk om de validator-module in een interactive debug-omgeving zoals Visual Studio Code te verkennen, testen en door te ontwikklen. Bezoek voor meer informatie de [documentatie-pagina](https://hetwaterschapshuis.github.io/HyDAMOValidatieModule/){:target="_blank"} van de bijbehorende GitHub-repository.