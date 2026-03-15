import json
import os
import random
import pandas as pd # type: ignore
import re

DATA_FILE = "sentences.json"
SOURCE_FILE = "source.json"
EXCEL_FILE = "database.xlsx"

DEFAULT_REVIEW = 3

OPIC_FILE = "opic.json"

OPIC_TOPICS = [
    "music",
    "movies",
    "travel",
    "hometown",
    "technology"
]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def normalize(text):
    return text.lower().strip()


def load_json(path):
    if not os.path.exists(path):
        return {"sentences": []}

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def split_sentences(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def opic_practice():

    data = load_json(OPIC_FILE)
    items = data["items"]

    clear_screen()

    print("OPIC Topics")
    print("----------------------")

    for i, t in enumerate(OPIC_TOPICS, 1):
        print(f"{i}. {t}")

    choice = input("\nChoose topic: ")

    if not choice.isdigit():
        return

    topic = OPIC_TOPICS[int(choice)-1]

    topic_items = [x for x in items if x["topic"] == topic]

    if not topic_items:
        print("No questions for this topic.")
        input()
        return

    remaining_items = topic_items.copy()
    total_questions = len(topic_items)

    while remaining_items:

        item = random.choice(remaining_items)

        sentences_en = split_sentences(item["answer_en"])
        sentences_vi = split_sentences(item["answer_vi"])

        total_sentences = len(sentences_en)

        for i in range(total_sentences):

            sentence_en = sentences_en[i]

            if i < len(sentences_vi):
                sentence_vi = sentences_vi[i]
            else:
                sentence_vi = ""

            wrong = None

            while True:

                clear_screen()

                print("Question Progress")
                print("--------------------------------")
                print(f"{total_questions - len(remaining_items) + 1} / {total_questions}")

                print("\nSentence Progress")
                print("--------------------------------")
                print(f"{i+1} / {total_sentences}")

                print("\nQuestion")
                print("--------------------------------")
                print(item["question"])

                print("\nSentence meaning")
                print("--------------------------------")
                print(sentence_vi)

                print("\nType the English sentence")
                print("--------------------------------")

                if wrong:
                    print("❌", wrong)
                    print("✅", sentence_en)

                user = input("\nYour answer: ")

                if normalize(user) == normalize(sentence_en):

                    clear_screen()
                    print("✅ Correct!")

                    input("\nPress Enter for next sentence...")
                    break

                else:

                    wrong = user

        remaining_items.remove(item)

        clear_screen()

        finished = total_questions - len(remaining_items)

        print("✅ Finished this question!")

        print(f"\nQuestion progress: {finished} / {total_questions}")

        input("\nPress Enter to continue...")

    clear_screen()

    print("🎉 You finished all questions in this topic!")

    input("\nPress Enter to return...")

# =========================
# IMPORT EXCEL
# =========================

def import_excel():

    if not os.path.exists(EXCEL_FILE):
        return

    print("Importing Excel database...")

    df = pd.read_excel(EXCEL_FILE)

    records = []

    for _, row in df.iterrows():

        records.append({
            "vi": str(row["Vietnamese"]),
            "ref": str(row["English"])
        })

    source_data = {"sentences": records}

    save_json(SOURCE_FILE, source_data)

    os.remove(EXCEL_FILE)

    print("Excel imported → source.json")
    input("Press Enter to continue...")


# =========================
# PRACTICE MODE
# =========================

def practice():

    data = load_json(DATA_FILE)
    sentences = data["sentences"]

    last_sentence = None

    while True:

        sentences_to_learn = [s for s in sentences if s["review_count"] > 0]

        if not sentences_to_learn:

            clear_screen()
            print("🎉 All sentences completed!")
            input("\nPress Enter to return...")
            return

        candidates = sentences_to_learn.copy()

        if last_sentence and len(candidates) > 1:
            candidates = [s for s in candidates if s != last_sentence]

        weights = [1 + s["times_wrong"] for s in candidates]

        s = random.choices(candidates, weights=weights, k=1)[0]

        wrong_answer = None
        first_attempt = True

        while True:

            clear_screen()

            print("Practice Mode")
            print("----------------------")
            print(f"Remaining reviews: {s['review_count']}")

            print("\nVietnamese:")
            print(s["vi"])

            if wrong_answer:
                print()
                print("❌", wrong_answer)
                print("✅", s["en"])

            user_input = input("\nYour answer: ")

            if normalize(user_input) == normalize(s["en"]):

                s["times_correct"] += 1

                if first_attempt:
                    s["review_count"] -= 1

                save_json(DATA_FILE, data)

                clear_screen()
                print("✅ Correct!")

                input("\nPress Enter to continue...")

                last_sentence = s
                break

            else:

                s["times_wrong"] += 1

                if first_attempt:
                    s["review_count"] = DEFAULT_REVIEW

                save_json(DATA_FILE, data)

                wrong_answer = user_input
                first_attempt = False


# =========================
# TRANSLATE MODE
# =========================

def translate_mode():
    
    while True:
        source = load_json(SOURCE_FILE)
        data = load_json(DATA_FILE)

        sentences = source["sentences"]

        if not sentences:

            clear_screen()
            print("No sentences left to translate.")
            input("\nPress Enter to return...")
            return
        total = len(sentences)
        s = sentences[0]

        clear_screen()

        print("Translate Mode")
        print("----------------------")
        print(f"Remaining sentences: {total}")

        print("\nVietnamese:")
        print(s["vi"])

        print("\nReference:")
        print(s["ref"])

        user_translation = input("\nYour translation: ").strip().lower()

        new_sentence = {
            "vi": s["vi"],
            "en": user_translation,
            "review_count": DEFAULT_REVIEW,
            "times_correct": 0,
            "times_wrong": 0
        }

        data["sentences"].append(new_sentence)

        sentences.pop(0)

        save_json(DATA_FILE, data)
        save_json(SOURCE_FILE, source)

        print("\n✅ Saved and removed from source.")
        input("\nPress Enter to continue...")
    


# =========================
# MENU
# =========================

def main():

    import_excel()

    while True:

        clear_screen()

        print("English Learning CLI")
        print("----------------------")
        print("1. Practice")
        print("2. Translate")
        print("3. OPIC")
        print("4. Exit")

        choice = input("\nChoose option: ")

        if choice == "1":
            practice()

        elif choice == "2":
            translate_mode()
        elif choice == "3":
            opic_practice()
        elif choice == "4":
            break


if __name__ == "__main__":
    main()