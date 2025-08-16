"""
👥 TWO POINTERS - The Dynamic Duo of Algorithms! 👥

🎭 Imagine This Epic Scene:
You're watching a spy movie. Two secret agents start from opposite ends of a bridge.
They walk toward each other, communicating and making decisions as they meet.
Sometimes one agent moves faster, sometimes the other, sometimes they both move together.
That's exactly how the two pointers technique works! 🕵️‍♂️🕵️‍♀️

🚀 The Superpower:
Two pointers can solve many array problems in O(n) time that would otherwise take O(n²)!
Instead of nested loops, we use TWO smart pointers that dance together through the data! 💃🕺

📚 The Golden Rules of Two Pointers:
🔑 RULE #1: Usually works on sorted arrays (but not always!)
🔑 RULE #2: Two pointers start at strategic positions (often opposite ends)
🔑 RULE #3: Move pointers based on some condition or comparison
🔑 RULE #4: Continue until pointers meet or cross each other

🎪 When Should You Think "Two Pointers"?
🚨 RED FLAG #1: Need to find pairs or triplets with certain properties
🚨 RED FLAG #2: Array is sorted and you're looking for target sums
🚨 RED FLAG #3: Palindrome detection problems
🚨 RED FLAG #4: Removing duplicates from sorted arrays
🚨 RED FLAG #5: Merging two sorted arrays

🎮 The Two Pointers Battle Plan:

🎯 BASIC STRATEGY: Opposite Ends Approach
1. 📍 Start: left = 0, right = length - 1
2. 🔄 Loop: while left < right
3. 🧠 Logic: Compare elements at both pointers
4. 🎯 Move: Decide which pointer(s) to move based on condition

The Ultimate Template:
def two_pointers_template(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        # 🧠 Do your logic here
        if condition_met:
            # 🎉 Found solution!
            return result
        elif need_smaller_value:
            right -= 1  # 📉 Move right pointer left
        else:
            left += 1   # 📈 Move left pointer right
    
    return default_result
"""

from typing import List, Optional

# 🎯 CHALLENGE #1: The Mirror Word Detective
def is_palindrome_detective(text: str) -> bool:
    """
    Detect if a word reads the same forwards and backwards!
    
    🔍 THE MYSTERY:
    You're a word detective investigating mysterious mirror words!
    Words like "racecar", "madam", and "level" read the same both ways.
    Your mission: crack the palindrome code using two pointer technique!
    
    🧠 STRATEGY: Mirror Check Approach!
    - Place one detective at the start, one at the end
    - They walk toward each other, comparing characters
    - If any mismatch is found, it's NOT a palindrome!
    
    Args:
        text: The suspicious word to investigate
    
    Returns:
        True if it's a palindrome, False otherwise
    """
    # 🧹 Clean the evidence (remove spaces and make lowercase)
    cleaned_text = text.replace(" ", "").lower()
    
    left_detective = 0                          # 🕵️‍♂️ Detective starting from left
    right_detective = len(cleaned_text) - 1     # 🕵️‍♀️ Detective starting from right
    
    print(f"🔍 Investigating word: '{text}'")
    print(f"🧹 Cleaned version: '{cleaned_text}'")
    print(f"📏 Length: {len(cleaned_text)} characters")
    print("🕵️ Starting mirror investigation...\n")
    
    step = 1
    while left_detective < right_detective:
        left_char = cleaned_text[left_detective]
        right_char = cleaned_text[right_detective]
        
        print(f"🔍 Step {step}: Comparing positions {left_detective} and {right_detective}")
        print(f"   🕵️‍♂️ Left detective found: '{left_char}'")
        print(f"   🕵️‍♀️ Right detective found: '{right_char}'")
        
        if left_char != right_char:
            print(f"   ❌ MISMATCH! '{left_char}' ≠ '{right_char}'")
            print(f"   🚨 NOT A PALINDROME!")
            return False
        
        print(f"   ✅ MATCH! Both found '{left_char}'")
        print(f"   👥 Detectives move closer...")
        
        left_detective += 1     # 📈 Left detective moves right
        right_detective -= 1    # 📉 Right detective moves left
        step += 1
        print()
    
    print("🎉 CASE SOLVED: It's a PALINDROME! All characters match perfectly!")
    return True

# 🧪 Test the palindrome detective!
test_words = ["racecar", "hello", "madam", "python", "level"]

print("🕵️ PALINDROME DETECTIVE AGENCY!")
print("=" * 50)

for word in test_words:
    result = is_palindrome_detective(word)
    status = "✅ PALINDROME" if result else "❌ NOT PALINDROME"
    print(f"🏆 VERDICT for '{word}': {status}")
    print("=" * 50)

