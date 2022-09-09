# Docker exercises

## 1. Hello world
Je zou het niet je eerste Docker container mogen noemen, als we niet met `Hello world` zouden beginnen.

De opdracht:
- Open een Command Prompt of Terminal
- Haal het [Hello world](https://hub.docker.com/_/hello-world) image binnen en run deze.
- Je zou nu logging voorbij moeten zien komen met daarin de tekst `Hello from Docker!`.

## 2. Python API
Hieronder staat een `main.py` (een Python [FastAPI](https://fastapi.tiangolo.com/) API) en een `requirements.txt` met libraries.
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
  return {"message": "Welcome"}
  
@app.get("/hello/{name}")
def read_hello(name: str):
  return {"message": f"Hello {name}"}
```
```text
fastapi==0.75.1
uvicorn==0.17.6
```

De opdracht:
- Sla deze bestanden op in map op je laptop.
- Voeg een `Dockerfile` toe waarin onderstaande instructies worden uitgevoerd zie ook de [Dockerfile documentatie](https://docs.docker.com/engine/reference/builder/):
    - Definieer het base image en gebruik hiervoor een standaard [Python image](https://hub.docker.com/_/python).
    - Kopieer de bestanden in het image.
    - Installeer de libraries uit de `requirements.txt`.
    - Specifieer het commando van het Docker image. Gebruik hiervoor `uvicorn main:app`.
- Bouw het image
- Run de gemaakte Docker container
- Probeer de API aan te roepen vanaf je laptop. Je zult merken dat dit nog niet lukt.
- Ga verder naar [2.1 Debuggen van de Docker container](#21-debuggen-van-de-docker-container)

### 2.1 Debuggen van de Docker container
Is het gelukt de Docker container te bouwen, maar kun je hem niet aanroepen? Dan wordt het tijd dat we eens in een draaiende Docker container gaan kijken.

Dit kunnen we op 3 manieren doen:
- We kunnen een commando of interactieve shell openen in een draaiende container.
    - `docker exec -it {container} {commando of shell}`.
- Of we kunnen bij het starten van de docker container het run commando overschrijven.
    - `docker run -it {image} {commando of shell}`.
- Mocht het Docker image voorzien zijn van een [entrypoint](https://docs.docker.com/engine/reference/builder/#entrypoint), dan dienen we deze te overschrijven.
    - `docker run -it --entrypoint {commando of shell} {image}`

> Het verschil tussen CMD en Entrypoint:
>
> CMD sets default command and/or parameters, which can be overwritten from command line when docker container runs.
>
> ENTRYPOINT command and parameters will not be overwritten from command line. Instead, all command line arguments will be added after ENTRYPOINT parameters.

Aangezien we hier willen debuggen of onze code draait kiezen we voor de eerste aanpak:

De opdracht:
- Start de container
- Open een shell
- Valideer dat de API draait en dat je hem binnen de container kunt benaderen. Er zijn allerlei Linux tools die je hierbij kunnen helpen, hieronder 2 voorbeelden:
    - [WGET](https://www.gnu.org/software/wget/) of [CURL](https://curl.se/), voer een request via de command line uit naar de API.
    - [Netstat](https://en.wikipedia.org/wiki/Netstat), controleer wat er draait op welke poort.
> Mogelijk beschikt onze Docker container niet over de juiste tooling voor het debuggen. Deze dienen we te installeren.
> Dit kun je in de Docker container doen of in het image d.m.v. de Dockerfile. Bij het direct installeren in de conatiner is de tooling verdwenen na een herstart van deze container.
- Repareer het commando in de Dockerfile. Je zult hiervoor het `--host` argument dienen toe te voegen.

## 3. Environment variabelen
Bij het ontwikkelen van software, zijn er altijd omgevingsspecifieke variabelen die je wilt kunnen wijzigen. Zo heeft ook Docker hier een oplossing voor.

In onze Dockerfile hebben we gespecificeerd dat we onze API opstarten met [Uvicorn](https://www.uvicorn.org/). Standaard draait deze webserver op poort 8000.

De opdracht:
- Wijzig de Dockerfile zodat het poort nummer waarop Uvicorn wordt geserveerd vanaf een environment variabele wordt veranderd. Je zult hiervoor het `--port` argument dienen toe te voegen aan het uvicorn commando.
- Bouw vervolgens het image opnieuw en run deze waarbij je het poort nummer 8080 als environment variabele mee geeft.

## 4. Volumes
Binnen Docker is het mogelijk om een volume te mounten in je container. Aangezien een Docker container zelf geen state heeft, kun je het volume gebruiken om je state op weg te schrijven.

Tijdens ontwikkelen van code in een Docker container is het handig om de source code als een volume te mounten. Wanneer je dit doet, worden de gemaakte wijziginen aan de code direct beschikbaar in de container.

De opdracht:
- Mount de code als een volume in je Docker container.
- Wijzig daarnaast het run commando van uvicorn zodat deze automatische herstart bij aangebrachte wijzigingen. Gebruik hiervoor het `--reload` argument.
- Bouw en run de Docker container.
- En breng een wijziging in de code aan en valideer dat de wijziging direct in de Docker container is doorgevoerd.
