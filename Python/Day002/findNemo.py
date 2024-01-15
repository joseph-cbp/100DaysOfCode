def find_nemo(sentense : str):
    new_sentense = sentense.split()
    position = 1;
    for word in new_sentense:
        if word == "Nemo":
            break
        position += 1
    print(f"I found Nemo at {position}")

find_nemo("I am finding Nemo !")
find_nemo("I Nemo am")
find_nemo("Nemo is me")