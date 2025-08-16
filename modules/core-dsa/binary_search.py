"""
🔍 BINARY SEARCH - The Ultimate Guessing Game Master! 🔍

🎯 Imagine This Epic Scene:
You're playing a number guessing game with your friend. They pick a number between 1 and 1000.
AMATEUR approach: "Is it 1? Is it 2? Is it 3?..." (could take 1000 guesses! 😱)
PRO GAMER approach: "Is it 500?" → "Too high!" → "Is it 250?" → "Too low!" → "Is it 375?"...

That's binary search! You eliminate HALF the possibilities with each guess! 🤯

🚀 The Superpower:
Instead of checking elements one by one (taking O(n) time), binary search finds your target in O(log n) time!
In a list of 1 million items, you only need about 20 checks! Talk about efficiency! ⚡

📚 The Golden Rules of Binary Search:
🔑 RULE #1: Your array/list MUST be sorted! (This is non-negotiable!)
🔑 RULE #2: Think "divide and conquer" - split the problem in half every time
🔑 RULE #3: Three pointers are your best friends: left, right, and middle
🔑 RULE #4: Eliminate half the search space with each comparison

🎪 When Should You Think "Binary Search"?
🚨 RED FLAG #1: Array is sorted (or can be sorted)
🚨 RED FLAG #2: You need to find a specific value
🚨 RED FLAG #3: You need to find the "first/last" occurrence of something
🚨 RED FLAG #4: You're looking for a "minimum/maximum" value that satisfies a condition
🚨 RED FLAG #5: Problem involves "guess and check" scenarios

🎮 The Binary Search Battle Plan:

🎯 BASIC STRATEGY: Find the Exact Target
1. 📍 Set boundaries: left = 0, right = length - 1
2. 🎯 Find middle: mid = (left + right) // 2
3. 🔍 Compare middle with target:
   - If middle == target: 🎉 FOUND IT!
   - If middle < target: 📈 Search right half (left = mid + 1)
   - If middle > target: 📉 Search left half (right = mid - 1)
4. 🔄 Repeat until found or boundaries cross

The Ultimate Template:
def binary_search_template(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid  # 🎯 Target found!
        elif arr[mid] < target:
            left = mid + 1  # 📈 Go right
        else:
            right = mid - 1  # 📉 Go left
    
    return -1  # 😞 Target not found
"""

from typing import List, Optional

# 🎯 CHALLENGE #1: The Library Book Hunt
def find_library_book(book_ids: List[int], target_book: int) -> int:
    """
    Find the position of a book using binary search!
    
    📚 THE QUEST:
    You're a librarian in the world's most organized library! 
    Books are arranged by ID numbers in perfect order: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    A student rushes in asking for book ID 13. 
    Can you find it WITHOUT checking every single book?

    🧠 STRATEGY: Use the divide-and-conquer approach!
    Start in the middle, then eliminate half the books with each check!
    
    Args:
        book_ids: Sorted list of book ID numbers
        target_book: The book ID we're looking for
    
    Returns:
        Index of the book (or -1 if not found)
    """
    left_shelf = 0                          # 📍 Start of our search area
    right_shelf = len(book_ids) - 1         # 📍 End of our search area
    search_steps = 0                        # 📊 Count our efficiency!
    
    print(f"📚 Library books: {book_ids}")
    print(f"🔍 Looking for book ID: {target_book}")
    print(f"📏 Total books to search through: {len(book_ids)}\n")
    
    while left_shelf <= right_shelf:
        search_steps += 1
        
        # 🎯 Find the middle book
        middle_shelf = (left_shelf + right_shelf) // 2
        middle_book = book_ids[middle_shelf]
        
        print(f"🔍 Step {search_steps}:")
        print(f"   📖 Checking middle book at position {middle_shelf}: ID {middle_book}")
        print(f"   📚 Current search range: [{left_shelf}, {right_shelf}] = {book_ids[left_shelf:right_shelf+1]}")
        
        if middle_book == target_book:
            print(f"   🎉 FOUND IT! Book {target_book} is at position {middle_shelf}!")
            print(f"   ⚡ Total steps taken: {search_steps} (vs {len(book_ids)} for linear search)")
            return middle_shelf
            
        elif middle_book < target_book:
            print(f"   📈 {middle_book} < {target_book}, so target is in the RIGHT half")
            left_shelf = middle_shelf + 1
            
        else:
            print(f"   📉 {middle_book} > {target_book}, so target is in the LEFT half")
            right_shelf = middle_shelf - 1
        
        print()
    
    print(f"   😞 Book {target_book} not found in the library!")
    print(f"   📊 Total search steps: {search_steps}")
    return -1

# 🧪 Test the library book hunt!
library_books = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
missing_book = 13

print("📚 LIBRARY BOOK HUNT CHALLENGE!")
result = find_library_book(library_books, missing_book)

if result != -1:
    print(f"\n🏆 SUCCESS: Found book {missing_book} at shelf position {result}!")
