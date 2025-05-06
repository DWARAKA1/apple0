import os

from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

from groq import Groq

client = Groq()
completion = client.chat.completions.create(
    model="deepseek-r1-distill-llama-70b",
    messages=[
        {
            "role": "user",
            "content": "How many fruits are there in the world?"
        }
    ],
    temperature=0.6,
    max_completion_tokens=1024,
    top_p=0.95,
    stream=True,
    reasoning_format="raw"
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")