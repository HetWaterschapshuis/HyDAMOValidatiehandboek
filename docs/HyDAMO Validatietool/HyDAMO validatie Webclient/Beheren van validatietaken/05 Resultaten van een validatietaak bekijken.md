# Resultaten van een validatietaak bekijken

Als de status van een validatietaak gelijk is ‘finished' of ‘error’ is het uitvoeren van de validatietaak (zie ook [Een validatietaak starten](04%20Een%20validatietaak%20starten.md)) gereed. Bekijk in beide gevallen eerst de metadata van de validatie-taak. Klik op icoon <img src="..\..\..\images\e4cfed32-dfad-43df-b6a7-921a68cc593f.png"/> in de rij van de betreffende validatietaak (in de kolom 'Acties’). Er verschijnt een popup venster met daarin informatie over de validatietaak.

<img src="..\..\..\images\d79b2148-e544-42ee-ab2d-648d8c099394.png"/>

De volgende informatie wordt in de metadata getoond (van boven naar beneden):

- task\_id: de id van de validatietaak waarvoor metadata is opgevraagd.
- api-version: de versie van de HyDAMO Validatietool API die is/wordt gebruikt.
- user\_name: je eigen gebruikersnaam.
- task\_started; datum en tijd waarop de validatietaak is gestart.
- task\_finished: datum en tijd waarop de validatietaak is geëindigd.
- success: indicator of de validatietaak succesvol is uitgevoerd ('true') of niet ('false').
- module\_version: de versie van de HyDAMO Validatiemodule die is gebruikt.
- duration: de tijd de nodig was om de validatietaak (en dus de validatie) uit te voeren.
- status: de status van de validatietaak.
- dataset\_layers: een overzicht van de objectlagen dat aanwezig was in de dataset bestanden die aan de validatietaak zijn toegevoegd (objectlagen gescheiden met een puntkomma).
- result\_layers: het aantal objectlagen dat aanwezig was in de dataset bestanden en waarvoor een validatie resultaat is bepaald (objectlagen gescheiden met een puntkomma). Hiervan kunnen de resultaten gedownload worden.
- missing layers: het aantal objectlagen dat onderdeel is van het DAMO datamodel, maar niet aanwezig waren in de dataset bestanden die aan de validatietaak zijn toegevoegd (objectlagen gescheiden met een puntkomma).
- error\_layers: het aantal objectlagen dat aanwezig was in de dataset bestanden, maar die niet gevalideerd konden worden (objectlagen gescheiden met een puntkomma).
- syntax\_result: het aantal objectlagen dat aanwezig was in de dataset bestanden en waarvoor een syntax validatie resultaat beschikbaar is (objectlagen gescheiden met een puntkomma).
- validation\_result: het aantal objectlagen dat aanwezig was in de dataset bestanden en waarvoor een (topo)logisch validatie resultaat beschikbaar is (objectlagen gescheiden met een puntkomma).
- error: een foutmelding als de validatietaak niet uitgevoerd kon worden.
- warnings: waarschuwingen die tijdens de validatie zijn opgetreden.
- log: een volledige log van de verschillende stappen van de HyDAMO Validatiemodule tijdens de uitvoering van de validatietaak.

Als een validatietaak succesvol is uitgevoerd kan het validatie resultaat bekeken worden op een kaart (zie [Bekijken van validatie resultaten op een kaart](..\04%20Bekijken%20van%20validatie%20resultaten%20op%20een%20kaart.md)) of in tabel (zie [Bekijken van validatie resultaten in tabel](..\05%20Bekijken%20van%20validatie%20resultaten%20in%20tabel.md)). Ook kunnen de resultaten direct worden gedownload door de knop <img src="..\..\..\images\92c420f0-e246-4470-a930-62e7b3d10353.png"/> in de kolom 'Acties' te activeren. Er wordt een zip-bestand (naam gelijk aan de id en naam van de validatietaak, gescheiden door een streepje) gedownload met daarin de volgende bestanden:

- validator.log met de volledige inhoud van de log van de verschillende stappen van de HyDAMO Validatiemodule tijdens de uitvoering van de validatietaak.
- valiation\_result.json met de volledige inhoud van de metadata van de validatietaak (zoals hierboven beschreven en afgebeeld in het screenshot van de metadata).
- results.gpkg met alle validatie resultaten voor alle objectlagen in Geopackage formaat.
- submap 'geosjon' met daarin voor elke objectlaag een geojson met de validatie resultaten van de betreffende objectlaag.
