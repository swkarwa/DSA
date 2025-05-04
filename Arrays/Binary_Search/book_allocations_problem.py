class Solution:

    # Function to find minimum number of pages.
    def is_possible(self, books, students, pages_can_red):
        current_pages_red = 0
        needed_students = 1
        for pages in books:
            if ((current_pages_red + pages) <= pages_can_red):
                current_pages_red += pages
            else:
                needed_students += 1
                current_pages_red = pages
        if (needed_students <= students):
            return True
        return False

    def findPages(self, arr, m):
        if(len(arr) < m):
            return -1
        l, h = max(arr), sum(arr)
        ans = 0
        while (l <= h):
            pages = (l + h) // 2
            if (self.is_possible(arr, m, pages)):
                ans = pages
                h = pages - 1
            else:
                l = pages + 1
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    ob = Solution().findPages([12 ,34 ,67 ,90] , 2)
    print(ob)


# } Driver Code Ends
