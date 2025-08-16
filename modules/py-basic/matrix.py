
"""
🎮 MATRIX / 2D ARRAYS - The Grid Master's Adventure! 🎮

🗺️ Imagine This Epic Scene:
You're exploring a mystical world laid out on a grid, like a giant game board!
Each cell contains treasures, monsters, or magical items.
You need to navigate this 2D world, perform epic quests, and master the grid!

Think of a matrix as:
🎯 A chessboard with pieces
🏘️ A city with buildings arranged in blocks
🎮 A game map with different terrains
📊 A spreadsheet with rows and columns

🚀 The Superpower:
Matrices let you organize data in rows and columns, making it perfect for:
- Image processing (pixels in a grid)
- Game boards (chess, tic-tac-toe, battleship)
- Maps and navigation systems
- Mathematical computations
- Data tables and spreadsheets

📚 The Golden Rules of Matrix Mastery:
🔑 RULE #1: Matrix[row][column] - Always row first, then column!
🔑 RULE #2: Think "down then right" - rows go down, columns go right
🔑 RULE #3: Nested loops are your best friend for traversal
🔑 RULE #4: Watch out for bounds! Don't fall off the grid!

🎪 When Should You Think "Matrix"?
🚨 RED FLAG #1: 2D grids, game boards, or coordinate systems
🚨 RED FLAG #2: Image/pixel manipulation problems
🚨 RED FLAG #3: Path finding or navigation challenges
🚨 RED FLAG #4: Pattern matching in 2D space
🚨 RED FLAG #5: Dynamic programming on grids

🎮 The Matrix Navigation Patterns:

🎯 BASIC TRAVERSAL: Visit Every Cell
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        # Visit matrix[row][col]
        process_cell(matrix[row][col])

🧭 DIRECTIONAL MOVEMENT: Explore Neighbors
directions = [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up
for dr, dc in directions:
    new_row, new_col = row + dr, col + dc
    if is_valid_position(new_row, new_col):
        # Explore neighbor
"""

from typing import List, Tuple, Optional

# 🎯 CHALLENGE #1: The Treasure Map Explorer
def explore_treasure_map(treasure_map: List[List[int]]) -> dict:
    """
    Explore a treasure map and count all the goodies!
    
    🗺️ THE QUEST:
    You're an explorer with an ancient treasure map! Each cell contains:
    💰 Gold coins (positive numbers)
    🕳️ Empty spaces (zeros) 
    💀 Traps (negative numbers)
    
    Your mission: Navigate the entire map and count your findings!
    
    🧠 STRATEGY: Systematic Grid Traversal!
    Visit every single cell row by row, like reading a book!
    
    Args:
        treasure_map: 2D list representing the map grid
    
    Returns:
        Dictionary with exploration statistics
    """
    if not treasure_map or not treasure_map[0]:
        return {"error": "Empty map!"}
    
    rows = len(treasure_map)
    cols = len(treasure_map[0])
    
    print(f"🗺️ TREASURE MAP EXPLORATION!")
    print(f"📏 Map size: {rows} rows × {cols} columns")
    print("🎒 Starting exploration...\n")
    
    # 📊 Statistics tracking
    total_gold = 0
    empty_spaces = 0
    traps_found = 0
    max_treasure = float('-inf')
    max_position = None
    
    # 🗺️ Print the map first
    print("🗺️ TREASURE MAP:")
    for i in range(rows):
        row_display = ""
        for j in range(cols):
            value = treasure_map[i][j]
            if value > 0:
                row_display += f"💰{value:2d} "
            elif value == 0:
                row_display += "🕳️ 0  "
            else:
                row_display += f"💀{value:2d} "
        print(f"   Row {i}: {row_display}")
    print()
    
    # 🧭 Explore every cell
    for row in range(rows):
        for col in range(cols):
            current_treasure = treasure_map[row][col]
            
            print(f"🧭 Exploring position ({row}, {col}): ", end="")
            
            if current_treasure > 0:
                print(f"💰 Found {current_treasure} gold coins!")
                total_gold += current_treasure
                if current_treasure > max_treasure:
                    max_treasure = current_treasure
                    max_position = (row, col)
            elif current_treasure == 0:
                print("🕳️ Empty space")
                empty_spaces += 1
            else:
                print(f"💀 Trap with {abs(current_treasure)} damage!")
                traps_found += 1
    
    # 📊 Exploration results
    results = {
        "total_gold": total_gold,
        "empty_spaces": empty_spaces,
        "traps_found": traps_found,
        "biggest_treasure": max_treasure if max_treasure != float('-inf') else 0,
        "treasure_location": max_position,
        "map_size": (rows, cols)
    }
    
    print(f"\n🏆 EXPLORATION COMPLETE!")
    print(f"💰 Total gold collected: {results['total_gold']}")
    print(f"🕳️ Empty spaces found: {results['empty_spaces']}")
    print(f"💀 Traps encountered: {results['traps_found']}")
    if max_position:
        print(f"👑 Biggest treasure: {results['biggest_treasure']} at position {results['treasure_location']}")
    
    return results

