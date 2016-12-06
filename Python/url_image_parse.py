"""
Image parse.

. . .
"""
from bs4 import BeautifulSoup
# from base64 import b64decode
import os
import time
import urllib
import re
import sys


RE_SRC = re.compile(r"""<img.*?(?:src|data-src)="(.*?)"""")


# def discern_scheme(path, list_value):
    """Data url scheme discern and saving function."""
    # for value in list_value:
    #     if "data:image" in value:
    #         code = value.split(',')[1]
    #         extension = value[value.find('/') + 1:value.find(';')]
    #         with open("{}{}.{}".format(path, code, extension), "wb") as image:
    #             image.write(str(b64decode(code)))
    #         del(list_value[list_value.index(value)])
    #         print(value)

    # return list_value


def duplicate_remove_list(list_what):
    """Removing duplicate elements in list."""
    return list(set(list_what))


def get_list_img(source):
    """Return img tag list."""
    soup = BeautifulSoup(source, "html.parser")

    return soup.find_all("img")


def get_src_value(list_img_tag):
    """Return src value list."""
    list_value = []
    for img in list_img_tag:
        list_value.append(RE_SRC.findall(str(img))[0])

    return duplicate_remove_list(list_value)


def get_url_read(url):
    """Return html for url."""
    url_open = urllib.urlopen(url)
    read = url_open.read()
    url_open.close()

    return read


def make_directory():
    """Make directtory and return path function."""
    folder = os.getcwd() + "\\" + str(time.time()).split('.')[0] + "\\"

    if os.path.isdir(folder) is False:
        os.mkdir(folder)


def save_image_file_link(image_url, folder):
    """Save image in timestamp folder."""
    file = image_url[image_url.rfind("/") + 1:]
    if "?" in file:
        file = file[:file.find('?')]

    urllib.urlretrieve(image_url, folder + file)


def usage():
    """Usage function."""
    print("{} [url]".forma(sys.argv[0]))
    exit()


def main(url):
    """Main function."""
    source = get_url_read(url)
    list_img_tag = get_list_img(source)
    print(list_img_tag)
    list_value = get_src_value(list_img_tag)
    path_folder = make_directory()
    # list_value = discern_scheme(path_folder, list_value)

    if len(list_value) != 0:
        for value in list_value:
            save_image_file_link(value, path_folder)


if __name__ == "__main__":
    # url = "http://www.naver.com"
    if len(sys.argv) != 2:
        usage()

    main(sys.argv[1])
