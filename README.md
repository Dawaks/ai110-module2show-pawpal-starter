# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Implementation Summary

PawPal+ uses four main classes that work together to manage pet care tasks. The `Owner` class manages multiple pets, while each `Pet` stores its own list of `Task` objects. The `Scheduler` collects tasks across all of the owner's pets and provides basic scheduling features such as sorting tasks by time, filtering tasks by pet or completion status, and identifying tasks scheduled at the same time.

The backend logic is tested through a command-line demo before being connected to the Streamlit interface.

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  
pip install -r requirements.txt

# Windows: .venv\Scripts\activate
```
### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Running:

```bash
python main.py
```

produces:

```text
Today's Schedule
----------------
07:00  Luna - Breakfast (daily)
08:00  Rex - Morning walk (daily)
12:00  Luna - Brush fur (weekly)
18:30  Rex - Evening walk (daily)
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# 2 passed in 0.07s
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | Scheduler.sort_by_time() | Sorts tasks by time |
| Filtering | Scheduler.filter_tasks() | Filters by pet or completion status |
| Conflict handling | Scheduler.detect_conflicts() | Detects exact-time conflicts |
| Recurring tasks | | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
