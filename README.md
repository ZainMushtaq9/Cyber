# Smart Grid Cybersecurity Framework - Backend

AI-Enabled Perceptual Detection System for Smart Grid Security

## 📋 Overview

This backend implements Chunks 0, 1, and 2 of the Smart Grid Cybersecurity Framework:
- **Chunk 0**: System initialization and health monitoring
- **Chunk 1**: Smart grid event simulation
- **Chunk 2**: Perceptual detection layer (3 agents)

## 🏗️ Architecture

### Perceptual Detection Layer

```
Smart Grid Event
       ↓
[Data Fusion Agent] → Structures raw data
       ↓
[Behavioral Envelope Agent] → Calculates deviations
       ↓
[Anomaly Detection Agent] → Applies threshold rules
       ↓
Detection Result + Logging
```

### Agent Details

1. **Data Fusion Agent**
   - Structures raw event data
   - Normalizes sensor readings
   - Prepares system state

2. **Behavioral Envelope Agent**
   - Calculates voltage deviation from baseline (230V)
   - Calculates latency deviation from baseline (20ms)
   - Generates behavioral metrics

3. **Anomaly Detection Agent**
   - Applies deterministic threshold rules
   - Voltage threshold: 15V deviation
   - Latency threshold: 50ms deviation
   - Assigns severity levels: NORMAL, MEDIUM, HIGH, CRITICAL

## 🚀 Deployment

### Railway Deployment (Production)

1. **Prerequisites**
   - Railway account
   - GitHub repository

2. **Deploy Steps**
   ```bash
   # Push code to GitHub
   git add .
   git commit -m "Deploy backend"
   git push origin main
   
   # In Railway Dashboard:
   # 1. Create New Project
   # 2. Deploy from GitHub repo
   # 3. Railway auto-detects Python/Flask
   # 4. Deployment starts automatically
   ```

3. **Environment Variables** (Optional)
   ```
   PORT=5000  # Railway sets this automatically
   ```

4. **Verify Deployment**
   ```bash
   curl https://your-app.up.railway.app/
   # Should return: {"status": "running", ...}
   ```

### Local Development

1. **Setup**
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Run**
   ```bash
   python app.py
   # Server runs on http://localhost:5000
   ```

## 📡 API Endpoints

### Health Check
```http
GET /
```
**Response:**
```json
{
  "status": "running",
  "message": "AI-Enabled Smart Grid Cybersecurity Framework",
  "version": "1.0.0",
  "chunks_active": [0, 1, 2]
}
```

### Simulate Event
```http
GET /simulate
```
**Response:**
```json
{
  "event": {
    "timestamp": "2024-02-11T10:30:00.123456",
    "component": "Transformer_T1",
    "voltage": 225.5,
    "frequency": 50.1,
    "network_latency": 25.3,
    "event_type": "normal"
  },
  "behavioral_metrics": {
    "voltage_deviation": 4.5,
    "latency_deviation": 5.3,
    "frequency": 50.1
  },
  "detection": {
    "is_anomaly": false,
    "severity": "NORMAL",
    "alert_type": "No Anomaly",
    "voltage_anomaly": false,
    "latency_anomaly": false
  }
}
```

### Get Metrics
```http
GET /metrics
```
**Response:**
```json
{
  "total_events": 45,
  "total_anomalies": 13,
  "detection_rate": 28.89
}
```

### Get Logs
```http
GET /logs?limit=10
```
**Response:**
```json
{
  "logs": [...],
  "total_logs": 10
}
```

### Get History
```http
GET /history?limit=10
```
**Response:**
```json
{
  "history": [...],
  "total_in_memory": 10
}
```

### Export Logs (CSV)
```http
GET /export
```
Returns CSV file with all logged events.

## 🧪 Testing

### Manual Testing

1. **Health Check Test**
   ```bash
   curl https://your-app.up.railway.app/
   ```
   Expected: JSON response with "status": "running"

2. **Simulation Test**
   ```bash
   curl https://your-app.up.railway.app/simulate
   ```
   Expected: Full event data with detection results

3. **Metrics Test**
   ```bash
   curl https://your-app.up.railway.app/metrics
   ```
   Expected: Current metrics

4. **Repeated Simulation** (10 times)
   ```bash
   for i in {1..10}; do
     curl https://your-app.up.railway.app/simulate
     echo ""
   done
   ```
   Expected: Mix of normal and anomaly events

### Automated Testing Script

Create `test_backend.py`:
```python
import requests
import json

BASE_URL = "https://your-app.up.railway.app"

def test_health():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "running"
    print("✅ Health check passed")

def test_simulation():
    response = requests.get(f"{BASE_URL}/simulate")
    assert response.status_code == 200
    data = response.json()
    assert "event" in data
    assert "detection" in data
    print(f"✅ Simulation passed - {data['detection']['alert_type']}")

def test_metrics():
    response = requests.get(f"{BASE_URL}/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "total_events" in data
    print(f"✅ Metrics passed - {data['total_events']} events")

if __name__ == "__main__":
    test_health()
    for i in range(10):
        test_simulation()
    test_metrics()
    print("\n✅ All tests passed!")
```

Run:
```bash
python test_backend.py
```

## 📊 Logging System

### Log Format (JSONL)
Each event is logged to `event_logs.jsonl`:
```json
{"timestamp": "2024-02-11T10:30:00", "component": "Transformer_T1", "voltage": 225.5, "frequency": 50.1, "network_latency": 25.3, "voltage_deviation": 4.5, "latency_deviation": 5.3, "is_anomaly": false, "severity": "NORMAL", "alert_type": "No Anomaly"}
```

### Accessing Logs
- **API**: `GET /logs?limit=N`
- **Export**: `GET /export` (CSV format)
- **File**: Read `event_logs.jsonl` directly

## 🔧 Configuration

### Detection Thresholds
Modify in `app.py`:
```python
VOLTAGE_THRESHOLD = 15.0   # Volts
LATENCY_THRESHOLD = 50.0   # Milliseconds
BASELINE_VOLTAGE = 230.0   # Volts
BASELINE_LATENCY = 20.0    # Milliseconds
```

### Event Generation Probabilities
```python
is_attack = random.random() < 0.3  # 30% attack, 70% normal
```

## 📈 Metrics & Monitoring

### Real-time Metrics
- Total events processed
- Total anomalies detected
- Detection rate (%)

### Event History
- Last 100 events stored in memory
- Full history in `event_logs.jsonl`

## 🔮 Future Layers (Placeholders)

The following endpoints exist for future implementation:
- `POST /threat-model` - Threat Modeling Layer
- `POST /cascade-predict` - Cascade Prediction Layer

Currently return 501 (Not Implemented).

## 🐛 Troubleshooting

### CORS Issues
Ensure `flask-cors` is installed and CORS is enabled:
```python
from flask_cors import CORS
CORS(app)
```

### Port Issues on Railway
Railway auto-assigns PORT. Code uses:
```python
port = int(os.environ.get('PORT', 5000))
```

### Logs Not Persisting
Railway has ephemeral filesystem. Logs reset on redeploy.
For persistent logs, consider:
- Database integration
- External logging service
- Cloud storage

## 📞 Support

For issues or questions:
1. Check Railway logs
2. Verify CORS settings
3. Test endpoints with curl
4. Review error messages in browser console

## 📄 License

Academic project - Smart Grid Cybersecurity Framework
