import os
import requests
import json

source = "https://api.github.com/repos/cvrve/New-Grad-2025/readme"

response = requests.get(source)
url = json.loads(response.text)["download_url"]

readme = requests.get(url).text
oldReadme = None
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


# check if diff is markdown table
def addHeader(num_cols):
    return "|" * (num_cols + 1) + "\n" + "|-" * num_cols + "|" + "\n"


result = addHeader(4) + "\n".join(diff)


# with open("cache/saved-readme.md", "w") as f:
#     f.write(readme)

with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
    print(f'{"SCRAPER_OUTPUTS"}={result}', file=fh)
