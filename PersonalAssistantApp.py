# Q1: Python's Built-in Libraries

import math
import random
import datetime as dt
import os

# Random motivational quote
quotes = [
    "Never give up!",
    "Keep learning and growing.",
    "Success requires consistency.",
    "success required perseverance"
]

print("Motivational Quote:", random.choice(quotes))
print()

# Current date and time
print("Current Date:", dt.datetime.now())
print()

# Q2: Applying datetime and os Libraries

# Get and format today's date
current_date = dt.datetime.now()
folder_name = current_date.strftime("%Y-%m-%d")

# Create a folder if it does not exist
if os.path.isdir(folder_name):
    print("Folder already exists")

elif os.path.exists(folder_name):
    raise FileExistsError(
        "A file already exists with this name."
    )

else:
    os.mkdir(folder_name)
    print("Folder created successfully")

# Define the daily log file location
log_path = os.path.join(
    folder_name, "Daily_userlog.txt"
)

# Save the daily user log
with open(log_path, "a", encoding="utf-8") as file:
    file.write(
        "Daily log: " + str(current_date) + "\n"
    )

print("Daily user log saved successfully!")


# Q3: Demonstrating OOP Principles

from datetime import datetime

class ScheduledTask:

    def __init__(self, name, due_date):
        self.name = name
        self.__due_date = due_date

    def schedule(self):
        today = datetime.now().date()

        if today == self.__due_date:
            print(self.name, "is scheduled for today.")

        elif today > self.__due_date:
            print(self.name, "is overdue.")

        else:
            print(
                self.name,
                "is scheduled for",
                self.__due_date
            )

    def show_info(self):
        print("Task:", self.name)
        self.schedule()

    def update_due_date(self, new_date):
        self.__due_date = new_date


# Creating multiple objects
task1 = ScheduledTask(
    "Study Python",
    datetime(2026, 10, 24).date()
)

task2 = ScheduledTask(
    "Submit assignment",
    datetime(2026, 10, 30).date()
)

task1.show_info()
print()
task2.show_info()
print()

# Q4: Implementing a Task Management Class

from datetime import date

class Task:

    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.status = "Pending"

    def mark_complete(self):
        self.status = "Completed"
        print(f"{self.name} is completed.")

    def reschedule(self, new_date):

        if not isinstance(new_date, date):
            raise TypeError(
                "The new due date must be a date object."
            )

        self.due_date = new_date

        print(
            f"{self.name} rescheduled to {self.due_date}"
        )

    def show_info(self):
        print(f"Task: {self.name}")
        print(f"Due Date: {self.due_date}")
        print(f"Status: {self.status}")
        print("--------------------")


# Creating multiple task objects
task1 = Task(
    "Study Python",
    datetime(2026, 10, 24).date()
)

task2 = Task(
    "Submit Assignment",
    datetime(2026, 10, 30).date()
)

task3 = Task(
    "Organize Reports",
    datetime(2026, 11, 2).date()
)

# Updating individual tasks
task1.mark_complete()

task2.reschedule(
    datetime(2026, 11, 1).date()
)

# Displaying task information
task1.show_info()
task2.show_info()
task3.show_info()