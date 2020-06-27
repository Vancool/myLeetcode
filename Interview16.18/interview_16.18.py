class Solution(object):
    def patternMatching(self, pattern, value):
        if len(pattern) == 1: return True
        def Process(a, b, pattern, value):
            if not pattern: return len(value) == 0
            hashmap = {"a": a, "b": b}
            if a and b:
                tmp = ""
                for key in pattern:
                    tmp += hashmap[key]
                return tmp == value
            for key in pattern:
                if len(hashmap[key]) > 0:
                    v = hashmap[key]
                    if v == value[0:len(v)]:
                        return Process(a, b, pattern[1:], value[len(v):])
                    else:
                        return False
                else:
                    tmp = hashmap['a'] if key == 'b' else hashmap['b']
                    for i in range(len(value)):
                        v = value[:i]
                        if v == tmp: continue
                        if key == 'a':
                            if Process(v, b, pattern[1:], value[i:]):
                                return True
                        else:
                            if Process(a, v, pattern[1:], value[i:]):
                                return True
            return False

        return Process("","", pattern, value)


a = Solution()
pattern = "abba"
value = "dogcatcatdog"
print(a.patternMatching(pattern, value))
