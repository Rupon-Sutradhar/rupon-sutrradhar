import random
import nltk


nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('popular')
responses = {
    "greeting": ["Hello!", "Hi there!", "Greetings!"],
    "goodbye": ["Goodbye!", "See you later!", "Have a nice day!"],
    "default": ["I'm not sure I understand. Can you rephrase?", "Interesting! Tell me more.", "That's a great question."]
}

def chat_bot():
    print("Chatbot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: ", random.choice(responses["goodbye"]))
            break
        else:
            tokens = nltk.word_tokenize(user_input)
            pos_tags = nltk.pos_tag(tokens)
            response = handle_input(pos_tags)
            print("Chatbot: ", response)

def handle_input(pos_tags):
    for tag in pos_tags:
        if tag[1] == "NNP" and tag[0].lower() in ["hello", "hi", "greetings"]:
            return random.choice(responses["greeting"])
    return random.choice(responses["default"])

if __name__ == "__main__":
    chat_bot()