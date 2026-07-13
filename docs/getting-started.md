# Aan de slag

Deze documentatie bundelt de kerninformatie van de oorspronkelijke Confluence-homepage van de HyDAMO Validatietool in een MkDocs-omgeving die beter aansluit op deze repository.

## Waarvoor gebruik je de validatietool?

De HyDAMO Validatietool helpt bij het verbeteren van de kwaliteit van HyDAMO-brondata binnen een cyclisch modelleerproces. Nieuwe inzichten uit analyses en modelruns kunnen worden terugvertaald naar de brondata, waarna datasets opnieuw gevalideerd en verwerkt kunnen worden.

De tool is ontworpen om op meerdere plekken in het proces inzetbaar te zijn, waaronder:

- bij waterschappen;
- bij het GKW (Gegevensknooppunt Waterschappen);
- bij het NHI.

## Voorwaarden voordat je start

Voordat je een dataset valideert, moet die voldoen aan het DAMO 2.2-datamodel. In de oorspronkelijke documentatie wordt daarvoor expliciet verwezen naar de HyDAMO Wasmachine.

Gebruik de HyDAMO Wasmachine om:

- het verplichte attribuut `NEN3610id` toe te voegen;
- domeinwaarden om te zetten naar omschrijvingen;
- het resultaat weg te schrijven in het juiste GeoPackage-formaat.

Meer context en downloads staan op [HyDAMO Wasmachine](wasmachine.md).

## Onderdelen van de oplossing

De HyDAMO Validatietool bestaat volgens de bronpagina uit drie hoofdcomponenten:

### Validatiemodule

Een Python-validatiemodule die een of meer datasets toetst aan een set validatieregels.

### Validatie-API

De API maakt het mogelijk om:

1. validatietaken te definieren;
2. databestanden en validatieregels aan een taak toe te voegen;
3. een validatietaak te starten;
4. het validatieresultaat te downloaden.

### Webclient

De webclient biedt een grafische interface voor de API en ondersteunt eenvoudige analyses van validatieresultaten.

## Belangrijke verwijzingen

!!! info "Bekende issues en versies"
    De oorspronkelijke Confluence-homepage meldde een nieuwe versie 1.4 van de validatiemodule en verwees daarnaast naar een pagina met bekende issues. In deze repository zijn validatieregelbestanden aanwezig tot en met versie 1.5. Controleer operationele aandachtspunten nog steeds via de oorspronkelijke bronpagina's.

- Oorspronkelijke homepage: [HyDAMO Validatietool op Confluence](https://hkvconfluence.atlassian.net/wiki/spaces/VAL/overview?homepageId=1984462869)
- Validatietool: [validatietool.hydamo.nl](https://validatietool.hydamo.nl/)
- Gebruikersregistratie: [Gebruikersregistratie](02%20Gebruikersregistratie.md)
- Bekende problemen: [Known issues en tips](03%20Known%20issues%20en%20tips.md)
- Actuele softwareversies: [Versie overzicht](04%20Versie%20overzicht.md)
- Repository-overzicht van bestanden: [Bestanden en versies](resources.md)
- Guide voor aanpassen van regels: [Validatieregels bewerken](guides/edit_rules.md)

## Contact

Voor vragen of opmerkingen over de oorspronkelijke wiki vermeldt de bronpagina dit adres:

`helpdesk-hydamo-validatietool@hkv.nl`
