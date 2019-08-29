import re
import selenium
import selenium.webdriver
driver = selenium.webdriver.Firefox()
ls = list()
def res(url):

    driver.get(url)
    html = driver.page_source
    # print(html)
    restr = """<a href="problem.php.id=(\\d+)">(.*?)</a>"""
    regax = re.compile(restr)
    ks = regax.findall(html)
    ls.extend(ks)
    print("爬虫运行中。。。。")

if __name__ == "__main__":
    url = "http://acm.zzuli.edu.cn/problemset.php?page="
    for i in range(17):
        i = url + str(i)
        res(i)
    for pro in ls:
        print(pro)
    driver.quit()