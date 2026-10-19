"""
Activity 5: Additional Exercises
Author: Laurence Segundo
"""

# Student-specific Inputs
LAST_NAME = "SEGUNDO"
STUDENT_ID = "TUPM-26-1220"
FAVORITE_ARTIST = "TAYLOR SWIFT"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)
ARTIST_SUM = sum(ord(c.upper()) - 64 for c in FAVORITE_ARTIST if c.isalpha())

print("=== STUDENT CONFIGURATION ===")
print(f"Seed Digit: {SEED_DIGIT}, ID Sum: {ID_SUM}, Artist Sum: {ARTIST_SUM}\n")


# ==========================================
# 1. EMERGENCY DISPATCH RECORD SEARCH
# ==========================================
print("=== 1. EMERGENCY DISPATCH RECORD SEARCH ===")
# Generate unique numerical records and rotate them
original_records = list(range(10, 10 + (ID_SUM % 10) + 10))
rotation_point = SEED_DIGIT % len(original_records)
rotated_records = original_records[rotation_point:] + original_records[:rotation_point]

target_incident = (ID_SUM + ARTIST_SUM) % 100 + 1

# Search in rotated list using modified binary/linear approach or index tracking
def search_rotated(data, target):
    comparisons = 0
    for i, val in enumerate(data):
        comparisons += 1
        if val == target:
            return i, comparisons
    return -1, comparisons

index, comp = search_rotated(rotated_records, target_incident)
print(f"Original Records : {original_records}")
print(f"Rotated Records  : {rotated_records}")
print(f"Target Incident  : {target_incident}")
print(f"Found at Index   : {index} | Comparisons: {comp}\n")


# ==========================================
# 2. UNIVERSITY ENROLLMENT RECORDS
# ==========================================
print("=== 2. UNIVERSITY ENROLLMENT RECORDS ===")
dept_a = sorted([(ID_SUM * i) % 200 for i in range(1, 6)])
dept_b = sorted([(ARTIST_SUM * i) % 200 for i in range(1, 6)])

def merge_departments(a, b):
    merged = []
    i = j = comparisons = 0
    while i < len(a) and j < len(b):
        comparisons += 1
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged, comparisons

consolidated, merge_comp = merge_departments(dept_a, dept_b)
print(f"Department A     : {dept_a}")
print(f"Department B     : {dept_b}")
print(f"Consolidated     : {consolidated}")
print(f"Comparisons      : {merge_comp}\n")


# ==========================================
# 3. E-COMMERCE ORDER PROCESSING
# ==========================================
print("=== 3. E-COMMERCE ORDER PROCESSING ===")
import random
base_orders = [(ARTIST_SUM * i) % 500 for i in range(1, 11)]

orders_sorted = sorted(base_orders)
orders_reverse = sorted(base_orders, reverse=True)
orders_random = base_orders.copy()
random.shuffle(orders_random)

def bubble_sort_metrics(data):
    a, comps, swaps = data.copy(), 0, 0
    for i in range(len(a)):
        swapped = False
        for j in range(len(a) - i - 1):
            comps += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return comps, swaps

print("Performance across conditions (Bubble Sort):")
for name, dataset in [("Sorted", orders_sorted), ("Reverse", orders_reverse), ("Random", orders_random)]:
    c, s = bubble_sort_metrics(dataset)
    print(f" - {name:8s} -> Comparisons: {c:3d}, Swaps: {s:3d}")