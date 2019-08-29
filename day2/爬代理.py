from selenium import webdriver
import re

url = "http://www.xiladaili.com/https/"
brower = webdriver.Firefox()

def parse(url):
    brower.get(url)
    print(brower.page_source)
    regax = re.compile("<tr>\s+<td>(.*?)</td>")
    lit = regax.findall(brower.page_source)
    for proxy in lit:
        with open("httpsproxies.txt",'a+') as f:
            f.write(proxy)
            f.write('\n')



if __name__ == "__main__":
    for page in range(1):
        page = url + str(page)
        parse(page)


    # brower.get(url)
    # print(brower.page_source)
    # brower.close()