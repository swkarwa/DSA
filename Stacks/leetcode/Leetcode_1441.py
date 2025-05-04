class Solution:
    def buildArray(self, target, n: int):
        result = list()
        j = 0
        for i in range(1, n + 1):
            if (i == target[j]):
                result.append("Push")
                j += 1
            else:
                result.append("Push")
                result.append("Pop")
            if (j >= len(target)):
                break;
        return result

Solution().buildArray([1,3] , 3)