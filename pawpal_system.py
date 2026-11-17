"""PawPal+ class skeletons based on diagrams/uml.mmd."""

from dataclasses import dataclass, field


@dataclass
class Task:
    description: str
    time: str
    frequency: str
    completed: bool = False

    def mark_complete(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        pass


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        pass

    def get_all_tasks(self):
        pass


class Scheduler:
    def __init__(self, owner):
        self.owner = owner

    def sort_by_time(self):
        pass

    def filter_tasks(self, completed=None, pet_name=None):
        pass

    def detect_conflicts(self):
        pass
