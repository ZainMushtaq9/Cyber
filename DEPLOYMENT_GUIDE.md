# 🚀 QUICK DEPLOYMENT GUIDE

## Step 1: Backend Deployment (Railway)

### Upload Backend Files to Your Repository
1. Upload these files to your GitHub repository:
   - `app.py`
   - `requirements.txt`
   - `Procfile`
   - `.gitignore`

### Deploy to Railway
1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway will auto-detect Python and deploy
5. Your backend URL: `https://cyber-production-7ec6.up.railway.app`

### Verify Backend
```bash
curl https://cyber-production-7ec6.up.railway.app/
```
Should return:
```json
{"status": "Smart Grid Agentic Framework Running"}
```

---

## Step 2: Frontend Deployment

### Option A: GitHub Pages (Recommended)
1. Upload frontend files to your repository:
   - `index.html`
   - `style.css`
   - `script.js`

2. Go to repository Settings → Pages
3. Select source: `main` branch
4. Save and access at: `https://[username].github.io/[repo]/`

### Option B: Local Testing
Just open `index.html` in your browser!

---

## Step 3: Test Integration

1. Open your frontend dashboard
2. Click "⚡ Simulate Grid Event"
3. Observe:
   - Event data displays
   - Status shows Normal/Anomaly
   - Metrics update
   - Alerts appear (if anomaly)

---

## 🎯 What Each File Does

### Backend Files (Railway)
- **app.py** - Main FastAPI application with AI agents
- **requirements.txt** - Python dependencies
- **Procfile** - Railway deployment configuration
- **.gitignore** - Ignore unnecessary files

### Frontend Files (GitHub Pages)
- **index.html** - Dashboard UI
- **style.css** - Dark cybersecurity theme
- **script.js** - API integration & dynamic updates

---

## ✅ Success Criteria

- ✓ Backend returns JSON on /simulate
- ✓ Frontend displays event data
- ✓ Anomalies trigger red alerts
- ✓ Normal events show green status
- ✓ Metrics update correctly

---

## 🔧 If Something's Wrong

### Backend Issues
- Check Railway logs
- Verify Procfile is present
- Ensure requirements.txt has correct versions

### Frontend Issues
- Open browser console (F12)
- Check API_BASE_URL in script.js matches your Railway URL
- Verify CORS is enabled in backend

---

## 📁 File Organization

```
Backend Repository (Railway):
├── app.py
├── requirements.txt
├── Procfile
└── .gitignore

Frontend Repository (GitHub Pages):
├── index.html
├── style.css
└── script.js
```

OR combine all in one repository - works either way!

---

## 🎊 You're Done!

Your Smart Grid Cybersecurity Framework is production-ready!

Check README.md for detailed documentation.
