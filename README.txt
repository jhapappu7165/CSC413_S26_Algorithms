CSC 413 — Inversion Count (Divide-and-Conquer)
==============================================

TASK
----
Count inversions in IntegerArray.txt (100,000 distinct integers 1 through
100,000; one integer per line, in array order). Use divide-and-conquer:
count inversions during the merge step (merge-sort style).

SOFTWARE ENVIRONMENT
--------------------
- Python 3.x
- Input file: IntegerArray.txt (same directory as the script)

HOW TO COMPILE AND RUN
----------------------
No compile step. From the project folder:

    python3 inversion_count.py

OUTPUT
------
- Prints: inversion count and running time (seconds).
- Writes: SortedArray.txt (sorted array, one integer per line).
