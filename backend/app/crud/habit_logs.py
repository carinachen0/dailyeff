from datetime import datetime, date
#from database import db # uncomment when ready
#from models.habitLogs import HabitLogCreate, HabitUpdate # uncomment when ready

# Habits themselves don’t “refresh” — instead:
# HabitLogs (daily records):
# One log per habit per date
# status (done/missed/skipped)
# optional value (for count/duration habits)
# optional timeSpentSec

habitlogs_collection = [] #initial empty habit log list

# CREATE or Update a new habit log
async def create_update_habit_log(habit_id: int, log: HabitLogCreate) :
    """
    Create new daily log or update existing log for a habit
    """
    log_date = log.date or date.today().isoformat() # todays date as a string in YYYY-MM-DD format
    
    # check if log exists 
    for existing_log in habitlogs_collection:
        if existing_log["habitId"] == habit_id and existing_log["date"] == log_date:
            # update existing data, only provided fields to prevent data loss
            if log.status is not None: 
                existing_log["status"] = log.status
            if log.value is not None: 
                existing_log["value"] = log.value
            if log.timeSpentSec is not None: 
                existing_log["timeSpentSec"] = log.timeSpentSec
            return existing_log["_id"]
    
    # create new if log not found    
    new_log = {
        "_id" : len(habitlogs_collection) + 1,
        "habitId" : habit_id,
        "date" : log_date, 
        "status" : log.status,
        "value" : log.value,
        "timeSpentSec" : log.timeSpentSec
    }
    habitlogs_collection.append(new_log)
    return new_log["_id"]

# READ a single log
async def get_habit_log(habit_id: int, log_date: str):
    """
    Check if log exists today
    """
    for log in habitlogs_collection:
        if log["habitId"] == habit_id and log["date"] == log_date:
            return log
    return None

# READ ALL habit logs for 1 habit
async def get_habit_logs(habit_id: int, start_date: str, end_date: str):
    """
    All logs for streak calculation
    """
    return [
        log for log in habitlogs_collection 
        if log["habitId"] == habit_id
        and start_date <= log["date"] <= end_date
    ]
        
# READ ALL habit logs for a specific date
async def get_logs_for_date(log_date: str):
    return [
        log for log in habitlogs_collection
        if log["date"] == log_date
    ]

