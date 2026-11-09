---
hide:
- toc
---

# De tool in een oogopslag

## Wat is de HyDAMO-validatietool?

De HyDAMO-validatietool is een (online) webservice (validation as a service) waarmee hydrologische datasets in GeoPackage-formaat gevalideerd kunnen worden. De tool valideert de datasets aan de hand van het gespecificeerde HyDAMO-datamodel en de opgegeven validatieregels. 

De tool is opgebouwd uit drie componentlagen die in samenhang (via webclient) of afzondelijk kunnen worden aangeroepen:

<div class="component-list" markdown="1">

<div class="component" markdown="1">
<div class="component-icon" markdown="1">
:material-monitor-screenshot:
</div>

<div class="component-text" markdown="1">
**Validatie-webclient**

 De [Validatie-webclient](https://validatietool.hydamo.nl/){:target="_blank"} is de visuele schil van de Validatietool en geeft de gebruiker de mogelijkheid om de API grafisch te besturen. Daarnaast geeft de webclient de mogelijkheid om invoerbestanden en rekenresultaten op de kaart of als tabel te bekijken. Om van de webclient gebruik te kunnen maken is het nodig om een [gebruikersaccount](../Aan%20de%20slag/01%20Gebruikersregistratie.md) te hebben.
</div>
</div>


<div class="component" markdown="1">
<div class="component-icon" markdown="1">
:material-api: 
</div>

<div class="component-text" markdown="1">
**Validatie-API**

Met de [Validatie-API](../Aan%20de%20slag/03%20De%20API.md) kun je validatietaken aanmaken, datasets en validatieregels toevoegen, een taak starten en de resultaten downloaden. De API maakt hiervoor gebruik van de rekenmodule. Om van de API gebruik te kunnen maken is het nodig om een [gebruikersaccount](../Aan%20de%20slag/01%20Gebruikersregistratie.md) te hebben.
</div>
</div>


<div class="component" markdown="1">
<div class="component-icon" markdown="1">
:simple-python:
</div>

<div class="component-text" markdown="1">
**Validatiemodule**

 De [Validatiemodule](../Aan%20de%20slag/04%20De%20Validatiemodule.md) is de binnenste schil en voert de daadwerkelijke validatie van de datasets door. Hij is ontwikkeld in Python en beschikbaar als [openbare repository](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule){:target="_blank"} en standalone [Python-package](https://project/hydamo-validation/){:target="_blank"}.
</div>
</div>

</div>


## Essentiële onderdelen van een validatie

Verdere kernelementen in het validatieproces zijn:

<div class="component-grid-2frames" markdown="1">
<div class="component-mini" markdown="1">
<div class="component-mini-icon" markdown="1">
:fontawesome-solid-book-reader:
</div>

<div class="component-mini-text" markdown="1">
**Handboek**

[Handboek](https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek){:target="_blank"} Het handboek is een openbare GitHub-repository waarvan dit handboek onderdeel uitmaakt. Dit is de centrale opslagplaats voor relevante documentatie, referentiebestanden en voorbeelddatasets. Onder andere bevinden zich hier de officiële [Validatieregelsets](https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek/tree/main/validation_rules){:target="_blank"}, de [HyDAMO-datamodelschema's](https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek/tree/main/validation_schemas/datamodellen_hydamo){:target="_blank"} en de [HyDAMO-wasmachine](https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek/tree/main/hydamo_wasmachine){:target="_blank"}.
</div>
</div>

<div class="component-mini" markdown="1">
<div class="component-mini-icon" markdown="1">
:material-format-list-checks: 
</div>

<div class="component-mini-text" markdown="1">
**Validatieregels**

Bij een validatie horen altijd [validatieregels](02%20Validatieregels.md) die aangeven op welke aspecten gecontroleerd moet worden. De regels worden in een apart JSON-bestand meegegeven en zijn beschikbaar op de openbare [GitHub-repository](https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek/tree/main/validation_rules){:target="_blank"} van het handboek.
</div>
</div>

<div class="component-mini" markdown="1">
<div class="component-mini-icon" markdown="1">
:material-washing-machine:
</div>

<div class="component-mini-text" markdown="1">
**HyDAMO-wasmachine**

[HyDAMO-wasmachine](https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek/tree/main/hydamo_wasmachine){:target="_blank"}: De validatietooling van HKV wil gegevens conform een vooraf afgesproken formaat. Het is afgesproken dat de invoerdatasets als GeoPackage worden aangeboden, objecten het veld NEN3610ID moeten bevatten en getaldomeinen als omschrijving worden omgezet. De HyDAMO-wasmachine is een FME-gebaseerde GUI die DAMO-objecten omzet naar het benodigde formaat. 
</div>
</div>

<div class="component-mini" markdown="1">
<div class="component-mini-icon" markdown="1">
:fontawesome-solid-chart-diagram:
</div>

<div class="component-mini-text" markdown="1">
**HyDAMO-datamodel**

In de validatieregels moet het [HyDAMO-datamodel](https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek/tree/main/validation_schemas/datamodellen_hydamo){:target="_blank"} van de gebruikte dataset opgegeven worden onder de parameter 'hydamo_version'. In het HyDAMO-datamodel is vastgelegd welke object(-namen) toegestaan zijn en voor ieder object wat de attribuutdefinities zijn zoals: veldnaam, datatype, toegestane waarden, min- en max-lengte etc. De HyDAMO-versies 
volgen de jaarlijkse doorontwikkelingen van de HyDAMO-mappings binnen [DAMO](https://damo.hetwaterschapshuis.nl){ target="_blank" } . 
</div>
</div>
</div>
