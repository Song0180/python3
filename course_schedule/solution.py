class Solution:
    # Time: O(V + E)
    # Space: O(V + E)
    def can_finish_dfs(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        pre_map = {i: [] for i in range(num_courses)}

        for c, p in prerequisites:
            pre_map[c].append(p)

        visiting = set()
        completed = set()

        def dfs(course):
            if course in visiting:
                return False

            if course in completed:
                return True

            visiting.add(course)

            for pre in pre_map[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            completed.add(course)
            return True

        for i in range(num_courses):
            if not dfs(i):
                return False

        return True
