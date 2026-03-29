# sysmon-dashboard

A full-stack system monitoring dashboard that displays live CPU, memory, disk, and network stats via a Flask REST API. The frontend auto-refreshes every 3 seconds.

## Tech Stack
- **Backend:** Python, Flask, psutil
- **Frontend:** HTML, CSS, vanilla JavaScript
- **DevOps:** Docker, GitHub Actions CI
- **Testing:** pytest

## Running locally
```bash
git clone https://github.com/an0ushkaaa/sysmon-dashboard
cd sysmon-dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```
Open `http://localhost:5000`

## Running with Docker
```bash
docker build -t sysmon-dashboard .
docker run -p 5000:5000 sysmon-dashboard
```

## API
`GET /metrics` — returns live system stats as JSON

## CI
GitHub Actions runs pytest and builds the Docker image on every push to master.