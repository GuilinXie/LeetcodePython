class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.strip().split("/")
        stack = []
        for p in paths:
            if p == "." or p == "":
                continue
         
            if p == ".." and stack:
                stack.pop()
            elif p == ".." and not stack:
                continue
            else:
                stack.append(p)
                
        if not stack:
            return "/"
        else:
            return '/' + "/".join(stack)
