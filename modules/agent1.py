import os
from groq import Groq  
from dotenv import load_dotenv

load_dotenv()


class LLMProcessor:
    def __init__(self):
        self.api_key = os.getenv("GROQ_KEY")
        if not self.api_key:
            raise ValueError("GROQ_KEY not found in environment variables.")
        self.client = Groq(api_key=self.api_key)

    def process_with_llm(self, content: str) -> str:
       
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an assistant that helps clarify and summarize search results. "
                            "Please summarize the following information concisely."
                        ),
                    },
                    {"role": "user", "content": content},
                ],
                model="mixtral-8x7b-32768",  
                temperature=0.7,
                max_tokens=256,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"Error processing with LLM: {str(e)}")
            return "Error processing request."
