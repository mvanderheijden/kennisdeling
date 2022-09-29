# Helm exercises

## 1. Maak een Helm Chart
Maak van de `service.yaml`, `ingress.yaml` en `deployment.yaml` uit de kubernetes exercises een Helm Chart.
Zet hiervoor onderstaande mappen structuur op:
```
demo (map)
    templates (map)
        deployment.yaml (file)
        ingress.yaml (file)
        service.yaml (file)
    Chart.yaml (file)
    values.yaml
```
Zorg ervoor dat je in de `Chart.yaml` in ieder geval de volgende 3 keys hebt gedefinieerd: version, apiVersion, name.
Voor nu kun je de de `values.yaml` leeg laten.

We gaan nu de Helm Chart valideren en uitrollen:
- Run het commando: `helm lint` en valideer dat je geen errors ziet
- Run het commando: `helm template -f values.yaml --namespace test demo .` bekijk de template bestanden.
- Run het commando: `helm install -f values.yaml --namespace test demo .` de Helm Chart wordt nu uitgerold.
- Ga in je browser naar `http://localhost/hello/deelnemer` en valideer dat je applicatie draait.
- Run het commando: `helm ls --namespace demo` je zult hier details van je uitgerolde Helm Chart zien.
- Ruim de Helm Chart weer op met het commando: `helm uninstall --namespace test demo`

## 2. Values templaten
Zorg ervoor dat het poort nummer en het aantal instanties (replicas) vanuit de `values.yaml` wordt ingevuld.
Vul daarnaast de namespace in door gebruik te maken van de namepace in de release
Gebruik hiervoor `{{ .Values.Port }}`, `{{ .Values.Port }}` en `{{ .Release.Namespace }}`
Valideer of het werkt door middel van de validatie en uitrol stappen uit exercise 1.