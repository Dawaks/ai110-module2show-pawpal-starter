# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
  My initial UML design includes four main classes: Owner, Pet, Task, and Scheduler.
- What classes did you include, and what responsibilities did you assign to each?
  The Owner class represents the person using the application and manages the pets linked to that owner. The Pet class stores information about each pet and the care tasks assigned to it. The Task class represents individual activities such as feeding, walking, medication, grooming, or appointments. The Scheduler class is responsible for collecting tasks across all of the owner's pets and organizing them into a schedule.

The relationships are simple: one Owner can have multiple Pets, each Pet can have multiple Tasks, and the Scheduler works with the Owner to access and organize tasks across all pets.

**b. Design changes**

- Did your design change during implementation? Yes. My design changed slightly as I started implementing and reviewing the class structure.
- If yes, describe at least one change and why you made it.
One change was updating filter_tasks() to accept completed and pet_name as optional parameters. The original method did not have a clear way to specify what should be filtered.
I also added a due_date attribute to the Task class and a mark_task_complete() method to the Scheduler. This was needed to support recurring tasks so that completing a daily or weekly task could create the next occurrence on the correct date.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
The scheduler currently considers task time, completion status, pet name, due date, recurrence, and scheduling conflicts. Tasks can be sorted by time, filtered by completion status or pet, checked for tasks scheduled at the same time, and automatically rescheduled when they repeat daily or weekly.
- How did you decide which constraints mattered most?
  I focused first on time, completion status, and recurrence because they directly affect whether a pet owner can follow a daily care schedule. The system needs to know what still needs to be done, when it should happen, and whether the task needs to occur again. Priority-based scheduling could be added later as a more advanced feature.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
  One tradeoff in my scheduler is that conflict detection only checks whether two tasks are scheduled at exactly the same time. It does not currently detect overlapping tasks. For example, a 30-minute walk starting at 8:00 AM would not be considered a conflict with another task scheduled for 8:15 AM.
- Why is that tradeoff reasonable for this scenario?
  I think this is reasonable for the current version because it keeps the scheduling logic simple and easy to understand while still catching obvious conflicts. A future version could include task duration and compare time ranges to detect overlapping activities.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
  I used Claude in VS Code throughout the project to help with system design, UML generation, class scaffolding, implementation, test creation, and reviewing the scheduling logic. I used AI one step at a time instead of asking it to build the entire project at once.
- What kinds of prompts or questions were most helpful?
  Small, focused prompts were the most helpful. For example, I asked Claude to implement one method at a time, such as sort_by_time() or detect_conflicts(), while specifically telling it not to modify unrelated code. This made the changes easier to review and understand before moving on.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
  During the design review, Claude suggested that I could add a pet_name attribute directly to the Task class. I decided not to make that change because each task already belongs to a Pet, so storing the pet name inside the task would duplicate information.
- How did you evaluate or verify what the AI suggested?
  I reviewed the suggested code and compared it with the relationships in my UML design. I accepted Claude's suggestion to add completed and pet_name parameters to filter_tasks() because it made the method more useful without unnecessarily changing the class structure. I also verified the implementation by running main.py and using pytest after changes were made.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
  I tested five main behaviors:
marking a task as completed
adding a task to a pet
sorting tasks in chronological order
creating the next occurrence of a daily recurring task
detecting tasks scheduled at the same time
All five tests passed successfully using pytest.
- Why were these tests important?
  These tests cover the main behaviors that the scheduler depends on. They verify that task state changes correctly, pets can store tasks, scheduling order is correct, recurring tasks create the next occurrence, and obvious scheduling conflicts are detected. Testing these behaviors individually helped confirm that the backend logic was working before connecting it to the user interface.

**b. Confidence**

- How confident are you that your scheduler works correctly?
  I would rate my confidence as 4 out of 5. The core behaviors I implemented are covered by automated tests, and all five tests currently pass.
- What edge cases would you test next if you had more time?
I would test weekly recurrence, pets with no tasks, invalid or inconsistent time formats, tasks with the same description, and overlapping tasks that start at different times. I would also test how the scheduler behaves when there are many pets and tasks.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I am most satisfied with how the classes work together without becoming overly complicated. The Owner provides access to tasks across multiple pets, while the Scheduler handles sorting, filtering, recurrence, and conflict detection. I also like that I built and tested the backend logic before connecting it to the Streamlit interface.
**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I would improve the scheduling logic by adding task duration and priority. This would allow the scheduler to detect overlapping tasks instead of only exact-time conflicts and make better decisions about which activities should be completed first. I would also consider stronger validation for time and date inputs.
**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
  One important thing I learned is that AI is more useful when I give it small, specific tasks and review the results instead of asking it to build everything at once. Designing the UML first also made the implementation easier because I already understood how the classes were supposed to interact before writing the full logic.
