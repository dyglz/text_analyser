
import re
from collections import Counter
from typing import Dict
from dataclasses import dataclass


@dataclass
class TextAnalyser:
    text: str

    @property
    def count_of_sentences(self) -> int:
        return self.text.count(".") + self.text.count("?") + self.text.count("!")
        
    @property
    def count_of_words(self) -> int:
        words = re.findall(r"\b[\w']+\b", self.text)
        return len(words)
    
    @property
    def count_of_numbers(self) -> int:
        numbers_count = len(re.findall(r"\d+", self.text))
        return numbers_count
    
    @property
    def most_common_word(self) -> str:
        words = re.findall(r"\b[\w']+\b", self.text.lower())
        most_common = Counter(words).most_common(1)
        if most_common and most_common[0][1] > 1:
            return most_common[0][0]
        else:
            return f"No most common word found..."
        
        
    def text_report(self) -> Dict:
        return {
            "fixed_text": self.text,
            "number_of_words": self.count_of_words,
            "number_of_sentences": self.count_of_sentences,
            "count_of_numbers": self.count_of_numbers,
            "most common word": self.most_common_word
        }
