class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        arrayWord1 = list(word1)
        arrayWord2 = list(word2)
        mergeAlternately = ""
        while len(arrayWord1) or len(arrayWord2):
            if len(arrayWord1):
                char = arrayWord1.pop(0)
                mergeAlternately += char
            if len(arrayWord2):
                character = arrayWord2.pop(0)
                mergeAlternately += character
        return mergeAlternately
    
