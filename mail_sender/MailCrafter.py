"""
Author: francesco boldrin francesco.boldrin@studenti.unitn.it
Date: 2025-01-06 14:14:55
LastEditors: francesco boldrin francesco.boldrin@studenti.unitn.it
LastEditTime: 2025-02-01 20:55:06
FilePath: mail_sender/MailCrafter.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
import json

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
    # prompt = f"""
    # I need your help crafting a formal email from the administrative office to a student. The purpose of the email is to encourage the student to reinsert their login credentials by clicking a provided link. The email should be persuasive, clear, and professional in tone, focusing on ensuring the student understands the importance of completing this action promptly.
    # this is what i have so far:
    # {answer.text}
    # Please only improve the **body** of the email (do not include additional introductory or closing text).
    # Important details:
    # - **Action required**: Reinsert login credentials.
    # - **Goal**: Persuade the student to click on the provided link.
    # - **Tone**: Formal and professional.
    # - **Greetings**: Dear [Student's Name],
    # - **Link to the login page**: http://localhost:3000
    # Use the information above to refine the body of the email effectively.
    # """

    # 
    # # response = model.generate_content(prompt,
    # #                                 generation_config=genai.types.GenerationConfig(
    # #                                     max_output_tokens=None,
    # #                                     temperature=0.7,
    # #                                 )
    # #                                 )
    # 
    # print("The second email is: ", response.text)
    
    return answer.text

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

import re


def convert_to_html(email_body, logo_cid):
    """
    Converts plain text email into HTML format with embedded links as buttons and a logo.
    """
    # Convert line breaks to HTML
    email_body = email_body.replace("\n", "<br>")

    # Convert links to HTML buttons with surrounding line breaks
    email_body = re.sub(r'\[(http[s]?:\/\/[^\]]+)\]',
                        r'<br><br><a href="\1" style="display:inline-block;padding:10px 20px;color:#fff;background:#007bff;text-decoration:none;border-radius:5px;">Click Here</a><br><br>',
                        email_body)

    # Append logo at the bottom
    email_body += f'<br><br><img src="cid:{logo_cid}" alt="Company Logo" style="width:150px; height:auto;">'

    return f"""<html><body>{email_body}</body></html>"""
    
def craft_mail(user_data):
    
    prompt = f"""
    I need your help crafting a formal email from the administrative office to a student. 
    The purpose of the email is to encourage the student to reinsert their login credentials by clicking a provided link. 
    The email should be persuasive, clear, and professional in tone, focusing on ensuring the student understands the importance of completing this action promptly.

    The following user data is provided:
    {user_data}

    Please only improve the **body** of the email (do not include additional introductory or closing text).

    Important details:
    - **Action required**: Reinsert login credentials.
    - **Goal**: Persuade the student to click on the provided link.
    - **Tone**: Formal and professional.
    - **Link to the login page**: http://localhost:3000
    - **Final Greetings**: Administrative Office,\n Zimbra solutions.

    Use the information above to refine the body of the email effectively.
    """

    # prompt = f"""
    # J'ai besoin de votre aide pour rédiger un e-mail formel de la part du bureau administratif à un étudiant. L'objectif de l'e-mail est d'encourager l'étudiant à réinsérer ses identifiants de connexion en cliquant sur un lien fourni. L'e-mail doit être persuasif, clair et professionnel, tout en insistant sur l'importance de réaliser cette action rapidement.
    # 
    # Les informations suivantes concernant l'utilisateur sont fournies :
    # {user_data}
    # 
    # Veuillez uniquement améliorer le **corps** de l'e-mail (n'ajoutez pas de texte introductif ou de conclusion supplémentaire).
    # 
    # Détails importants :
    # - **Action requise** : Réinsérer les identifiants de connexion.
    # - **Objectif** : Encourager l'étudiant à cliquer sur le lien fourni.
    # - **Ton** : Formel et professionnel.
    # - **Lien vers la page de connexion** : http://localhost:3000
    # 
    # Utilisez les informations ci-dessus pour affiner efficacement le corps de l'e-mail.
    # """
    
    response = crafting_mail(prompt)
    
    # Convert link to button in the email body
    response = convert_to_html(response, "logo_cid")
    
    return f"{response}"