# 🎯 CHALLENGE #2: The Perfect Pair Treasure Hunt
def find_target_sum_pair(treasures: List[int], target_gold: int) -> List[int]:
    """
    Find two treasures that sum up to the target amount!
    
    💰 THE TREASURE HUNT:
    You're a treasure hunter with a sorted list of gold values: [1, 2, 3, 4, 6, 8, 9, 11]
    The ancient map says you need exactly 10 gold pieces to unlock the secret door.
    Find TWO treasures that add up to exactly 10! Which treasures should you pick?
    
    🧠 STRATEGY: Squeeze Technique!
    - Start with the smallest and largest treasures
    - If sum is too small, take a bigger small treasure (move left pointer right)
    - If sum is too big, take a smaller big treasure (move right pointer left)
    - Keep squeezing until you find the perfect pair!
    
    Args:
        treasures: Sorted list of treasure values
        target_gold: The exact amount needed
    
    Returns:
        List containing the two values that sum to target, or empty list if not found
    """
    left_hunter = 0                         # 🏃‍♂️ Hunter starting with smallest treasure
    right_hunter = len(treasures) - 1       # 🏃‍♀️ Hunter starting with largest treasure
    
    print(f"💰 Available treasures: {treasures}")
    print(f"🎯 Target gold needed: {target_gold}")
    print("🏃‍♂️🏃‍♀️ Starting the treasure hunt...\n")
    
    step = 1
    while left_hunter < right_hunter:
        left_treasure = treasures[left_hunter]
        right_treasure = treasures[right_hunter]
        current_sum = left_treasure + right_treasure
        
        print(f"💎 Step {step}: Examining treasure pair")
        print(f"   🏃‍♂️ Left hunter picks: {left_treasure} (position {left_hunter})")
        print(f"   🏃‍♀️ Right hunter picks: {right_treasure} (position {right_hunter})")
        print(f"   🧮 Total gold: {left_treasure} + {right_treasure} = {current_sum}")
        
        if current_sum == target_gold:
            print(f"   🎉 JACKPOT! Found perfect pair: {left_treasure} + {right_treasure} = {target_gold}")
            return [left_treasure, right_treasure]
        elif current_sum < target_gold:
            print(f"   📈 {current_sum} < {target_gold}, need MORE gold!")
            print(f"   🏃‍♂️ Left hunter moves to bigger treasure...")
            left_hunter += 1
        else:
            print(f"   📉 {current_sum} > {target_gold}, need LESS gold!")
            print(f"   🏃‍♀️ Right hunter moves to smaller treasure...")
            right_hunter -= 1
        
        step += 1
        print()
    
    print("😞 No perfect pair found! The treasure combination doesn't exist.")
    return []

# 🧪 Test the treasure hunt!
treasure_vault = [1, 2, 3, 4, 6, 8, 9, 11]
target_amount = 10

print("💰 PERFECT PAIR TREASURE HUNT!")
result = find_target_sum_pair(treasure_vault, target_amount)

if result:
    print(f"🏆 SUCCESS: Found treasure pair {result[0]} + {result[1]} = {target_amount}!")
else:
    print("❌ FAILURE: No treasure pair adds up to the target amount.")

# 🎯 CHALLENGE #3: The Container Water Engineer
def max_water_container(heights: List[int]) -> int:
    """
    Find the maximum water that can be trapped between two walls!
    
    💧 THE ENGINEERING CHALLENGE:
    You're a water engineer with walls of different heights: [1, 8, 6, 2, 5, 4, 8, 3, 7]
    You need to pick TWO walls to create a water container.
    The water level will be limited by the shorter wall.
    Which two walls will give you the MAXIMUM water storage?
    
    🧠 STRATEGY: Greedy Wall Selection!
    - Start with the widest possible container (first and last walls)
    - Always move the pointer with the shorter wall (it's the bottleneck!)
    - Keep track of the maximum water seen so far
    - Width × Min_Height = Water Volume
    
    Args:
        heights: List of wall heights
    
    Returns:
        Maximum water volume that can be contained
    """
    left_wall = 0                       # 🧱 Left wall engineer
    right_wall = len(heights) - 1       # 🧱 Right wall engineer
    max_water = 0                       # 💧 Best container found so far
    
    print(f"🧱 Wall heights: {heights}")
    print("💧 Starting water container optimization...\n")
    
    step = 1
    while left_wall < right_wall:
        left_height = heights[left_wall]
        right_height = heights[right_wall]
        width = right_wall - left_wall
        
        # 💧 Water level is limited by the shorter wall
        water_level = min(left_height, right_height)
        current_water = width * water_level
        
        print(f"💧 Step {step}: Testing container")
        print(f"   🧱 Left wall (pos {left_wall}): height {left_height}")
        print(f"   🧱 Right wall (pos {right_wall}): height {right_height}")
        print(f"   📏 Width: {width}")
        print(f"   🌊 Water level: {water_level} (limited by shorter wall)")
        print(f"   💧 Water volume: {width} × {water_level} = {current_water}")
        
        # 🏆 Update maximum if this container is better
        if current_water > max_water:
            max_water = current_water
            print(f"   🎉 NEW RECORD! Best container so far: {max_water} units")
        else:
            print(f"   📊 Current best: {max_water} units")
        
        # 🧠 Move the shorter wall (it's the bottleneck!)
        if left_height < right_height:
            print(f"   📈 Left wall is shorter, moving left engineer right...")
            left_wall += 1
        else:
            print(f"   📉 Right wall is shorter/equal, moving right engineer left...")
            right_wall -= 1
        
        step += 1
        print()
    
    print(f"🏆 OPTIMAL SOLUTION: Maximum water container holds {max_water} units!")
    return max_water

