class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        name_dict = {}
        for index, name in enumerate(keyName):
            name_dict[name]= name_dict.get(name, [])
            name_dict[name].append(int(keyTime[index].replace(":","")))
        ans = []

        for name, key_list in name_dict.items():
            key_list.sort()
            n = len(key_list)
            for i in range(n-2):
                if key_list[i+2] - key_list[i] <= 100:
                    ans.append(name)
                    break
        
        return sorted(ans)