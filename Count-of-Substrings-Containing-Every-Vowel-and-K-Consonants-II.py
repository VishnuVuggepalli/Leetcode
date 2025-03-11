class Solution:
    def countOfSubstrings(self, word: str, thre: int) -> int:
        def check_least(k):
            i, j = 0, 0
            vowels = ('a','e','i','o','u')
            vowel_freq = defaultdict(int)
            char_count = 0
            count = 0
            while j < len(word) or i < len(word):
                if len(vowel_freq) == 5 and char_count >= k:
                    count += len(word) - j + 1
                    if word[i] not in vowels:
                        char_count -= 1
                    else:
                        vowel_freq[word[i]] -= 1
                        if vowel_freq[word[i]] == 0: 
                            del vowel_freq[word[i]]
                    i += 1
                else:
                    if j == len(word):
                        break
                    if word[j] not in vowels : 
                        char_count += 1
                    else:
                        vowel_freq[word[j]] += 1
                    j += 1
            return count
        # print(check_least(thre), check_least(thre + 1))

        return check_least(thre) - check_least(thre + 1)
        
        # while i < j:
        #     if len(vowel_freq) == 5 and char_count == k:
        #         count += 1
        #     else:
        #         break
        #     if word[i] in vowels:
        #         vowel_freq[word[i]] -= 1
        #         if vowel_freq[word[i]] == 0: 
        #             del vowel_freq[word[i]]
        #     else:
        #         char_count -= 1
        #     i += 1

        # print(i,j, vowel_freq, char_count, count)
        return count