"""
Author: francesco boldrin francesco.boldrin@studenti.unitn.it
Date: 2025-01-06 14:14:55
LastEditors: francesco boldrin francesco.boldrin@studenti.unitn.it
LastEditTime: 2025-01-06 15:12:56
FilePath: MailCrafter.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
# connect to gemini to use llm
import google.generativeai as genai


def crafting_mail(prompt):

    genai.configure(api_key="AIzaSyDoxp3PrUCHmG1-faxv4yNpzDpEmLyqvos")
    
    model = genai.GenerativeModel("gemini-1.5-flash")

    answer = model.generate_content(prompt,
                                    generation_config=genai.types.GenerationConfig(
                                        max_output_tokens=None,
                                        temperature=0.7,
                                    )
                                    )
    # take the text from the answer and ask to gemini to generate the email

    prompt = (f"""
        I need your help refining an email to send to my friend. The goal is to casually and naturally encourage him to use my link to check out my beautiful website.

        This is my first draft:
        {answer}

        Please improve only the body of the email. Make it more engaging and persuasive while keeping the tone friendly, informal, and relatable—like a natural chat between friends. Avoid any formal language or being too pushy. The content should spark his curiosity and interest without feeling forced.

        **Important**: Only improve the body of the email. Do not add any additional introductory or closing text—just refine the main message.

        **Please ensure the link remains intact and is not altered in any way.**

        Please deliver the revised email, fully written and ready to send, ONLY ONE OPTION.
    """)

    response = model.generate_content(prompt,
                                    generation_config=genai.types.GenerationConfig(
                                        max_output_tokens=None,
                                        temperature=0.7,
                                    )
                                    )
    
    print("The second email is: ", response.text)
    
    return response.text

import openai

# Set your OpenAI API key
api_key = "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"

# Function to send a query to the OpenAI API
openai.api_key = api_key

def ask_openai(query, model="gpt-3.5-turbo", max_tokens=150):
    try:
        # Call ChatCompletion API
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ],
            max_tokens=max_tokens,
            temperature=0.7,
        )
        # Extract and return the response
        return response['choices'][0]['message']['content'].strip()

    except openai.error.OpenAIError as e:
        return f"An error occurred: {str(e)}"

# Example usage
def test_crafting_mail():
    data = {
        "name_of_receiver": "adrian merle",
        "nickname_of_receiver": "Big A",
        "school": "INSA Lyon",
        "sender_name": "Ricky Martin",
        "nickname_of_sender": "Ricky M",
        "best_friend_name": "francesco boldrin",
        "nickname_of_best_friend": "frank",
        "favorite_food": "pizza",
        "sport": "basketball",
        "movie": "star wars",
        "website": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "message": "this is a test message"
    }

    prompt = (f"""
            I need your help crafting an email to send to my friend. The goal is to casually and naturally encourage him to use my link to check out my beautiful website. 
            Please use all the details I’ve provided below to make the email feel like a genuine conversation between friends:
            {data}

            The tone should be friendly, informal, and relatable—like a natural chat. Avoid sounding overly formal or pushy, but still make it engaging and persuasive enough to spark his curiosity and interest.
            Please deliver the email fully written and ready to send.
            """)
    
    response = crafting_mail(prompt)
    
    
    return f"{response}"

if __name__ == "__main__":
    test_crafting_mail()

