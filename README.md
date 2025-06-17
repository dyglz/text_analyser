### text_analyser
---
- [ ] deadline 17/06/2025

---

**💡 Objective 2**  
Refactor prompt analyzer. Move back end logic to Flask application
and dockerize it. Mongo DB part will follow later with lectures.
The application itself must serve only UI and all data operations must
be served through container as API layer.

---

**💡 Objective 1**  
Create a CLI (Command-Line Interface application) application that would let user enter random lentgh text (minimum 5 sentences).
This random text then should be cleaned: All words which start after end of sentence should start with capital letter, there should be a gap after comma.

Option 1: GET Report option should give answer in this format: [✔]
{
    "fixed_text": 'text',
    "number_of_words": 'number_of_words',
    "number_of_sentences": 'number_of_sentences'
    "count_of_numbers": 'count_of_numbers' //how many numbers were in the text
    "most common word/words": 'most common word'
}

There should be other options as well for every other field.
Option 2: Number of words [✔]
Option 3: Number of sentences [✔]
Option 4: Count of numbers [✔]
Option 5: Most common word [✔]

**Code must include**
- Class (if applicable: All 4 OOP principles, static, class methods, property decorators, dataclasses, use at least 3 python magic methods)
- Types everywhere
- Logging setup
- Error handling 
- Github Repo

---



