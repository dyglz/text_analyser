
from logging_info import LoggingInfo
import re
from collections import Counter
from text_validator import TextValidator

   
class TextAnalyser:
    
    @staticmethod
    def number_of_sentences(formatted_text: str) -> int:
        return formatted_text.count(".") + formatted_text.count("?") + formatted_text.count("!")
        
    @staticmethod
    def number_of_words(formatted_text: str) -> int:
        words = re.findall(r"\b[\w']+\b", formatted_text)
        return len(words)
    
    @staticmethod
    def count_of_numbers(formatted_text: str) -> int:
        numbers_count = len(re.findall(r"\d+", formatted_text))
        if numbers_count > 0:
            return numbers_count
        else:
            return 0
    
    @staticmethod
    def most_common_word(formatted_text: str) -> str:
        words = re.findall(r"\b[\w']+\b", formatted_text.lower())
        most_common = Counter(words).most_common(1)
        if most_common:
            return most_common[0][0]
        else:
            return f"No text found..."
        
    @staticmethod
    def text_report(formatted_text: str) -> dict:
        report = {
            "fixed_text": formatted_text,
            "number_of_words": TextAnalyser.number_of_words(formatted_text),
            "number_of_sentences": TextAnalyser.number_of_sentences(formatted_text),
            "count_of_numbers": TextAnalyser.count_of_numbers(formatted_text),
            "most common word": TextAnalyser.most_common_word(formatted_text)
        }
        # for key, value in report.items():
        #     print(f"{key}: {value}")
        return report

        
        
        
        
        

