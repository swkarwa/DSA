class Solution:
    def trap(self, height) -> int:
        lmax = [0] * len(height)
        rmax = [0] * len(height)
        lmax[0] = height[0]
        rmax[-1] = height[-1]

        # find overall max from left
        for i in range(1, len(height)):
            lmax[i] = max(lmax[i - 1], height[i])

        for i in range(len(height) - 2, -1, -1):
            rmax[i] = max(rmax[i + 1], height[i])
        ans = 0;
        for i in range(1, len(height)):
            ans += min(lmax[i], rmax[i]) - height[i]
        return ans

result = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(result)