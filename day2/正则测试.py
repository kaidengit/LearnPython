
import re


str = '<dd class="col-md-3"><a href="/book/87/23974066.html" title="第1292章 杀念">第1294章 大战刑开</a></dd>'

pat = '<dd class="col-md-3"><a href="(.*?)" title="第1292章ds'

sg = re.compile(pat)
lst = sg.findall(str)
if lst == None:
    print("no")
else :
    print("yes")