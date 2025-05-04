class Solution:
    def exclusiveTime(self, n: int, logs):
        result = [0]*n
        stack = list()
        for log in logs:
            func_id , log_type , time = log.split(":")
            if(log_type == 'start'):
                func_id = int(func_id)
                time = int(time)
                data = [func_id, time, 0]
                stack.append(data)
            else:
                top = stack.pop()
                interval = int(time) - top[1] + 1
                actual_time = interval - top[2]
                result[top[0]] += actual_time
                if(stack):
                    stack[-1][2] += interval
        print(result)
        return result

Solution().exclusiveTime(2,
    ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
)
