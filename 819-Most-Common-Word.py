class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = paragraph.lower()
        for c in words:
            if c == '!' or c == '?' or c == '\'' or c == ',' or c == '.' or c == '\"' or c == ';':
                words = words.replace(c, ' ')
        words = words.split()
        count_map = {}
        max_count = 0
        common_word = ""

        for word in words:
            if word not in banned:
                if word not in count_map:
                    count_map[word] = 1
                count_map[word] += 1
                if count_map[word] > max_count:
                    max_count = count_map[word]
                    common_word = word
        
        return common_word