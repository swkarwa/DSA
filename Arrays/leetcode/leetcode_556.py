class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Handle single-digit edge case
        if n <= 9:
            return -1

        # Convert the number to a list of digits
        digits = [int(d) for d in str(n)]

        # Step 1: Find the first decreasing element from the right
        si = None
        for i in range(len(digits) - 1, 0, -1):
            if digits[i - 1] < digits[i]:
                si = i - 1
                break

        # If no such element is found, the digits are in descending order
        if si is None:
            return -1

        # Step 2: Find the smallest digit larger than `digits[si]` to the right
        for i in range(len(digits) - 1, si, -1):
            if digits[i] > digits[si]:
                # Swap the elements
                digits[si], digits[i] = digits[i], digits[si]
                break

        # Step 3: Sort the digits after the `si` index to get the smallest permutation
        digits[si + 1:] = sorted(digits[si + 1:])

        # Convert the list of digits back to an integer
        result = int(''.join(map(str, digits)))

        # Ensure the result fits within a 32-bit signed integer
        return result if result <= (2 ** 31) - 1 else -1

print(Solution().nextGreaterElement(124310))