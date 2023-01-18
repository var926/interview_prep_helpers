import os
import random
from termcolor import colored
import shutil
from pathlib import Path
from typing import List, Tuple

REMAINIG_LINKS_PATH = Path("remaining_leet.txt")
ALL_LEET_LINKS_PATH = Path("leet_links.txt")

def link_extract(driver_path: Path="C:\Program Files (x86)\chromedriver.exe") -> None:
    '''
    gets all leet questions links and their difficulty level and saves it to a file
    '''
    from bs4 import BeautifulSoup
    from selenium import webdriver
    neet_code_url = "https://neetcode.io/practice"
    
    driver = webdriver.Chrome(driver_path)
    driver.get(neet_code_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    all_links = []
    for link in soup.find_all("a"):
        curr_link = link.get("href")
        if curr_link and "leetcode.com" in curr_link:
            all_links.append(curr_link)
    
    difficulties = []
    for link in soup.find_all("b"):
        difficulty = link.text
        if difficulty in ['Easy', 'Medium', 'Hard']:
            difficulties.append(difficulty)

    all_links = [f"{difficulties[i]} : {all_links[i]}" for i in range(len(all_links))]
    with open(ALL_LEET_LINKS_PATH, "w+") as f:
        f.writelines("\n".join(all_links))


def _get_link() -> Tuple[str, List[str]]:
    with open(REMAINIG_LINKS_PATH,"r+") as f:
        all_links = f.readlines()
    
    while (all_links):
        random_link = random.choice(all_links)
        all_links.remove(random_link)
        yield random_link, all_links
        with open(REMAINIG_LINKS_PATH) as f:
            all_links = f.readlines()

def link_generator() -> None:
    ''' 
    randomly extracts a single link from the remaining links file. if the question is excepted, link is removed.
    '''
    if not os.path.exists(REMAINIG_LINKS_PATH):
        if not os.path.exists(ALL_LEET_LINKS_PATH):
            link_extract()
        shutil.copy(ALL_LEET_LINKS_PATH, REMAINIG_LINKS_PATH)

    for link, remainig_links in _get_link():
        input("Press to get new link\n")
        print(colored(f"{link}","green"))
        is_excepted = input("is leet link excepted? Y/N \n Q-for exit\n")
        while is_excepted not in ["N","n","Y","y","q","Q"]:
            print(colored("Invalid Choice", "red"))
            is_excepted = input("is leet link excepted? Y/N \n Q-for exit\n")
        if is_excepted in "Nn":
            remainig_links.append(link)
        elif is_excepted in "Qq":
            exit()

        with open(REMAINIG_LINKS_PATH, "w") as f:
                f.writelines("".join(remainig_links))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Actions for leet extractor')
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('-c', "--collect", action="store_true", help='Download links from neetcode.com')
    group.add_argument('-i', "--indicate_web_driver", type=str, default="C:\Program Files (x86)\chromedriver.exe", help='path for sutible web driver')
    group.add_argument('-g', "--generate",  action="store_true", help='start the link generator')
    args = parser.parse_args()

    if args.collect:
        link_extract(args.indicate_web_driver)

    if args.generate:
        link_generator()
