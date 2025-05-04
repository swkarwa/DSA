
from collections import deque
from typing import List
class Solution:
    def minMutation(self, start_gen: str, end_gen: str, bank: List[str]) -> int:
        valid_gene = list({ ch for ch in start_gen})
        seen = set()
        q = deque()
        q.append(start_gen)
        seen.add(start_gen)
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                current = q.popleft()
                if current == end_gen:
                    return level
                for c in valid_gene:
                    idx = 0
                    while idx < len(current):
                        ch = start_gen[idx]
                        changed_gen = ""
                        if ch != c:
                            changed_gen = current[0:idx] + c + current[idx+1:]
                        if changed_gen in bank and changed_gen not in seen:
                            q.append(changed_gen)
                            seen.add(changed_gen)
                        idx+=1
            level+=1
        return -1


start_gene = "AACCGGTT"
end_gene = "AACCGCTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]

ans = Solution().minMutation(start_gene , end_gene , bank)
print(ans)