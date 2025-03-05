class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # # preprocess the freq count
        # freq_count = {}

        # for i in s :
        #     if i not in freq_count:
        #         freq_count[i] = 0
        #     freq_count[i] += 1
        
        # # Maintain a count of prev freq and haset to store the visited vals
        # visited = set()
        # count = 0
        # res = []
        # cur_count = 0

        # for c in s:
        #     cur_count += 1
        #     if c not in visited:
        #         count += 1
        #         visited.add(c)
        #     freq_count[c] -= 1
        #     if freq_count[c] == 0:
        #         count -= 1
        #     if count == 0:
        #         res.append(cur_count)
        #         cur_count = 0
        # return res

        ## Alternative Approach instead of count - save index in hashmap

        last_index_map = {}

        for i in range(len(s)):
            last_index_map[s[i]] = i
        
        end, cur_count = 0,0
        res = []

        for i in range(len(s)):
            cur_count += 1
            end = max(end, last_index_map[s[i]])

            if i == end:
                res.append(cur_count)
                cur_count = 0
        return res


            