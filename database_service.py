import harperdb
from config import config, SCHEMA, TABLE, TABLE_TODAY

# Initialize database connection
db = None
if config["url"] != "demo":
    try:
        db = harperdb.HarperDB(
            url=config["url"],
            username=config["username"],
            password=config["password"]
        )
        print(f"✅ Connected to HarperDB at: {config['url']}")
    except Exception as e:
        print(f"❌ Failed to connect to HarperDB: {e}")
        print("Please check your configuration in config.py")
        db = None
else:
    print("🎭 Running in DEMO mode - no database connection needed")

# Demo data for testing
DEMO_WORKOUTS = [
    {
        "video_id": "dQw4w9WgXcQ",
        "channel": "Demo Channel",
        "title": "Full Body HIIT Workout - Demo",
        "duration": 1800
    },
    {
        "video_id": "abc123def",
        "channel": "Demo Channel",
        "title": "Yoga for Beginners - Demo",
        "duration": 2700
    }
]

def insert_workout(workout_data):
    if config["url"] == "demo":
        print("🎭 Demo mode: Workout would be inserted")
        return {"message": "Demo mode - workout not actually saved"}

    if not db:
        print("❌ Database not connected")
        return None
    try:
        return db.insert(SCHEMA, TABLE, [workout_data])
    except Exception as e:
        print(f"❌ Error inserting workout: {e}")
        return None

def delete_workout(workout_id):
    if config["url"] == "demo":
        print("🎭 Demo mode: Workout would be deleted")
        return {"message": "Demo mode - workout not actually deleted"}

    if not db:
        print("❌ Database not connected")
        return None
    try:
        return db.delete(SCHEMA, TABLE, [workout_id])
    except Exception as e:
        print(f"❌ Error deleting workout: {e}")
        return None

def get_all_workouts():
    if config["url"] == "demo":
        print("🎭 Demo mode: Returning demo workouts")
        return DEMO_WORKOUTS

    if not db:
        print("❌ Database not connected")
        return []
    try:
        return db.sql(f"SELECT video_id, channel, title, duration FROM {SCHEMA}.{TABLE}")
    except harperdb.exceptions.HarperDBError as e:
        print(f"❌ HarperDB error: {e}")
        return []
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return []

def get_workout_today():
    if config["url"] == "demo":
        print("🎭 Demo mode: Returning demo workout for today")
        return [DEMO_WORKOUTS[0]]

    if not db:
        print("❌ Database not connected")
        return None
    try:
        return db.sql(f"SELECT * FROM {SCHEMA}.{TABLE_TODAY} WHERE id = 0")
    except Exception as e:
        print(f"❌ Error getting today's workout: {e}")
        return None

def update_workout_today(workout_data, insert=False):
    if config["url"] == "demo":
        print("🎭 Demo mode: Today's workout would be updated")
        return {"message": "Demo mode - workout not actually updated"}

    if not db:
        print("❌ Database not connected")
        return None
    try:
        workout_data['id'] = 0
        if insert:
            return db.insert(SCHEMA, TABLE_TODAY, [workout_data])
        return db.update(SCHEMA, TABLE_TODAY, [workout_data])
    except Exception as e:
        print(f"❌ Error updating today's workout: {e}")
        return None

