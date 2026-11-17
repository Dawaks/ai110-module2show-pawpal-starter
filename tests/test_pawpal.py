from datetime import date

from pawpal_system import Owner, Pet, Scheduler, Task


def test_mark_complete_changes_status():
    task = Task("Morning walk", "08:00", "daily")
    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_add_task_increases_task_count():
    pet = Pet("Rex", "dog")
    task = Task("Breakfast", "07:00", "daily")

    pet.add_task(task)

    assert len(pet.tasks) == 1


def test_daily_task_creates_next_day_task():
    owner = Owner("Sam")
    pet = Pet("Rex", "dog")
    owner.add_pet(pet)

    task = Task("Morning walk", "08:00", "daily", due_date=date(2026, 11, 17))
    pet.add_task(task)

    scheduler = Scheduler(owner)
    scheduler.mark_task_complete(pet, task)

    # The original task is done
    assert task.completed is True

    # A new task was added to the same pet
    assert len(pet.tasks) == 2
    new_task = pet.tasks[1]
    assert new_task.completed is False

    # The new task is due exactly one day later
    assert new_task.due_date == date(2026, 11, 18)


def test_sort_by_time_returns_chronological_order():
    owner = Owner("Sam")
    rex = Pet("Rex", "dog")
    luna = Pet("Luna", "cat")
    owner.add_pet(rex)
    owner.add_pet(luna)

    # Add tasks out of order on purpose
    rex.add_task(Task("Evening walk", "18:30", "daily"))
    luna.add_task(Task("Breakfast", "07:00", "daily"))
    rex.add_task(Task("Morning walk", "08:00", "daily"))

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()

    times = [task.time for task in sorted_tasks]
    assert times == ["07:00", "08:00", "18:30"]


def test_detect_conflicts_finds_same_time_tasks():
    owner = Owner("Sam")
    rex = Pet("Rex", "dog")
    luna = Pet("Luna", "cat")
    owner.add_pet(rex)
    owner.add_pet(luna)

    # Two tasks at the exact same time
    rex.add_task(Task("Morning walk", "08:00", "daily"))
    luna.add_task(Task("Breakfast", "08:00", "daily"))

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert "08:00" in conflicts[0]
