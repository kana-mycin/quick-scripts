import java.util.Random;
import java.util.Arrays;

/**
  * Reference implementations of several sorting algorithms from CS61B, with annotations.
  */
public class Sorts {

    /* Utility to swap array values. Note that the order of index1 and index2 does not matter. */
    public static void swap(int[] arr, int index1, int index2) {
        int swap = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = swap;
    }

    /* An implementation of bubble sort, which runs in O(n^2). Not great. */
    public static void bubbleSort(int[] arr) {
        // "i" is the farthest point we'll iterate to. 
        // Every pass we make over the array, we have 1 less value to worry about (it's the biggest), so we decrement i.
        for (int i = arr.length - 1; i >= 0; i--) {
            // Among the remaining values, bubble up from left to right.
            for (int j = 0; j < i; j++) {
                if (arr[j] > arr[j+1]) {
                    swap(arr, j, j+1);
                }
            }
        }
    }

    /* Insertion sort runs in O(n^2), but works well on almost-sorted lists. */
    public static void insertionSort(int[] arr) {
        // Leftmost index of the unsorted area. Everything to the left is sorted already.
        for (int i = 1; i < arr.length; i++) {
            // Insert the next value into the list.
            for (int j = i; j >= 1; j--) {
                if (arr[j-1] > arr[j]) {
                    swap(arr, j, j-1);
                }
            }
        }
    }

    /* A recursive implementation of mergesort. Requires the creation of an extra memory buffer. */
    public static void mergeSort(int[] arr) {
        int[] buf = new int[arr.length];
        mergeHelper(arr, 0, arr.length-1, buf);
    }

    private static void mergeHelper(int[] arr, int start, int end, int[] buf) {
        if (start >= end) {
            return;
        } else {
            // Sort both halves (divide and conquer!)
            int mid = (start+end) / 2;
            mergeHelper(arr, start, mid, buf);
            mergeHelper(arr, mid+1, end, buf);

            // Merge the two sorted halves into a combined, sorted section.
            int leftPtr = start;
            int rightPtr = mid+1;
            for (int bufPtr = start; bufPtr <= end; bufPtr++) {
                // Pick the smallest element of either left or right that hasn't been used yet, add it to the growing sorted section.
                if (rightPtr > end) {
                    buf[bufPtr] = arr[leftPtr];
                    leftPtr++;
                } else if (leftPtr > mid) {
                    buf[bufPtr] = arr[rightPtr];
                    rightPtr++;
                } else if (arr[leftPtr] < arr[rightPtr]) {
                    buf[bufPtr] = arr[leftPtr];
                    leftPtr++;
                } else {
                    buf[bufPtr] = arr[rightPtr];
                    rightPtr++;
                }
            }

            // Copy the sorted section back
            for (int bufPtr = start; bufPtr <= end; bufPtr++) {
                arr[bufPtr] = buf[bufPtr];
            }
        }
    }

    /* Recursive implementation of quicksort. This implementation is not the most efficient in terms of swaps, but is easy to understand. */
    public static void quickSort(int[] arr) {
        quickSortHelper(arr, 0, arr.length-1);
    }

    private static void quickSortHelper(int[] arr, int start, int end) {
        if (start >= end) {
            return;
        } else {
            // There are many ways to select a good pivot value. You can use the first value, the midpoint, or you can even pick it randomly.
            // For simplicity, we'll just pick whatever value is at the midpoint.
            int pivot = (start+end) / 2;
            int pivotValue = arr[pivot];

            // We want to shove everything less than or equal to the pivot value to the left, and everything greater than the pivot value to the right.

            // First, every time we find a larger value to the left of the pivot, move it to the right side and shift the pivot.
            int leftPtr = start;
            while (leftPtr < pivot) {
                if (arr[leftPtr] > pivotValue) {
                    swap(arr, leftPtr, pivot-1);
                    swap(arr, pivot-1, pivot);
                    pivot--;
                } else {
                    leftPtr++;
                }
            }

            // Then, do the same to the right side.
            int rightPtr = end;
            while (rightPtr > pivot) {
                if (arr[rightPtr] < pivotValue) {
                    swap(arr, rightPtr, pivot+1);
                    swap(arr, pivot+1, pivot);
                    pivot++;
                } else {
                    rightPtr--;
                }
            }

            // Now sort the two partitioned halves. The partition should be such that leftPtr points to the start of the right partition.
            quickSortHelper(arr, start, pivot-1);
            quickSortHelper(arr, pivot+1, end);
        }
    }

    /* Check if an array is sorted. */
    public static boolean isSorted(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i+1]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        // First create an array and populate it with random numbers.
        Random rand = new Random();
        int[] arr = new int[20];
        for (int i=0; i<arr.length; i++) {
            arr[i] = rand.nextInt(100);
        }
        int[] input1 = Arrays.copyOf(arr, arr.length);
        // int[] input2 = Arrays.copyOf(arr, arr.length);
        // Sort the array.
        quickSort(input1);
        System.out.println(Arrays.toString(input1));
        System.out.println("Sorted? " + isSorted(input1));
    }

}