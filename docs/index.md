---
hide:
  - toc
---

<div class="hero">
  <div class="hero__content">
    <p class="hero__eyebrow">HyDAMO Validatietool</p>
    <h1>Documentatie voor validatie, regels en voorbereiding van HyDAMO-data</h1>
    <p class="hero__lead">
      Deze site bundelt de kerninformatie van de oorspronkelijke Confluence-homepage in een compact
      MkDocs-handboek, aangevuld met directe downloads van validatieregels, schema's en
      wasmachinebestanden uit deze repository.
    </p>
    <div class="hero__actions">
      <a class="md-button md-button--primary" href="getting-started/">Aan de slag</a>
      <a class="md-button" href="resources/">Bekijk bestanden</a>
    </div>
  </div>
</div>

!!! info "Belangrijk"
    De publieke Confluence-homepage noemt expliciet een release van versie 1.4 van de validatiemodule en verwijst naar bekende issues. In deze repository zijn validatieregelbestanden aanwezig tot en met versie 1.5.

## Waarom deze validatietool?

Als gevolg van verdere digitalisering spelen data en datakwaliteit een steeds grotere rol in het afwegen en nemen van besluiten. De HyDAMO Validatietool ondersteunt daarom een cyclisch modelleerproces waarin nieuwe inzichten worden gebruikt om brondata te verbeteren, modellen te genereren en bestaande modellen te actualiseren.

De validatietool is bedoeld als schakel in dat proces en draagt bij aan betrouwbaardere invoerbestanden voor modelgeneratoren. De tool is ontworpen om op meerdere plekken in de keten inzetbaar te zijn, waaronder bij waterschappen, het GKW en het NHI.

## Opbouw van de oplossing

<div class="grid cards" markdown>

- **Validatiemodule**

  De Python-validatiemodule voert de daadwerkelijke validatie uit van een of meer datasets aan de hand van een set validatieregels.

- **Validatie-API**

  De API ondersteunt het definieren van validatietaken, het toevoegen van databestanden en regels, het starten van validatie en het downloaden van resultaten.

- **Webclient**

  De webclient biedt een eenvoudige grafische interface voor de API en maakt basisanalyse van validatieresultaten mogelijk.

</div>

## Voor je begint

Voordat je met de HyDAMO Validatietool aan de slag gaat, moet de dataset voldoen aan het DAMO 2.2-datamodel. Daarvoor is de HyDAMO Wasmachine bedoeld.

Met de wasmachine kun je:

- het verplichte attribuut `NEN3610id` toevoegen;
- domeinwaarden omzetten naar omschrijvingen;
- het resultaat wegschrijven in het juiste GeoPackage-formaat.

[Meer over de HyDAMO Wasmachine](wasmachine.md)

## Snel naar de juiste informatie

<div class="grid cards" markdown>

- [**Aan de slag**](getting-started.md)

  Uitleg over doel, gebruik, componenten en de belangrijkste verwijzingen vanuit de oorspronkelijke wiki.

- [**Gebruikersregistratie**](02%20Gebruikersregistratie.md)

  Praktische informatie over toegang en gebruik voor nieuwe gebruikers.

- [**Known issues en tips**](03%20Known%20issues%20en%20tips.md)

  Bekende problemen, workarounds en operationele aandachtspunten.

- [**Versie overzicht**](04%20Versie%20overzicht.md)

  Actuele versies en release notes van module, API en webclient.

- [**Bestanden en versies**](resources.md)

  Directe downloads van validatieregels, JSON-schema's en het overzichtsbestand per versie.

- [**HyDAMO Wasmachine**](wasmachine.md)

  Toelichting op de voorbereidende stap voordat je data laat valideren.

- [**Validatieregels bewerken**](guides/edit_rules.md)

  Praktische handleiding om `ValidationRules`-bestanden met schema-validatie te wijzigen.

- [**Webclient**](06%20HyDAMO%20validatie%20Webclient.md)

  Uitleg over inloggen, taken beheren en resultaten bekijken op kaart en in tabellen.

- [**Validatie-API**](07%20HyDAMO%20validatie-API.md)

  Overzicht van endpoints, validatietaken, datasets, regels en resultaatdownloads.

- [**Validatiemodule**](08%20HyDAMO%20Validatiemodule.md)

  Achtergrond over syntax-, logische en topologische validatie en lokaal gebruik van de module.

</div>

## Oorspronkelijke bronnen

- Confluence-homepage: [HyDAMO Validatietool](https://hkvconfluence.atlassian.net/wiki/spaces/VAL/overview?homepageId=1984462869)
- Publieke applicatie: [validatietool.hydamo.nl](https://validatietool.hydamo.nl/)
- Contactadres uit de bronpagina: `helpdesk-hydamo-validatietool@hkv.nl`

## Context van deze repository

Deze documentatie richt zich op de onderdelen die daadwerkelijk in deze repository aanwezig zijn:

- validatieregels in JSON-formaat;
- schema's voor die regels;
- ondersteunende wasmachinebestanden;
- praktische instructies voor beheer en bewerking van regels.

De tool is ontwikkeld door HKV lijn in water BV, D2Hydro en HydroConsult in opdracht van Het Waterschapshuis.
