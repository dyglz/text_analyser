from logging_info import LoggingInfo
from text_analyser import TextAnalyser
from text_validator import TextValidator

LoggingInfo.configure_logging()
LoggingInfo.log_info("App is running.")
formatted_sentences = ""
analyser = None

# text_example = Python's popularity...!  has 3 grown? significantly in recent years. largely due to its versatility and the .growing4 demand for data  . analysis and .artificial@ intelligence []? applications! What is this @all about..?5

while True:
    print("===   Text Analyser   ===")
    print("1. Enter text\n2. Text Report\n3. Number of words\n4. Number of sentences\n5. Number of numbers\n6. Most common word\n0. Exit")
    
    try:
        menu_selection = int(input("Enter your selection: "))
        if 0 <= menu_selection <=6:
            if menu_selection == 0:
                print("===    Exiting App    ===")
                LoggingInfo.log_info("App is Closed.")
                break
            elif menu_selection == 1:
                LoggingInfo.log_info("User is entering text.")
                text = input("\nEnter your text (minimum 5 sentences): ")
                validator = TextValidator(text)
                if validator.validate_text_lenght():
                    formatted_sentences = validator.text_formatting()
                    analyser = TextAnalyser(formatted_sentences)
                    print("\nText entered successfully!")
                    print(f"{formatted_sentences}")
                else:
                    print("Text is too short. Must contain at least 5 sentences.\n")                
            elif menu_selection == 2:
                if analyser:
                    print("------  Text Report  -------")
                    print(analyser.text_report())
                    LoggingInfo.log_info("Displaying text report.")
                else:
                    print("No text entered yet...\n")                  
            elif menu_selection == 3:
                if analyser:
                    print("----  Number of words  -----")
                    print(analyser.number_of_words)
                    LoggingInfo.log_info("Displaying number of words.")              
                else:
                    print("No text entered yet...\n") 
            elif menu_selection == 4:
                if analyser:
                    print("---  Number of sentences  --")
                    print(analyser.number_of_sentences)
                    LoggingInfo.log_info("Displaying number of sentences.")               
                else:
                    print("No text entered yet...\n") 
            elif menu_selection == 5:
                if analyser:
                    print("----  Count of numbers  ----")
                    print(analyser.count_of_numbers)
                    LoggingInfo.log_info("Displaying count of numbers.")
                else:
                    print("No text entered yet...\n") 
            elif menu_selection == 6:
                if analyser:
                    print("----  Most common word  ----")
                    print(analyser.most_common_word)
                    LoggingInfo.log_info("Displaying most common word.")
                else:
                    print("No text entered yet...\n") 
        else:
            print("Invalid selection!\n")
            LoggingInfo.log_warning("User Entered Non Existing Number in Menu Selection.")
    except ValueError:
        print("Invalid symbol entered!\n")
        LoggingInfo.log_warning("User Entered Symbol/Character in Menu Selection.")
    except Exception as e:
        print(f"Unexpected error occured: {e}\n")
        LoggingInfo.log_critical(f"Unexpected Error: {str(e)}.")
