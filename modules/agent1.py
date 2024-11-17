import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
groq_token=os.getenv("GROQ_KEY")



client=Groq(api_key=groq_token)

chat_completion=client.chat.completions.create(
    messages=[
        {
            "role":"system",
            "content":"You are an assistant that helps with rephrasing and clarifying information."
                  "The user has provided the following answer:"

                  "Please rephrase this information in a concise and clear manner."
        },
        {
            "role":"user",
            "content":"explain llm",
        }
    ],
    model="mixtral-8x7b-32768",
    temperature=0.7,
    max_tokens=256,
    
)

print(chat_completion.choices[0].message.content)
