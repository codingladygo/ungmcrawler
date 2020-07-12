import requests
from bs4 import BeautifulSoup

# def getRequest(url):
#     response = requests.get(url)
#     response_result = response.content
#     return response_result

# def responseAnalyse(url):
#     response = getRequest(url)
#     response_analyse_result = BeautifulSoup(response,'lxml')
#     return response_analyse_result

# # def firstItemEleAnalyse(url):
# #     response_analyse_result = responseAnalyse(url)
# #     response_analyse_result.find('dev')

if __name__ == "__main__":


    response = requests.get("http://ungm.org.cn/home/ungm/unspsc").content

    response_analyse = BeautifulSoup(response,'lxml')

    firstItemList = response_analyse.find('div',{'class':'unspsc1'}).find_all('div',{'onclick':'fun(this)'})
    print(firstItemList)

    firstItemResult = []
    for ele in firstItemList:
        firstItemResult.append(ele.contents[0])

    print(firstItemResult) #解析出的以及目录，生成List对象


    print(requests.get("http://ungm.org.cn/home/ungm/unspsc").cookies)

    # data = {
    #     "id": (None, "100001")
    # }

    # print(reponse.cookies)

    # headers = {"X-CSRF-TOKEN":BeautifulSoup(reponse_result,'lxml').find("meta",{"name":"csrf-token"}).content,
    #     "laravel_session":reponse.cookies.get("laravel_session"),
    #     "Cookie":"XSRF-TOKEN=eyJpdiI6IlRBVzJ2RDcrRTh5am51Q2Y5d3ZyVnc9PSIsInZhbHVlIjoicExMN3pXWWVkZUs3ekpGb2FLQTFvSld0U2hcL3ZMUjhIYTYrWlZxNnI4WnA4WUpuWXJwb0VoejhvOGhPeXo0b3loeTAzQUM0Z0pqdmZPZVhobm51TUZ3PT0iLCJtYWMiOiI3YzQxN2U0MzY3MmQzZjFmNTEwMDcwY2QwZDdlNWEyZjk4NzgwNmM1NzY0ZjdmNmUzZjkwODk2YmRlMDA4ZWY3In0%3D; laravel_session=eyJpdiI6IkNHdTVCcE9uVEZYdE1nZm9lMHFlXC9RPT0iLCJ2YWx1ZSI6ImRwT0tIdmJabUI2RVZ3Uk9GWGNcL28rdXFDODhEOUJGZ3liVlBaMFI4UVlIdTdad3VKNnkwWUJmakpQS25iTitHNndyRGNtYTE5cmlcL25kSlJxRlE2Qmc9PSIsIm1hYyI6ImE4NTkwYzMxNjBmNWUwYjM0MmM3OWMwNjJiNWM1N2EzZjE0OTVmNGM1Njg2YmMyNTE4OTgxOTA0NTI0MDI5NDAifQ%3D%3D"}

    # cookies = {"XSRF-TOKEN":reponse.cookies.get("XSRF-TOKEN"),
    #     "laravel_session":reponse.cookies.get("laravel_session")}
    # print(headers)
    # reponse_result_2 = requests.post("http://ungm.org.cn/home/ungm/fun1",files = data, headers = headers)

    # print(reponse_result_2.content)