# Question 1: String Manipulation

messy_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "

# Remove leading and trailing spaces and convert to lowercase
lower_strip = messy_feedback.strip().lower()

# Replace "speaker" with "presenter"
replaced_feedback = lower_strip.replace("speaker", "presenter")

# Remove extra internal spaces
internal_space = " ".join(replaced_feedback.split())

# Convert the cleaned text to title case
clean_feedback = internal_space.title()

# Display the final output using an f-string
print(f"Final cleaned feedback title: {clean_feedback}")
print()

# Question 2: File Handling

feedback_list = [
    "The activities were fun and interesting.",
    "The presentation was too long.",
    "I learned many great new skills today."
]

# Write the three feedback messages to the file
with open("feedback.txt", "w", encoding="utf-8") as file:
    for feedback in feedback_list:
        file.write(feedback + "\n")

# Read and print the original feedback
print("--- Original Feedback Messages ---")

with open("feedback.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Append a fourth feedback message
with open("feedback.txt", "a", encoding="utf-8") as file:
    file.write("The workshop was very informative.\n")

# Read and print the updated feedback
print("\n--- Updated Feedback List ---")

with open("feedback.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
print()


# Question 3: Exception Handling

try:
    with open("feedback.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("File not found. Please create feedback.txt first.")

except PermissionError:
    print("Permission denied. Close the file and try again.")

finally:
    print("Operation completed.")
print()


# Question 4: Feedback Analysis and Summary Report

total_feedback = 0
count_great = 0

# Read feedback and count entries containing "great"
with open("feedback.txt", "r", encoding="utf-8") as file:
    for line in file:
        total_feedback += 1

        if "great" in line.lower():
            count_great += 1

# Write the summary report
with open("summary.txt", "w", encoding="utf-8") as summary:
    summary.write("=== Workshop Feedback Summary ===\n")
    summary.write(f"Total Feedback: {total_feedback}\n")
    summary.write(f"Mentions of 'Great': {count_great}\n")

# Display the summary using formatted output
print(f"=== Workshop Feedback Summary ===")
print(f"Total Feedback: {total_feedback}")
print(f"Mentions of 'Great': {count_great}")


