# 🧪 Test the water container challenge!
wall_heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print("💧 CONTAINER WATER ENGINEERING CHALLENGE!")
result = max_water_container(wall_heights)
print(f"🎯 FINAL RESULT: Maximum water volume = {result} units")

# 🎯 CHALLENGE #4: The Array Cleanup Crew
def remove_duplicates_in_place(sorted_nums: List[int]) -> int:
    """
    Remove duplicates from a sorted array in-place!
    
    🧹 THE CLEANUP MISSION:
    You're part of the Array Cleanup Crew! Your sorted array has duplicates: [1, 1, 2, 2, 2, 3, 4, 4, 5]
    Your mission: Remove duplicates IN-PLACE without using extra memory!
    The array should become: [1, 2, 3, 4, 5, _, _, _, _] (underscores are leftover spaces)
    
    🧠 STRATEGY: Slow-Fast Pointer Technique!
    - Slow pointer: Tracks position of unique elements
    - Fast pointer: Scouts ahead to find new unique elements
    - When fast finds a new unique element, slow takes it and advances
    
    Args:
        sorted_nums: Sorted array with potential duplicates (modified in-place)
    
    Returns:
        Length of the new array with unique elements
    """
    if not sorted_nums:
        return 0
    
    slow_cleaner = 0                    # 🐌 Slow pointer: "Placer" of unique elements
    
    print(f"🧹 Original messy array: {sorted_nums}")
    print("🚀 Starting cleanup operation...\n")
    
    # 🏃‍♂️ Fast pointer starts at index 1 (scout ahead)
    for fast_scout in range(1, len(sorted_nums)):
        current_element = sorted_nums[fast_scout]
        last_unique = sorted_nums[slow_cleaner]
        
        print(f"🔍 Step {fast_scout}: Scout examining element at position {fast_scout}")
        print(f"   🏃‍♂️ Fast scout found: {current_element}")
        print(f"   🐌 Last unique element: {last_unique} (at position {slow_cleaner})")
        
        if current_element != last_unique:
            print(f"   ✨ NEW UNIQUE ELEMENT! {current_element} ≠ {last_unique}")
            slow_cleaner += 1   # 🐌 Advance the slow pointer
            sorted_nums[slow_cleaner] = current_element  # 📥 Place the unique element
            print(f"   📥 Placed {current_element} at position {slow_cleaner}")
            print(f"   🧹 Clean array so far: {sorted_nums[:slow_cleaner+1]}")
        else:
            print(f"   🔄 DUPLICATE! {current_element} == {last_unique}, skipping...")
        
        print()
    
    unique_length = slow_cleaner + 1
    print(f"🏆 CLEANUP COMPLETE!")
    print(f"✨ Unique elements: {sorted_nums[:unique_length]}")
    print(f"📊 New array length: {unique_length} (removed {len(sorted_nums) - unique_length} duplicates)")
    
    return unique_length

# 🧪 Test the array cleanup!
messy_array = [1, 1, 2, 2, 2, 3, 4, 4, 5]
print("🧹 ARRAY CLEANUP CREW MISSION!")

# Make a copy to show the transformation
original = messy_array.copy()
new_length = remove_duplicates_in_place(messy_array)

print(f"\n📊 TRANSFORMATION REPORT:")
print(f"   Before: {original}")
print(f"   After:  {messy_array[:new_length]} (unique elements)")
print(f"   Saved:  {len(original) - new_length} array spaces!")