# 🧪 Test the treasure map exploration!
ancient_map = [
    [10, 0, 5, -2],
    [3, 15, 0, 7],
    [-1, 8, 12, 0]
]

print("🗺️ ANCIENT TREASURE MAP QUEST!")
exploration_results = explore_treasure_map(ancient_map)
print("=" * 60)

# 🎯 CHALLENGE #2: The Matrix Transformer
def transform_matrix_elements(power_grid: List[List[int]], amplifier: int) -> List[List[int]]:
    """
    Transform a power grid by amplifying all energy levels!
    
    ⚡ THE MISSION:
    You're an electrical engineer working on a power grid! 
    Grid: [[5, 9, -2], [2, -5, 7]]
    Each cell represents energy levels in different sectors.
    Your mission: Amplify ALL energy levels by the amplifier factor!
    
    🧠 STRATEGY: Element-wise Transformation!
    Create a new grid and multiply each element by the amplifier!
    
    Args:
        power_grid: 2D list representing energy levels
        amplifier: Multiplication factor for amplification
    
    Returns:
        New 2D list with amplified energy levels
    """
    if not power_grid or not power_grid[0]:
        return []
    
    rows = len(power_grid)
    cols = len(power_grid[0])
    
    print(f"⚡ POWER GRID TRANSFORMATION!")
    print(f"🔧 Amplifier setting: ×{amplifier}")
    print(f"📏 Grid size: {rows} rows × {cols} columns\n")
    
    # 🗂️ Display original grid
    print("🔋 ORIGINAL POWER GRID:")
    for i in range(rows):
        row_display = "   "
        for j in range(cols):
            value = power_grid[i][j]
            row_display += f"{value:4d} "
        print(f"Row {i}: {row_display}")
    print()
    
    # ⚡ Create amplified grid using list comprehension magic!
    amplified_grid = [[0 for j in range(cols)] for i in range(rows)]
    
    print("🔄 TRANSFORMATION IN PROGRESS...")
    for i in range(rows):
        for j in range(cols):
            original_value = power_grid[i][j]
            amplified_value = original_value * amplifier
            amplified_grid[i][j] = amplified_value
            
            print(f"   Cell ({i},{j}): {original_value} × {amplifier} = {amplified_value}")
    
    print("\n⚡ AMPLIFIED POWER GRID:")
    for i in range(rows):
        row_display = "   "
        for j in range(cols):
            value = amplified_grid[i][j]
            row_display += f"{value:4d} "
        print(f"Row {i}: {row_display}")
    
    return amplified_grid

# 🧪 Test the matrix transformer!
energy_grid = [
    [5, 9, -2],
    [2, -5, 7]
]
boost_factor = 3

print("⚡ POWER GRID AMPLIFICATION MISSION!")
boosted_grid = transform_matrix_elements(energy_grid, boost_factor)
print("=" * 60)

