# HarperDB Configuration
# Choose your setup: CLOUD, LOCAL, or DEMO

# Option 1: HarperDB Cloud (Recommended)
HARPERDB_CONFIG = {
    "url": "https://your-instance.harperdbcloud.com",  # Replace with your actual HarperDB URL
    "username": "your_username",                       # Replace with your actual username
    "password": "your_password"                        # Replace with your actual password
}

# Option 2: Local HarperDB (Free)
LOCAL_HARPERDB_CONFIG = {
    "url": "http://localhost:9925",
    "username": "HDB_ADMIN",
    "password": "your_local_password"  # Replace with your local password
}

# Option 3: Demo Mode (No Database - For Testing)
DEMO_CONFIG = {
    "url": "demo",
    "username": "demo",
    "password": "demo"
}

# Database Schema and Tables
SCHEMA = "workout_repo"
TABLE = "workouts"
TABLE_TODAY = "workout_today"

# Choose your setup here:
# "CLOUD" = Use HarperDB Cloud
# "LOCAL" = Use Local HarperDB
# "DEMO" = Demo mode (no database needed)
SETUP_TYPE = "DEMO"  # Change this to "CLOUD" or "LOCAL" when ready

# Get the right config based on setup type
if SETUP_TYPE == "CLOUD":
    config = HARPERDB_CONFIG
elif SETUP_TYPE == "LOCAL":
    config = LOCAL_HARPERDB_CONFIG
else:
    config = DEMO_CONFIG

print(f"🔧 Using {SETUP_TYPE} configuration")
if SETUP_TYPE == "DEMO":
    print("📝 Note: Demo mode - no database connection needed for testing")
