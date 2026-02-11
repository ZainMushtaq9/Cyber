# 🔒 AI-Enabled Cybersecurity Framework for Smart Grid Threat Modeling

## Production-Ready Smart Grid Agentic AI System

### 📋 Project Overview

This framework implements an intelligent cybersecurity system for smart grid infrastructure, featuring:
- **Real-time threat detection**
- **Anomaly analysis using perceptual AI agents**
- **Event simulation and monitoring**
- **Scalable architecture for advanced threat modeling**

---

## 🏗️ System Architecture

```
Frontend (HTML/CSS/JS)
        ↓
Railway Backend (FastAPI)
        ↓
Smart Grid Simulator
        ↓
Perceptual Agents
        ↓
(Threat Modeling Layers - Planned)
```

### Active Components (Chunks 0-2)

✅ **Chunk 0: Cloud Foundation**
- Railway deployment
- Health monitoring
- CORS configuration

✅ **Chunk 1: Smart Grid Simulator**
- Event generation (70% normal, 30% attack)
- Component simulation
- Realistic parameter ranges

✅ **Chunk 2: Perceptual Detection Layer**
- DataFusionAgent
- BehavioralEnvelopeAgent
- AnomalyDetectionAgent

### Planned Components (Architectural Placeholders)

🔄 **Threat Modeling Layer**
- ArchitecturalAnalyzerAgent
- ThreatContextWeaverAgent

🔄 **Cascade Prediction Layer**
- CascadePredictorAgent
- GoalInferencerAgent

🔄 **Strategic Orchestration Layer**
- CognitiveOrchestratorAgent
- MitigationGeneratorAgent
- ResourceSchedulerAgent

---

## 🚀 Backend Deployment (Railway)

### Prerequisites
- Railway account
- GitHub repository

### Step 1: Deploy to Railway

