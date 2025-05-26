# IKI KITOS SAVAITES ANTRADIENIO 
# class, method, ir tada CLI dali

from logging_info import LoggingInfo
import re
import string


LoggingInfo.configure_logging()
LoggingInfo.log_info("App is running.")

text = "Python's popularity...3 !  has grown? significantly in recent years. largely due to its versatility and the .growing demand for data  . analysis and .artificial@ intelligence []? applications!"

class TextValidator:
    @staticmethod
    def text_lenght(text: str) -> bool:
        sentence_count = text.count(".") + text.count("?") + text.count("!")
        if sentence_count >= 5:
           LoggingInfo.log_info("User entered >= 5 sentences")
           return True
        else:
            LoggingInfo.log_warning("User entered < 5 sentences")
            return False
    
    @staticmethod    
    def text_formatting(text: str) -> str:
        if not TextValidator.text_lenght(text):
            return "Text is too short. Must contain at least 5 sentences."
        
        formated_sentences = []
        sentences = re.split(r'(?<=[.?!])\s*', text.strip())
              
        for sentence in sentences: 
            sentence = re.sub(r'\s+([.?!])', r'\1', sentence)
            if sentence in string.punctuation:
                LoggingInfo.log_info("Ignoring sentences with only punctuation signs.")
                pass      
            elif sentence:
                formated_sentences.append(sentence[0].upper() + sentence[1:])
                
        return ' '.join(formated_sentences)
            
                    
       
class TextAnalyser:
    
    @staticmethod
    def number_of_words():
        pass
        
        
        
        
        
        
        
        
print(TextValidator.text_lenght(text))
print(TextValidator.text_formatting(text))