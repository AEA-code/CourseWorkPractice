from typing import List, Dict

# Type alias representing one day's fitness information
DailyLog = Dict[str, int]


# Calculates the average steps, calories, and exercise minutes
# for all days included in the weekly data.
def calculate_weekly_average(week_data: List[DailyLog]) -> DailyLog:
    # Store the total for each fitness category
    totals = {"steps": 0, "calories": 0, "minutes": 0}

    # Add each day's values to the weekly totals
    for day in week_data:
        for key in totals:
            totals[key] += day.get(key, 0)

    # Count the number of days in the data
    days = len(week_data)

    # Avoid division by zero if no data is provided
    if days == 0:
        return totals

    # Calculate and return the average for each category
    return {key: totals[key] / days for key in totals}


# Checks whether the fitness goals were met for one day.
# Returns True or False for each goal.
def check_daily_goals(day: DailyLog, goals: DailyLog) -> Dict[str, bool]:
    return {
        key: day.get(key, 0) >= goals.get(key, 0)
        for key in goals
    }


# Displays the weekly average and shows whether each day's goals
# were achieved.
def display_summary(week_data: List[DailyLog], goals: DailyLog) -> None:
    # Calculate the weekly averages using the separate function
    average = calculate_weekly_average(week_data)
    print("Weekly Average:", average)

    # Check and display the goals for each day
    for number, day in enumerate(week_data, start=1):
        print(f"Day {number}: {check_daily_goals(day, goals)}")