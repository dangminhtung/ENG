import json
import os
import random

DATA_FILE = "sentences.json"
DEFAULT_REVIEW = 3


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def normalize(text):
    return text.lower().strip()


def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def practice():

    data = load_data()
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

        # weighted random
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

                save_data(data)

                clear_screen()
                print("✅ Correct!")

                input("\nPress Enter to continue...")

                last_sentence = s
                break

            else:

                s["times_wrong"] += 1

                if first_attempt:
                    s["review_count"] = DEFAULT_REVIEW

                save_data(data)

                wrong_answer = user_input
                first_attempt = False


def translate_mode():

    data = load_data()

    clear_screen()
    print("Translate Mode")
    print("----------------------")

    vi = input("Vietnamese: ").strip()
    en = input("English: ").strip().lower()

    new_sentence = {
        "vi": vi,
        "en": en,
        "review_count": DEFAULT_REVIEW,
        "times_correct": 0,
        "times_wrong": 0
    }

    data["sentences"].append(new_sentence)

    save_data(data)

    print("\n✅ Sentence added!")
    input("\nPress Enter to continue...")


def main():

    while True:

        clear_screen()

        print("English Learning CLI")
        print("----------------------")
        print("1. Practice")
        print("2. Translate (add new sentence)")
        print("3. Exit")

        choice = input("\nChoose option: ")

        if choice == "1":
            practice()

        elif choice == "2":
            translate_mode()

        elif choice == "3":
            break


if __name__ == "__main__":
    main()