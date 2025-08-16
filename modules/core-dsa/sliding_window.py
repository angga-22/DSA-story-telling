'''
🪟 THE SLIDING WINDOW TECHNIQUE - Your Secret Weapon for Array Problems! 🪟

🎬 Imagine This Scene:
You're looking through a train window as it moves through the countryside. 
The window frame stays the same size, but the scenery changes as the train moves forward.
Sometimes you want to see more, so you make the window bigger.
Sometimes the view gets too crowded, so you make it smaller.
That's exactly how the sliding window technique works with arrays!

🔍 What's a Subarray Anyway?
Think of an array like a chocolate bar: [🍫, 🍫, 🍫, 🍫, 🍫]
A subarray is just a continuous piece you break off - you can't skip squares!

Example with [1, 2, 3, 4]:
🔸 Size 1 pieces: [1], [2], [3], [4] 
🔸 Size 2 pieces: [1,2], [2,3], [3,4]
🔸 Size 3 pieces: [1,2,3], [2,3,4]
🔸 The whole bar: [1,2,3,4]

📍 The Two Pointers: Left & Right
Think of them as your window's left and right edges:
- LEFT pointer: "Where does my window start?"
- RIGHT pointer: "Where does my window end?"

🎯 When Should You Use Sliding Window?

🚨 RED FLAG #1: The problem mentions "subarray" or "substring"
🚨 RED FLAG #2: You need to find something "optimal" (longest, shortest, maximum, minimum)
🚨 RED FLAG #3: There's a condition that makes subarrays "valid" or "invalid"

Examples that scream "SLIDING WINDOW!":
✅ "Find the longest subarray with sum ≤ k"
✅ "Find the shortest substring containing all characters"
✅ "Count subarrays with exactly k different elements"

🎮 The Sliding Window Game Plan:

🎪 STRATEGY 1: The Expanding & Shrinking Window
1. Start with both pointers at the beginning (left = 0, right = 0)
2. 📈 EXPAND: Move right pointer to include more elements
3. 📉 SHRINK: If window becomes invalid, move left pointer to fix it
4. 🏆 TRACK: Keep track of the best window you've seen

Basic Template:
def sliding_window_magic(nums, condition):
    left = 0
    window_state = 0  # Track sum, count, etc.
    best_result = 0
    
    for right in range(len(nums)):
        # 📈 EXPAND: Add right element to window
        window_state += nums[right]
        
        # 📉 SHRINK: Fix invalid window
        while window_is_invalid(window_state):
            window_state -= nums[left]
            left += 1
        
        # 🏆 UPDATE: Track the best window
        best_result = max(best_result, right - left + 1)
    
    return best_result
'''

from typing import List

# 🎯 CHALLENGE #1: The Treasure Hunt
'''
🏴‍☠️ PIRATE'S PROBLEM:
You're a pirate with a map showing treasure values: [3, 1, 2, 7, 4, 2, 1, 1, 5]
Your ship can only carry treasure worth up to 8 gold pieces at once.
What's the LONGEST stretch of consecutive treasures you can collect without exceeding the limit?

🧠 STRATEGY: Use expanding & shrinking window!
- Expand window by taking more treasures (move right)
- If total > limit, shrink window by dropping leftmost treasures (move left)
'''

def longest_treasure_hunt(treasures: List[int], max_weight: int) -> int:
    """
    Find the longest consecutive stretch of treasures we can carry!
    
    Args:
        treasures: List of treasure values
        max_weight: Maximum weight our ship can carry
    
    Returns:
        Length of longest valid treasure stretch
    """
    left_treasure = 0                    # 📍 Left boundary of our collection
    current_weight = 0                   # ⚖️ Current weight in our ship
    longest_stretch = 0                  # 🏆 Best stretch we've found
    
    # 🔍 Explore each treasure position as right boundary
    for right_treasure in range(len(treasures)):
        # 📈 EXPAND: Pick up the treasure at right position
        current_weight += treasures[right_treasure]
        
        print(f"🏴‍☠️ Treasures [{left_treasure}:{right_treasure+1}] = {treasures[left_treasure:right_treasure+1]}")
        print(f"⚖️ Current weight: {current_weight}, Max: {max_weight}")
        
        # 📉 SHRINK: Too heavy? Drop treasures from the left!
        while current_weight > max_weight:
            print(f"💥 Overweight! Dropping treasure {treasures[left_treasure]} from position {left_treasure}")
            current_weight -= treasures[left_treasure]
            left_treasure += 1
        
        # 🏆 UPDATE: Is this the best stretch yet?
        current_stretch = right_treasure - left_treasure + 1
        longest_stretch = max(longest_stretch, current_stretch)
        print(f"🎯 Current stretch: {current_stretch}, Best so far: {longest_stretch}\n")
    
    return longest_stretch

# 🧪 Test the treasure hunt!
treasure_map = [3, 1, 2, 7, 4, 2, 1, 1, 5]
ship_capacity = 8

