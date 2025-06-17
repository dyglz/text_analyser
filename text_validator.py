
from typing import List
from logging_info import LoggingInfo
import re
import string


class TextValidator:
    def __init__(self, text: str) -> None:
        self.text = text
    
    def validate_text_length(self) -> bool:
        sentence_count = self.text.count(".") + self.text.count("?") + self.text.count("!")
        if sentence_count >= 5:
            LoggingInfo.log_info("User entered >= 5 sentences. Trying to format the text.")      
            return True
        else:
            LoggingInfo.log_warning("User entered < 5 sentences.")
            return False
    
    def text_formatting(self) -> str:
        formatted_text: List[str] = []
        sentences = re.split(r'(?<=[.?!])\s*', self.text.strip())
              
        for sentence in sentences: 
            sentence = re.sub(r'\s+([.?!])', r'\1', sentence)
            if sentence in string.punctuation:
                LoggingInfo.log_info("Ignoring sentences with only punctuation signs.")
                continue      
            elif sentence:
                formatted_text.append(sentence[0].upper() + sentence[1:])
        
        LoggingInfo.log_info("Text is formatted.")       
        return ' '.join(formatted_text)
            