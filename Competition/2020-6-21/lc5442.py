from collections import deque
class Solution(object):
    def avoidFlood(self, rains):
        if len(rains) == 1: return [-1]
        hashmap = {}
        res = [-1] * len(rains)
        zero_queue = deque()
        invalid_rain = deque()
        # while i < len(rains) and rains[i] > 0:
        #     if rains[i] in hashmap: return []
        #     hashmap.add(rains[i])
        #     i += 1
        # if i == len(rains): return [-1] * len(rains)
        fast = 0
        # while fast < len(rains) and not rains[fast]:
        #      zero_queue.append(fast)
        #      fast += 1
        while fast < len(rains):
            if rains[fast] > 0:
                if rains[fast] in hashmap:
                    # if zero_queue:
                    #pos = zero_queue.pop()
                        # if pos < hashmap[rains[fast]]: return []
                        # res[pos] = rains[fast]
                    #     hashmap[rains[fast]] = fast
                    # else:
                    #     return []
                    invalid_rain.append((hashmap[rains[fast]],fast))
                hashmap[rains[fast]] = fast
            else:
                zero_queue.append(fast)
            fast += 1
        while invalid_rain:
            pre_pos, rain_pos = invalid_rain[-1]
            i = len(zero_queue)-1
            while i >= 0:
                pos = zero_queue[i]
                if pre_pos <pos < rain_pos:
                    res[pos] = rains[rain_pos]
                    zero_queue.remove(pos)
                    invalid_rain.pop()
                    break
                i -= 1
            if i < 0: return []
        while zero_queue:
            res[zero_queue.popleft()] = 1
        return res

a = Solution()
rains = [1,0,2,0,2,1]
print(a.avoidFlood(rains))