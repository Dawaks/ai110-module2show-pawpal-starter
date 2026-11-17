import streamlit as st

from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

# Keep the owner and scheduler between reruns
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler(st.session_state.owner)

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
st.session_state.owner.name = owner_name.strip()
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

owner = st.session_state.owner

if st.button("Add pet"):
    clean_name = pet_name.strip()

    # Check whether a pet with this name already exists
    name_taken = False
    for pet in owner.pets:
        if pet.name == clean_name:
            name_taken = True

    if clean_name == "":
        st.error("Please enter a pet name.")
    elif name_taken:
        st.error(f"You already have a pet named {clean_name}.")
    else:
        owner.add_pet(Pet(clean_name, species))
        st.success(f"Added {clean_name} the {species}!")

if owner.pets:
    st.write("Current pets:")
    for pet in owner.pets:
        st.write(f"- {pet.name} ({pet.species})")
else:
    st.info("No pets yet. Add one above.")

st.markdown("### Tasks")

if not owner.pets:
    st.info("Add a pet first, then you can give it tasks.")
else:
    # Choose which pet the task is for
    pet_names = [pet.name for pet in owner.pets]
    selected_pet_name = st.selectbox("Pet", pet_names)

    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col3:
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

    col4, col5 = st.columns(2)
    with col4:
        task_time = st.time_input("Time")
    with col5:
        frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])

    if st.button("Add task"):
        # Find the Pet object that matches the selected name
        selected_pet = None
        for pet in owner.pets:
            if pet.name == selected_pet_name:
                selected_pet = pet

        new_task = Task(
            description=task_title,
            time=task_time.strftime("%H:%M"),  # e.g. "08:00", so sorting works
            frequency=frequency,
            duration_minutes=int(duration),
            priority=priority,
        )
        selected_pet.add_task(new_task)
        st.success(f"Added '{task_title}' for {selected_pet.name}!")

    # Show every task from every pet
    task_rows = []
    for pet in owner.pets:
        for task in pet.tasks:
            task_rows.append(
                {
                    "Pet": pet.name,
                    "Task": task.description,
                    "Time": task.time,
                    "Duration (min)": task.duration_minutes,
                    "Priority": task.priority,
                    "Frequency": task.frequency,
                }
            )

    if task_rows:
        st.write("Current tasks:")
        st.table(task_rows)
    else:
        st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("Builds today's plan from all of your pets' tasks.")

if st.button("Generate schedule"):
    scheduler = st.session_state.scheduler

    # Get tasks in time order, keeping only the ones not done yet
    todays_tasks = []
    for task in scheduler.sort_by_time():
        if task.completed is False:
            todays_tasks.append(task)

    if not todays_tasks:
        st.info("No incomplete tasks to schedule. Add a task above.")
    else:
        # Build one table row per task, including the pet it belongs to
        schedule_rows = []
        for task in todays_tasks:
            pet_name_for_task = "Unknown"
            for pet in owner.pets:
                for pet_task in pet.tasks:
                    if pet_task is task:
                        pet_name_for_task = pet.name

            schedule_rows.append(
                {
                    "Time": task.time,
                    "Pet": pet_name_for_task,
                    "Task": task.description,
                    "Duration (min)": task.duration_minutes,
                    "Priority": task.priority,
                    "Frequency": task.frequency,
                }
            )

        st.write(
            "Tasks are ordered by scheduled time. "
            "Only incomplete tasks are included in today's plan."
        )
        st.table(schedule_rows)

    # Check for tasks booked at the same time
    conflicts = scheduler.detect_conflicts()
    if conflicts:
        for conflict in conflicts:
            st.warning(conflict)
    else:
        st.success("No scheduling conflicts were detected.")
