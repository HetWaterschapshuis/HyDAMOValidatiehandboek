# Voorbeelden gebruik API

De API kan gebruikt worden in combinatie met een script omgeving. Op deze pagina zijn een aantal voorbeelden opgenomen die zijn gemaakt met een Python notebook. In de voorbeelden worden alle stappen van de API toegelicht. Enige basiskennis van het gebruik van Python is verondersteld bij het beschouwen van onderstaande voorbeelden.

- [Informatie van de API opvragen](#informatie-van-de-api-opvragen)
- [Inloggen en authentiseren](#inloggen-en-authentiseren)
- [Een nieuwe validatie-taak aanmaken](#een-nieuwe-validatie-taak-aanmaken)
- [Een dataset toevoegen aan de validatie-taak](#een-dataset-toevoegen-aan-de-validatie-taak)
- [Een bestand met validatieregels toevoegen aan de validatie-taak](#een-bestand-met-validatieregels-toevoegen-aan-de-validatie-taak)
- [Controleer de status van een validatie-taak](#controleer-de-status-van-een-validatie-taak)
- [Start een validatie-taak](#start-een-validatie-taak)
- [Download metadata van de validatie-taak](#download-metadata-van-de-validatie-taak)
- [Download resultaten van de validatie-taak in CSV formaat](#download-resultaten-van-de-validatie-taak-in-csv-formaat)
- [Download resultaten van de validatie-taak in geopackage formaat](#download-resultaten-van-de-validatie-taak-in-geopackage-formaat)
- [Download alle resultaat bestanden van de validatie-taak](#download-alle-resultaat-bestanden-van-de-validatie-taak)
- [Een validatie-taak annuleren](#een-validatie-taak-annuleren)
- [Een validatie-taak verwijderen](#een-validatie-taak-verwijderen)

## Informatie van de API opvragen

U kunt informatie over de API opvragen zonder in te loggen. In onderstaand voorbeeld wordt eerst het gebruik van de module ‘requests' (zie ook [deze documentatie](https://docs.python-requests.org/en/latest/)) gedefiieerd, zodat de HyDAMO validatie-API in Python gebruikt kan worden. Ook worden het gebruik van de module ‘os' en 'time’ gedefinieerd, zodat verderop in deze voorbeelden, eenvoudig bestanden en paden kunnen worden samenvoegd (met het commando os.path.join) en een tijdindicator kan worden gebruikt. Vervolgens wordt de URL van de server met de HyDAMO validatie-API opgegeven.

Daarna wordt het GET request uitgevoerd voor het verkrijgen van de informatie over de validatie-API en wordt het resultaat opgeslagen in de variabele 'response’. Als de HTML statuscode van de response gelijk is aan 200 (de validatie-API geeft succesvol een resultaat van de request), dan wordt het resultaat van de response weggeschreven naar het scherm met een print commandp. In Python ziet dat er als volgt uit:

```py
import requests
import os
import time

server = "https://validatie-api.hydamo.nl"

#https://validatie-api.hydamo.nl/
response = requests.get(f"{server}/")

if response.status_code == 200:
  print(response.text)
```

Het resultaat is:

*{"version":"1.2.2","validation\_module":"1.0.0","title":"HyDAMO Validationtool","description": "HyDAMO Validationtool","contact":"*[hydamo-validatietool@hetwaterschapshuis.nl](mailto:hydamo-validatietool@hetwaterschapshuis.nl)*"}*

## Inloggen en authentiseren

Om gebruik te kunnen maken van de HyDAMO Validatiemodule en de validatie-API moet een gebruiker geauthentiseerd worden. Authenticatie in de validatie-API vindt plaats aan de hand van een gebruikersnaam en wachtwoord. Voor een beschrijving van het opvragen van een gebruikersnaam en wachtwoord wordt verwezen naar [Gebruikersregistratie](..\02%20Gebruikersregistratie.md). De validatie-API maakt gebruik van OAuth Firebase Authentication. Dit betekent dat authenticatie plaatsvindt bij een server van Google, middels een standaard API van Google. Om bij Google kenbaar te maken dat authenticatie voor de HyDAMO Validatietool wordt gevraagd, moet gebruik gemaakt worden van een specifieke (Firebase) key (AIzaSyAU17otJko594SYoCulCPfXwkHOXQEieXE) die aan de validatie-API is gekoppeld. In onderstaand voorbeeld wordt vervolgens een Python dictionary gedefinieerd met een gebruikersnaam (label ‘email’) en een wachtwoord (label 'password'). Daarna wordt een POST request naar de Google API gedefinieerd, waarbij de key en de dictionary met de login cedentials meegestuurd wordt. Als de HTML statuscode van de response gelijk is aan 200 (de Google API geeft succesvol een resultaat), dan bevat de response een zogenaamde id\_token. Deze wordt tot slot omgezet in een Bearer token (een gecodeerde token) die daarna als header meegeven kan worden aan toekomstige requests aan de HyDAMO validatie-API. De header wordt naar het scherm geprint. Let op dat de houdbaarheid van van de token maximaal een uur is. Daarna moet er opnieuw een token aangevraagd worden via de procdure zoals hier weergegeven. In Python ziet de code er als volgt uit (gebruikersnaam en wachtwoord zijn fictief in het voorbeeld):

```py
username = "gebruiker@hydamo.nl"
password = "*****"

firebase_url = "https://identitytoolkit.googleapis.com/v1"
firebase_key = "AIzaSyAU17otJko594SYoCulCPfXwkHOXQEieXE"

response = requests.post(f"{firebase_url}/accounts:signInWithPassword?key={firebase_key}", data={'email': username, 'password': password, 'returnSecureToken': 'true'})

if response.status_code == 200:
  id_token = response.json()['idToken']
  my_headers = {'Authorization': f"Bearer {id_token}"}   
  print(my_headers)
```

Het resultaat is (de daadwerkelijke Bearer token is vervangen door sterretjes):

{'Authorization': 'Bearer \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*'}

## Een nieuwe validatie-taak aanmaken

Met de de HyDAMO validatie-API kan een nieuwe validatie-taak aangemaakt worden. Hiertoe moet een unieke Bearer token beschikbaar zijn (zie vorige paragraaf), waarmee geauthentiseerd kan worden. Voor elke een nieuwe validatie-taak moet eerst een willekeurige naam gedefinieerd worden. Met een POST request naar de API op het endpoint *tasks* kan vervolgens een nieuwe validatie-taak aangemaakt worden. In dat request wordt de naam van de taak en de Bearer token (opgeslagen in my\_headers) meegegeven. Als de HTML statuscode van de response gelijk is aan 201 (het post request geeft aan dat de aanpassing succesvol is doorgevoerd), kunnen verschillende gegevens (data) van de validatie-taak uit de response uitgelezen worden en afgedrukt worden naar het scherm:

- de unieke id (automatisch toegewezen) van een validatie-taak
- de naam die aan een nieuwe validatie-taak is meegegeven
- de status van een nieuwe validatie-taak (altijd gelijk aan 'new')
- het aantal dataset bestanden dat is toegevoegd aan een validatie-taak
- en of de validatie-taak validatieregels bevat.

```py
task_name = "Voorbeeld_Wiki"

#https://validatie-api.hydamo.nl/tasks/Voorbeeld_Wiki
response_new_task= requests.post(f"{server}/tasks/{task_name}", headers=my_headers)

if response_new_task.status_code == 201:
  data = response_new_task.json()
  print("id: " + str(data["id"]))
  print("naam: " + str(data["name"]))
  print("status: " + str(data["status"]))
  print("aantal dataset bestanden: " + str(data["numberOfDatasets"]))
  print("validatieregels aanwezig: " + str(data["validationRules"]))
```

Het resultaat is:

*id: 999 (dit id is een voorbeeld)*  
*naam: Voorbeeld\_Wiki*  
*status: new*  
*aantal dataset bestanden: 0*  
*validatieregels aanwezig: False*

## Een dataset toevoegen aan de validatie-taak

Als er een validatie-taak beschikbaar is, kunnen 1 of meerdere dataset bestanden toegevoegd worden aan deze validatie-taak. Hiertoe moet eerst een verwijzing naar deze databestanden gemaakt worden. Een databestand kan 1 of meerdere objectlagen (stuwen, gemalen, hydro-objecten, etc.) bevatten. Het is mogelijk om meerdere databestanden met elk 1 objectlaag toe te voegen aan een validatie-taak. De dataset bestanden:

- moeten voldoen aan het *DAMO 2.5*. datamodel. Zie voor meer informatie [DAMO Objectenboek](https://damo.hetwaterschapshuis.nl/DAMO%202.2/Objectenhandboek%20DAMO%202.6/HTML/Inleiding.html).
- de data is van het (open data) formaat Geopackage (extensie \*.gpkg). Zie voor meer informatie [Geopackage](https://www.geopackage.org/).

In dit voorbeeld worden meerdere databestanden (met duikersifonhevels, hydro-objecten en regelmiddelen) toegevoegd aan een bestaande validatie-taak. Hiertoe is eerst een array (tabel) *datasets* gedefinieerd met de namen van de dataset bestanden (geopackages). Deze dataset bestanden staan in een lokale folder op een computersysteem (*file\_path*). Om de datasets te kunnen toevoegen aan een validatie-taak, is de taak-id van een bestaande validatie-taak nodig. Deze id kan uit de response van het API request, waamee een nieuwe taak is aangemaakt (zie voorgaande paragraaf), gehaald worden (*attribuut: id*). Vervolgens worden in een lus de verschillende databestanden 1 voor 1 toegevoegd aan de validatie-taak. Voor elke dataset wordt eerst een dictionary *params* aangemaakt. Hierin wordt de naam van het databestand opgeslagen (label ‘file’). Daarna wordt een dictionary *files* aangemaakt. Hierin wordt het databestand zelf opgeslagen (via een commando ‘open' en het attribuut 'rb’; de dataset wordt als een binair bestand opgeslagen). Met een POST request naar de validatie-API op het endpoint *task/datasets* wordt vervolgens het databestand toegevoegd aan een bestaande validatie-taak. In het request wordt de id van de validatie-taak meegegeven (in de URL) samen met de dictionaries *files* en *params* en de Bearer token (opgeslagen in my\_headers). Als de HTML statuscode van de response gelijk is aan 201 (het post request geeft aan dat de aanpassing succesvol is doorgevoerd), kunnen verschillende gegevens (data) van de validatie-taak uit de response uitgelezen worden, waaronder:

- de unieke id van een validatie-taak
- en het aantal dataset bestanden dat is toegevoegd aan een validatie-taak.

De lus eindigt na het wegschrijven van de resultaten (id en het aantal dataset bestanden toegevoegd aan uw taak) naar het scherm.

```py
file_path = r"...\ValidatietoolHyDAMO\Wiki\Datasetbestanden"
datasets = ["DuikerSifonHevel.gpkg", "HydroObject.gpkg", "Regelmiddel.gpkg"]
task_id = response_new_task.json()["id"]

for dataset in datasets:
  params = {"file": dataset}
  files = {"file": open(os.path.join(file_path,dataset), "rb")}
  
  #https://validatie-api.hydamo.nl/task/[task_id]/datasets
  response_upload_datasets = requests.post(f"{server}/task/{task_id}/datasets", files=files, params=params, headers=my_headers) 
  if response_upload_datasets.status_code == 201:
    data = response_upload_datasets.json()
    print("id: " + str(data["id"]))
    print("naam dataset: " + dataset)
    print("aantal dataset bestanden: " + str(data["numberOfDatasets"])) 
```

Het resultaat is:

*id: 999 (dit id is een voorbeeld)*  
*naam dataset: DuikerSifonHevel.gpkg*  
*aantal dataset bestanden: 1*   
*id: 999 (dit id is een voorbeeld)*  
naam dataset: *HydroObject.gpkg*  
*aantal dataset bestanden: 2*   
*id: 999 (dit id is een voorbeeld)*   
naam dataset: *Regelmiddel.gpkg*  
*aantal dataset bestanden: 3*

## Een bestand met validatieregels toevoegen aan de validatie-taak

Als er een validatie-taak beschikbaar is, kan er een bestand met validatieregels toegevoegd worden aan deze validatie-taak. Meer informatie over de inhoud van het bestand met validatieregels vindt u hier [Basis validatieregels](..\05%20Basis%20validatieregels.md). Een basisset validatieregels kunt u op [Github](https://github.com/HetWaterschapshuis/HyDAMOValidatieregels/tree/main/validation_rules) downloaden.

Het bestand met validatieregels staat in een lokale folder op een computersysteem (*file\_path*). Om validatieregels te kunnen toevoegen aan een bestaande validatie-taak, is de taak-id nodig van de validatie-taak (zie voorgaande stappen). Vervolgens wordt een dictionary *params* aangemaakt waarin de naam van het bestand met validatieregels opgeslagen wordt (label ‘file’). Daarna wordt een dictionary *files* aangemaakt. Hierin wordt het bestand met validatieregels zelf opgeslagen (via een commando ‘open' en het attribuut 'rb’; het bestand met validatieregels wordt als een binair bestand opgeslagen). Met een POST request naar de API op het endpoint *task/validationrules* wordt het bestand met validatieregels toegevoegd aan de validatie-taak. Naast de id van de validatie-taak (in de URL) worden ook de dictionaries *files* en *params* en de Bearer token (opgeslagen in my\_headers) meegegeven in het request. Als de HTML statuscode van de response gelijk is aan 201 (het post request geeft aan dat de aanpassing succesvol is doorgevoerd), kunnen verschillende gegevens (data) van de validatie-taak uit de response uitgelezen worden, waaronder:

- de unieke id van uw validatie-taak
- en of de validatie-taak validatieregels bevat.

```py
file_path = r"...ValidatietoolHyDAMO\Wiki\Validatieregels"
validationrules = "validationrules.json"

params = {"file": validationrules}
files = {"file": open(os.path.join(file_path,validationrules), "rb")}

#http://validatie-api.hydamo.nl/task/[task_id]/validationrules
response_upload_validationrules = requests.post(f"{server}/task/{task_id}/validationrules", files=files, params=params, headers=my_headers) 

if response_upload_validationrules.status_code == 201:
    data = response_upload_validationrules.json()
    print("id: " + str(data["id"]))
    print("validatieregels aanwezig: " + str(data["validationRules"])) 
```

Het resultaat is:

*id: 999 (dit id is een voorbeeld)*  
*validatieregels aanwezig: True*

## Controleer de status van een validatie-taak

Voordat een validatie-taak gestart kan worden moet een validatie-taak minimaal 1 dataset bestand en een bestand met validatieregels bevatten. U kunt aan de hand van de status van een validatie-taak controleren of een validatie-taak gereed is voor validatie. De status is dan gelijk aan *ready\_to\_validate*.

De status van een validatie-taak kan op elk moment opgevraagd worden met een GET request naar de validatie-API op het endpoint *task*, waarbij de validatie-taak id (in de URL) en de Bearer token (opgeslagen in my\_headers) meegegeven wordt. ls de HTML statuscode van de response gelijk is aan 200 (het post request geeft aan dat de informatie succesvol is opgehaald), kunnen verschillende gegevens (data) van de validatie-taak uit de response uitgelezen worden, waaronder de status van de validatie-taak.

```py
#http://validatie-api.hydamo.nl/task/[task_id]/
response_get_task = requests.get(f"{server}/task/{task_id}", headers=my_headers) 

if response_get_task.status_code == 200:
    data = response_get_task.json()
    print(str(data["status"]))
```

Het resultaat is:

*status: ready\_to\_validate*

## Start een validatie-taak

Als de status van een validatie-taak gelijk is aan ‘ready\_to\_validate' kan deze taak gestart worden. De validatie-API geeft dan 'opdracht’ aan de Validatiemodule om de validatie van de (aan de validatie-taak) toegevoegde databestanden met de (aan de validatie-taak) toegevoegde validatieregels uit te voeren.

Alleerst moet het resultaat van een validatie opdracht gedefinieerd. Met het resultaat wordt hier bedoeld in welke bestandstypen het resultaat door de Validatiemodule wordt weggeschreven. Er zijn drie mogelijkheden: een CSV bestand, een Geopackage bestand of een Geojson bestand. Elke willekeurige combinatie van deze bestandstype is toegestaan, dus alleen het CSV bestand of zowel een Geopackage als een Geojson bestand, etc. Hiertoe wordt een (string) variabele *format* gedefineerd met de gewenste uitvoerformaten (komma gescheiden bij meerdere bestandstypen). Vervolgens wordt een POST request gedaan naar de validatie-API op het endpoint *execute*, waarbij de validatie-taak id en de variabele ‘format' (beide in de URL) en de Bearer token (opgeslagen in my\_headers) meegegeven wordt. ls de HTML statuscode van de response gelijk is aan 202 (het post request geeft aan dat de actie is geaccepteerd), dan wordt de validatie-taak gestart. Om dit te controleren kan de status van de validatie-taak gecontroleerd worden (zie voorgaande paragraaf). Allereerst zal deze gelijk zijn aan ‘pending’. De validatie-taak is toegevoegd aan de wachtrij. Zodra er rekencapaciteit beschikbaar is, wordt de taak gestart en wijzigt de status in ‘validating’. Door de status periodiek te controleren (bijvoorbeeld eens per minuut), kan bepaald worden of de validatie-taak klaar is. Een validatie-taak is klaar als de status is aangepast in ‘finished’ (de validatie-taak is succesvol tot een einde gekomen) pf 'error’ (de validatie-taak is met een fout gestopt).

```py
#http://validatie-api.hydamo.nl/task/[task_id]/execute/csv,geopackage,geojson
format = "csv,geopackage,geojson"

response_execute_task = requests.post(f"{server}/task/{task_id}/execute/{format}", headers=my_headers) 

if response_execute_task.status_code == 202:
    print("Taak wordt gestart!")
    #controleer de status van de validatie-taak (periodiek)
    response_get_task = requests.get(f"{server}/task/{task_id}", headers=my_headers) 
    if response_get_task.status_code == 200:
        status = str(response_get_task.json()["status"]) 
        while not (status == "finished" or status == "error"):
            response_get_task = requests.get(f"{server}/task/{task_id}", headers=my_headers)
            if response_get_task.status_code == 200:
                status = str(response_get_task.json()["status"])
                print(f"status taak: {status}")
            time.sleep(60)
```

Het resultaat is:

*Taak wordt gestart!*  
*status taak: pending*  
*status taak: validating*  
*…*  
*status taak: validating*  
*status taak: finished*

Let op: validatie-taken van grote datasets kunnen aanzienlijke tijd in beslag nemen. Wanneer de validatie tijd meer dan 30 minuten wordt, wordt geadviseerd om opnieuw te authentiseren op de validatie-API, om te voorkomen dat de token verloopt.

## Download metadata van de validatie-taak

Als een validatie-taak is beeindigd (al dan niet succesvol), kan de metadata van de validatie-taak gedownload worden ter controle van het validatie resultaat. Allereerst wordt een lokale folder op een computersysteem gedefinieerd waar naartoe een bestand met metadata kan worden gedownload. Met een POST request naar de API op het endpoint *task/result/metadata* wordt een bestand met metadata van de validatie-taak opgevraagd. Naast de id van de validatie-taak (in de URL) wordt ook de Bearer token (opgeslagen in my\_headers) meegegeven in het request. Als de HTML statuscode van de response gelijk is aan 200 (het post request geeft een succesvol resultaat), kan het bestand met de metadata worden opgeslagen in de lokale folder. Hiertoe wordt het resultaat van het request eerst opgeslaten in de variabele ‘result\_data'. Vervolgens wordt gecontroleerd of de map waar het bestand opgeslagen moet worden bestaat en zo niet, dan wordt deze aangemaakt. Tot slot wordt het resultaat van het request opgeslagen in het bestand '*taak-id*\_metadata.json’.

```py
result_folder = r"...\Resultaten"

#http://validatie-api.hydamo.nl/task/[task_id]/result/metadata
response_get_metadata = requests.get(server + '/task/' + str(task_id) + '/result/metadata', headers=my_headers)

if response_get_metadata.status_code == 200:
    result_data = bytes(response_get_metadata.content)
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    open(os.path.join(result_folder,f"{task_id}_metadata.json"), 'wb').write(response_get_metadata.content)
```

Het resultaat is een json bestand met de volgende inhoud (zie ook [Resultaten](..\HyDAMO%20Validatiemodule\03%20Resultaten.md)):

*{*  
*"api\_version": "1.0.0",*  
*"user\_name": "thonus",*  
*"task\_started": "2022-02-11 13:18:07",*  
*"task\_finished": "2022-02-11 13:26:14",*  
*"success": true,*  
*"module\_version": "1.0.0",*  
*"date\_check": "2022-02-11T13:18:07.817032",*  
*"duration": 487.0597188472748,*  
*"status": "finished",*  
*"dataset\_layers": [*  
*"duikersifonhevel",*  
*"hydroobject",*  
*"regelmiddel"*  
*],*  
*"result\_layers": ["duikersifonhevel", "hydroobject", "regelmiddel"],*  
*"missing\_layers": ["admingrenswaterschap","afsluitmiddel","afvoergebiedaanvoergebied","aquaduct","beheergrenswaterschap","bodemval","brug",…,"sturing","stuw","vispassage","vispassagevlak","vuilvang","zandvang"*  
*],*  
*"error\_layers": [],*  
*"syntax\_result": ["duikersifonhevel","hydroobject","regelmiddel"],*  
*"validation\_result": ["duikersifonhevel","regelmiddel","hydroobject"]*  
*}*

## Download resultaten van de validatie-taak in CSV formaat

Als er geen fouten voorkomen in de metadata van een afgeronde validatie-taak kunnen de resultaten gedownload worden. In deze stap wordt het validatie-resultaat in een CSV bestand gedownload. N.B. dit is alleen mogelijk als bij het uitvoeren van de validatie-taak ook het format CSV is meegegeven! Een CSV bestand met validatie-resultaten kan gedownload worden door een GET request naar de API op het endpoint *task/result* te maken. Naast de id van de validatie-taak (in de URL) moet ook de naam van de objectlaag gevolgd door ‘.csv' meegegeven worden in de URL. Daarnaast is ook de Bearer token (opgeslagen in my\_headers) meegegeven in het request. Als de HTML statuscode van de response gelijk is aan 200 (het post request geeft een succesvol resultaat), kan het CSV bestand met validatie-resultaten worden opgeslagen in de lokale folder. In dit voorbeeld hebben de resultaten van object 'duikersifonhevel’ beschouwd. N.B. voor elke objectlaag moeten een apart CSV bestand gedownload worden!

```py
#http://validatie-api.hydamo.nl/task/[task_id]/result/[objectlaag].csv
response_get_results_csv = requests.get(server + '/task/' + str(task_id) + '/result/duikersifonhevel.csv', headers=my_headers)
                                
if response_get_results_csv.status_code == 200:
    result_data = bytes(response_get_results_csv.content)
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    open(os.path.join(result_folder,"duikersifonhevel.csv"), 'wb').write(response_get_results_csv.content)
```

Het resultaat is een CSV bestand met resultaten van de validatie van de duikersifonhevels in de dataset (zie ook [Resultaten](..\HyDAMO%20Validatiemodule\03%20Resultaten.md)).

## Download resultaten van de validatie-taak in geopackage formaat

Op vergelijkbare manier als in de beschrijving voor het downloaden van een resultaat in CSV formaat, kunnen de resultaten ook in een geopackage gedownload worden, zodat deze te gebruiken zijn in een GIS programma. N.B. dit is alleen mogelijk als bij het uitvoeren van de validatie-taak ook het format geopackage is meegegeven! Een geopackage bestand met validatie-resultaten kan gedownload worden door een GET request naar de API op het endpoint *task/result* te maken. Naast de id van de validatie-taak (in de URL) moet ook het fomat ‘geopackage' meegegeven worden in de URL. Daarnaast is ook de Bearer token (opgeslagen in my\_headers) meegegeven in het request. Als de HTML statuscode van de response gelijk is aan 200 (het post request geeft een succesvol resultaat), kan het geopackage bestand met validatie-resultaten worden opgeslagen in de lokale folder. In tegenstelling tot het downloaden CSV bestand met validatie-resultaten per objectlaag, kunnen in een geopackage meerdere objectenlagen opgeslagen worden. Er hoeft in dus maar 1 geopackage bestand gedownload te worden.

```py
#http://validatie-api.hydamo.nl/task/[task_id]/result/geopackage
response_get_results_geopackage = requests.get(server + '/task/' + str(task_id) + '/result/geopackage', headers=my_headers)

if response_get_results_geopackage.status_code == 200:
    result_data = bytes(response_get_results_geopackage.content)
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    open(os.path.join(result_folder,"validationresults.gpkg"), 'wb').write(response_get_results_geopackage.content)
```

Het resultaat is een geopackage bestand met resultaten van de validatie voor alle objectlagen in de dataset (zie ook [Resultaten](..\HyDAMO%20Validatiemodule\03%20Resultaten.md)).

## Download alle resultaat bestanden van de validatie-taak

Het is ook mogelijk om alle resultaat bestanden van een validatietaak tegelijk te downloaden in een zip-bestand. Dit zip-bestand bevat dan zowel het metadata JSON bestand als de alle uitvoerformaten die bij het starten van de taak zijn meegegeven (geopackage, CSV bestanden en/of GEOJSON bestanden). Een zip-bestand met alle resultaten kan gedownload worden door een GET request naar de API op het endpoint *task/result* te maken. Naast de id van de validatie-taak (in de URL) moet ook het fomat ‘zip' meegegeven worden in de URL. Daarnaast is ook de Bearer token (opgeslagen in my\_headers) meegegeven in het request. Als de HTML statuscode van de response gelijk is aan 200 (het post request geeft een succesvol resultaat), kan het zip-bestand met validatie-resultaten worden opgeslagen in de lokale folder.

```py
#http://validatie-api.hydamo.nl/task/[task_id]/result/zip
response_get_all_results = requests.get(server + '/task/' + str(task_id) + '/result/zip', headers=my_headers)

if response_get_all_results.status_code == 200:
    result_data = bytes(response_get_all_results.content)
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    open(os.path.join(result_folder,"validationresults.zip"), 'wb').write(response_get_all_results.content)
```

Het resultaat is een zip-bestand met alle bestanden van de validatietaak.

## Een validatie-taak annuleren

Het kan voorkomen dat een validatie-taak wordt gestart die veel doorlooptijd vraagt, maar waarvan op een gegeven moment wordt geconcludeerd dat er iets niet klopt. Een validatie-taak die gestart is kan door een gebruiker geannuleerd worden door een POST request naar de API op het endpoint *task/kill* te sturen. Naast de id van de validatie-taak (in de URL) wordt ook de Bearer token (opgeslagen in my\_headers) meegegeven in het request. Als de HTML statuscode van de response gelijk is aan 202 (het post request geeft aan dat de actie is geaccepteerd), wordt de taak geannuleerd.

```py
#http://validatie-api.hydamo.nl/task/[task_id]/kill
response_kill_task = requests.post(server + '/task/' + str(task_id) + '/kill', headers=my_headers)
                                
if response_kill_task.status_code == 202:
    print('De taak is geannuleerd!')
```

Het resultaat is dat de taak is geannuleerd. Dit kan eventueel met gecontroleerd worden door de status van de taak op te vragen.

## Een validatie-taak verwijderen

Elke validatie-taak kan weer verwijderd worden uit de lijst met validatie-taken. Alleen validatie-taken die gestart zijn, m.a.w. waarvan de validatie wordt uitgevoerd kunnen niet verwijderd worden. Deze validatie-taken zullen eerst geannuleerd moeten worden (zie voorgaande paragraaf). Een taak kan verwijderd worden door een DELETE request naar de API op het endpoint *task* te sturen. Naast de id van de validatie-taak (in de URL) wordt ook de Bearer token (opgeslagen in my\_headers) meegegeven in het request. Als de HTML statuscode van de response gelijk is aan 200 (het delete request geeft een succesvol resultaat), is de taak verwijderd. Bij het verwijderen van de taak worden ook alle toegevoegde dataset bestanden en bestanden met validatieregels verwijderd. N.B. na 10 dagen worden validatie-taken die gevalideerd zijn door het systeem verwijderd.

```py
#http://validatie-api.hydamo.nl/task/[task_id]
response_delete_task = requests.delete(server + '/task/' + str(task_id), headers=my_headers)
                                
if response_delete_task.status_code == 200:
    print('Taak is verwijderd!')
```

Het resultaat is dat de validatie-taak uit de takenlijst is verwijderd.

Bovenstaande voorbeelden zijn opgenomen in een Jupyter notebook. Dit notebook kunt u [hier](../../downloads/Voorbeeld_Wiki.ipynb) downloaden. Let op: u moet wel de paden en login gegevens zelf aanpassen, anders werkt het notebook niet.