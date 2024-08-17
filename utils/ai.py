import openai
import os

openai_client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY", ""))
