# Validatieregels bewerken

In `ValidationRules` definieer je de topologische en logische regels die op HyDAMO-data worden uitgevoerd. Voor het aanpassen van regels heb je steeds twee bestanden nodig:

1. een `ValidationRules_*.json`-bestand met de daadwerkelijke regels;
2. een `rules_*.json`-schema dat de structuur van dat bestand definieert.

Voor de meest recente set in deze repository kun je direct deze bestanden gebruiken:

- [ValidationRules_1.5.json](../downloads/ValidationRules_1.5.json)
- [rules_1.5.json](../downloads/rules_1.5.json)

Dezelfde bestanden voor oudere versies staan op [Bestanden en versies](../resources.md).

## Geschikte editors

Onderstaande werkwijze gebruikt tools die JSON-schema-validatie ondersteunen:

- Altova XMLSpy
- JSON Editor Online

## Altova XMLSpy

Hiervoor heb je een licentie en installatie van [Altova XMLSpy](https://www.altova.com/xmlspy-xml-editor) nodig.

Het voordeel van XMLSpy is de combinatie van een tekstweergave en een rasterweergave, waardoor regels sneller te controleren en aan te passen zijn.

![](images/altova_text.png "Altova Text-view")
![](images/altova_grid.png "Altova Grid-view")

### Schema koppelen

1. Open het gewenste `ValidationRules_*.json`-bestand.
2. Ga naar `Info` -> `JSON`.
3. Kies `Select JSON Schema` en wijs het juiste `rules_*.json`-bestand toe.
4. Bewerk de regels en sla op. XMLSpy controleert daarbij meteen of de JSON nog aan het schema voldoet.

![](images/altova_assign_schema.png "Assign schema")

## JSON Editor Online

Gebruik hiervoor [JSON Editor Online](https://jsoneditoronline.org).

Het voordeel van JSON Editor Online is eenvoud: je kunt snel bestanden openen en het schema toewijzen zonder lokale installatie.

![](images/jsoneditonline_startup.png "JSON Editor Online startup")

### Schema koppelen

1. Open links je `ValidationRules_*.json` via `Open` -> `From disk`.
2. Open rechts het bijbehorende `rules_*.json` via `Open` -> `From disk`.
3. Koppel het schema via `Settings` -> `JSON schema` -> `Document`.
4. Bewerk vervolgens de regels en controleer de validatiemeldingen.

![](images/jsoneditoronline_assign_schema.png "Assign schema")
