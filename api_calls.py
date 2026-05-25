import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
load_dotenv()


os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

model = init_chat_model(
    model="groq:openai/gpt-oss-20b"
)

for chunk in model.stream("what is ai?"):
    print(chunk.content, end="")