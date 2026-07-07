class Solution:
    # Time: O(n)
    # Space: O(n)
    def insert_bf(
        self, intervals: list[list[int]], new_interval: list[int]
    ) -> list[list[int]]:
        head, tail = [], []
        ins_idx = 0
        for i in range(len(intervals)):
            if intervals[i][0] >= new_interval[0]:
                break
            head.append(intervals[i])
            ins_idx += 1

        affected = []

        if (
            len(intervals) >= 1
            and intervals[ins_idx - 1][1] >= new_interval[0]
            and intervals[ins_idx - 1][0] < new_interval[0]
        ):
            affected.append(intervals[i - 1])
            if head:
                head.pop()

        end_idx = ins_idx
        while end_idx < len(intervals) and new_interval[1] >= intervals[end_idx][0]:
            affected.append(intervals[end_idx])
            end_idx += 1

        for j in range(end_idx, len(intervals)):
            tail.append(intervals[j])

        merged = None
        if not affected:
            merged = new_interval
        else:
            merged = [
                min(new_interval[0], affected[0][0]),
                max(new_interval[1], affected[len(affected) - 1][1]),
            ]

        # print("affected", affected, merged, "head", head, tail, ins_idx, end_idx)
        return head + [merged] + tail

    # time: O(n)
    # space: O(1) extra, O(n) res
    def insert(
        self, intervals: list[list[int]], new_interval: list[int]
    ) -> list[list[int]]:
        n = len(intervals)
        i = 0
        res = []

        while i < n and intervals[i][1] < new_interval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and new_interval[1] >= intervals[i][0]:
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])
            i += 1
        res.append(new_interval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res
