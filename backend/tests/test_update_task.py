# tests/test_update_task.py

from app.crud.tasks import update_task_sync

def main():
    # Test 1: Partial update
    task = {"title": "Write report", "priority": 2, "completed": False}
    updates = {"priority": 3, "completed": None}
    updated = update_task_sync(task.copy(), updates)
    print("Test 1:", updated)

    # Test 2: Update all fields
    updates2 = {"title": "Finish backend", "priority": 5, "completed": True, "status": "done"}
    updated2 = update_task_sync(task.copy(), updates2)
    print("Test 2:", updated2)

if __name__ == "__main__":
    main()
