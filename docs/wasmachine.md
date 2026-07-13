# HyDAMO Wasmachine

Volgens de oorspronkelijke documentatie moet een dataset eerst voldoen aan het DAMO 2.2-datamodel voordat validatie zinvol is. De HyDAMO Wasmachine is het hulpmiddel dat daarbij ondersteunt.

## Functie van de wasmachine

De HyDAMO Wasmachine helpt om datasets voor te bereiden door:

- het verplichte attribuut `NEN3610id` toe te voegen;
- domeinen om te zetten naar omschrijvingen;
- uitvoer weg te schrijven in het juiste GeoPackage-formaat.

Daarmee vormt de wasmachine een logische stap voorafgaand aan het uitvoeren van de validatiemodule.

## Bestanden in deze repository

De volgende gerelateerde bestanden zijn als download opgenomen in deze documentatiesite:

- [DamoMapping 2.2-2.2.xlsx](downloads/DamoMapping%202.2-2.2.xlsx)
- [HyDAMOWasmachine.pptx](downloads/HyDAMOWasmachine.pptx)
- [wasmachineHyDAMO.fmw](downloads/wasmachineHyDAMO.fmw)

## Wanneer gebruik je dit?

Gebruik de wasmachine wanneer:

- je brondata nog niet volledig in lijn is met DAMO 2.2;
- verplichte identifiers ontbreken;
- domeinwaarden eerst vertaald moeten worden;
- je een schoon GeoPackage wilt opleveren voor validatie.

## Relatie met de validatietool

Na de voorbewerking met de wasmachine kun je de dataset laten toetsen met de validatieregels en bijbehorende schema's uit deze repository. Zie daarvoor [Bestanden en versies](resources.md).
