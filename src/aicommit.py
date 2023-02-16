import os
import subprocess
import sys

import inquirer
from dotenv import load_dotenv

from .utils import generate_commit_messages, get_diff

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_KEY:
    print(
        "Please save your OpenAI API key as an env variable by doing 'export OPENAI_API_KEY=YOUR_API_KEY'"
    )
    sys.exit(1)


def main():
    try:
        subprocess.check_output(
            "git rev-parse --is-inside-work-tree", shell=True, stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError:
        print("This is not a git repository")
        sys.exit(1)

    diff_per_file = False
    commit_conventional = False
    commit_language = "en"
    commit_choice = 0

    # Check for flags
    if len(sys.argv) > 1:
        if "--help" in sys.argv:
            print(
                "Usage: python git_ai_commit.py [--diff-per-file] [--conventional] [--language <language>] [--choice <choice>]\n"
            )
            print("Flags:")
            print("  --diff-per-file     Generate commit message per changed file")
            print("  --conventional      Use conventional commit format")
            print(
                "  --language          Language for generated commit message (default: en)"
            )
            print(
                "  --choice            Choose from 5 different generated commit messages (default: 0)\n"
            )
            sys.exit(0)

        flags = sys.argv[1:]

        if "--diff-per-file" in flags:
            diff_per_file = True

        if "--conventional" in flags:
            commit_conventional = True

        if "--language" in flags:
            language_index = flags.index("--language")
            commit_language = flags[language_index + 1]

        if "--choice" in flags:
            choice_index = flags.index("--choice")
            commit_choice = int(flags[choice_index + 1])

    diff = get_diff(diff_per_file)

    if not diff:
        print(
            "No staged changes found. Make sure there are changes and run `git add .`"
        )
        sys.exit(1)

    # Accounting for GPT-3's input requirement of 4k tokens (approx 8k chars)
    if len(diff) > 8000:
        print(
            "The diff is too large to write a commit message for. Please split your changes into multiple commits."
        )
        sys.exit(1)

    choices = generate_commit_messages(OPENAI_KEY, diff, commit_language)

    if len(choices) == 0:
        print("No commit message generated.")
        sys.exit(1)

    if commit_choice < 0 or commit_choice >= len(choices):
        print(
            f"Invalid choice '{commit_choice}'. Choose a number between 0 and {len(choices)-1}."
        )
        sys.exit(1)

    commit_messages = generate_commit_messages(OPENAI_KEY, diff, commit_language, 5)

    if commit_conventional:
        conventional_choices = [
            "feat",
            "fix",
            "docs",
            "style",
            "refactor",
            "test",
            "chore",
        ]
        questions = [
            inquirer.List(
                "conventional_choice",
                message="What type of change are you making?",
                choices=conventional_choices,
            )
        ]

    message_choices = [f"{i+1}. {msg}" for i, msg in enumerate(commit_messages)]
    questions = [
        inquirer.List(
            "message_choice",
            message="Select a commit message:",
            choices=message_choices,
        )
    ]
    answers = inquirer.prompt(questions)

    # Get the selected commit message
    selected_message = commit_messages[int(answers["message_choice"][0]) - 1]

    print(f"Commit Message:\n{selected_message}")

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
        sys.exit(1)

    subprocess.run(["git", "commit", "-m", f"{str(selected_message)}"])


if __name__ == "__main__":
    main()
