# HyDAMO validatie-API

De HyDAMO Validatiemodule wordt in een online (reken)omgeving aangeboden. Communicatie met deze online (reken)omgeving gaat via een API (Application Programming Interface). De HyDAMO validatie-API maakt het mogelijk om opdrachten (vanuit een script omgeving zoals Python, Visual Studio Code, maar ook FME) naar de online (reken)omgeving te sturen.

De HyDAMO validatie-API bestaat uit verschillende zogenoemde endpoints. Elke endpoint heeft een url om een actie (request) uit te voeren. Deze requests bestaan uit het opvragen van data (GET request), het toevoegen van data (POST request) en het vewijderen van data (DELETE request).

In de HyDAMO validatie-API hebben we onderscheid gemaakt in:

- Informatie

  - informatie over de API en de Validatiemodule kan opgevraagd worden (GET).
- Validatie-taken

  - een overzicht van validatie-taken kan opgevraagd worden (GET).
  - detail informatie van een specifieke validatie-taak kan opgevraagd worden (GET).
  - een niewe validatie-taak kan aangemaakt worden (POST).
  - een validatie-taak kan verwijderd worden (DELETE).
  - een validatie-taak kan gestart worden (POST).
  - een validatie-taak die uitgevoerd wordt kan geannuleerd worden (POST).
- Datasets

  - een overzicht van alle datasets van een specifiek validatie-taak kan opgevraagd worden (GET).
  - een dataset van een specifieke validatie-taak kan gedownload worden (GET).
  - een nieuwe dataset kan toegevoegd worden aan een specifieke validatie-taak (POST).
  - een dataset kan verwijderd worden uit een specifieke validatie-taak (DELETE).
- Validatieregels

  - een nieuw bestand met validatieregels kan toegevoegd worden aan een specifieke validatie-taak (POST).
  - een bestand met validatieregels van een specifieke validatie-taak kan gedownload worden (GET).
  - validatieregels kunnen verwijderd worden uit een specifieke validatie-taak (DELETE).
- Validatie resultaat

  - Het validatie resultaat kan (in verschillende bestandformaten) worden gedownload (GET).

[API definitie](HyDAMO%20validatie-API\01%20API%20definitie.md) vindt u de OAS3 API specificatie van de HyDAMO Validatie API.

Voordat u aan de slag gaat met de HyDAMO Validatietool moet uw dataset voldoen aan DAMO 2.2 datamodel. Hiertoe heeft Het WaterschapsHuis een extra hulpmiddel ontwikkeld, de HyDAMO Wasmachine. Met de HyDAMO Wasmachine kunt u het verplichte attribuut NEN3610id toevoegen aan uw dataset, worden domeinen omgezet naar omschrijvingen en wordt het resultaat in het correcte Geopackage formaat weggeschreven. De HyDAMO Wasmachine staat hier: [HyDAMO Wasmachine op Github](https://github.com/HetWaterschapshuis/HyDAMOValidatieregels/tree/main/hydamo_wasmachine).

Bekijk [hier](HyDAMO%20validatie-API\01%20API%20definitie.md) de API definitie en [hier](HyDAMO%20validatie-API\02%20Voorbeelden%20gebruik%20API.md) voorbeeld van het gebruik van de API.