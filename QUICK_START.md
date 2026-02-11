# 🚀 QUICK START GUIDE
## Get Your System Running in 10 Minutes

---

## ⚡ FASTEST PATH TO DEPLOYMENT

### Step 1: Deploy Backend (3 minutes)

1. **Go to Railway**
   - Visit https://railway.app
   - Sign in with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Select the `backend` folder (or root if backend files are at root)

3. **Wait for Deployment**
   - Railway auto-detects Python/Flask
   - Builds and deploys automatically
   - Wait for "Deployed" status
   - Copy your Railway URL: `https://your-app.up.railway.app`

4. **Test Backend**
   ```bash
   curl https://your-app.up.railway.app/
   ```
   Should return: `{"status": "running"}`

**✅ Backend Done!**

---

### Step 2: Deploy Frontend (3 minutes)

1. **Update API URL**
   - Open `frontend/index.html`
   - Find line: `const API_BASE_URL = '...'`
   - Replace with your Railway URL
   - Save file

2. **Deploy to GitHub Pages**
   - Create GitHub repository
   - Upload `index.html`
   - Go to Settings → Pages
   - Source: Deploy from branch (main)
   - Save

3. **Access Dashboard**
   - GitHub Pages URL: `https://yourusername.github.io/repo-name/`
   - Wait 1-2 minutes for deployment
   - Open URL in browser

**✅ Frontend Done!**

---

### Step 3: Test System (2 minutes)

1. **Open Dashboard**
   - Should show "✅ System Online"
   
2. **Simulate Event**
   - Click "⚡ Simulate Grid Event"
   - See event data appear
   - See detection results

3. **Run Multiple Times**
   - Click 5-10 times
   - Should get mix of normal and anomaly events

4. **Check Metrics**
   - Total events should increase
   - Detection rate should show

**✅ System Working!**

---

## 🔧 ALTERNATIVE: LOCAL TESTING (5 minutes)

### Backend Locally

```bash
# Navigate to backend folder
cd backend

# Install dependencies
pip install -r requirements.txt

# Run server
python app.py
```

Backend runs at: `http://localhost:5000`

### Frontend Locally

```bash
# Navigate to frontend folder
cd frontend

# Update API URL in index.html
# Change to: const API_BASE_URL = 'http://localhost:5000';

# Start simple server
python -m http.server 8000
```

Frontend runs at: `http://localhost:8000`

**Test:** Open `http://localhost:8000` in browser

---

## ✅ VERIFICATION CHECKLIST

After deployment, verify:

- [ ] Backend health endpoint returns `{"status": "running"}`
- [ ] Frontend loads without errors
- [ ] System status shows "✅ System Online"
- [ ] Simulate button works
- [ ] Event data displays
- [ ] Detection results show
- [ ] Metrics update
- [ ] No CORS errors in browser console

---

## 🐛 COMMON ISSUES & FIXES

### Issue: "System Offline"

**Fix:**
```bash
# Test backend directly
curl https://your-railway-url.up.railway.app/

# If it returns JSON, issue is in frontend API_BASE_URL
# Make sure it matches your Railway URL exactly
```

### Issue: CORS Error

**Fix:**
- Backend should have `flask-cors` in `requirements.txt`
- Backend should have `CORS(app)` in `app.py`
- Redeploy backend if missing

### Issue: 404 on Frontend

**Fix:**
- GitHub Pages: Check repo settings → Pages is enabled
- Check file is named `index.html` (not `Index.html`)
- Wait 2-3 minutes for GitHub Pages to build

### Issue: Simulate Button Does Nothing

**Fix:**
1. Open browser console (F12)
2. Look for errors
3. Check Network tab for failed requests
4. Verify API_BASE_URL is correct

---

## 📱 MOBILE ACCESS

After deployment:
- Dashboard works on mobile browsers
- Responsive design
- All features functional
- Share URL with supervisor for remote testing

---

## 🎯 NEXT STEPS

Once system is running:

1. **Run Automated Tests**
   ```bash
   python backend/test_backend.py
   ```

2. **Generate Sample Data**
   - Simulate 20-30 events
   - Get mix of normal and anomalies
   - Build up history for demo

3. **Export Logs**
   - Click "Export Logs" button
   - Verify CSV downloads
   - Check data format

4. **Prepare Demo**
   - Read `SUPERVISOR_DEMO_GUIDE.md`
   - Practice presentation
   - Test on presentation computer

---

## 💡 PRO TIPS

### For Demo Prep
- Simulate 15-20 events before demo
- Ensure at least 3 anomalies in history
- Test export functionality
- Have backup screenshots

### For Development
- Use local backend for faster testing
- Monitor Railway logs for debugging
- Keep API_BASE_URL updated
- Test on multiple browsers

### For Production
- Monitor Railway usage/costs
- Set up error logging
- Consider database for persistent logs
- Add authentication for production use

---

## 📚 NEED MORE HELP?

- **Backend Issues**: See `backend/README.md`
- **Frontend Issues**: See `frontend/README.md`
- **Demo Prep**: See `SUPERVISOR_DEMO_GUIDE.md`
- **Architecture**: See `backend/app.py` comments

---

## 🎉 SUCCESS!

If you've completed all steps:
- ✅ Backend deployed on Railway
- ✅ Frontend deployed on GitHub Pages
- ✅ System running and tested
- ✅ Ready for supervisor demo

**Total Time**: ~10 minutes  
**Status**: Production Ready 🚀

---

**Need rapid support?** Check error logs:
- Railway: Project → Deployments → Logs
- Frontend: Browser Console (F12)
- Backend: Railway logs or local terminal

**You're ready to demonstrate your working AI-powered smart grid cybersecurity system!**
