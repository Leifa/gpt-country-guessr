import os
import openai

# Set up your OpenAI API credentials
openai.api_key = os.environ.get("OPENAI_API_KEY")

# We define a conversation history, so that the chatbot sees the pattern how it should answer the questions.
conversation = [
        {"role": "system", "content": "You are an intelligent assistant who thinks well before answering. It is extremely important that your answers are correct. To achieve this, you seperate every of you responses into two sections: 1. INNER MONOLOGUE: Here you think about the prompt of the user, restate all relevant information and contemplate about different possible answers you could give. You have all the time in the world to find the correct answer. The user can not see this part of your response! 2. FINAL ANSWER: Here you give the final answer to the user. Only this part of your response will be shown to the user."},
    {"role": "user", "content": "I want to play a guessing game. You think of a number between 1 and 7 (inclusive) and do not tell me the number. I have to guess the number, and you always respond to my guesses with either \"higher\" or \"lower\" or \"correct\"."},
    {"role": "assistant", "content": "INNER MONOLOGUE: Ok, I have to think of a number first. Let's go with the number 2. Now the user can start guessing. FINAL ANSWER: Ok, I thought of a number. You can start guessing!"},
    {"role": "user", "content": "5"},
    {"role": "assistant", "content": "INNER MONOLOGUE: My number is 2. The user guessed 5. My number is lower than the number that the user guessed. FINAL ANSWER: Lower."},
    {"role": "user", "content": "1"},
    {"role": "assistant", "content": "INNER MONOLOGUE: My number is 2. The user guessed 1. My number is higher than the number that the user guessed. FINAL ANSWER: Higher."},
    {"role": "user", "content": "2"},
    {"role": "assistant", "content": "INNER MONOLOGUE: My number is 2. The user guessed 2. The user has found my number. FINAL ANSWER: Correct!"},
    {"role": "user", "content": "Ok, now let's lay a country guessing game. In your inner monologue, you choose a random country in the world. Don't make it too easy! Then I have to guess the country using yes-or-no questions."}]

# Here are some alternatives for the last element of the conversation history, to play different kinds of games:

    #{"role": "user", "content": "Ok, let's play again, but with a number between 1 and 1000. First, you choose the number in you inner monologue, then I have to guess it."}
    #{"role": "user", "content": "Ok, now let's play an animal guessing game. You choose a random animal and mention this animal in you inner monologue. But don't choose elephant or giraffe! Then I have to guess the animal using yes-or-no quesions."}
#    {"role": "user", "content": "Ok, now let's lay a food guessing game. You choose a random food. It can be a fruit or a vegetable. Mention the food in your inner dialogue!!! Then I have to guess the food using yes-or-no questions."}

# We save the inner monologues in a file, so we can examine in later
with open("full.txt", "w") as file:
    file.truncate()

def ask_chatgpt(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    # Get the assistant's reply
    reply = response.choices[0].message['content']
    with open("full.txt", "a") as file:
        file.write(reply + "\n")
    conversation.append({"role": "assistant", "content": reply})
    final_answer = reply.split("FINAL ANSWER: ")[1]
    return final_answer

print("Bot: Let me think a moment...")
print("Bot: " + ask_chatgpt(conversation))

while True:
    user_input = input("You: ")
    conversation.append({"role": "user", "content": user_input})
    answer = ask_chatgpt(conversation)
    print("Bot: " + answer)
