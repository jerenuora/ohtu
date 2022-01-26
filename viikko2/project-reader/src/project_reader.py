from ast import parse
import imp
from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed = toml.loads(content)
        parsed_poetry = parsed['tool']['poetry']
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(parsed_poetry['name'], parsed_poetry['description'],parsed_poetry['dependencies'], parsed_poetry['dev-dependencies'])
