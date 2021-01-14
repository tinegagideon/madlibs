# string concatenation
# creating a subscribe to string i.e "subscribe to ___"
# youtuber = "miles"

# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")


# adj = input('Adjective: ')
# verb1 = input('verb:')
# verb2 = input('verb:')
# famous_person = input('Famous Person:')

# madlib = f'computer programming is so {adj}! it makes me so excited all the time because \n i love to {verb1}.stay hydrated and {verb2} like you are {famous_person}!'
# print(madlib)


#creating own madlib program




def madlib():
    noun1 = input('Noun: ')
    noun2 = input('Noun: ')
    adjective1 = input('Adjective: ')
    adjective2 = input('Adjective: ')
    time_of_day = input('Time of The Day(Description): ')
    city = input('City: ')
    meal = input('Meal(Any): ')
    verb = input('verb: ')
    color = input('Color: ')

    madlib = f'I like to {verb} in the {time_of_day},my favourite meal is {meal}.{color} is my favourite color.\nTravelling to {city} is what i would really love in the future.I consider myself a {adjective1} and {adjective2} person.\nMy friends are {noun1} and {noun2} :)'

    print(madlib)

madlib()