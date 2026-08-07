import os
import requests
import json
from utils import set_multiline_output, addHeader

result = ""
sources = []

with open("sources.txt", "r") as f:
    for line in f:
        sources.append(line.strip())

for source in sources:
    print("Scraping README.md from", source)
    try:
        owner = source.split("/")[-2]
        repo = source.split("/")[-1]

        cacheURL = f"cache/{owner}-{repo}.md"
        readmeEndpoint = f"https://api.github.com/repos/{owner}/{repo}/readme"

        response = requests.get(readmeEndpoint)
        response.raise_for_status()
        url = json.loads(response.text)["download_url"]

        readme = requests.get(url)
        readme.raise_for_status()
        readme_text = readme.text

        if os.path.isfile(cacheURL):
            with open(cacheURL, "r") as f:
                oldReadme = f.read()

            print("loaded from cache")

            readme_lines = readme_text.split("\n")
            oldReadme_lines = set(oldReadme.split("\n"))

            diff = [line.strip() for line in readme_lines if line.strip() not in oldReadme_lines and line.strip().startswith("|")]

            if diff:
                result += "## " + source + "\n\n"
                rows = diff[0].count("|") - 1
                result += addHeader(rows) + "\n".join(diff)
                result += "\n\n"
        else:
            print("no cache: creating cache at", cacheURL)

        with open(cacheURL, "w") as f:
            f.write(readme_text)

    except Exception as e:
        print("ERROR SCRAPING", source, str(e))

if result == "":
    result = "No new jobs for now."

print(result)
set_multiline_output("SCRAPER_OUTPUTS", result)