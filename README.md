# AICommit

[![Pypi](https://img.shields.io/pypi/v/psgen.svg)](https://pypi.org/project/aicommit/)
[![PyPI - Python](https://img.shields.io/badge/python-3.6%20|%203.7%20|%203.8-blue.svg)](https://pypi.org/project/aicommit/)
[![Downloads](https://pepy.tech/badge/psgen)](https://pepy.tech/project/aicommit)
[![tests](https://github.com/Nneji123/psgen/actions/workflows/test.yml/badge.svg)](https://github.com/Nneji123/aicommit/actions/workflows/test.yml)
[![MIT licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://raw.githubusercontent.com/Nneji123/aicommit/LICENSE)


AICommit - An AI-powered git commit message generator written in python. Inspired by [@Nutlope](https://github.com/Nutlope/aicommits)

# Description

AICommits is a Python script that generates a git commit message using OpenAI's GPT-3 language model. The script takes the git diff of the staged changes and generates a commit message using GPT-3.

The generated commit message is presented to the user who has the option to accept or reject it. If the user accepts the commit message, the script commits the changes using the generated message.

The script requires an OpenAI API key, which can be obtained from the OpenAI website.




# Dependencies

    Python 3.6 or higher
    openai 0.10.2
    inquirer 3.7.0
    python-dotenv 0.19.1

# Shortcomings

The script has the following shortcomings:

1. The generated commit message may not always be suitable for the changes being committed.
    
2. The script depends on an external service (OpenAI) and requires an API key.
   
3. The generated commit message may not be human-readable or make sense in the context of the changes being committed.
    
4. The script may generate commit messages that do not follow the best practices for writing commit messages.

However, these shortcomings can be addressed by improving the script and the model used to generate the commit messages.

# Installation and Usage

To use AICommits, do the following: 

1. Export your OpenAI API key as an environment variable by running:

```bash
export OPENAI_API_KEY=YOUR_API_KEY
```


2. install aicommit from pypi by running:

```bash
pip install ai_commits
```

Then, run the script using the command `aicommit`.


The script will prompt you to confirm the generated commit message. If you accept the message, the changes will be committed using the generated message.

## Install from Source

To install AICommits from source, follow these steps:

1. Clone the repository using the command git clone https://github.com/nneji123/aicommit.git.
    
2. Navigate to the project directory using the command `cd aicommit`.

3. Install the required dependencies by running pip install -r requirements.txt.

4. Set your OpenAI API key as an environment variable by running export OPENAI_API_KEY=YOUR_API_KEY.
    
5. Run the script using the command `python "src/ai_commits.py"`.

The script will prompt you to confirm the generated commit message. If you accept the message, the changes will be committed using the generated message.

# License
[MIT](https://github.com/Nneji123/aicommit/LICENSE/)

