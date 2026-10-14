

# Question One

# A program that manages a list of books available in the library

booktitles = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]

# Adding two more books to the list

booktitles.append("Practical Algebra")
booktitles.append("Discrete Mathematics")

# Removing Moby Dick because it has been damaged

booktitles.remove("Moby Dick")

# Sorting the list alphabetically

booktitles.sort()

# Displaying the final list

print("Final list in alphabetical order:", booktitles)
print()


# Question Two

# A Python program that creates a tuple to store one borrower's immutable personal details

Borrower_details = ("John Doe", "B1023", "2025-10-15")
Labels = ("Borrower Name", "Library ID", "Membership Date")

# Attempting to modify an element in the tuple

try:
    Borrower_details[0] = "David Amenyo"
except TypeError as error:
    print("Observation: Tuples are immutable and cannot be modified.")
    print("Error:", error)

# Displaying the length of the tuple

length = len(Borrower_details)
print("The length of the tuple is:", length)

# Displaying each element using a loop

for label, detail in zip(Labels, Borrower_details):
    print(f"{label}: {detail}")
print()


# Question Three

# Performing tuple packing and unpacking

# Tuple packing

book_info = ("The Alchemist", "Paulo Coelho", 1988)

# Tuple unpacking

title, author, publication_year = book_info

# Printing the book information in a readable format

print("Title:", title)
print("Author:", author)
print("Publication Year:", publication_year)

# Explanation:

# Tuple packing allows related information to be grouped together

# and stored as one tuple.

# Tuple unpacking allows the individual values in the tuple to be

# assigned to separate variables.

# This makes the code more organized, readable, and easier to understand.
print()


# Question Four

# A program representing the number of books borrowed each week

borrowed_books = [23, 19, 31, 27, 22, 30, 25]

# Extracting the records from week 2 to week 5 using slicing

extract_week = borrowed_books[1:5]

# Replacing the number of books borrowed in week 1 with 20

borrowed_books[0] = 20

# Displaying the sliced portion and updated list

print("The sliced portion:", extract_week)
print("The updated list is:", borrowed_books)




