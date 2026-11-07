'''
435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.


Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.


'''


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        remove = 0
        #End time of the first interval
        prev_end = intervals[0][1]

        for i  in range(1,len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start < prev_end:
                remove = remove+1
            else:
                prev_end = end
        return remove
    

obj = Solution()

intervals = [[1,2],[2,3],[3,4],[1,3]]

print(obj.eraseOverlapIntervals(intervals))  # Output: 1



'''

Topic: Greedy Algorithm + Sorting
Difficulty: Medium
Main concept: Find the minimum number of intervals to remove so that the remaining intervals do not overlap.

Let's understand the problem with a simple example first, then solve it using Python.

Each interval contains:
- First number = Start time
- Second number = End time
We need to remove the minimum number of intervals so that no two remaining intervals overlap.


3. Which approach should we use?
We use Greedy Algorithm.

The greedy strategy is:
Always keep the interval that finishes earliest.

Why?

If an interval finishes early, it gives us more available time to accommodate future intervals.



'''


'''

For LeetCode 435, we use the Greedy Algorithm with Sorting.

I'll explain the complete approach step by step, especially:

1. Why we sort by ending time.
2. Why we store the first interval's ending time.
3. How we identify overlapping intervals.
4. Why we update `prev_end` only when we keep an interval.

## 1. Understand our goal

Given:

```
intervals = [    [1, 2],    [2, 3],    [3, 4],    [1, 3]]
```

We need to remove the minimum number of intervals so that the remaining intervals don't overlap.

## 2. Step 1: Sort intervals by ending time

```
intervals.sort(key=lambda x: x[1])
```

Why?

Our strategy is:

Always try to keep the interval that finishes earliest.

Because an interval that finishes early gives us more opportunities to accommodate other intervals.

After sorting:

```
intervals = [    [1, 2],    [2, 3],    [1, 3],    [3, 4]]
```

Look at the ending times:

```
2 → 3 → 3 → 4
```

They are now in ascending order.

## 3. Step 2: Initialize variables

```
remove = 0prev_end = intervals[0][1]
```

Let's understand both.

`remove = 0`

Initially, we haven't removed any interval.

`prev_end = intervals[0][1]`

This is important.

`intervals[0]` gives us the first interval:

```
intervals[0] = [1, 2]
```

`intervals[0][1]` gives us its ending time:

```
prev_end = 2
```

Why store this?

Because we need to compare the next interval's starting time with the ending time of the last interval we kept.

## 4. Step 3: Iterate through intervals

```
for i in range(1, len(intervals)):
```

Why start from 1 instead of 0?

Because we already considered the first interval and stored its ending time in `prev_end`.

Now let's compare the remaining intervals.

Dry run

First interval kept

# [1, 2]

`prev_end = 2`

This is our reference interval.

Iteration 1

## [2, 3]

```
start = 2prev_end = 2
```

Check:

```
if start < prev_end:    # 2 < 2 → False
```

No overlap. Keep `[2,3]`.

Update:

```
prev_end = 3
```

Keep

Iteration 2

## [1, 3]

```
start = 1prev_end = 3
```

Check:

```
if start < prev_end:    # 1 < 3 → True
```

Overlap! Remove `[1,3]`.

```
remove += 1
```

Remove

`prev_end` remains 3.

Iteration 3

## [3, 4]

```
start = 3prev_end = 3
```

Check:

```
if start < prev_end:    # 3 < 3 → False
```

No overlap. Keep `[3,4]`.

Update:

```
prev_end = 4
```

Keep

Final result

# 1

Minimum number of intervals removed.

## 5. Complete code with comments

```
class Solution:    def eraseOverlapIntervals(self, intervals):        # Step 1: Sort by ending time        intervals.sort(key=lambda x: x[1])        # Step 2: Initialize        remove = 0        prev_end = intervals[0][1]        # Step 3: Iterate from second interval        for i in range(1, len(intervals)):            start = intervals[i][0]            end = intervals[i][1]            # Step 4: Check overlap            if start < prev_end:                # Remove current interval                remove += 1            else:                # Keep current interval                prev_end = end        return remove
```

## 6. Remember this important logic

| Condition           | Meaning    | Action                                      |
| ------------------- | ---------- | ------------------------------------------- |
| `start < prev_end`  | Overlap    | Remove current interval                     |
| `start >= prev_end` | No overlap | Keep current interval and update `prev_end` |

One important point: We don't actually delete intervals from the array. We simply count how many intervals we need to remove.

## 7. Test your understanding

Let's try a different example.

```
intervals = [    [1, 5],    [2, 3],    [3, 4]]
```

After sorting by ending time:

```
[[2, 3], [3, 4], [1, 5]]
```

Question 1: Which interval will we keep first?

`[1,5]`

`[2,3]`

`[3,4]`

Check answer

Correct!The first interval after sorting is `[2,3]`, because its ending time (3) is the smallest.

The key concept to remember for interviews:

Sort by ending time → Keep earliest finishing interval → Compare next starting time → Remove if overlapping.



'''












