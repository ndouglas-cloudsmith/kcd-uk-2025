# kcd-uk-2025
Random scripts for the KCD workshop

```
cat <<'EOF' > Dockerfile
FROM python:3.11-slim

# Install the legitimate requests package
RUN pip install requests

# --- Create and install the FAKE package ---

# 1. Make a temporary directory for our fake package
# 2. Write a minimal setup.py file (using 'printf' for portability)
# 3. Use pip to "install" this local, fake package
# 4. Clean up the temporary directory
RUN mkdir /fake-pkg && \
    printf "from setuptools import setup\nsetup(name='reuests', version='0.0.1')" > /fake-pkg/setup.py && \
    pip install /fake-pkg && \
    rm -rf /fake-pkg

# --- End of new section ---

# Just to show the container can run
CMD ["python", "-c", "import requests; print('Container is running. Requests version:', requests.__version__)"]
EOF

ls | grep Dockerfile
```

```
docker build -t typosquatted-image:latest .
```

```
docker tag typosquatted-image:latest docker.cloudsmith.io/acme-corporation/acme-repo-one/typosquatted-image:latest
```
```
docker login docker.cloudsmith.io -u "$USERNAME" -p "$CLOUDSMITH_API_KEY"
```
```
docker push docker.cloudsmith.io/acme-corporation/acme-repo-one/typosquatted-image:latest
```

```
kubectl create ns malware
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: typosquatted-pod
  namespace: malware
  labels:
    app: ai-image
spec:
  replicas: 3
  selector:
    matchLabels:
      app: typosquatted-image
  template:
    metadata:
      labels:
        app: typosquatted-image
    spec:
      containers:
        - name: typosquatted-image-container
          image: docker.cloudsmith.io/acme-corporation/acme-repo-one/typosquatted-image:latest
          imagePullPolicy: Always # force pull on every pod start
          ports:
            - containerPort: 8080
EOF
```

Install syft (Linux/macOS)
```
curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin
```

Then run it on your image:
```
syft typosquatted-image:latest
```

List the pip packages running within the pod:
```
docker run --rm docker.cloudsmith.io/acme-corporation/acme-repo-one/typosquatted-image:latest pip list
```

```
cat <<EOF > deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: insecure-web-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web-container
        image: nginx:1.18.0
        ports:
        - containerPort: 80
        securityContext:
          runAsUser: 0
          allowPrivilegeEscalation: true
          privileged: true
        resources: {}
EOF
```

```
export TMPDIR=/tmp
trivy config deployment.yaml
```

```
trivy config --severity HIGH deployment.yaml
```
