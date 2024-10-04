import os
import requests

env_file = os.getenv('GITHUB_ENV')

with open(env_file, "a") as myfile:
    myfile.write("SCRAPER_OUTPUTS=MY_VALUE")