from flask import Flask, jsonify, request
import json
import os
from typing import Optional, Dict, List

from logging_info import LoggingInfo
from text_analyser import TextAnalyser
from text_validator import TextValidator

app = Flask(__name__)
LoggingInfo.configure_logging()
LoggingInfo.log_info("App is running.")

DATA_FILE = "saved_texts.json"
analyser = None

def load_from_file() -> List[Dict[str, str]]:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as saved_texts:
            return json.load(saved_texts)
    else:
        return []
    
def save_to_file(data: List[Dict[str, str]]) -> None:
    with open(DATA_FILE, "w") as saved_texts:
        json.dump(data, saved_texts, indent=2)
    
db: List[Dict[str, str]] = load_from_file()



@app.route('/enter_text', methods=['POST'])
def enter_text():
    LoggingInfo.log_info("User is entering text.")
    text = request.get_data(as_text=True).strip()
    
    if not text:
        return jsonify({"error": "No text provided.\n"}), 400

    validator = TextValidator(text)
    if not validator.validate_text_length():
        return jsonify({"error": "Text must contain at least 5 sentences."}), 400

    formatted_text = validator.text_formatting()

    db.append({
        "raw_text": text,
        "formatted_text": formatted_text
    })
    save_to_file(db)

    return jsonify({
        "formatted_sentences": formatted_text
    }), 200

def get_analyser() -> Optional[TextAnalyser]:
    if db and isinstance(db[-1], dict) and "formatted_text" in db [-1]:
        return TextAnalyser(db[-1]["formatted_text"])
    return None


@app.route('/text_report', methods=['GET'])
def text_report():
    analyser = get_analyser()
    if analyser:
        LoggingInfo.log_info("Displaying text report.")
        print("------  Text Report  -------")
        return jsonify(analyser.text_report()), 200
    else:
        return jsonify({"error": "No text entered yet..."}), 400


@app.route('/count_of_words', methods=['GET'])
def count_of_words():
    analyser = get_analyser()
    if analyser:
        LoggingInfo.log_info("Displaying count of words.")
        return jsonify({"word_count": analyser.count_of_words}), 200
    else:
        return jsonify({"error": "No text entered yet..."}), 400
   
@app.route('/count_of_sentences', methods=['GET'])
def count_of_sentences():
    analyser = get_analyser()
    if analyser:
        LoggingInfo.log_info("Displaying count of sentences.")
        return jsonify({"sentence_count": analyser.count_of_sentences}), 200
    else:
        return jsonify({"error": "No text entered yet..."}), 400

@app.route('/count_of_numbers', methods=['GET'])
def count_of_numbers():
    analyser = get_analyser()
    if analyser:
        LoggingInfo.log_info("Displaying count of sentences.")
        return jsonify({"number_count": analyser.count_of_numbers}), 200
    else:
        return jsonify({"error": "No text entered yet..."}), 400


@app.route('/most_common_word', methods=['GET'])
def most_common_word():
    analyser = get_analyser()
    if analyser:
        LoggingInfo.log_info("Displaying count of sentences.")
        return jsonify({"most_common_word": analyser.most_common_word}), 200
    else:
        return jsonify({"error": "No text entered yet..."}), 400



if __name__ == "__main__":
    print("...starting flask app...")
    app.run(host='0.0.0.0', port=8000, debug=True)

