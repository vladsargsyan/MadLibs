# main.py
from functions import generate_story


def main():
    # Ask the user to input words
    person_name = input("Input Person Name: ")
    noun = input("Input noun: ")
    feeling1 = input("Input adjective (feeling): ")
    verb1 = input("Input verb: ")
    feeling2 = input("Input adjective (feeling): ")
    animal = input("Input an animal: ")
    verb2 = input("Input a verb: ")
    color1 = input("Input a color: ")
    verb_ing = input("Input a verb + ing: ")
    adverb_ly = input("Input an adverb + ly: ")
    number = input("Input a number: ")
    time_measure = input("Measure of time: ")
    color2 = input("Input a color: ")
    animal2 = input("Input an animal: ")
    number2 = input("Input a number: ")
    silly_word = input("Input a silly word: ")
    noun2 = input("Input a noun again: ")

    # Generate the story
    story = generate_story(person_name, noun, feeling1, verb1, feeling2, animal, verb2, color1, verb_ing,
                           adverb_ly, number, time_measure, color2, animal2, number2, silly_word, noun2)

    # Print the story
    print(story)


if __name__ == "__main__":
    main()
