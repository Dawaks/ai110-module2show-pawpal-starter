"""PawPal+ class skeletons based on diagrams/uml.mmd."""

from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    description: str
    time: str
    frequency: str
    completed: bool = False
    due_date: date = field(default_factory=date.today)
    duration_minutes: int = 15
    priority: str = "medium"

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """Add a task to this pet's task list."""
        self.tasks.append(task)


class Owner:
    def __init__(self, name):
        """Create an owner with a name and no pets yet."""
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        """Add a pet to this owner's pet list."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return one list of every task from all of the owner's pets."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append(task)
        return all_tasks


class Scheduler:
    def __init__(self, owner):
        """Create a scheduler that works with the given owner."""
        self.owner = owner

    def sort_by_time(self):
        """Return all tasks sorted by time, earliest first."""
        all_tasks = self.owner.get_all_tasks()
        return sorted(all_tasks, key=lambda task: task.time)

    def filter_tasks(self, completed=None, pet_name=None):
        """Return tasks matching the given completion status and/or pet name."""
        filtered_tasks = []
        for pet in self.owner.pets:
            # Skip pets that don't match the requested name
            if pet_name is not None and pet.name != pet_name:
                continue
            for task in pet.tasks:
                # Skip tasks that don't match the requested status
                if completed is not None and task.completed != completed:
                    continue
                filtered_tasks.append(task)
        return filtered_tasks

    def detect_conflicts(self):
        """Return a message for each time that has more than one task."""
        # Group tasks by time, e.g. {"08:00": ["Rex - Walk", "Luna - Feed"]}
        tasks_by_time = {}
        for pet in self.owner.pets:
            for task in pet.tasks:
                label = f"{pet.name} - {task.description}"
                if task.time not in tasks_by_time:
                    tasks_by_time[task.time] = []
                tasks_by_time[task.time].append(label)

        # Any time with more than one task is a conflict
        conflicts = []
        for time, labels in tasks_by_time.items():
            if len(labels) > 1:
                conflicts.append(f"Conflict at {time}: " + ", ".join(labels))
        return conflicts

    def mark_task_complete(self, pet, task):
        """Mark a pet's task complete and schedule the next one if it repeats."""
        task.mark_complete()

        # Work out how many days until the next occurrence
        frequency = task.frequency.lower()
        if frequency == "daily":
            days_until_next = 1
        elif frequency == "weekly":
            days_until_next = 7
        else:
            return None  # Not a repeating task, so nothing more to do

        next_task = Task(
            description=task.description,
            time=task.time,
            frequency=task.frequency,
            completed=False,
            due_date=task.due_date + timedelta(days=days_until_next),
            duration_minutes=task.duration_minutes,
            priority=task.priority,
        )
        pet.add_task(next_task)
        return next_task
