# This script uses wikipedia API to return random articles
# You can contribute for this script if you have any cool ideas!

import requests

random_article = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

def get_random_article():
  r = requests.get(url = random_article)
  page = r.json()
  full_url = f'https://en.wikipedia.org/wiki/{page["titles"]["canonical"]}'
  print(f'Title: {page["title"]}\n') 
  print(f'Summary: {page["extract"]}\n') 
  choice = input("Do you want to keep reading the article? [y/n] ")
  if choice.lower() == "y":
    print(f"Click here: {full_url}")
  elif choice.lower() == "n":
    print("Run again for new articles!")
  else:
    print("Invalid option!")

get_random_article()
