# HyDAMO validatie-API

Als de entrale schakel communiceert de API (Application Programming Interface) tussen de webclient als grafische schil van de tool en de Python-rekenmodule. De API regelt het aanmaken van validatietaken, toevoegen van datasets en validatieseregels, opstarten van taken en downloaden van resultaten. Het is mogelijk om de HyDAMO validatie-API direct aan te roepen en validatieopdrachten zonder de webclient door te voeren. Dit kan vanuit een scripting-omgeving zoals Python Notebook, Visual Studio Code of FME.

De HyDAMO validatie-API bestaat uit verschillende **endpoints**. Elke endpoint heeft een URL om een bepalde actie (request) uit te voeren. Deze requests bestaan uit het opvragen van informatie en data (GET), het toevoegen van data (POST) of het vewijderen van data (DELETE).

![swagger_screenshot](../../images/swagger.png)

Bekijk voor een complete overzicht van de API-functionaliteit de interactieve [Swagger documentatie](https://validatie-api.hydamo.nl/docs){:target="_blank"} van de Validatie-API. Als je een bepaald GET-, POST- of DELETE-endpoint openklapt kan je de achterliggende functionaliteit met de knopjes 'Try it out' en 'Execute uitproberen en krijg de API-response te zien. Let op, voor het testen van bijna alle endpoints is het noodigzakelijk dat je je van te voren eenmalig authentiseerd. Je moet hiervoor een Firebase ID-token aanmaken en deze token bij de button 'Authorize' boven-rechts invullen. De token verkrijg je door met geldig gebruikersnaam en wachtwoord onderstaande bevelen in de powershel uit te voeren:

```powershell
$body = @{
    email = "wolf.waterman@hydamo.nl"
    password = "*****"
    returnSecureToken = $true
} | ConvertTo-Json

$response = Invoke-RestMethod `
    -Method Post `
    -Uri "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyAU17otJko594SYoCulCPfXwkHOXQEieXE" `
    -ContentType "application/json" `
    -Body $body

$response.idToken
```

## Gebruik van de API

De API gebruikt je vanuit een scripting-omgeving zoals Python Notebook, Visual Studio Code of FME. Hieronder vind je stukjes script-code die je door de meest relevante alle stappen in het gebruik van de API leidt.

Onderstaande voorbeelden zijn ook opgenomen in een [Jupyter-notebook](../../downloads/Voorbeeld_Wiki.ipynb). Let op, je moet wel de paden en login gegevens zelf aanpassen.

### 1. Informatie van de API opvragen

Ja kan informatie over de API opvragen zonder in te loggen. In onderstaand voorbeeld wordt eerst het gebruik van de module ‘requests' (zie ook [deze documentatie](https://docs.python-requests.org/en/latest/)) mogelijk gemaakt door het importeren van de 'request' librarie. Daarnaast worden ook de libraries ‘os' en 'time’ geimporteerd voor het makkelijke gebruik van besstandspaden (os) en het bijhouden van de duur van de uitgevoerde stappen (time). In de variable 'server' defineer je voor het eerst een API-URL. In dit geval de basis-URL van de HyDAMO Validatie server.

Met de GET request wordt de server-URL aangeroepen. De server antwoord met informatie over de validatie-API die in de variable 'response' wordt opgeslagen. Als de HTTP statuscode van de response gelijk is aan 200 betekend dit dat het verzoek successvol was. Het resultaat van het antwoord wordt  naar het scherm geschreven door een print commando. In Python ziet dat als volgt uit:

```py
import requests
import os
import time

server = "https://validatie-api.hydamo.nl"

response = requests.get(f"{server}/")

if response.status_code == 200:
  print(response.text)
```

Het resultaat is:

*{"version":"1.2.4","validation_module":"1.6.0","title":"HyDAMO Validationtool","description": ... "}*

### 2. Inloggen en authentiseren

Om gebruik te kunnen maken van taak- en validatiegerelateerde API-functionaliteit moet je je als gebruiker geauthentiseren. De authenticatie vindt plaats door middel van een gebruikersnaam en wachtwoord. Hier vind je meer over de [gebruikersregistratie](01%20Gebruikersregistratie.md).

De validatie-API maakt gebruik van OAuth Firebase Authentication van Google. Om bij Google kenbaar te maken dat authenticatie voor de HyDAMO Validatietool wordt gevraagd, moet de specifieke Firebase-key - AIzaSyAU17otJko594SYoCulCPfXwkHOXQEieXE - meegevenen worden die aan de validatie-API is gekoppeld. In onderstaand voorbeeld wordt de key in een Python dictionary geplaatst samen met de gebruikersnaam (label ‘email’) en wachtwoord (label 'password'). Daarna wordt een POST-request naar de Google API gedefinieerd, waarbij de dictionary met de login cedentials meegestuurd wordt. Bij een succesvolle HTTP statuscode van 200 dan bevat de response een id_token. Deze wordt tot slot omgezet in een Bearer-token (een gecodeerde token) die daarna als header meegeven wordt aan alle volgende verzoeken aan de HyDAMO validatie-API. De header wordt naar het scherm geprint. Let op dat de houdbaarheid van van de token maximaal een uur is. Daarna moet er opnieuw een token aangevraagd worden. In Python ziet de code als volgt uit:

```py
username = "wolf.waterman@hydamo.nl"
password = "*****"

firebase_url = "https://identitytoolkit.googleapis.com/v1"
firebase_key = "AIzaSyAU17otJko594SYoCulCPfXwkHOXQEieXE"

response = requests.post(f"{firebase_url}/accounts:signInWithPassword?key={firebase_key}", data={'email': username, 'password': password, 'returnSecureToken': 'true'})

if response.status_code == 200:
  id_token = response.json()['idToken']
  my_headers = {'Authorization': f"Bearer {id_token}"}   
  print(my_headers)
```

Het resultaat is (de daadwerkelijke Bearer-token is vervangen door sterretjes):

{'Authorization': 'Bearer \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*'}

### 3. Een nieuwe validatietaak aanmaken

Uiteraard kan je met de validatie-API een nieuwe validatietaak aanemaken. Hiertoe moet een unieke Bearer-token beschikbaar zijn in de variable 'my_headers' (zie vorige paragraaf). Ernaast moet je voor elke nieuwe validatietaak een willekeurige taaknaam definieren. Bearer-token en taaknaam worden in een POST request op het endpoint *tasks* meegegeven en het aanmaken van de validatietaak in gang gezet. Een HTTP-statuscode van 201 betekend dat de aangevraagde aanpassing door de post-request succesvol is doorgevoerd. Het antwoord wordt naar het scherm afgedrukt. Daar vind je verschillende gegevens over de aangemaakte validatietaak:

- De unieke id (automatisch toegewezen) van de validatietaak,
- De naam van de validatietaak,
- De status van de validatietaak (in deze fase 'new'),
- Het aantal invoerdatasets die zijn toegevoegd (in deze fase 0),
- Of de validatietaak validatieregels bevat (in deze fase 'false').

```py
task_name = "Voorbeeld_Handleiding"

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
*naam: Voorbeeld_Handleiding*  
*status: new*  
*aantal dataset bestanden: 0*  
*validatieregels aanwezig: False*

### 4. Invoerdatasets toevoegen aan de validatietaak

Je kan aan een validatietaak 1 of meerdere invoerdatasets toevoegen. Hiervoor moet eerst een verwijzing naar deze databestanden gemaakt worden. Een invoerdataset kan 1 of meerdere objectlagen (stuwen, gemalen, hydro-objecten, etc.) bevatten. Het is mogelijk om meerdere bestanden met elk 1 objectlaag toe te voegen aan een validatietaak. De bestanden moeten voldoen aan:

- een versie van het HyDAMO-datamodel, bijvoorbeeld *DAMO 2.5*. Zie voor meer informatie [DAMO Objectenboek](https://damo.hetwaterschapshuis.nl/DAMO%202.2/Objectenhandboek%20DAMO%202.6/HTML/Inleiding.html).
- het dataformaat GeoPackage (extensie \*.gpkg). Zie voor meer informatie [Geopackage](https://www.geopackage.org/).

In onderstaand voorbeeld worden meerdere invoerbestanden (met duikersifonhevels, hydro-objecten en regelmiddelen) toegevoegd aan een bestaande validatietaak. Hiervoor wordt de lijst *datasets* gedefinieerd met daarin de namen van de te gebruiken GeoPackage-bestanden. De locatie van de lokale map met deze bestanden wordt opgegeven in de pad-variable 'file_path'. Verder heb je de id ('taak_id') van de validatietaak nodig waaraan je de datasets wil toevoegen. Deze id kan uit de response van het aanmaken van een nieuwe taak komen (zie voorgaande paragraaf).

Vervolgens worden in een lus de verschillende databestanden 1 voor 1 toegevoegd aan de validatietaak. Voor elke dataset wordt eerst een dictionary *params* aangemaakt. Hierin wordt de naam van het bestand opgeslagen (label ‘file’). Daarna wordt een dictionary *files* aangemaakt. Hierin wordt het databestand zelf opgeslagen (via een commando ‘open' en het attribuut 'rb’). Met een POST request op het endpoint *task/datasets* wordt vervolgens ieder bestand toegevoegd aan een bestaande validatietaak.

In de request wordt de taak-id (in de URL) samen met de dictionaries *files* en *params* en de Bearer-token (variable my_headers). Met een succesvolle HTTP-statuscode van 201 kan je verschillende gegevens van de validatietaak uit de response lezen, onder meer:

- De id van de validatietaak,
- De namen en volgnummers van de toegevoegde invoerdatasets.

```py
file_path = r"...\ValidatietoolHyDAMO\Wiki\Datasetbestanden"
datasets = ["DuikerSifonHevel.gpkg", "HydroObject.gpkg", "Regelmiddel.gpkg"]
task_id = response_new_task.json()["id"]

for dataset in datasets:
  params = {"file": dataset}
  files = {"file": open(os.path.join(file_path,dataset), "rb")}
  
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

### 5. Validatieregels toevoegen aan de validatietaak

Je kan aan een bestaande validatietaak een bestand met [validatieregels](hier een link toevoegen!) toegevoegen. Het bestand met validatieregels dien je in een lokale folder te zetten (varibale *file_path*). Je hebt verder de id ('taak_id') van de validatietaak nodig waarvoor je de regels wil toevoegen. Deze id kan uit de response van het aanmaken van een nieuwe taak komen (zie voorgaande stappen).

Een dictionary *params* wordt aangemaakt waarin de naam van het regelbestand wordt opgeslagen (label ‘file’). Daarna wordt een dictionary *files* aangemaakt. Hierin wordt het bestand met validatieregels zelf opgeslagen (via een commando ‘open' en het attribuut 'rb’). Met een POST request op het endpoint *task/validationrules* wordt het regelbestand toegevoegd aan de validatietaak. Naast de taak-id (in de URL) worden ook de dictionaries *files* en *params* en de Bearer-token (variable my_headers) meegegeven in het request. Bij een succesvolle HTTP-statuscode van 201 kan je verschillende gegevens van de validatietaak uit de response lezen, waaronder:

- De id van uw validatietaak,
- Of de validatietaak validatieregels bevat.

```py
file_path = r"...ValidatietoolHyDAMO\Wiki\Validatieregels"
validationrules = "validationrules.json"

params = {"file": validationrules}
files = {"file": open(os.path.join(file_path,validationrules), "rb")}

response_upload_validationrules = requests.post(f"{server}/task/{task_id}/validationrules", files=files, params=params, headers=my_headers) 

if response_upload_validationrules.status_code == 201:
    data = response_upload_validationrules.json()
    print("id: " + str(data["id"]))
    print("validatieregels aanwezig: " + str(data["validationRules"])) 
```

Het resultaat is:

*id: 999 (dit id is een voorbeeld)*  
*validatieregels aanwezig: True*

### 6. De status van de validatietaak controleSren

Voordat je een validatietaak kan opstarten moet een taak minimaal 1 invoerdataset en 1 bestand met validatieregels bevatten. Aan de hand van de taak-status kan je controleren of een taak gereed is voor validatie. De status is dan gelijk aan *ready_to_validate*.

Je kan de status van een bestaande validatietaak op elk moment opvragen met een GET request op het endpoint *task*. De taak-id (in de URL) en de Bearer-token (opgeslagen in my\_headers) moeten meegegeven worden. Bij een succesvolle HTTP-statuscode van 200 kan je verschillende gegevens van de validatietaak uitlezen, waaronder de status van de validatietaak.

```py
response_get_task = requests.get(f"{server}/task/{task_id}", headers=my_headers) 

if response_get_task.status_code == 200:
    data = response_get_task.json()
    print(str(data["status"]))
```

Het resultaat is:

*status: ready_to_validate*

### 7. De validatietaak starten

Als de status van de validatietaak is ‘ready_to_validate' kan je deze taak opstarten. De API geeft dan 'opdracht’ aan de Validatiemodule om de aan de taak toegevoegde databestanden aan de hand van de opgegeven validatieregels te controleren.

Eerst moet je het uitvoerformaat van het validatieresultaat definieren in de variable *format*. Er zijn drie mogelijkheden: een CSV-bestand, een GeoPackage-bestand of een GeoJSON-bestand. Elke selectie of combinatie van deze bestandstypes is toegestaan. Vervolgens wordt een POST-request gedaan naar op het endpoint *execute*, waarbij de taak-id en de variabele ‘format' (beide in de URL) en de Bearer-token (variable my_headers) meegegeven wordt. Bij een succesvolle HTTP-statuscode van de response van 202 heeft de API de actie uit het POST-request geaccepteerd en wordt de validatie gestart.

Om dit te controleren kan je de status van de taak uitlezen (zie voorgaande paragraaf). Initieel zal de status ‘pending’ zijn. De validatietaak is dan toegevoegd aan de wachtrij. Zodra er rekencapaciteit beschikbaar is, wordt de taak gestart en wijzigt de status naar ‘validating’. Door de status periodiek te controleren (bijvoorbeeld eens per minuut), kan bepaald worden of de validatietaak klaar is. De status verandert dan naar in ‘finished’ (de validatietaak is succesvol tot een einde gekomen) of 'error’ (de validatietaak is met een fout gestopt).

```py
format = "csv,geopackage,geojson"

response_execute_task = requests.post(f"{server}/task/{task_id}/execute/{format}", headers=my_headers) 

if response_execute_task.status_code == 202:
    print("Taak wordt gestart!")
    #controleer de status van de validatietaak (periodiek)
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

Let op: validatietaken van grote datasets kunnen aanzienlijke verwerkingstijden in beslag nemen. Wanneer de validatie tijd meer dan 30 minuten wordt, wordt geadviseerd dat je opnieuw authentisert, om te voorkomen dat de token verloopt.

### 8. De log van de validatietaak downloaden

Als een validatietaak is beeindigd (succesvol of met fout), kan je de log ('metadata') van de taak downloaden en het verloop en resultaat van de validatie in detail controlen. Eerst moet je een lokale folder (variable 'result_folder') definieren waar naartoe het metadata-bestand weggeschreven kan worden. Met een POST-request op het endpoint *task/result/metadata* wordt dit bestand opgevraagd. Naast de taak-id (in de URL) wordt de Bearer-token (variable my_headers) meegegeven in het verzoek. Als de HTTP-statuscode 200 is wordt het metadata-bestand opgeslagen in opgegeven locatie. Als de doel-map waar het bestand opgeslagen moet worden niet bestaat wordt geprobeerd om deze aan te maken. Het bestand krijgt de naam '*taak-id*_metadata.json’.

```py
result_folder = r"...\Resultaten"

response_get_metadata = requests.get(server + '/task/' + str(task_id) + '/result/metadata', headers=my_headers)

if response_get_metadata.status_code == 200:
    result_data = bytes(response_get_metadata.content)
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    open(os.path.join(result_folder,f"{task_id}_metadata.json"), 'wb').write(response_get_metadata.content)
```

Het resultaat is een json bestand met de volgende inhoud (voor meer informatie over het interpreteren van de resultaten zie ook [Resultaten](05%20Resultaten%20interpreteren.md):

*{*  
*"api_version": "1.2.4",*  
*"user_name": "Wolf Waterman",*  
*"task_started": "2022-02-11 13:18:07",*  
*"task_finished": "2022-02-11 13:26:14",*  
*"success": true,*  
*"module_version": "1.6.0",*  
*"date_check": "2022-02-11T13:18:07.817032",*  
*"duration": 487.0597188472748,*  
*"status": "finished",*  
*"dataset_layers": [*  
*"duikersifonhevel",*  
*"hydroobject",*  
*"regelmiddel"*  
*],*  
*"result_layers": ["duikersifonhevel", "hydroobject", "regelmiddel"],*  
*"missing_layers": ["admingrenswaterschap","afsluitmiddel","afvoergebiedaanvoergebied","aquaduct","beheergrenswaterschap","bodemval","brug",…,"sturing","stuw","vispassage","vispassagevlak","vuilvang","zandvang"*  
*],*  
*"error_layers": [],*  
*"syntax_result": ["duikersifonhevel","hydroobject","regelmiddel"],*  
*"validation_result": ["duikersifonhevel","regelmiddel","hydroobject"]*  
*}*

Lees in [dit hoofdstuk](05%20Resultaten%20interpreteren.md) hoe je de metadata van een validatie kan interpreteren.

### 9. De resultaten in CSV-formaat downloaden

Als er geen fouten voorkomen in de metadata van een afgeronde validatietaak kan je de resultaten downloaden. In deze stap wordt het validatieresultaat als CSV-bestand gedownload. Let op dit is alleen mogelijk als je bij opstarten van de taak het format CSV hebt meegegeven! Hiervoor wordt een GET-request op het endpoint *task/result* verstuurd. Naast de taak-id (in de URL) moet je de taaknaam, de objectlaag gevolgd door ‘.csv' en de Bearer-token (variable my_headers) meegeven. Bij een succesvolle HTTP-statuscode van 200 wordt het CSV-bestand met de validatie-resultaten opgeslagen in de opgegeven locatie. In onderstaand voorbeeld zijn de resultaten van object 'duikersifonhevel’ beschouwd. Let op, voor elke objectlaag moet je een apart CSV-bestand downloaden!

```py
response_get_results_csv = requests.get(server + '/task/' + str(task_id) + '/result/duikersifonhevel.csv', headers=my_headers)
                                
if response_get_results_csv.status_code == 200:
    result_data = bytes(response_get_results_csv.content)
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    open(os.path.join(result_folder,"duikersifonhevel.csv"), 'wb').write(response_get_results_csv.content)
```

Lees in [dit hoofdstuk](05%20Resultaten%20interpreteren.md) hoe je de gedownloade resultaat-objectlagen kan interpreteren.

### 10. De resultaten in GeoPackage-formaat downloaden

Je kan bij de download het GeoPackage-formaat gebruiken om de validatieresultaten in een GIS-programma te bekijken. Let op, dit is alleen mogelijk als je bij het opstarten van de taak het format GeoPackage het meegegeven! Het proces gebeurt op vergelijkbare manier als voor het downloaden van een CSV (zie voorgaande paragraaf). Alleen kan je - in tegenstelling tot het downloaden van een CSV-bestand - in een GeoPackage meerdere objectenlagen opslagen. Er hoeft dus maar 1 GeoPackage-bestand gedownload te worden.

```py
response_get_results_geopackage = requests.get(server + '/task/' + str(task_id) + '/result/geopackage', headers=my_headers)

if response_get_results_geopackage.status_code == 200:
    result_data = bytes(response_get_results_geopackage.content)
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    open(os.path.join(result_folder,"validationresults.gpkg"), 'wb').write(response_get_results_geopackage.content)
```

Lees in [dit hoofdstuk](05%20Resultaten%20interpreteren.md) hoe je de gedownloade resultaat-objectlagen kan interpreteren.

### 11. Alle resultaten van de validatietaak downloaden

Het is ook mogelijk om alle resultaat-bestanden van een taak tegelijk te downloaden in een zip-bestand. Dit zip-bestand bevat zowel de metadata-JSON met de loggegevens als de alle bij het opstarten van de taak opgegeven uitvoerformaten (GeoPackage, CSV, en/of GeoJSON). Hiervoor wordt een GET-request op het endpoint *task/result* verstuurd. Naast de taak-id (in de URL) moet je ook het fomat ‘zip' meegeven. Daarnaast is ook de Bearer-token (variable my_headers) nodig in de request. Bij een successvolle HTTP-statuscode van 200 wordt het zip-bestand met alle validatie-resultaten opgeslagen in de opgegeven locatie.

```py
response_get_all_results = requests.get(server + '/task/' + str(task_id) + '/result/zip', headers=my_headers)

if response_get_all_results.status_code == 200:
    result_data = bytes(response_get_all_results.content)
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    open(os.path.join(result_folder,"validationresults.zip"), 'wb').write(response_get_all_results.content)
```

Lees in [dit hoofdstuk](05%20Resultaten%20interpreteren.md) hoe je de gedownloade resultaat-objectlagen kan interpreteren.

### 12. Een validatietaak annuleren

Het kan voorkomen dat je bijvoorbeeld een validatietaak start die veel doorlooptijd vraagt maar waarvan je in de tussentijd concludeerd dat bij de taak iets niet klopt. Een opgestarte validatietaak kan door de gebruiker geannuleerd worden door een POST request op het endpoint *task/kill* te sturen. Naast de taak-id (in de URL) moet je ook de Bearer-token (variable my\_headers) meegeven. Bij een succesvolle HTTP-statuscode van 202 heeft de API de actie uit het POST-request geaccepteerd en wordt de validatie geannuleerd.

```py
response_kill_task = requests.post(server + '/task/' + str(task_id) + '/kill', headers=my_headers)
                                
if response_kill_task.status_code == 202:
    print('De taak is geannuleerd!')
```

Het resultaat is dat de taak is geannuleerd. Dit kan gecontroleerd worden door de status van de taak op te vragen.

### 13. Een validatietaak verwijderen

Elke validatietaak kan weer verwijderd worden uit de lijst met taken. Alleen validatietaken die gestart zijn én nog uitgevoerd worden kan je niet verwijderen. In dit geval zullen deze validatietaken eerst geannuleerd moeten worden (zie voorgaande paragraaf). Je verwijdert de taak door een DELETE-request op het endpoint *task* te sturen. Naast de taak-id (in de URL) moet ook de Bearer-token (variable my_headers) meegegeven worden. Bij een succesvolle HTTP-statuscode van 200 is de taak verwijderd. Bij het wissen van de taak worden ook alle toegevoegde invoerdatasets en validatieregels verwijderd.

```py
response_delete_task = requests.delete(server + '/task/' + str(task_id), headers=my_headers)
                                
if response_delete_task.status_code == 200:
    print('Taak is verwijderd!')
```
