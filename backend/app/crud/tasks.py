from datetime import datetime, date
#from database import db # uncomment when ready
#from models.task import TaskCreate, TaskUpdate # uncomment when ready

tasks_collection = [] #initial empty task list

# #create a new task
async def create_task(task: TaskCreate):
    """
    Create a new task with default values
    - status: todo
    - completedAt: none
    """
    task_dict = task.dict()
    task_dict.update({
        "status" : "todo",
        "completedAt" : None,
        "_id" : len(tasks_collection) + 1
    })
    
    task_dict["status"] = "todo"
    task_dict["completedAt"] = None
    task_dict["_id"] = len(tasks_collection) + 1
    tasks_collection.append(task_dict)
    return task_dict["_id"]

# READ a single task
async def get_task(task_id: int):
    """
    Fetch a task by its id from placeholder collection
    """
    for t in tasks_collection:
        if t["_id"] == task_id:
            return t
    return None

# READ all tasks today 
async def list_tasks_today():
    """
    Return all tasks schedueled for today
    """
    today = date.today()
    # today_tasks = []
    
    # for task in tasks_collection:
    #     if task["scheduledDate"] == today:
    #         today_tasks.append(task)
    # return today_tasks    
    return [t for t in tasks_collection if t.get("scheduledDate") == today]
    
# READ all tasks
async def list_tasks():
    """
    Return all tasks (placeholder)
    """
    return tasks_collection
  
# UPDATE a task 
async def update_task(task_id: int, task_update: dict): # chanege to task_update: TaskUpdate 
    """
    Update task fields 
    """
    for t in tasks_collection: #placeholder
        if t["_id"] == task_id:
            update_data = {
                k: v #key value pair
                for k, v in task_update.dict().items()
                if v is not None #ignore fields that are None/ no value
            }
            # if task is updated to "done" set "completedAt" time
            if update_data.get("status") == "done" :
                update_data["completedAt"] = datetime.now()

            t.update(update_data)
            return t
    return None #task not found

# def update_task_sync(task, updates):
#     """
#     Synchronous version for testing without DB/models
#     """
#     update_data = {k: v for k, v in updates.items() if v is not None}

#     # simulate setting completedAt if status is done
#     if update_data.get("status") == "done":
#         update_data["completedAt"] = datetime.now()

#     task.update(update_data)
#     return task


# DELETE a task
async def delete_task(task_id: int):
    """
    Delete a task based on id
    """
    for i, t in enumerate(tasks_collection):
        if t["_id"] == task_id :
            tasks_collection.pop(i)
            return True
    return False
            
