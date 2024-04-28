# functions.py

def generate_story(person_name, noun, feeling1, verb1, feeling2, animal, verb2,
                   color1, verb_ing, adverb_ly, number, time_measure, color2,
                   animal2, number2, silly_word, noun2):
    # Construct the story using the provided template
    story = (
        f"This weekend I am going camping with {person_name}. I packed my lantern, "
        f"sleeping bag, and {noun}. I am so {feeling1} to {verb1} in a tent. I am "
        f"{feeling2} we might see a(n) {animal}, I hear they’re kind of dangerous. "
        f"While we’re camping, we are going to hike, fish, and {verb2}. I have heard "
        f"that the {color1} lake is great for {verb_ing}. Then we will {adverb_ly} "
        f"hike through the forest for {number} {time_measure}. If I see a {color2} "
        f"{animal2} while hiking, I am going to bring it home as a pet! At night we "
        f"will tell {number2} {silly_word} stories and roast {noun2} around the "
        f"campfire!!"
    )
    return story
