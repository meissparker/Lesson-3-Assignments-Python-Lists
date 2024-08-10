# Task 1 
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted:
    if "Alice" in attended:
        print("Alice submitted her assignments and attended class")
    else:
        print("Alice submitted her assignment but did not attend class.")
elif "Alice" in attended:
    print("Alice attended class but did not submit her assignment.")