test_data = [
    {
        "name": "Alice Bernard",
        "role": "Student",
    },
    {
        "name": "Bob Smith",
        "role": "Student",
    },
    {
        "name": "Charlie Davis",
        "role": "Student",
    },
    {
        "name": "David Evans",
        "role": "Student"
    },
    {
        "name": "Ella Foster",
        "role": "Student"
    },
    {
        "name": "Frank Green",
        "role": "Student"
    },
    {
        "name": "Grace Hill",
        "role": "Student"
    },
    {
        "name": "Henry Ives",
        "role": "Student"
    },
    {
        "name": "Ivy Johnson",
        "role": "Student"
    },
    {
        "name": "Jack King",
        "role": "Student"
    },
    {
        "name": "Katie Lee",
        "role": "Student"
    },
    {
        "name": "Liam Miller",
        "role": "Professor"
    },
    {
        "name": "Mia Nelson",
        "role": "Professor"
    },
    {
        "name": "Noah Oliver",
        "role": "Professor"
    },
    {
        "name": "Olivia Parker",
        "role": "Professor"
    },
    {
        "name": "Peter Quinn",
        "role": "Professor"
    },
    {
        "name": "Quinn Reed",
        "role": "Professor"
    },
    {
        "name": "Rachel Smith",
        "role": "Professor"
    },
    {
        "name": "Sam Taylor",
        "role": "Professor"
    },
    {
        "name": "Tom Underwood",
        "role": "Professor"
    },
    {
        "name": "Ursula Vaughan",
        "role": "Professor"
    },
    {
        "name": "Victor Ward",
        "role": "Professor"
    },
    {
        "name": "Wendy Xu",
        "role": "Professor"
    },
    {
        "name": "Xander Young",
        "role": "Professor"
    },
    {
        "name": "Yara Zane",
        "role": "Professor"
    },
    {
        "name": "Zoe Adams",
        "role": "Professor"
    },
    {
        "name": "Adam Brown",
        "role": "Professor"
    },
    {
        "name": "Benjamin Clark",
        "role": "Professor"
    },
    {
        "name": "Catherine Davis",
        "role": "Professor"
    },
    {
        "name": "Daniel Evans",
        "role": "Professor"
    },
    {
        "name": "Emily Foster",
        "role": "Professor"
    },
    {
        "name": "George Hill",
        "role": "Professor"
    },
    {
        "name": "Hannah Ives",
        "role": "Professor"
    },
    {
        "name": "Isaac Johnson",
        "role": "Professor"
    },
    {
        "name": "Jacob King",
        "role": "Professor"
    },
    {
        "name": "Katherine Lee",
        "role": "Professor"
    },
    {
        "name": "Lily Miller",
        "role": "Professor"
    },
    {
        "name": "Michael Nelson",
        "role": "Professor"
    },
    {
        "name": "Nora Oliver",
        "role": "Professor"
    },
    {
        "name": "Oliver Parker",
        "role": "Professor"
    },
    {
        "name": "Penelope Quinn",
        "role": "Professor"
    },
    {
        "name": "Quentin Reed",
        "role": "Professor"
    },
    {
        "name": "Rebecca Smith",
        "role": "Professor"
    },
    {
        "name": "Samuel Taylor",
        "role": "Professor"
    },
    {
        "name": "Thomas Underwood",
        "role": "Professor"
    },
    {
        "name": "Ulysses Vaughan",
        "role": "Professor"
    },
    {
        "name": "Victoria Ward",
        "role": "Professor"
    },
    {
        "name": "William Xu",
        "role": "Professor"
    },
    {
        "name": "Xavier Young",
        "role": "Professor"
    },
    {
        "name": "Yvonne Zane",
        "role": "Professor"
    },
    {
        "name": "Zachary Adams",
        "role": "Professor"
    }
]

def ground_truth():
    mail_created = []
    for user_data in test_data:
        print(f"Email for: {user_data['name']} ({user_data['role']})")
        # print(craft_mail(user_data))
        print("\n")
        mail_created.append(craft_mail(user_data))
        
        # append the email to the json file
        data = []
        with open("./mail_sender/mails_created.json", "r") as file:
            data = json.load(file)
        data.append({"email": craft_mail(user_data)})
        with open("./mail_sender/mails_created.json", "w") as file:
            # indent=4 for pretty printing
            json.dump(data, file, indent=4)