# 🎯 CHALLENGE #5: The Three Musketeers Sum Quest
def find_three_sum(numbers: List[int], target: int) -> List[List[int]]:
    """
    Find all unique triplets that sum to the target!
    
    ⚔️ THE QUEST:
    You're leading the Three Musketeers! Array: [-1, 0, 1, 2, -1, -4]
    Find ALL unique groups of 3 musketeers whose skills sum to 0 (perfect balance)!
    This is the famous "3Sum" problem - a classic two pointers application!
    
    🧠 STRATEGY: Fixed + Two Pointers!
    - Fix one musketeer, then use two pointers to find the other two
    - Sort the array first to use two pointers effectively
    - Skip duplicates to avoid identical triplets
    
    Args:
        numbers: List of integers (musketeer skill levels)
        target: Target sum we want to achieve
    
    Returns:
        List of all unique triplets that sum to target
    """
    numbers.sort()  # 📊 Sort to enable two pointers magic
    triplets = []   # 🏆 Collection of successful musketeer groups
    
    print(f"⚔️ Musketeer skills (sorted): {numbers}")
    print(f"🎯 Target sum: {target}")
    print("👥 Forming musketeer triplets...\n")
    
    for i in range(len(numbers) - 2):  # 🎯 Fix the first musketeer
        # Skip duplicate first musketeers
        if i > 0 and numbers[i] == numbers[i-1]:
            print(f"🔄 Skipping duplicate first musketeer: {numbers[i]}")
            continue
        
        first_musketeer = numbers[i]
        remaining_target = target - first_musketeer
        
        print(f"👤 Fixed first musketeer: {first_musketeer} (position {i})")
        print(f"🎯 Need two more musketeers to sum to: {remaining_target}")
        
        # 👥 Use two pointers to find the other two musketeers
        left_scout = i + 1              # 🏃‍♂️ Second musketeer scout
        right_scout = len(numbers) - 1   # 🏃‍♀️ Third musketeer scout
        
        while left_scout < right_scout:
            second_musketeer = numbers[left_scout]
            third_musketeer = numbers[right_scout]
            current_sum = second_musketeer + third_musketeer
            
            print(f"   🔍 Testing: {second_musketeer} + {third_musketeer} = {current_sum}")
            print(f"   🎯 Need: {remaining_target}")
            
            if current_sum == remaining_target:
                triplet = [first_musketeer, second_musketeer, third_musketeer]
                triplets.append(triplet)
                print(f"   ⚔️ SUCCESSFUL TRIPLET: {triplet} (sum = {sum(triplet)})")
                
                # Skip duplicates for second musketeer
                while left_scout < right_scout and numbers[left_scout] == second_musketeer:
                    left_scout += 1
                # Skip duplicates for third musketeer  
                while left_scout < right_scout and numbers[right_scout] == third_musketeer:
                    right_scout -= 1
                    
            elif current_sum < remaining_target:
                print(f"   📈 Sum too small, need bigger second musketeer")
                left_scout += 1
            else:
                print(f"   📉 Sum too big, need smaller third musketeer")
                right_scout -= 1
        
        print()
    
    print(f"🏆 QUEST COMPLETE! Found {len(triplets)} unique triplet(s):")
    for i, triplet in enumerate(triplets, 1):
        print(f"   {i}. {triplet} (sum = {sum(triplet)})")
    
    return triplets

# 🧪 Test the three musketeers quest!
musketeer_skills = [-1, 0, 1, 2, -1, -4]
balance_target = 0

print("⚔️ THREE MUSKETEERS SUM QUEST!")
result = find_three_sum(musketeer_skills, balance_target)

if result:
    print(f"\n🎉 SUCCESS: Found {len(result)} balanced musketeer group(s)!")
else:
    print("\n😞 No balanced musketeer groups found.")

print("\n" + "🎊" * 20 + " TWO POINTERS MASTERY COMPLETE! " + "🎊" * 20)
print("""
🏆 CONGRATULATIONS! You've mastered the two pointers technique!

📚 KEY TAKEAWAYS:
✅ Two pointers work great on sorted arrays
✅ Start pointers at strategic positions (usually opposite ends)
✅ Move pointers based on comparison logic
✅ Perfect for pair/triplet finding problems
✅ Reduces O(n²) problems to O(n) time complexity
✅ Great for in-place array modifications

🔥 ADVANCED PATTERNS YOU'VE LEARNED:
🎯 Palindrome Detection: Mirror comparison technique
🎯 Two Sum: Target sum finding with squeeze approach
🎯 Container Water: Greedy optimization with bottleneck logic
🎯 Remove Duplicates: Slow-fast pointer for in-place cleanup
🎯 Three Sum: Fixed + two pointers for triplet problems

🚀 NOW GO SOLVE ARRAY PROBLEMS WITH YOUR POINTER POWERS!
""")
