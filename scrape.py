import os
import requests
import json
import uuid

source = "https://api.github.com/repos/cvrve/New-Grad-2025/readme"

response = requests.get(source)
url = json.loads(response.text)["download_url"]

result = ""
readme = requests.get(url).text
oldReadme = None


def addHeader(num_cols):
    return "|" * (num_cols + 1) + "\n" + "|-" * num_cols + "|" + "\n"


if os.path.isfile("cache/saved-readme.md"):
    with open("cache/saved-readme.md", "r") as f:
        oldReadme = f.read()

    print("loaded from cache")
    # print(oldReadme)

    diff = []

    if oldReadme is not None:
        readme_split = readme.split("\n")
        oldReadme_split = oldReadme.split("\n")
        index = 0
        for i in range(len(readme_split)):
            if readme_split[i] != oldReadme_split[index]:
                diff.append(readme_split[i])
                continue
            index += 1

    result += addHeader(4) + "\n".join(diff)
    print(result)

with open("cache/saved-readme.md", "w") as f:
    f.write(readme)


def set_multiline_output(name, value):
    with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
        delimiter = uuid.uuid1()
        print(f"{name}<<{delimiter}", file=fh)
        print(value, file=fh)
        print(delimiter, file=fh)


# should we throw exception?
if result == "":
    result = "No new jobs for now."

set_multiline_output("SCRAPER_OUTPUTS", result)