else:
    print(f"\n❌ FAILURE: Book {missing_book} is not in our library.")

print("=" * 60)

# 🎯 CHALLENGE #2: The Detective's First & Last Case
def find_crime_timeline(timestamps: List[int], crime_time: int) -> tuple:
    """
    Find the first and last occurrence of the crime timestamp.
    
    🕵️ THE MYSTERY:
    Detective Smith is investigating a crime scene with security logs.
    Timestamps: [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5]
    The crime happened at timestamp 4. But when did it START and when did it END?
    Find the FIRST and LAST occurrence of timestamp 4!

    🧠 STRATEGY: Binary search with a twist!
    - For FIRST occurrence: when we find target, keep searching LEFT
    - For LAST occurrence: when we find target, keep searching RIGHT
    
    Args:
        timestamps: Sorted list of security timestamps
        crime_time: The timestamp we're investigating
    
    Returns:
        Tuple of (first_occurrence, last_occurrence) or (-1, -1) if not found
    """
    
    def find_first_occurrence(arr: List[int], target: int) -> int:
        """Find the leftmost (first) occurrence of target"""
        left, right = 0, len(arr) - 1
        first_pos = -1
        
        print(f"🔍 Searching for FIRST occurrence of {target}...")
        
        while left <= right:
            mid = (left + right) // 2
            print(f"   📍 Checking position {mid}: value {arr[mid]}")
            
            if arr[mid] == target:
                first_pos = mid  # 🎯 Found one! But keep looking left
                right = mid - 1  # 📉 Continue searching in left half
                print(f"   ✅ Found {target} at {mid}, but checking if there's an earlier one...")
            elif arr[mid] < target:
                left = mid + 1   # 📈 Go right
                print(f"   📈 {arr[mid]} < {target}, searching right half")
            else:
                right = mid - 1  # 📉 Go left
                print(f"   📉 {arr[mid]} > {target}, searching left half")
        
        return first_pos
    
    def find_last_occurrence(arr: List[int], target: int) -> int:
        """Find the rightmost (last) occurrence of target"""
        left, right = 0, len(arr) - 1
        last_pos = -1
        
        print(f"🔍 Searching for LAST occurrence of {target}...")
        
        while left <= right:
            mid = (left + right) // 2
            print(f"   📍 Checking position {mid}: value {arr[mid]}")
            
            if arr[mid] == target:
                last_pos = mid   # 🎯 Found one! But keep looking right
                left = mid + 1   # 📈 Continue searching in right half
                print(f"   ✅ Found {target} at {mid}, but checking if there's a later one...")
            elif arr[mid] < target:
                left = mid + 1   # 📈 Go right
                print(f"   📈 {arr[mid]} < {target}, searching right half")
            else:
                right = mid - 1  # 📉 Go left
                print(f"   📉 {arr[mid]} > {target}, searching left half")
        
        return last_pos
    
    print(f"🕵️ Security timestamps: {timestamps}")
    print(f"🔍 Investigating crime time: {crime_time}\n")
    
    first = find_first_occurrence(timestamps, crime_time)
    print()
    last = find_last_occurrence(timestamps, crime_time)
    
    return (first, last)

# 🧪 Test the detective case!
security_logs = [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5]
crime_timestamp = 4

print("🕵️ DETECTIVE'S FIRST & LAST CASE!")
first_crime, last_crime = find_crime_timeline(security_logs, crime_timestamp)

if first_crime != -1:
    crime_duration = last_crime - first_crime + 1
    print(f"\n🏆 CASE SOLVED!")
    print(f"📅 Crime started at position {first_crime}")
    print(f"📅 Crime ended at position {last_crime}")
    print(f"⏱️ Total duration: {crime_duration} timestamps")
else:
    print(f"\n❌ No evidence found for timestamp {crime_timestamp}")

print("=" * 60)

# 🎯 CHALLENGE #3: The Perfect Temperature Quest
def find_perfect_temperature(temperatures: List[int], experiment_success_threshold: int) -> int:
    """
    Find the lowest temperature where experiment succeeds.
    
    🌡️ THE EXPERIMENT:
    You're a scientist testing different temperatures: [10, 20, 30, 40, 50, 60, 70, 80, 90]
    You need to find the PERFECT temperature where your experiment succeeds.
    The rule: "Experiment succeeds if temperature >= 60"
    What's the LOWEST temperature that makes your experiment succeed?

    🧠 STRATEGY: Binary search for the "first true" condition!
    This is a classic "search for boundary" problem.
    
    Args:
        temperatures: Sorted list of possible temperatures
        experiment_success_threshold: Minimum temperature for success
    
    Returns:
        Lowest temperature that meets the threshold (or -1 if none)
    """
    left_temp = 0
    right_temp = len(temperatures) - 1
    perfect_temp = -1
    
    print(f"🌡️ Available temperatures: {temperatures}")
    print(f"🎯 Experiment succeeds when temperature >= {experiment_success_threshold}")
    print("🧪 Testing temperatures...\n")
    
    while left_temp <= right_temp:
        mid_temp = (left_temp + right_temp) // 2
        current_temperature = temperatures[mid_temp]
        
        print(f"🌡️ Testing temperature {current_temperature} at position {mid_temp}")
        
        # Check if experiment succeeds at this temperature
        if current_temperature >= experiment_success_threshold:
            print(f"   ✅ SUCCESS! Experiment works at {current_temperature}°")
            perfect_temp = mid_temp  # 🎯 Found a working temp!
            right_temp = mid_temp - 1  # 📉 But let's see if there's a lower one
            print(f"   🔍 Checking if there's a lower working temperature...")
        else:
            print(f"   ❌ FAILURE! {current_temperature}° is too low")
            left_temp = mid_temp + 1  # 📈 Need higher temperature
            print(f"   📈 Need to try higher temperatures")
        
        print()
    
    return perfect_temp

