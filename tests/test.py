import os
from src.aicommit import generate_commit_message
from dotenv import load_dotenv

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_KEY:
    print(
        "Please save your OpenAI API key as an env variable by doing 'export OPENAI_API_KEY=YOUR_API_KEY'"
    )


def test_generate_commit_message():
    
    prompt = "test diff"
    commit_message = generate_commit_message(OPENAI_KEY, prompt)
    assert isinstance(commit_message, str)
    assert len(commit_message) > 0
    assert commit_message != prompt


    