print("🏴‍☠️ TREASURE HUNT BEGINS!")
print(f"Treasure map: {treasure_map}")
print(f"Ship capacity: {ship_capacity} gold pieces\n")

result = longest_treasure_hunt(treasure_map, ship_capacity)
print(f"🏆 RESULT: Longest treasure stretch = {result} treasures!")

print("=" * 60)

# 🎯 CHALLENGE #2: The Binary Light Switch Game
'''
💡 THE CHALLENGE:
You have a string of light bulbs: some ON ("1") and some OFF ("0")
Example: "1101100111"
You can flip AT MOST ONE "0" to "1" (turn one OFF bulb ON)
What's the LONGEST string of consecutive ON bulbs you can achieve?

🧠 STRATEGY: Track how many "0"s are in our current window
- If we have ≤ 1 zero, the window is valid (we can flip that zero)
- If we have > 1 zeros, shrink the window until we have ≤ 1 zero
'''

def longest_light_sequence(bulbs: str) -> int:
    """
    Find the longest sequence of ON bulbs after flipping at most one OFF bulb.
    
    Args:
        bulbs: String of "0"s and "1"s representing OFF and ON bulbs
    
    Returns:
        Length of longest possible sequence of ON bulbs
    """
    left_bulb = 0                       # 📍 Left boundary of our window
    zeros_in_window = 0                 # 🔢 Count of "0"s in current window  
    longest_sequence = 0                # 🏆 Best sequence we've found
    
    print(f"💡 Bulb configuration: {bulbs}")
    print("Starting the light optimization...\n")
    
    # 🔍 Explore each bulb position as right boundary
    for right_bulb in range(len(bulbs)):
        # 📈 EXPAND: Add current bulb to our window
        if bulbs[right_bulb] == "0":
            zeros_in_window += 1
            print(f"💡 Found OFF bulb at position {right_bulb} (total zeros: {zeros_in_window})")
        
        # 📉 SHRINK: Too many OFF bulbs? Remove from left!
        while zeros_in_window > 1:
            if bulbs[left_bulb] == "0":
                zeros_in_window -= 1
                print(f"🔄 Removing OFF bulb at position {left_bulb} (zeros now: {zeros_in_window})")
            left_bulb += 1
        
        # 🏆 UPDATE: Is this the longest sequence yet?
        current_sequence = right_bulb - left_bulb + 1
        longest_sequence = max(longest_sequence, current_sequence)
        
        window = bulbs[left_bulb:right_bulb+1]
        print(f"🪟 Window [{left_bulb}:{right_bulb+1}] = '{window}' (length: {current_sequence})")
        print(f"🏆 Best sequence so far: {longest_sequence}\n")
    
    return longest_sequence

# 🧪 Test the light switch game!
light_pattern = "1101100111"

print("💡 LIGHT SWITCH OPTIMIZATION GAME!")
result = longest_light_sequence(light_pattern)
print(f"🏆 RESULT: Longest possible ON sequence = {result} bulbs!")


print("=" * 60)

# 🎯 ADVANCED TECHNIQUE: Counting All Valid Windows
'''
🎪 THE MAGIC TRICK: Counting Subarrays

Here's a mind-bending insight! 🤯
If you have a valid window from position `left` to `right`,
how many valid subarrays END at position `right`?

Think about it:
- Window [left, right] ✅
- Window [left+1, right] ✅  
- Window [left+2, right] ✅
- ...
- Window [right, right] ✅

Total count = right - left + 1 (the window size!)

This is how we count ALL valid subarrays, not just find the longest one.
'''

# 🎯 CHALLENGE #3: The Product Detective
'''
🕵️ THE MYSTERY:
You're investigating a series of numbers: [10, 5, 2, 6]
You need to find ALL subarrays where the product is LESS than 100.
How many such "suspicious" subarrays exist?

🔍 Expected subarrays with product < 100:
[10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6] = 8 total
'''

def count_suspicious_products(evidence: List[int], max_product: int) -> int:
    """
    Count all subarrays where product is less than max_product.
    
    Args:
        evidence: List of numbers to investigate
        max_product: Maximum allowed product
    
    Returns:
        Total count of valid subarrays
    """
    if max_product <= 1:
        return 0  # No positive products can be < 1
    
    total_suspicious = 0                # 📊 Total count of suspicious subarrays
    left_evidence = 0                   # 📍 Left boundary of investigation
    current_product = 1                 # 🔢 Current product in window
    
    print(f"🕵️ Evidence: {evidence}")
    print(f"🎯 Looking for products < {max_product}\n")
    
    # 🔍 Investigate each position as right boundary
    for right_evidence in range(len(evidence)):
        # 📈 EXPAND: Include new evidence
        current_product *= evidence[right_evidence]
        print(f"🔍 Investigating position {right_evidence}: {evidence[right_evidence]}")
        print(f"🔢 Current product: {current_product}")
        
        # 📉 SHRINK: Product too big? Remove left evidence!
        while current_product >= max_product:
            print(f"💥 Product too big! Removing {evidence[left_evidence]} from left")
            current_product //= evidence[left_evidence]  # Integer division
            left_evidence += 1
        
        # 🎪 MAGIC COUNT: All subarrays ending at right_evidence
        new_subarrays = right_evidence - left_evidence + 1
        total_suspicious += new_subarrays
        
        print(f"🪟 Valid window: {evidence[left_evidence:right_evidence+1]}")
        print(f"✨ New suspicious subarrays ending at {right_evidence}: {new_subarrays}")
        print(f"📊 Total suspicious count: {total_suspicious}\n")
    
    return total_suspicious