# 🧪 Test the perfect temperature quest!
lab_temperatures = [10, 20, 30, 40, 50, 60, 70, 80, 90]
success_threshold = 60

print("🌡️ PERFECT TEMPERATURE QUEST!")
result_index = find_perfect_temperature(lab_temperatures, success_threshold)

if result_index != -1:
    perfect_temp = lab_temperatures[result_index]
    print(f"🏆 EUREKA! Perfect temperature found: {perfect_temp}° at position {result_index}")
else:
    print("❌ No temperature high enough for the experiment!")

print("=" * 60)

# 🎯 CHALLENGE #4: The Square Root Calculator
def find_square_root(number: int) -> int:
    """
    Find the integer square root of a number using binary search.
    
    🔢 THE MATHEMATICAL CHALLENGE:
    Your calculator is broken! The square root button doesn't work.
    But you're clever - you can use binary search to find square roots!
    Find the square root of 64 without using any math functions!

    🧠 STRATEGY: Binary search on the answer space!
    We know √64 is somewhere between 0 and 64. Keep guessing!
    
    Args:
        number: The number to find square root of
    
    Returns:
        Integer square root (floor value)
    """
    if number < 0:
        return -1  # No real square root for negative numbers
    
    if number <= 1:
        return number  # √0 = 0, √1 = 1
    
    left_guess = 0
    right_guess = number
    result = 0
    
    print(f"🔢 Finding square root of {number}")
    print(f"🎯 Search range: {left_guess} to {right_guess}")
    print("🔍 Starting the guessing game...\n")
    
    while left_guess <= right_guess:
        mid_guess = (left_guess + right_guess) // 2
        square = mid_guess * mid_guess
        
        print(f"🎲 Guessing: {mid_guess}")
        print(f"   📊 {mid_guess} × {mid_guess} = {square}")
        
        if square == number:
            print(f"   🎉 PERFECT! {mid_guess} is exactly √{number}")
            return mid_guess
        elif square < number:
            print(f"   📈 {square} < {number}, so {mid_guess} is too small")
            result = mid_guess  # 🎯 This might be our answer
            left_guess = mid_guess + 1
        else:
            print(f"   📉 {square} > {number}, so {mid_guess} is too big")
            right_guess = mid_guess - 1
        
        print()
    
    print(f"🏆 Best integer square root: {result}")
    return result

# 🧪 Test the square root calculator!
mystery_number = 64

print("🔢 SQUARE ROOT CALCULATOR CHALLENGE!")
sqrt_result = find_square_root(mystery_number)
verification = sqrt_result * sqrt_result

print(f"\n🎯 RESULT: √{mystery_number} ≈ {sqrt_result}")
print(f"🔍 Verification: {sqrt_result} × {sqrt_result} = {verification}")

if verification == mystery_number:
    print("✅ Perfect square found!")
else:
    next_square = (sqrt_result + 1) * (sqrt_result + 1)
    print(f"📊 {verification} < {mystery_number} < {next_square}")

print("\n" + "🎊" * 20 + " BINARY SEARCH MASTERY COMPLETE! " + "🎊" * 20)
print("""
🏆 CONGRATULATIONS! You've mastered binary search!

📚 KEY TAKEAWAYS:
✅ Binary search works ONLY on sorted arrays
✅ Always think: left, right, middle pointers
✅ Eliminate half the search space each time
✅ Time complexity: O(log n) - incredibly efficient!
✅ Use for: exact search, first/last occurrence, boundary problems
✅ Perfect for "guess and check" scenarios

🔥 ADVANCED PATTERNS YOU'VE LEARNED:
🎯 Basic Search: Find exact target
🎯 First/Last Occurrence: Find boundaries of duplicates  
🎯 Lower Bound: Find first element ≥ target
🎯 Answer Space Search: Binary search on possible answers

🚀 NOW GO BINARY SEARCH ALL THE THINGS!
""")
