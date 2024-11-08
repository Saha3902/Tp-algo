import random
import time
import tracemalloc
import matplotlib.pyplot as plt

# البحث التسلسلي البسيط
def linear_search(arr, target):
    comparisons = 0
    tracemalloc.start()  # بدء تتبع استهلاك الذاكرة
    start_time = time.time()

    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            break

    elapsed_time = (time.time() - start_time) * 1e9
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return comparisons, elapsed_time, peak - current



def optimized_linear_search(arr, target):
    comparisons = 0
    tracemalloc.start()
    start_time = time.time()

    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            break
        if arr[i] > target:
            break

    elapsed_time = (time.time() - start_time) * 1e9
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return comparisons, elapsed_time, peak - current


# البحث الثنائي التكراري
def iterative_binary_search(arr, target):
    comparisons = 0
    tracemalloc.start()
    start_time = time.time()

    low, high = 0, len(arr) - 1
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    elapsed_time = (time.time() - start_time) * 1e9
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return comparisons, elapsed_time, peak - current


# البحث الثنائي العودي
def recursive_binary_search(arr, low, high, target, comparisons=0):
    if low > high:
        return -1, comparisons

    comparisons += 1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return recursive_binary_search(arr, mid + 1, high, target, comparisons)
    else:
        return recursive_binary_search(arr, low, mid - 1, target, comparisons)

def recursive_binary_search_wrapper(arr, target):
    tracemalloc.start()
    start_time = time.time()
    index, comparisons = recursive_binary_search(arr, 0, len(arr) - 1, target)
    elapsed_time = (time.time() - start_time) * 1e9
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return comparisons, elapsed_time, peak - current


if __name__ == "__main__":
    # أحجام المصفوفات
    array_sizes = [10**3, 10**4, 10**5, 10**6]
    
    
    comparisons_data = {"Linear": [], "Optimized Linear": [], "Iterative Binary": [], "Recursive Binary": []}
    time_data = {"Linear": [], "Optimized Linear": [], "Iterative Binary": [], "Recursive Binary": []}
    memory_data = {"Linear": [], "Optimized Linear": [], "Iterative Binary": [], "Recursive Binary": []}

    
    for array_size in array_sizes:
        print(f"Testing array size: {array_size}")

        
        arr = sorted([random.uniform(0, 1000) for _ in range(array_size)])
        target = random.choice(arr)  

        
        comparisons, elapsed_time, memory_usage = linear_search(arr, target)
        comparisons_data["Linear"].append(comparisons)
        time_data["Linear"].append(elapsed_time)
        memory_data["Linear"].append(memory_usage)

        comparisons, elapsed_time, memory_usage = optimized_linear_search(arr, target)
        comparisons_data["Optimized Linear"].append(comparisons)
        time_data["Optimized Linear"].append(elapsed_time)
        memory_data["Optimized Linear"].append(memory_usage)

        comparisons, elapsed_time, memory_usage = iterative_binary_search(arr, target)
        comparisons_data["Iterative Binary"].append(comparisons)
        time_data["Iterative Binary"].append(elapsed_time)
        memory_data["Iterative Binary"].append(memory_usage)

        comparisons, elapsed_time, memory_usage = recursive_binary_search_wrapper(arr, target)
        comparisons_data["Recursive Binary"].append(comparisons)
        time_data["Recursive Binary"].append(elapsed_time)
        memory_data["Recursive Binary"].append(memory_usage)

    plt.figure(figsize=(12, 8))
    plt.plot(array_sizes, comparisons_data["Linear"], label="Linear Search")
    plt.plot(array_sizes, comparisons_data["Optimized Linear"], label="Optimized Linear Search")
    plt.plot(array_sizes, comparisons_data["Iterative Binary"], label="Iterative Binary Search")
    plt.plot(array_sizes, comparisons_data["Recursive Binary"], label="Recursive Binary Search")
    plt.title("Comparisons for Each Algorithm")
    plt.xlabel("Array Size")
    plt.ylabel("Comparisons")
    plt.xscale("log")
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(12, 8))
    plt.plot(array_sizes, time_data["Linear"], label="Linear Search")
    plt.plot(array_sizes, time_data["Optimized Linear"], label="Optimized Linear Search")
    plt.plot(array_sizes, time_data["Iterative Binary"], label="Iterative Binary Search")
    plt.plot(array_sizes, time_data["Recursive Binary"], label="Recursive Binary Search")
    plt.title("Execution Time for Each Algorithm (nanoseconds)")
    plt.xlabel("Array Size")
    plt.ylabel("Time (nanoseconds)")
    plt.xscale("log")
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(12, 8))
    plt.plot(array_sizes, memory_data["Linear"], label="Linear Search")
    plt.plot(array_sizes, memory_data["Optimized Linear"], label="Optimized Linear Search")
    plt.plot(array_sizes, memory_data["Iterative Binary"], label="Iterative Binary Search")
    plt.plot(array_sizes, memory_data["Recursive Binary"], label="Recursive Binary Search")
    plt.title("Memory Usage for Each Algorithm (bytes)")
    plt.xlabel("Array Size")
    plt.ylabel("Memory Usage (bytes)")
    plt.xscale("log")
    plt.legend()
    plt.grid(True)
    plt.show()
