def check_bot(sentence):


    if sentence in you:

        return random.choice(chatbot)


    else:

        return("I don't know what are you talking about")

while True:

    sentence = input("You :")

    if sentence == "end":

        sys.exit()

    response = check_bot(sentence)
    time.sleep(1)


    print("Chatbot :"+response)

    
