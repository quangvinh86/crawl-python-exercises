import requests
from bs4 import BeautifulSoup
import sys
import time

URL = "https://www.w3resource.com/python-exercises/numpy/python-{0}-exercise-{1}.php"


def get_data_from_w3resource(tut, number, to_number):
    for i in range(number, to_number + 1):
        question = ""
        code = ""
        output = ""
        try:
            url = URL.format(tut, i)
            resp = requests.get(url)
            data = BeautifulSoup(resp.text, 'html.parser')
            p_list = data.findAll("p")
            question = p_list[1].text
            code = data.findAll("code", {"class" : "language-python"})[0].text
            output = data.findAll("pre", {"class" : "output"})[0].text
        except Exception as ex:
            print(ex)
        finally:
            with open(tut + "_ex" + str(i) + ".py", "w", encoding='utf-8') as fsave:
                fsave.write("'''Question: \n")
                try:
                    fsave.write(question)
                except UnicodeEncodeError:
                    print("{} UnicodeError".format(i))
                fsave.write("\n'''\n\n")
                fsave.write("# Python code: \n\n")
                fsave.write(code)
                fsave.write("\n\n'''Output sample: \n")
                fsave.write(output)
                fsave.write("'''")
            print(tut + "_ex" + str(i) + ".py")
            time.sleep(5)


if __name__ == "__main__":
    get_data_from_w3resource("numpy", 6, 100)
