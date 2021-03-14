# holiday = 'holiday'
# noun1 = 'wedding'
# place = 'france'
# person = 'hulk'
# adj1 = 'big'
# body_part = 'arm'
# verb1 = 'run'
# adj2 = 'hard'
# noun2 = 'investment'
# food = 'pizza'
# plural_noun = 'saving'


madlibs = "I can't believe it's already {holiday}! \n" \
          "I can't wait to put on my {noun1} and visit every {place} in my neighborhood.\n" \
          "This year, I am going to dress up as {person} with {adj1} {body_part}.\n" \
          "Before I {verb1}, I make sure to grab my {adj2} {noun2} to hold all of my {food}.\n" \
          "Finally, all of my {plural_noun} are ready to go!".format(holiday = 'holiday',
noun1 = input('can I get a noun please!: '),
place = input('A place please: '),
person = input('Person: '),
adj1 = input('Adjective: '),
body_part = input('body part: '),
verb1 = input('verb: '),
adj2 = input('Adjective again: '),
noun2 = input('noun: '),
food = input('food: '),
plural_noun = input('plural noun!: '))
# holiday, noun1, place, person, adj1, body_part, verb1, adj2, noun2, food, plural_noun

print(madlibs)
