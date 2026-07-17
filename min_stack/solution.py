class MinStack:
    # Time: O(1)
    # Space: O(1)
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    # Time: O(1)
    # Space: O(1)
    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    # Time: O(1)
    # Space: O(1)
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    # Time: O(1)
    # Space: O(1)
    def top(self) -> int:
        return self.stack[-1]

    # Time: O(?)
    # Space: O(?)
    def get_min(self) -> int:
        return self.min_stack[-1]
