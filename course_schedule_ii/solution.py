class Solution:
    # Time: O(?)
    # Space: O(?)
    def find_order(self, num_courses: int, prerequisites: list[list[int]]) -> list[int]:
        order = []

        pre_map = {i: [] for i in range(num_courses)}
        for c, p in prerequisites:
            pre_map[c].append(p)

        visiting = set()
        complete = set()

        def dfs(course):
            if course in visiting:
                return False

            if course in complete:
                return True

            visiting.add(course)
            for pre in pre_map.get(course):
                if not dfs(pre):
                    return False
            visiting.remove(course)

            complete.add(course)
            order.append(course)
            return True

        for i in range(num_courses):
            if not dfs(i):
                return []

        return order
