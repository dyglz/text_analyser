
from typing import Optional
from logging_info import LoggingInfo
import re
import string


class TextValidator:
    
    @staticmethod
    def validate_text_lenght(text: str) -> bool:
        sentence_count = text.count(".") + text.count("?") + text.count("!")
        if sentence_count >= 5:
            LoggingInfo.log_info("User entered >= 5 sentences. Trying to format the text.")      
            return True
        else:
            LoggingInfo.log_warning("User entered < 5 sentences.")
            return False
    
    @staticmethod
    def text_formatting(text: str) -> str:
        formatted_sentences = []
        sentences = re.split(r'(?<=[.?!])\s*', text.strip())
              
        for sentence in sentences: 
            sentence = re.sub(r'\s+([.?!])', r'\1', sentence)
            if sentence in string.punctuation:
                LoggingInfo.log_info("Ignoring sentences with only punctuation signs.")
                pass      
            elif sentence:
                formatted_sentences.append(sentence[0].upper() + sentence[1:])
        
        LoggingInfo.log_info("Text is formatted.")       
        return ' '.join(formatted_sentences)
            