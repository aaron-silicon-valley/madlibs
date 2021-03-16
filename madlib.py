
def words():
    holidayR = str(input('Holiday: '))
    noun1R = str(input('noun: '))
    placeR = str(input('A place please: ')),
    personR = str(input('Person: ')),
    adj1R = str(input('Adjective: ')),
    body_partR = str(input('body part: ')),
    verb1R = str(input('verb: ')),
    adj2R = str(input('Adjective again: ')),
    noun2R = str(input('noun: ')),
    foodR = str(input('food: ')),
    plural_nounR = str(input('plural noun!: '))
    return holidayR, noun1R , placeR, personR, adj1R, body_partR, verb1R, adj2R, noun2R, foodR, plural_nounR

def main(holidayR, noun1R , placeR, personR, adj1R, body_partR, verb1R, adj2R, noun2R, foodR, plural_nounR):
    madlibs = "I can't believe it's already {holiday}! \n" \
              "I can't wait to put on my {noun1} and visit every {place} in my neighborhood.\n" \
              "This year, I am going to dress up as {person} with {adj1} {body_part}.\n" \
              "Before I {verb1}, I make sure to grab my {adj2} {noun2} to hold all of my {food}.\n" \
              "Finally, all of my {plural_noun} are ready to go!".format(
    holiday= holidayR,
    noun1 = noun1R ,
    place = placeR,
    person = personR,
    adj1 = adj1R,
    body_part = body_partR,
    verb1 = verb1R,
    adj2 = adj2R,
    noun2 = noun2R,
    food = foodR,
    plural_noun = plural_nounR)
    print(madlibs)


if __name__ == '__main__':
    holidayR, noun1R , placeR, personR, adj1R, body_partR, verb1R, adj2R, noun2R, foodR, plural_nounR = words()
    main(holidayR, noun1R , placeR, personR, adj1R, body_partR, verb1R, adj2R, noun2R, foodR, plural_nounR)




