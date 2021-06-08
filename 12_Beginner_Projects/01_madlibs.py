#string cocatenation (aka how to put strings together)
#suppose we want to create a string that says "suscribe to ______"
youtuber = "gusgluna"

# a few way to do this
# print("subscribe to "+ youtuber)
# print("subscritbe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("adjetive: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer progaming is so {adj}! It Makes me so exited all the time because \
    I love to {verb1}. Stay Hidrated and {verb2} like you are {famous_person}!"

print(madlib)