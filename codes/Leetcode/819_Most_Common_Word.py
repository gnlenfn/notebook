from typing import List
from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        remove_punc = re.sub(r'[^A-z ]', " ", paragraph)
        words = [w for w in remove_punc.split() if w not in banned]
        return Counter(words).most_common(1)[0][0]