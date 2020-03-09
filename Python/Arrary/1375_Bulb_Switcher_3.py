class Solution:
    # Method 1: store the max bulb,
    # and assume all bulb is blue
    # then check if all on bulbs are blue, using index
    def numTimesAllBlue(self, light):
        if len(light) <= 0:
            return 0
        maxOnBulb = 0
        res = 0
        for numOnBulb, bulb in enumerate(light, 1):
            maxOnBulb = max(bulb, maxOnBulb)
            if maxOnBulb == numOnBulb:
                res += 1
        return res

    # Method 2: keep a blueBulb to track the last max blueBulb Num
    # update blueBulb after turning every bulb
    def numTimesAllBlue(self, light):
        if len(light) <= 0:
            return 0
        seen = set()
        blueBulb = 0
        onSwitchCnt = 0
        res = 0
        for bulb in light:
            seen.add(bulb)
            onSwitchCnt += 1
            if self.checkBlue(bulb, seen, blueBulb):
                blueBulb += 1
                for i in range(bulb + 1, len(light) + 1):
                    if i not in seen:
                        break
                    blueBulb += 1
                if blueBulb == onSwitchCnt:
                    res += 1
        return res

    def checkBlue(self, bulb, seen, blueIndex):
        for i in range(blueIndex + 1, bulb):
            if i not in seen:
                return False
        return True