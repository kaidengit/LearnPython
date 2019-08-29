import selenium
import re
from selenium import webdriver
def res():
    url = "https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    driver = selenium.webdriver.Firefox()
    driver.get(url)
    page = driver.page_source
    print(type(page))
    print(page)
    restr = """共(\\d+)条职位"""
    regax = re.compile(restr,re.I)
    mylist = regax.findall(page)
    driver.quit()

    return mylist[0]

if __name__ == "__main__":
    # pro = input("输入你输入的岗位：")
    pro = ["python"]

    print(res())