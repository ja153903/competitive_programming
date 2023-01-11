class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk, res = [], []

        for i, ch in enumerate(s):
            if ch == "(":
                res.append("")
                stk.append(i)
            elif ch == ")":
                if stk:
                    top = stk.pop()
                    res[top] = "("
                    res.append(")")
                else:
                    res.append("")
            else:
                res.append(ch)

        return "".join([ch for ch in res if ch != ""])
