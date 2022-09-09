# Kubernetes exercises

## 1. Je eerste applicatie uitrollen
Maak eerst een namespace met de naam test aan in je Kubernetes cluster: `kubectl create namespace test`
We gaan onderstaande yaml configuraties van een applicatie uitrollen op jouw lokale Kubernetes cluster. Bestudeer het eerste yaml bestand en probeer deze uit te rollen op jouw lokale Kubernets cluster.
```yaml
# pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: demo
  namespace: test
  labels:
    app: demo
spec:
  containers:
    - name: demo
      image: mvanderheijden/demo:latest
      ports:
        - containerPort: 8000
          protocol: TCP
      resources:
        limits:
          cpu: 50m
          memory: 128Mi
        requests:
          cpu: 10m
          memory: 64Mi
```

### 1.1 Port forward
Leg een port-forward naar de container is de aangemaakte pod.
Ga vervolgens met de browser naar deze container poort toe en valideer dat de applicatie draait.

## 2 Toevoegen van een service
Met behulp van onderstaande service.yaml gaan we een service boven onze applicatie plaatsen voor de load balancing.
```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: demo
  namespace: test
spec:
  selector:
    app: demo
  ports:
    - port: 8000
      protocol: TCP
      targetPort: 8000
```
### 2.1 Port forward
Leg een port-forward naar de service en valideer met behulp van de browser dat de applicatie bereikbaar is.

## 3. Toevoegen van een Ingress
Met behulp van onderstaande ingress.yaml zorgen we ervoor dat de service van buiten het Kubernetes cluser te benaderen is (in dit geval localhost omdat we hier een Kubernetes cluster op je laptop hebben).
```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/rewrite-target: /$2
  name: demo
  namespace: test
spec:
  rules:
    - host: localhost
      http:
        paths:
          - backend:
              service:
                name: demo
                port:
                  number: 8000
            path: /demo(/|$)(.*)
            pathType: Prefix
```
### 3.1 Benader de applicatie
Ga in je browser naar http://localhost/demo/hello/deelnemer

## 4. Uitrollen met behulp van een deployment.yaml
We gaan nu de applicatie uitrollen dmv een deployment in plaats van rechtstreeks een pod.yaml
Verwijder eerst de pod.yaml: `kubectl --namespace test delete pod demo`
Creeer vervolgens de deployment door middel van onderstaande yaml. En valideer dat deze draait.
```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo
  namespace: test
  labels:
    app: demo
spec:
  replicas: 1
  strategy:
    type: RollingUpdate
  selector:
    matchLabels:
      app: demo
  template:
    metadata:
      name: demo
      labels:
        app: demo
    spec:
      containers:
        - name: demo-container
          image: mvanderheijden/demo:latest
          ports:
            - containerPort: 8000
              protocol: TCP
          resources:
            limits:
              cpu: 50m
              memory: 128Mi
            requests:
              cpu: 10m
              memory: 64Mi
```

### 4.1 Je applicatie schalen
Er zijn 2 manieren waarop je een applicatie kunt schalen. Horizontaal en verticaal.

Eerst gaan we verticaal schalen:
- Wijzig de deployment en verhoog de resources. CPU en Memory.
    - Gebruik hiervoor het commando `kubectl edit deployment`.
- Valideer dat de applicatie meer resources heeft gekregen.
Nu gaan we horizontaal schalen.
- Wijzig het aantal instanties van je applicatie.
    - Gebruik hiervoor het commando `kubectl scale deployment`.
- Valideer dat er meerder instanties draaien.