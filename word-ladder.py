class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordListSet = set(wordList)
        if endWord not in wordListSet:
            return 0
        alpha = "abcdefghijklmnopqrstuvwxyz"
        queue = [beginWord]
        ans = 1
        while queue:
            next_layer = []
            for curr in queue:
                if curr == endWord:
                    return ans
                for i in range(len(beginWord)):
                    for letter in alpha:
                        tmp = curr[:i] + letter + curr[i+1:]
                        if tmp in wordListSet:
                            wordListSet.remove(tmp)
                            next_layer.append(tmp)
            ans += 1
            queue = next_layer
        return 0
            
        