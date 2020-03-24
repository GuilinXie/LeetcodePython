class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, res, [], 0)
        return res

    def dfs(self, s, res, tmp, pos):

        if len(tmp) == 4 and pos == len(s):
            res.append(".".join(tmp))
            return
        # restriction to the following 1,2,3 pos
        for i in range(1, 4):

            # check conditions, if not satified, then not go into the next dfs
            if pos + i > len(s):
                break
            sub = s[pos:pos + i]
            if (len(sub) > 1 and sub[0] == "0"):
                break
            if int(sub) >= 256:
                break
            if len(tmp) > 4:
                break

            tmp.append(sub)
            self.dfs(s, res, tmp, pos + i)
            tmp.pop()  # backtrack


if __name__ == "__main__":
    s = Solution()
    res = s.restoreIpAddresses("25525511135")
    print(res)