def link_extract(driver_path):
    '''
    gets all leet questions links and their difficalty level and saves it to a file
    '''
    print("link extract")
    # from bs4 import BeautifulSoup
    # from selenium import webdriver
    # neet_code_url = "https://neetcode.io/practice"

    # from selenium import webdriver
    # driver = webdriver.Chrome(driver_path)
    # driver.get(neet_code_url)

    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    # all_links = []
    # for link in soup.find_all("a"):
    #     curr_link = link.get("href")
    #     if curr_link and "leetcode.com" in curr_link:
    #         all_links.append(curr_link)
    
    # difficulties = []
    # for link in soup.find_all("b"):
    #     difficulty = link.text
    #     if difficulty in ['Easy', 'Medium', 'Hard']:
    #         difficulties.append(difficulty)

    # all_links = [f"{difficulties[i]} : {all_links[i]}" for i in range(len(all_links))]
    # with open("leet_links.txt", "w+") as f:
    #     f.writelines("\n".join(all_links))



    
import random
def get_link():
    with open("remaining_leet.txt","r+") as f:
        
        all_links = f.readlines()
    
    while (all_links):
        random_link = random.choice(all_links)
        all_links.remove(random_link)
        
        yield random_link, all_links
        with open("remaining_leet.txt") as f:
            all_links = f.readlines()

def link_generator():
    ''' 
    randomly extracts single link from remaining links file. if question is excpted, link is removed.
    '''
    print("generator")
    # from termcolor import colored
    # for link, remainig_links in get_link():
    #     input("Press to get new link")
    #     print(colored(f"{link}","green"))
    #     is_excepted = input("is leet link excepted? Y/N")
    #     if is_excepted in "Nn":
    #         remainig_links.append(link)
    #     elif is_excepted not in "yY":
    #         exit()
    #     with open("remaining_leet.txt", "w") as f:
    #             f.writelines("".join(remainig_links))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Actions for leet extractor')
    group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('-c', "--collect", action="store_true", help='Download links from neetcode.com')
    group.add_argument('-i', "--indicate_web_driver", type=str, default="C:\Program Files (x86)\chromedriver.exe", help='path for sutible web driver')
    group.add_argument('-g', "--generate",  action="store_true", help='start the link generator')
    args = parser.parse_args()

    if args.collect:
        link_extract(args.indicate_web_driver)

    if args.generate:
        link_generator()