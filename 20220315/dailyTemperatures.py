def dailyTemperatures(self, T: List[int]) -> List[int]:
    answer = [0] * len(T)
    stack = []
    res = [0] * len(T)
    for i in range(len(T)):
        while stack and T[i] > T[stack[-1]]:
            cur = stack.pop()
            res[cur] = i - cur
        stack.append(i)
    return res



