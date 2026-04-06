import time

def readInputFile(filename):
    numbers = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                numbers.append(int(line))
    return numbers

def mergeAndCount(left, right):
    merged = []
    i = j = 0
    invCount = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            invCount += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, invCount

def sortAndCount(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    sortedLeft, leftInv = sortAndCount(left)
    sortedRight, rightInv = sortAndCount(right)
    merged, splitInv = mergeAndCount(sortedLeft, sortedRight)

    totalInv = leftInv + rightInv + splitInv
    return merged, totalInv

def writeOutputFile(filename, sortedNum):
    with open(filename, "w") as file:
        for num in sortedNum:
            file.write(f"{num}\n")


def main():
    inputF = "IntegerArray.txt"
    outputF = "SortedArray.txt"

    numbers = readInputFile(inputF)

    startTime = time.perf_counter()
    sortedNum, inversion_count = sortAndCount(numbers)
    endTime = time.perf_counter()

    running_time = endTime - startTime

    writeOutputFile(outputF, sortedNum)

    print("Inversion Count:", inversion_count)
    print("Running Time (seconds):", running_time)
    print("Sorted output saved to:", outputF)

if __name__ == "__main__":
    main()