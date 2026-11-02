---
hide:
- toc
---

# De tool in een oogopslag

## Wat is de HyDAMO Validatietool?

De HyDAMO Validatietool is in de basis een (online) webservice (validation as a service) waarmee hydrologische datasets in geopackage-formaat gevalideerd kunnen worden. De tool valideerd de datasets aan de hand van de opgegeven validatieregels en HyDAMO-datamodel. 

De tool is opgebouwd uit drie componentlagen:

<div class="component-list" markdown="1">

<div class="component" markdown="1">
<div class="component-icon" markdown="1">
:material-monitor-screenshot:
</div>

<div class="component-text" markdown="1">
**Validatie-Webclient**

 De [Validatie-Webclient](../../Aan%20de%20slag/02%20De%20Webclient) is de visuele schil van de Validatietool en geeft de gebruiker de mogelijkheid om het validatieproces graphisch te besturen. Onder de motorkap wordt hiermee de validatie-API aangestuurd. Daarnaast geeft de Webclient de mogelijkheid om invoerbestanden en rekenresultaten op de kaart of als tabel te bekijken. Om van de Webclient gebruik te kunnen maken is het nodig om een [gebruikersaccount](../../Aan%20de%20slag/01%20Gebruikersregistratie) te hebben.
</div>
</div>


<div class="component" markdown="1">
<div class="component-icon" markdown="1">
:material-api: 
</div>

<div class="component-text" markdown="1">
**Validatie-API**

De [Validatie-API](../../Aan%20de%20slag/03%20De%20API) is de centrale schakel tussen webclient en rekenmodule. Net als met de Webclient kan je door verzoeken aan de API te sturen validatietaken aanmaken, datasets en validatieregels toevoegen, een taak starten en de resultaten downloaden. De API geeft de rekentaken door en zet de rekenmodule in gang. Om van de API gebruik te kunnen maken is een [gebruikersaccount](../../Aan%20de%20slag/01%20Gebruikersregistratie) nodig.
</div>
</div>


<div class="component" markdown="1">
<div class="component-icon" markdown="1">
:simple-python:
</div>

<div class="component-text" markdown="1">
**Validatiemodule**

 De [Validatiemodule](../../Aan%20de%20slag/04%20De%20Validatiemodule) is de binnenste schil en voert de daadwerkelijke validatie van de datasets door. Hij is geschreven in Python en beschikaar als [openbare repository](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule){:target="_blank"} en standalone [Python package](https://pypi.org/project/hydamo-validation/){:target="_blank"}. Ontwikkelaars kunnen de code downloden en in een hiervoor opgezette ontwikkelomgeving lokaal runnen. 
</div>
</div>

</div>


## Essentiele onderdelen van een validatie

Verdere kernelementen van het validatieproces zijn:

<div class="component-grid-2frames" markdown="1">
<div class="component-mini" markdown="1">
<div class="component-mini-icon" markdown="1">
:fontawesome-solid-book-reader:
</div>

<div class="component-mini-text" markdown="1">
**Handboek**

[Handboek](https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek){:target="_blank"} Het handboek is een openbare GitHub-repository waarvan deze handleiding onderdeel uitmaakt. Dit is de centrale opslagplaats voor relevante documentatie, referentiebestanden en voorbeelddatasets. Onder andere bevinden zich hier de officiele [Validatieregelsets](https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek/tree/main/validation_rules){:target="_blank"}, de [HyDAMO-datamodelschema's](https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek/tree/main/validation_schemas/datamodellen_hydamo){:target="_blank"} en de [HyDAMO-wasmachine](https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek/tree/main/hydamo_wasmachine){:target="_blank"}.
</div>
</div>

<div class="component-mini" markdown="1">
<div class="component-mini-icon" markdown="1">
:material-format-list-checks: 
</div>

<div class="component-mini-text" markdown="1">
**Validatieregels**

Bij een validatie horen altijd [validatieregels](../../Introductie%20tool/02%20Validatieregels) die aangeven op welke aspecten gecontroleerd moet worden. De regels worden in een apart JSON-bestand meegegeven en zijn beschikbaar op de openbare [GitHub-repository](https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek/tree/main/validation_rules){:target="_blank"} van het handboek.
</div>
</div>

<div class="component-mini" markdown="1">
<div class="component-mini-icon" markdown="1">
:material-washing-machine:
</div>

<div class="component-mini-text" markdown="1">
**HyDAMO-wasmachine**

[HyDAMO-wasmachine](https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek/tree/main/hydamo_wasmachine){:target="_blank"}: De Validatie-tooling wil gegevens conform een vooraf afgesproken formaat. Het is bepaald dat de invoerdatasets als GeoPackage worden aangeboden, objecten het veld NEN3610ID moeten bevatten en getal-domeinen als omschrijving zijn omgezet. De HyDAMO-wasmachine is een FME-gebaseerde GUI die DAMO-objecten converteerd naar het benodigde formaat. 
</div>
</div>

<div class="component-mini" markdown="1">
<div class="component-mini-icon" markdown="1">
:fontawesome-solid-chart-diagram:
</div>

<div class="component-mini-text" markdown="1">
**HyDAMO-datamodel**

In de validatieregels staat het [HyDAMO-datamodel](https://github.com/HetWaterschapshuis/HyDAMOValidatiehandboek/tree/main/validation_schemas/datamodellen_hydamo){:target="_blank"} van de gebruike dataset opgegeven onder de parameter 'hydamo_version'. In het HyDAMO-datamodel is vastgelegd welke object(-namen) toegestaan zijn en voor ieder object welke attribuutdefinities erbij horen zoals: veldnaam, datatype, toegestane waarden, min- en max-lengte etc.. De HyDAMO-versies 
volgen de jaarlijkse doorontwikkelingen van de HyDAMO-mappings in [DAMO](https://damo.hetwaterschapshuis.nl){ target="_blank" } . 
</div>
</div>
</div>
