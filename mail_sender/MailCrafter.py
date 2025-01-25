"""
Author: francesco boldrin francesco.boldrin@studenti.unitn.it
Date: 2025-01-06 14:14:55
LastEditors: francesco boldrin francesco.boldrin@studenti.unitn.it
LastEditTime: 2025-01-25 14:59:00
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
def craft_mail(user_data):
    prompt = f"""
    I need your help crafting a formal email from the administrative office to a student. The purpose of the email is to encourage the student to reinsert their login credentials by clicking a provided link. The email should be persuasive, clear, and professional in tone, focusing on ensuring the student understands the importance of completing this action promptly.

    The following user data is provided:
    {user_data}

    Please only improve the **body** of the email (do not include additional introductory or closing text).

    Important details:
    - **Action required**: Reinsert login credentials.
    - **Goal**: Persuade the student to click on the provided link.
    - **Tone**: Formal and professional.
    - **Link to the login page**: http://localhost:3000

    Use the information above to refine the body of the email effectively.
    """
    
    response = crafting_mail(prompt)
    
    return f"{response}"

