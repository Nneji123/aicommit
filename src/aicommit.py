import os
import subprocess
import sys

import inquirer
import openai
from dotenv import load_dotenv
from openai.error import APIConnectionError

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_KEY:
    print(
        "Please save your OpenAI API key as an env variable by doing 'export OPENAI_API_KEY=YOUR_API_KEY'"
    )
    sys.exit(1)


def generate_commit_message(api_key: str, prompt: str) -> str:
    try:
        openai.api_key = api_key
        model_engine = "text-davinci-002"
        prompt = f"What follows '-------' is a git diff for a potential commit. Reply with an appropriate git commit message(a Git commit message should be concise but also try to describe the important changes in the commit) and don't include any other text but the message in your response. ------- {prompt}"
        try:
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=200,
                n=1,
                stop=None,
                temperature=0.7,
            )
        except openai.error.AuthenticationError as e:
            error_message = f"OpenAI API Error: {e}"
            print(error_message)
            sys.exit(1)

        return completions.choices[0].text.strip().replace("\n", "")
    except APIConnectionError as e:
        error_message = f"OpenAI API Error: {e}"
        print(error_message)
        raise openai.APIError(error_message)


def main():
    try:
        subprocess.check_output(
            "git rev-parse --is-inside-work-tree", shell=True, stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError:
        print("This is not a git repository")
        sys.exit(1)

    diff = subprocess.check_output(
        "git diff --cached .",
        shell=True,
        stderr=subprocess.STDOUT,
    ).decode("utf-8")

    if not diff:
        print(
            "No staged changes found. Make sure there are changes and run `git add .`"
        )
        sys.exit(1)

    # Accounting for GPT-3's input requirement of 4k tokens (approx 8k chars)
    if len(diff) > 8000:
        print("The diff is too large to write a commit message.")
        sys.exit(1)

    prompt = generate_commit_message(OPENAI_KEY, diff)
    print(str(prompt))

    print(f"Commit message: {prompt}")

    confirmation_message = inquirer.prompt(
        [
            inquirer.List(
                "use_commit_message",
                message="Would you like to use this commit message?",
                choices=["y", "n"],
                default="y",
            )
        ]
    )

    if confirmation_message["use_commit_message"] == "n":
        print("Commit message has not been committed.")
        print(prompt)
        sys.exit(1)

    subprocess.run(["git", "commit", "-m", f"{str(prompt)}"])


if __name__ == "__main__":
    print("Welcome to AICommits!")
    main()
