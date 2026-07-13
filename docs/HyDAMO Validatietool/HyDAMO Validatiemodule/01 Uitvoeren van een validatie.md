# Uitvoeren van een validatie

Het uitvoeren van een validatie met de Validatiemodule bevat drie stappen:

1. Het aanmaken van input met *datasets* en *validatieregels.* Een voorbeeld van input met datasets en validatieregels vind u op de[GitHub-pagina](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule/tree/main/tests/data/tasks/test_wrij). Deze bevatten:

   - *datasets:* een map met daarin een of meerdere [GeoPackages](https://www.geopackage.org/) met daarin object-lagen (stuw, hydroobject, …) conform het HyDAMO datamodel (op dit moment DAMO 2.5).
   - *validatieregels:* een JSON-bestand met daarin de [Validatieregels](02%20Validatieregels.md).
2. Het uitvoeren van een validatie met een lokale versie van de validatiemodule. Zie hiervoor de [HyDAMO Validatiemodule](..\08%20HyDAMO%20Validatiemodule.md) en een voorbeeld [Jupyter Notebook](https://github.com/HetWaterschapshuis/HyDAMOValidatieModule/blob/main/notebooks/test_wrij.ipynb).
3. Het analyseren van resultaten. Na een uitgevoerde validatie is er een map **results** bijgeschreven met daarin het volgende bestanden:

   - *validation\_result.json:* een JSON bestand met daarin een samenvatting van de validatie. Zie: [03%20Resultaten](03%20Resultaten.md) .
   - *results.gpkg:* een GeoPackage met daarin de validatieresultaten per HyDAMO object-laag.
   - *csv:* een map met daarin per HyDAMO object-laag het resultaat in CSV-formaat.
   - *geojson:* een map met daarin per HyDAMO object-laag het resultaat in geojson-formaat.

Resultaat als geopackage, csv en geojson (voor meer informatie zie [Resultaten](03%20Resultaten.md) ) is optioneel en wordt gespecificeerd bij het uitvoeren van de validatie in de parameter *result\_types.*
