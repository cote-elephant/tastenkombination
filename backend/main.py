import json
import random
#header
print("Tastenkombination")

#read/get anything from shortcuts.json
with open("data/shortcuts.json", "r", encoding='utf-8') as file:
    data = json.load(file)

random.shuffle(data)

failed_answers = 0
correct_answers = 0
current_index = 0

#running as long as failed_answers max 2
while failed_answers < 3:
    #current data choosen
    data_current = data[current_index]

    #user input in variable
    print(f"Was ist die Kombination von '{data_current['description']}'?")
    comb_user_input = input("In Textform (zb. 'Strg + c'): ")
    comb_input = comb_user_input.lower().replace(" ", "")

    if comb_input == data_current["answer"]:
        print(f"Richtig!\n{data_current['description']}\n{data_current['answer']}")
        correct_answers += 1
        print("Bisher richtig: ", correct_answers)
    else:
        print(f"Falsch!\n{data_current['description']}\n{data_current['answer']}")
        failed_answers += 1
        if failed_answers == 1:
            print("Oho. Erster Fehler:", failed_answers)
        elif failed_answers == 2:
            print("Letzte Chance. Zwei Fehler:", failed_answers)

print("Spiel beendet.")
print("Richtige Antworten:", correct_answers)
print("Fehler:", failed_answers)