# 🧪 Test the product detective!
evidence_numbers = [10, 5, 2, 6]
suspicious_limit = 100

print("🕵️ PRODUCT DETECTIVE INVESTIGATION!")
result = count_suspicious_products(evidence_numbers, suspicious_limit)
print(f"🏆 CASE CLOSED: Found {result} suspicious subarrays!")


print("=" * 60)

# 🎯 SPECIAL TECHNIQUE: Fixed Window Size
'''
🖼️ THE PICTURE FRAME TECHNIQUE:

Sometimes the problem gives you a FIXED window size k.
Think of it like a picture frame that never changes size - you just slide it along!

🎪 THE MAGIC:
- Build the first window (positions 0 to k-1)
- Slide the frame: add new element on right, remove old element on left
- Each slide changes exactly 2 elements!

Template for fixed windows:
1. 🏗️ BUILD: Create first window of size k
2. 🔄 SLIDE: For each new position, add right element & remove left element
3. 🏆 TRACK: Update best result as you slide
'''

# 🎯 CHALLENGE #4: The Casino Chip Counter
'''
🎰 THE CASINO PROBLEM:
You're counting chips at a casino table. You can only focus on exactly k=3 consecutive positions.
Chip values: [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
What's the MAXIMUM sum of chips you can count in any 3 consecutive positions?

🧠 STRATEGY: Slide a fixed-size window of 3!
'''

def max_casino_chips(chips: List[int], focus_size: int) -> int:
    """
    Find maximum sum of exactly focus_size consecutive chips.
    
    Args:
        chips: List of chip values at the table
        focus_size: How many consecutive chips we can focus on
    
    Returns:
        Maximum sum possible with fixed window size
    """
    if len(chips) < focus_size:
        print("❌ Not enough chips to make a valid focus window!")
        return -1
    
    print(f"🎰 Casino chips: {chips}")
    print(f"🔍 Focus window size: {focus_size}\n")
    
    # 🏗️ BUILD: Create the first window
    current_sum = 0
    for i in range(focus_size):
        current_sum += chips[i]
    
    max_sum = current_sum
    best_window_start = 0
    
    print(f"🎯 Initial window [0:{focus_size}] = {chips[0:focus_size]} → Sum: {current_sum}")
    
    # 🔄 SLIDE: Move the window across remaining positions
    for i in range(focus_size, len(chips)):
        # Remove leftmost chip and add new rightmost chip
        leaving_chip = chips[i - focus_size]
        entering_chip = chips[i]
        
        current_sum += entering_chip - leaving_chip
        
        window_start = i - focus_size + 1
        window = chips[window_start:i+1]
        
        print(f"🔄 Slide to [{window_start}:{i+1}] = {window}")
        print(f"   📤 Remove: {leaving_chip}, 📥 Add: {entering_chip} → Sum: {current_sum}")
        
        # 🏆 UPDATE: Is this the best sum yet?
        if current_sum > max_sum:
            max_sum = current_sum
            best_window_start = window_start
            print(f"   🎉 NEW BEST! Sum: {max_sum}")
        
        print()
    
    best_window = chips[best_window_start:best_window_start + focus_size]
    print(f"🏆 JACKPOT! Best window: {best_window} with sum: {max_sum}")
    
    return max_sum

# 🧪 Test the casino chip counter!
casino_chips = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
window_size = 3

print("🎰 CASINO CHIP COUNTING CHALLENGE!")
result = max_casino_chips(casino_chips, window_size)
print(f"🎯 FINAL RESULT: Maximum chip sum = {result}")

print("\n" + "🎊" * 20 + " SLIDING WINDOW MASTERY COMPLETE! " + "🎊" * 20)
print("""
🏆 CONGRATULATIONS! You've mastered the sliding window technique!

📚 KEY TAKEAWAYS:
✅ Sliding window = two pointers creating a flexible "window"
✅ Expand window (move right) to explore possibilities  
✅ Shrink window (move left) when constraints are violated
✅ Track the best result as you slide
✅ Use counting trick: window_size = valid subarrays ending at right
✅ Fixed windows: slide by removing left and adding right

🚀 NOW GO SOLVE SOME ARRAY PROBLEMS LIKE A PRO!
""")
