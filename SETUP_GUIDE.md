# 🚀 Complete Setup Guide - Fitness App

## 📋 Prerequisites Checklist

Before starting, ensure you have:
- ✅ Python 3.8+ installed
- ✅ pip package manager
- ✅ Git (for cloning)
- ✅ Web browser
- ✅ Internet connection

## 🎯 Quick Setup (Demo Mode)

### Step 1: Get the Project
```bash
git clone https://github.com/aditya3singh/fitness-app.git
cd fitness-app
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the App
```bash
python -m streamlit run app.py
```

### Step 4: Open in Browser
Navigate to: **http://localhost:8501**

**🎉 That's it! Your app is running in Demo Mode!**

## 🔧 Production Setup (Real Database)

### Option A: HarperDB Cloud (Recommended)

#### Step 1: Create HarperDB Account
1. Go to [HarperDB Cloud](https://harperdb.io/)
2. Click "Get Started Free"
3. Sign up with email/password
4. Verify your email

#### Step 2: Create Instance
1. Click "Create Instance"
2. Choose "Cloud Instance"
3. Select region (closest to you)
4. Choose plan (Free tier available)
5. Click "Create Instance"

#### Step 3: Get Credentials
1. Go to "Instance Details"
2. Copy your instance URL
3. Note your username/password
4. Save these securely

#### Step 4: Update Configuration
Edit `config.py`:
```python
SETUP_TYPE = "CLOUD"
HARPERDB_CONFIG = {
    "url": "https://your-instance.harperdbcloud.com",
    "username": "your_actual_username",
    "password": "your_actual_password"
}
```

#### Step 5: Create Database Schema
1. Open HarperDB Studio (from instance)
2. Create schema: `workout_repo`
3. Create table: `workouts`
4. Create table: `workout_today`
5. Set up proper indexes

### Option B: Local HarperDB

#### Step 1: Download HarperDB
1. Go to [HarperDB Downloads](https://harperdb.io/download/)
2. Download Community Edition
3. Extract to a folder

#### Step 2: Start HarperDB
```bash
cd harperdb-community
java -jar harperdb.jar
```

#### Step 3: Set Password
1. Open browser to `http://localhost:9925`
2. Set admin password
3. Note credentials

#### Step 4: Update Configuration
Edit `config.py`:
```python
SETUP_TYPE = "LOCAL"
LOCAL_HARPERDB_CONFIG = {
    "url": "http://localhost:9925",
    "username": "HDB_ADMIN",
    "password": "your_local_password"
}
```

## 🗄️ Database Schema Setup

### Required Tables

#### 1. workouts Table
```sql
CREATE TABLE workout_repo.workouts (
    video_id VARCHAR(20) PRIMARY KEY,
    title VARCHAR(500),
    channel VARCHAR(200),
    duration INTEGER,
    view_count INTEGER,
    like_count INTEGER,
    channel_id VARCHAR(50),
    categories TEXT,
    tags TEXT
);
```

#### 2. workout_today Table
```sql
CREATE TABLE workout_repo.workout_today (
    id INTEGER PRIMARY KEY,
    video_id VARCHAR(20),
    title VARCHAR(500),
    channel VARCHAR(200),
    duration INTEGER
);
```

#### 3. Insert Sample Data
```sql
INSERT INTO workout_repo.workout_today (id, video_id, title, channel, duration) 
VALUES (0, 'dQw4w9WgXcQ', 'Sample Workout', 'Demo Channel', 1800);
```

## 🧪 Testing Your Setup

### Test 1: Basic Functionality
1. Run the app
2. Check "Today's Workout" loads
3. Verify "All Workouts" shows data
4. Test "Add Workout" with YouTube URL

### Test 2: Database Operations
1. Add a new workout
2. Check if it appears in "All Workouts"
3. Delete a workout
4. Verify deletion worked

### Test 3: Error Handling
1. Try invalid YouTube URLs
2. Check error messages
3. Verify app doesn't crash

## 🐛 Common Issues & Solutions

### Issue 1: "Module not found"
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue 2: "Streamlit not recognized"
**Solution**: Use Python module syntax
```bash
python -m streamlit run app.py
```

### Issue 3: "Database connection failed"
**Solutions**:
- Check credentials in `config.py`
- Verify HarperDB instance is running
- Use Demo mode for testing

### Issue 4: "YouTube extraction failed"
**Solutions**:
- Check URL format
- Ensure video is public
- Try different workout videos

### Issue 5: "Port already in use"
**Solution**: Use different port
```bash
python -m streamlit run app.py --server.port 8502
```

## 🔒 Security Best Practices

### Environment Variables
1. Never commit real credentials
2. Use `.env` files (not included in repo)
3. Set up proper access controls

### Database Security
1. Use strong passwords
2. Limit database access
3. Regular backups
4. Monitor usage

### App Security
1. Input validation
2. Error handling
3. Rate limiting (if needed)
4. HTTPS in production

## 🚀 Deployment Options

### Streamlit Cloud (Easiest)
1. Push to GitHub
2. Connect Streamlit Cloud account
3. Deploy automatically
4. Get public URL

### Heroku
1. Add `Procfile`
2. Set environment variables
3. Deploy via CLI
4. Scale as needed

### AWS/GCP
1. Use Docker containers
2. Set up load balancers
3. Configure auto-scaling
4. Monitor performance

## 📊 Performance Optimization

### Caching Strategy
- Streamlit caching for workouts
- Database connection pooling
- YouTube data caching

### Database Optimization
- Proper indexes
- Query optimization
- Connection pooling
- Regular maintenance

### App Performance
- Lazy loading
- Pagination for large lists
- Optimized video loading
- Responsive design

## 🔄 Maintenance

### Regular Tasks
1. Update dependencies monthly
2. Monitor database performance
3. Check for YouTube API changes
4. Backup data regularly

### Updates
1. Pull latest changes
2. Test in staging
3. Deploy to production
4. Monitor for issues

## 📞 Support Resources

### Documentation
- [Streamlit Docs](https://docs.streamlit.io/)
- [HarperDB Docs](https://docs.harperdb.io/)
- [YouTube-dl Docs](https://github.com/ytdl-org/youtube-dl)

### Community
- [Streamlit Community](https://discuss.streamlit.io/)
- [HarperDB Community](https://community.harperdb.io/)
- [GitHub Issues](https://github.com/aditya3singh/fitness-app/issues)

### Troubleshooting
- Check logs for errors
- Verify configurations
- Test components individually
- Use Demo mode for isolation

---

## 🎯 Next Steps

1. **Test Demo Mode** - Ensure everything works
2. **Choose Database Option** - Cloud or Local
3. **Set Up Production** - Configure real database
4. **Customize App** - Add your own features
5. **Deploy** - Share with others

**🚀 Your fitness app is ready to help people get fit!**
