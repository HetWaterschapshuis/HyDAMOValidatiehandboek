# HyDAMO Validatietool

![](../images/6a50725b-bb14-42d7-8dda-5217a1d3131b.png)

### Er is een nieuwe versie va de Webclient en van de validatiemodule (met ondersteuning voor (Hy)DAMO 2.5) gelanceerd!

### Bekijk de [Known issues en tips](03%20Known%20issues%20en%20tips.md).

# HyDAMO Validatietool

Op deze Wiki treft u informatie aan over het gebruik van de HyDAMO Validatietool.

Heeft u vragen of opmerkingen over de Wiki, stuur dan een email naar [hydamo-validatietool@hetwaterschapshuis.nl](mailto:hydamo-validatietool@hetwaterschapshuis.nl).

Als gevolg van de digitalisering van processen neemt data een steeds belang­rijkere rol in bij het afwegen en nemen van beslissingen. De toegenomen databehoefte, de groei van de omvang van datasets en de continu veran­derende omgeving, vragen om een cyclisch modelleerproces, waarbij nieuw verkregen inzichten worden gebruikt om brondata te verbeteren. Met deze brondata kunnen modellen gegenereerd worden en/of bestaande modellen worden geactualiseerd. De HyDAMO Validatietool is een belangrijk schakel in dit cyclische modelleerproces en moet leiden tot een betere kwaliteit van de data. Door de HyDAMO Validatietool zo te ontwerpen dat deze op meerdere plekken in het modelleerproces kan worden toegepast (bij waterschappen, bij het GKW (GegevensKnooppunt Waterschappen) en bij het NHI), neemt de betrouwbaarheid en kwaliteit van invoerbestanden voor gebruik in modelgeneratoren toe.

De HyDAMO Validatietool is in de basis een (online) webservice (validation as a service) waarmee databestanden kunnen worden gevalideerd. De HyDAMO Validatietool bestaat uit de volgende componenten:

- Een HyDAMO Validatiemodule (ontwikkeld in Python) die de daadwerkelijke validatie van één of meerdere datasets uitvoert aan de hand van set validatieregels.
- Een HyDAMO validatie-API waarmee:

  - validatietaken kunnen worden gedefinieerd;
  - databestanden en validatieregels kunnen worden toegevoegd aan een validatietaak;
  - een validatietaak kan worden gestart (die dan uitgevoerd wordt door de Python validatiemodule) en;
  - een validatie resultaat kan worden gedownload.
- Een HyDAMO validatie Webclient waarmee een gebruiker beschikt over een eenvoudige gra­fische interface waarmee de (verschillende functies van de) validatie-API bediend kunnen worden en (eenvoudige) analyses van validatieresultaten kunnen worden uitgevoerd.

De HyDAMO Validatietool is ontwikkeld door HKV lijn in water BV, D2Hydro en HydroConsult in opdracht van Het Waterschapshuis.

Voordat u aan de slag gaat met de HyDAMO Validatietool moet uw dataset voldoen aan het DAMO datamodel. Hiertoe heeft Het WaterschapsHuis een extra hulpmiddel ontwikkeld, de HyDAMO Wasmachine. Met de HyDAMO Wasmachine kunt u het verplichte attribuut NEN3610id toevoegen aan uw dataset, worden domeinen omgezet naar omschrijvingen en wordt het resultaat in het correcte Geopackage formaat weggeschreven. De HyDAMO Wasmachine staat hier: [HyDAMO Wasmachine op Github](https://github.com/HetWaterschapshuis/HyDAMOValidatieregels/tree/main/hydamo_wasmachine).

# Inhoud van deze wiki
- [Gebruikersregistratie](02%20Gebruikersregistratie.md)
- [Known issues en tips](03%20Known%20issues%20en%20tips.md)
- [Versie overzicht](04%20Versie%20overzicht.md)
- [Basis validatieregels](05%20Basis%20validatieregels.md)
- [HyDAMO validatie Webclient](06%20HyDAMO%20validatie%20Webclient.md)
- [HyDAMO validatie-API](07%20HyDAMO%20validatie-API.md)
- [HyDAMO Validatiemodule](08%20HyDAMO%20Validatiemodule.md)
- [Mee-ontwikkelen](09%20Mee-ontwikkelen.md)
- [Gebruikersmiddag HyDAMO Validatietool](10%20Gebruikersmiddag%20HyDAMO%20Validatietool.md)
