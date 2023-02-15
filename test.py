from argparse import ArgumentParser
import requests, sys

parser = ArgumentParser(prog="python -m pkg_name_validator")
parser.add_argument("name", help="Package name to validate")
parser.add_argument("-r", "--repository", "--repo", dest="repo", help="Repository to check.", default="pypi")
args = parser.parse_args()

match args.repo:
	case "pypi":
		repo_url = "https://pypi.org/project/{}"
	case "testpypi":
		repo_url = "https://test.pypi.org/project/{}"
	case _:
		sys.exit(print(f"The repository {args.repo} is not defined. Feel free to add it here: https://github.com/tinkering-townsperson/pkg_name_validator"))

res = requests.get(repo_url.format(args.name))
invalid_names_res = requests.get("https://raw.githubusercontent.com/tinkering-townsperson/pkg_name_validator/main/lists/invalid_names.txt")
invalid_names = invalid_names_res.text.split("\n")

if res.status_code == 200:
	print(f"Package \"{args.name}\" is not available.")
	print(f"View it at: {repo_url.format(args.name)}")
elif args.name in invalid_names or " " in args.name or "\t" in args.name:
 	print(f"The package name \"{args.name}\" is not allowed")
elif res.status_code == 404:
	print(f"Package \"{args.name}\" is available!")
else:
	print(f"Pinging {repo_url} gave the status code {res.status_code}. If you know what that means, feel free to drop a pull request or issue at https://github.com/tinkering-townsperson/pkg_name_validator. Thank you!")
