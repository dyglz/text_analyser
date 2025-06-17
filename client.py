import requests
from logging_info import LoggingInfo

API_URL = "http://localhost:8000"

# text_example = Python's popularity...!  has 3 grown? significantly in recent years. largely due to its versatility and the .growing4 demand for data  . analysis and .artificial@ intelligence []? applications! What is this @all about..?5

def main():
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
                    response = requests.post(f"{API_URL}/enter_text", data=text.encode('utf-8'))
                    if response.status_code == 200:
                        result = response.json()
                        print("\nText entered successfully!")
                        print(result)
                    else:
                        print(response.json())                
                elif menu_selection == 2:
                    LoggingInfo.log_info("Displaying text report.")
                    response = requests.get(f"{API_URL}/text_report")
                    print(response.json())             
                elif menu_selection == 3:
                    LoggingInfo.log_info("Displaying number of words.")
                    response = requests.get(f"{API_URL}/count_of_words")
                    print(response.json())
                elif menu_selection == 4:
                    LoggingInfo.log_info("Displaying number of sentences.")
                    response = requests.get(f"{API_URL}/count_of_sentences")
                    print(response.json())
                elif menu_selection == 5:
                    LoggingInfo.log_info("Displaying count of numbers.")
                    response = requests.get(f"{API_URL}/count_of_numbers")
                    print(response.json())                   
                elif menu_selection == 6:
                    LoggingInfo.log_info("Displaying most common word.")
                    response = requests.get(f"{API_URL}/most_common_word")
                    print(response.json())     
            else:
                print("Invalid selection!\n")
                LoggingInfo.log_info("User Entered Non Existing Number in Menu Selection.")
        except ValueError:
            print("Invalid symbol entered!\n")
            LoggingInfo.log_info("User Entered Symbol/Character in Menu Selection.")
        except Exception as e:
            print(f"Unexpected error occured: {e}\n")
            LoggingInfo.log_info(f"Unexpected Error: {str(e)}.")

    
if __name__ == "__main__":
    main()