# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
  My initial UML design includes four main classes: Owner, Pet, Task, and Scheduler.
- What classes did you include, and what responsibilities did you assign to each?
  The Owner class represents the person using the application and manages the pets linked to that owner. The Pet class stores information about each pet and the care tasks assigned to it. The Task class represents individual activities such as feeding, walking, medication, grooming, or appointments. The Scheduler class is responsible for collecting tasks across all of the owner's pets and organizing them into a schedule.

The relationships are simple: one Owner can have multiple Pets, each Pet can have multiple Tasks, and the Scheduler works with the Owner to access and organize tasks across all pets.

**b. Design changes**

- Did your design change during implementation? Yes. My initial design changed slightly after reviewing the class skeleton. The original `filter_tasks()` method did not have any parameters, so there was no clear way to specify what the scheduler should filter.
- If yes, describe at least one change and why you made it.
I updated it to accept `completed` and `pet_name` as optional parameters. This makes the method more useful because it can later filter tasks by completion status or by pet, which matches the project requirements while keeping the design simple.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
  The scheduler currently considers task time, completion status, pet name, and scheduling conflicts. Tasks can be sorted by time, filtered by whether they are completed, filtered by pet, and checked for tasks that occur at the same time.
- How did you decide which constraints mattered most?
  I focused on time and task status first because they are the most important pieces for creating a simple daily pet-care schedule. The system needs to know what still needs to be done and when each task is scheduled before adding more advanced scheduling rules.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
  One tradeoff in my scheduler is that conflict detection only checks whether two tasks are scheduled at exactly the same time. It does not currently detect overlapping tasks. For example, a 30-minute walk starting at 8:00 AM would not be considered a conflict with another task scheduled for 8:15 AM.
- Why is that tradeoff reasonable for this scenario?
  I think this is reasonable for the current version because it keeps the scheduling logic simple and easy to understand while still catching obvious conflicts. A future version could include task duration and detect overlapping time ranges.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
  I used Claude in VS Code throughout the project to help with system design, UML generation, class scaffolding, and reviewing the scheduling logic. The most useful prompts were specific ones that described exactly what I wanted the system to do, such as asking Claude to create the four-class UML diagram, generate beginner-friendly class skeletons, or implement one method at a time without changing unrelated code.
- What kinds of prompts or questions were most helpful?
  Using small, focused prompts made it easier for me to review each change and understand what the code was doing before moving on.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
  I did not accept every AI suggestion automatically. During the design review, Claude suggested that I could add a `pet_name` attribute directly to the `Task` class. I decided not to make that change because the task already belongs to a `Pet`, so storing the pet name again would duplicate information.
- How did you evaluate or verify what the AI suggested?
  I did accept Claude's suggestion to add `completed` and `pet_name` parameters to `filter_tasks()` because the original method had no way to specify what should be filtered. I verified the changes by reviewing the code myself and later running the program and pytest tests to make sure the expected behavior still worked.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
