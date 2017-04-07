# -*- coding: utf-8 -*-
"""
DCInside ariticle write script. (Mobile)

Mobile dcinside write.
"""
from bs4 import BeautifulSoup
import json
import requests
import time


class DcWrite():
    """DCinside article write class."""

    def __init__(self, id_gall, name, passwd, subject, contents):
        """
        Dcwrite initialize method.

        self.url = Dc gallery write page url.
        self.id_gall = gallery name.
        self.name = article author.
        self.passwd = article password.
        self.subject = article subject.
        self.contents = article contents.
        """
        self.url = "http://m.dcinside.com/write.php?id={}&mode=write".format(id_gall)
        self.id_gall = id_gall
        self.name = name
        self.passwd = passwd
        self.subject = subject
        self.memo = contents

    def get_msg_data(self, option_data):
        """Method return msg data."""
        url = "http://m.dcinside.com/_option_write.php"
        self.session.headers["Referer"] = self.url
        self.session.headers["X-Requested-With"] = "XMLHttpRequest"
        while True:
            req = self.session.post(url, data=option_data)
            if req.text != '':
                return req.text

            time.sleep(1)


    def get_option_data(self):
        """Method return option_write data."""
        data = dict()
        data["id"] = self.id_gall
        data["w_subject"] = self.subject
        data["w_memo"] = self.memo
        data["w_filter"] = 1
        data["mode"] = "write_verify"

        return data

    def get_write_page(self):
        """Method return write page html."""
        return self.session.get(self.url).text

    def run(self):
        """Running method."""
        self.set_session()
        page = self.get_write_page()
        option_data = self.get_option_data()
        # msg["data"]
        msg = json.loads(self.get_msg_data(option_data))

    def set_session(self):
        """
        Method set request sessio.

        self.session = request session value.
        """
        self.session = requests.session()
        self.session.headers["User-Agent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1"


if __name__ == '__main__':
    test = DcWrite("4", "test", "test", "test", "test")
    test.run()