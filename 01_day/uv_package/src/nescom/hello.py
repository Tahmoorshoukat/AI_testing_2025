from litellm import completion
from dotenv import load_dotenv

load_dotenv()


def say_hello():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[
            {
                "role": "user",
                "content": "Who is the founder of Pakistan? only return person name."
            }
        ]
    )
    return response.choices[0].message.content