# 🎯 CHALLENGE #3: The Island Explorer
def count_islands(ocean_map: List[List[str]]) -> int:
    """
    Count the number of islands in an ocean!
    
    🏝️ THE ADVENTURE:
    You're a cartographer mapping islands in an ocean!
    'L' = Land (part of an island)
    'W' = Water
    Islands are formed by connected land cells (horizontally or vertically adjacent)
    
    🧠 STRATEGY: Flood Fill Algorithm!
    When you find land, explore all connected land to mark the entire island!
    
    Args:
        ocean_map: 2D grid with 'L' for land and 'W' for water
    
    Returns:
        Number of distinct islands found
    """
    if not ocean_map or not ocean_map[0]:
        return 0
    
    rows = len(ocean_map)
    cols = len(ocean_map[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    island_count = 0
    
    print(f"🏝️ ISLAND EXPLORATION MISSION!")
    print(f"🌊 Ocean map size: {rows} rows × {cols} columns\n")
    
    # 🗺️ Display the ocean map
    print("🗺️ OCEAN MAP:")
    for i in range(rows):
        row_display = "   "
        for j in range(cols):
            if ocean_map[i][j] == 'L':
                row_display += "🏝️ "
            else:
                row_display += "🌊 "
        print(f"Row {i}: {row_display}")
    print()
    
    def explore_island(start_row: int, start_col: int, island_num: int):
        """Explore an entire island using DFS (flood fill)"""
        if (start_row < 0 or start_row >= rows or 
            start_col < 0 or start_col >= cols or
            visited[start_row][start_col] or
            ocean_map[start_row][start_col] == 'W'):
            return
        
        # 🏴 Mark this land as part of current island
        visited[start_row][start_col] = True
        print(f"   🏴 Exploring land at ({start_row}, {start_col}) - Part of Island {island_num}")
        
        # 🧭 Explore all 4 directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = start_row + dr, start_col + dc
            explore_island(new_row, new_col, island_num)
    
    print("🧭 Starting island discovery...")
    
    # 🔍 Scan the entire ocean
    for row in range(rows):
        for col in range(cols):
            if ocean_map[row][col] == 'L' and not visited[row][col]:
                island_count += 1
                print(f"\n🏝️ DISCOVERED ISLAND #{island_count} at position ({row}, {col})!")
                explore_island(row, col, island_count)
    
    print(f"\n🏆 EXPLORATION COMPLETE!")
    print(f"🏝️ Total islands discovered: {island_count}")
    
    return island_count

# 🧪 Test the island explorer!
pacific_ocean = [
    ['L', 'L', 'W', 'W', 'W'],
    ['L', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'L']
]

print("🏝️ PACIFIC OCEAN ISLAND DISCOVERY!")
total_islands = count_islands(pacific_ocean)
print("=" * 60)

# 🎯 CHALLENGE #4: The Matrix Rotator
def rotate_matrix_90_degrees(game_board: List[List[int]]) -> List[List[int]]:
    """
    Rotate a square matrix 90 degrees clockwise!
    
    🎮 THE CHALLENGE:
    You're programming a puzzle game! Players can rotate the game board 90° clockwise.
    Original:     After Rotation:
    [1, 2, 3]     [7, 4, 1]
    [4, 5, 6] --> [8, 5, 2]
    [7, 8, 9]     [9, 6, 3]
    
    🧠 STRATEGY: Layer by Layer Rotation!
    1. Work from outside layers to inside
    2. For each layer, rotate 4 elements at a time
    3. Use temporary storage to avoid overwriting
    
    Args:
        game_board: Square 2D matrix to rotate
    
    Returns:
        New rotated matrix
    """
    if not game_board or len(game_board) != len(game_board[0]):
        print("❌ Error: Matrix must be square!")
        return game_board
    
    n = len(game_board)
    print(f"🎮 MATRIX ROTATION CHALLENGE!")
    print(f"📏 Board size: {n}×{n}\n")
    
    # 🎨 Display original board
    print("🎲 ORIGINAL GAME BOARD:")
    for i in range(n):
        row_display = "   "
        for j in range(n):
            row_display += f"{game_board[i][j]:3d} "
        print(f"Row {i}: {row_display}")
    print()
    
    # 🔄 Create a copy for rotation
    rotated = [[0 for _ in range(n)] for _ in range(n)]
    
    print("🔄 ROTATION IN PROGRESS...")
    print("🧭 Mapping: (row, col) → (col, n-1-row)")
    
    # 🎯 The rotation formula: (i,j) → (j, n-1-i)
    for i in range(n):
        for j in range(n):
            new_row = j
            new_col = n - 1 - i
            rotated[new_row][new_col] = game_board[i][j]
            print(f"   ({i},{j}) → ({new_row},{new_col}): {game_board[i][j]}")
    
    print("\n🎮 ROTATED GAME BOARD:")
    for i in range(n):
        row_display = "   "
        for j in range(n):
            row_display += f"{rotated[i][j]:3d} "
        print(f"Row {i}: {row_display}")
    
    return rotated

# 🧪 Test the matrix rotator!
puzzle_board = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]

print("🎮 PUZZLE BOARD ROTATION!")
rotated_board = rotate_matrix_90_degrees(puzzle_board)
print("=" * 60)

# 🎯 CHALLENGE #5: The Spiral Matrix Walker
def spiral_traverse(matrix: List[List[int]]) -> List[int]:
    """
    Walk through a matrix in spiral order!
    
    🌪️ THE QUEST:
    You're a spiral walker navigating a mystical matrix!
    Matrix:           Spiral Path:
    [1,  2,  3,  4]   1 → 2 → 3 → 4
    [12, 13, 14, 5]        ↓
    [11, 16, 15, 6]   12→13→14   5
    [10, 9,  8,  7]    ↑      ↓
                      11  16←15   6
                       ↑         ↓
                      10← 9← 8← 7
    
    Result: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    
    🧠 STRATEGY: Layer by Layer Spiral!
    Move: Right → Down → Left → Up, then shrink boundaries!
    
    Args:
        matrix: 2D matrix to traverse
    
    Returns:
        List of elements in spiral order
    """
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    
    # 🎯 Boundary markers
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1
    
    print(f"🌪️ SPIRAL MATRIX WALKER!")
    print(f"📏 Matrix size: {rows} rows × {cols} columns\n")
    
    # 🎨 Display the matrix with coordinates
    print("🗺️ MATRIX TO TRAVERSE:")
    for i in range(rows):
        row_display = "   "
        for j in range(cols):
            row_display += f"{matrix[i][j]:3d} "
        print(f"Row {i}: {row_display}")
    print()
    
    print("🌪️ SPIRAL TRAVERSAL:")
    direction_names = ["RIGHT", "DOWN", "LEFT", "UP"]
    direction_idx = 0
    
    while top <= bottom and left <= right:
        current_direction = direction_names[direction_idx % 4]
        print(f"\n🧭 Moving {current_direction}:")
        
        if direction_idx % 4 == 0:  # Moving RIGHT
            for col in range(left, right + 1):
                result.append(matrix[top][col])
                print(f"   📍 ({top},{col}) = {matrix[top][col]}")
            top += 1
            
        elif direction_idx % 4 == 1:  # Moving DOWN
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
                print(f"   📍 ({row},{right}) = {matrix[row][right]}")
            right -= 1
            
        elif direction_idx % 4 == 2:  # Moving LEFT
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
                print(f"   📍 ({bottom},{col}) = {matrix[bottom][col]}")
            bottom -= 1
            
        elif direction_idx % 4 == 3:  # Moving UP
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
                print(f"   📍 ({row},{left}) = {matrix[row][left]}")
            left += 1
        
        direction_idx += 1
    
    print(f"\n🌪️ SPIRAL COMPLETE!")
    print(f"🎯 Traversal result: {result}")
    
    return result

# 🧪 Test the spiral walker!
mystical_matrix = [
    [1,  2,  3,  4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9,  8,  7]
]

print("🌪️ MYSTICAL MATRIX SPIRAL QUEST!")
spiral_result = spiral_traverse(mystical_matrix)

print("\n" + "🎊" * 20 + " MATRIX MASTERY COMPLETE! " + "🎊" * 20)
print("""
🏆 CONGRATULATIONS! You've mastered 2D matrices and arrays!

📚 KEY TAKEAWAYS:
✅ Matrix[row][column] - Always row first, then column
✅ Nested loops are perfect for matrix traversal
✅ Check boundaries to avoid index errors
✅ Use helper functions for complex operations
✅ Visualize your matrix operations step by step
✅ Master the fundamental patterns: traverse, transform, search

🔥 ADVANCED PATTERNS YOU'VE LEARNED:
🎯 Basic Traversal: Visit every cell systematically
🎯 Element Transformation: Modify values across the matrix
🎯 Flood Fill: Explore connected components (islands)
🎯 Matrix Rotation: Geometric transformations
🎯 Spiral Traversal: Advanced navigation patterns

🚀 NOW GO BUILD AMAZING 2D APPLICATIONS!
Grid-based games, image processing, data analysis - the matrix world is yours!
""")
