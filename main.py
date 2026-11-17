"""Quick manual test of the PawPal+ backend."""

from pawpal_system import Owner, Pet, Task, Scheduler


def get_pet_name(owner, task):
    """Find which of the owner's pets this task belongs to."""
    for pet in owner.pets:
        for pet_task in pet.tasks:
            if pet_task is task:
                return pet.name
    return "Unknown"

# Create the owner and pets
owner = Owner("Sam")
rex = Pet("Rex", "dog")
luna = Pet("Luna", "cat")

owner.add_pet(rex)
owner.add_pet(luna)

# Create tasks (added out of order on purpose to show sorting)
rex.add_task(Task("Evening walk", "18:30", "daily"))
rex.add_task(Task("Morning walk", "08:00", "daily"))
luna.add_task(Task("Breakfast", "07:00", "daily"))
luna.add_task(Task("Brush fur", "12:00", "weekly"))

# Create the scheduler and print today's schedule
scheduler = Scheduler(owner)

print("Today's Schedule")
print("----------------")
for task in scheduler.sort_by_time():
    pet_name = get_pet_name(owner, task)
    print(f"{task.time}  {pet_name} - {task.description} ({task.frequency})")
