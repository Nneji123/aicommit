<div align="center">
  <div>
    <img src=".github/logo.png" alt="AI Commits"/>
    <!-- <h1 align="center">AICommit</h1> -->
  </div>
	<p>An AI-powered git commit message generator written in python. Inspired by @Nutlope</p>
  <a href="https://twitter.com/neji_14">
    <img src="https://img.shields.io/twitter/follow/nutlope?style=flat&label=neji_14&logo=twitter&color=0bf&logoColor=fff" alt="Ifeanyi Nneji Follower Count" />
  </a>
</div>



[![Pypi](https://img.shields.io/pypi/v/ai-commits.svg)](https://pypi.org/project/ai-commits/)
[![PyPI - Python](https://img.shields.io/badge/python-3.6%20|%203.7%20|%203.8-blue.svg)](https://pypi.org/project/ai-commits/)
[![Downloads](https://static.pepy.tech/badge/ai-commits)](https://pepy.tech/project/ai-commits)
[![MIT licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://raw.githubusercontent.com/Nneji123/aicommit/LICENSE)




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

# Changelog
## v1.0.0 (2023-02-16)

- Added support for generating commit messages in multiple languages

- Improved performance when generating commit messages for large diffs
    
- Added ability to select from multiple generated commit messages using the inquirer library
    
- Fixed various bugs and improved error handling

v0.0.5 (2023-02-15)

- Fixed a bug that caused the script to fail when no changes were staged

v0.0.4 [Initial Release] (2023-02-15)

- Initial release of aicommits
- Supports generating conventional commit messages
- Supports generating commit messages based on the changes in the staged files
- Uses OpenAI's GPT-3 to generate commit messages


# Contributing
Open an issue or submit a pull request if you want to contribute to the project.

# License
[MIT](https://github.com/Nneji123/aicommit/LICENSE/)

