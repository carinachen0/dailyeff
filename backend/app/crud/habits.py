from datetime import datetime, date
#from database import db # uncomment when ready
#from models.habit import HabitCreate, HabitUpdate # uncomment when ready

# Habits (recurring definitions):
# Name, schedule type (daily/weekdays/custom/weekly_x)
# targetType (binary/count/duration)
# targetValue if needed
# isActive

habits_collection = [] #initial empty habit list


# CREATE a new habit
async def create_habit(habit: HabitCreate):
    """
    Create a new habit with default values
    - isActive: True
    """
    habit_dict = habit.dict()
    habit_dict.update({
        "isActive" : True, #user 
        "_id" : len(habits_collection) + 1
    })
    habits_collection.append(habit_dict)
    return habit_dict["_id"]

# READ a single habit
async def get_habit(habit_id: int):
    """
    Fetch a habit by its id from placeholder collection
    """
    for h in habits_collection:
        if h["_id"] == habit_id:
            return h
    return None

# READ active habits (that you still want to track)
async def list_habits():
    """
    Fetch all habit by frontend filter (active and scheduele)
    """
    return [h for h in habits_collection if h.get("isActive", True)]
    
# READ ALL habits 
async def list_all_habits():
    """
    Fetch all habit (includding habits you paused / stop generating logs for)
    """
    return habits_collection
        
# UPDATE a habit
async def update_habit(habit_id: int, habit_update: HabitUpdate):
    """
    Update habit fields 
    """
    for h in habits_collection: #placeholder
        if h["_id"] == habit_id:
            update_data = {
                k: v #key value pair
                for k, v in habit_update.dict().items()
                if v is not None
            }
            h.update(update_data)
            return h
    return None

# DELETE a task
async def delete_task(task_id: int):
    """
    Delete a task based on id
    """
    for i, h in enumerate(habits_collection):
        if h["_id"] == task_id :
            habits_collection.pop(i)
            return True
    return False
     