1. **Create New Project in Railway**
   - Go to [Railway.app](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub repo"

2. **Configure Environment**
   - Add environment variable: `GROQ_API_KEY` (if needed for future features)
   - Railway will auto-detect Python and use `Procfile`

3. **Deploy**
   - Railway will automatically:
     - Install dependencies from `requirements.txt`
     - Run the application using `Procfile`
     - Assign a public URL

### Step 2: Verify Deployment

Test the health endpoint:
```bash
curl https://cyber-production-7ec6.up.railway.app/
```

Expected response:
```json
{
  "status": "Smart Grid Agentic Framework Running",
  "version": "1.0.0",
  "chunks_active": ["0", "1", "2"],
  "timestamp": "2024-XX-XXTXX:XX:XX"
}
```

---

## 💻 Frontend Setup

### Option 1: GitHub Pages

1. **Push to GitHub Repository**
   ```bash
   git add index.html style.css script.js
   git commit -m "Deploy Smart Grid Framework frontend"
   git push origin main
   ```

2. **Enable GitHub Pages**
   - Go to repository Settings
   - Navigate to "Pages"
   - Select source: `main` branch
   - Save

3. **Access Dashboard**
   - URL: `https://[username].github.io/[repository]/`

### Option 2: Local Development

```bash
# Simply open index.html in a browser
# Or use a local server:
python -m http.server 8080
# Access: http://localhost:8080
```

---

## 📡 API Endpoints

### 1. Health Check
```
GET /
```
Returns system status and version information.

### 2. Simulate Grid Event
```
GET /simulate
```

**Response (Normal Operation):**
```json
{
  "status": "Normal Operation",
  "event": {
    "component": "DER",
    "voltage": 235.4,
    "frequency": 50.1,
    "latency": 45.2,
    "timestamp": "2024-XX-XX..."
  },
  "metrics": {
    "voltage_deviation": 5.4,
    "latency_deviation": -4.8,
    "frequency_deviation": 0.1
  }
}
```

**Response (Anomaly Detected):**
```json
{
  "status": "Anomaly Detected",
  "event": { ... },
  "alert": {
    "anomaly_detected": true,
    "anomalies": [
      {
        "type": "Voltage Anomaly",
        "severity": "High",
        "deviation": 35.2
      }
    ],
    "total_anomalies": 1
  },
  "metrics": { ... }
}
```

### 3. System Information
```
GET /system-info
```
Returns architecture and agent information.

---

## 🔧 Configuration

### Backend (`app.py`)
- **PORT**: Auto-configured by Railway (default: 8000)
- **CORS**: Enabled for all origins
- **Thresholds**:
  - Voltage anomaly: ±15V from 230V baseline
  - Latency anomaly: ±120ms from 50ms baseline

### Frontend (`script.js`)
- **API_BASE_URL**: Update if backend URL changes
  ```javascript
  const API_BASE_URL = 'https://cyber-production-7ec6.up.railway.app';
  ```

---

## 🎯 Usage

### 1. Open Frontend Dashboard
Navigate to your deployed frontend URL.

### 2. Simulate Grid Event
Click the "⚡ Simulate Grid Event" button.

### 3. Monitor Results
- **Grid Event Data**: Component readings
- **Detection Status**: Normal/Anomaly badge
- **System Metrics**: Deviation values
- **Alert Information**: Anomaly details (if detected)

### 4. Interpret Results

**Green Status (Normal)**
- All parameters within acceptable ranges
- Minor deviations are acceptable

**Red Status (Anomaly)**
- Critical parameter deviations detected
- High/Medium severity alerts
- Immediate attention required

---

## 📊 Detection Logic

### Anomaly Rules

1. **Voltage Anomaly**
   - Triggered when: `|voltage - 230V| > 15V`
   - Severity:
     - High: deviation > 25V
     - Medium: deviation 15-25V

2. **Network Anomaly**
   - Triggered when: `|latency - 50ms| > 120ms`
   - Severity:
     - High: deviation > 200ms
     - Medium: deviation 120-200ms

---

## 📁 File Structure

```
project/
│
├── app.py                 # FastAPI backend
├── requirements.txt       # Python dependencies
├── Procfile              # Railway deployment config
│
├── index.html            # Frontend dashboard
├── style.css             # Styling
├── script.js             # API integration
│
└── README.md             # Documentation
```

---

## 🐛 Troubleshooting

### Backend Issues

**Problem**: Backend not responding
- **Solution**: Check Railway logs, verify deployment status

**Problem**: CORS errors
- **Solution**: Ensure CORS middleware is enabled in `app.py`

### Frontend Issues

**Problem**: "Backend Offline" status
- **Solution**: 
  1. Verify backend URL in `script.js`
  2. Check backend is running
  3. Test health endpoint manually

**Problem**: No data displaying
- **Solution**: Open browser console (F12) to check for errors

---

## 🔄 Future Enhancements (Next Phases)

### Phase 2: Threat Modeling
- Activate ArchitecturalAnalyzerAgent
- Implement ThreatContextWeaverAgent
- Add MITRE ATT&CK mapping

### Phase 3: Cascade Prediction
- NetworkX graph integration
- CascadePredictorAgent implementation
- Goal inference logic

### Phase 4: Strategic Layer
- Cognitive orchestration
- Automated mitigation
- Resource scheduling

---

## 📞 Support

For issues or questions:
1. Check Railway logs for backend errors
2. Inspect browser console for frontend errors
3. Verify API endpoint connectivity
4. Review this documentation

---

## 📄 License

Production deployment for Smart Grid Cybersecurity Framework v1.0.0

---

## ✅ Deployment Checklist

- [ ] Backend deployed to Railway
- [ ] Environment variables configured
- [ ] Health endpoint responding
- [ ] Frontend deployed to GitHub Pages
- [ ] API_BASE_URL updated in script.js
- [ ] Test simulation working
- [ ] Anomaly detection functioning
- [ ] All panels displaying correctly

---

**Status**: ✅ Production Ready | **Version**: 1.0.0 | **Chunks Active**: 0, 1, 2
