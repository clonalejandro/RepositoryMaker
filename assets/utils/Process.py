# -*- coding=utf-8 -*-

import os, sys
from subprocess import call
import json

# /**
# * Created by alejandrorioscalera
# * On 21/9/17
# *
# * -- SOCIAL NETWORKS --
# *
# * GitHub: https://github.com/clonalejandro or @clonalejandro
# * Website: https://clonalejandro.me/
# * Twitter: https://twitter.com/clonalejandro11/ or @clonalejandro11
# * Keybase: https://keybase.io/clonalejandro/
# *
# * -- LICENSE --
# *
# * All rights reserved for clonalejandro ©RepositoryMaker 2017 / 2018
# */


class Process(object):

    # SMALL CONSTRUCTORS

    __mvn = 'mvn'; __slash = 6
    __plugin = 'org.apache.maven.plugins:maven-install-plugin:2.5.2:install-file'
    __args = ["-Dfile=", "-DgroupId=", "-DartifactId=", "-Dversion=", "-Dpackaging=", "-DlocalRepositoryPath=", " \\"]

    # REST
    def config(self):
        jsonFile = open("config/config.json", "r")
        jsonCode = jsonFile.read()
        jsonFile.close()
        return json.loads(jsonCode)

    def makeRepo(self, jar, group, artifact, version):
        # Make vars
        repo = jar; mvn = self.__mvn; plugin = self.__plugin; args = self.__args; lFile = os.path.basename(repo).replace(".jar", "")
        raid = self.config()['raid'] + self.config()['dirOfrepos']; _repo = raid + lFile;
        _jar = args[0] + self.config()['raid'] + jar; _group = args[1] + group; _artifact = args[2] + artifact
        _version = args[3] + version; _packaging = args[4] + "jar"

        # Functions
        os.chdir(raid)

        if not os.path.exists(_repo):
            os.mkdir(_repo)

        call([mvn, plugin, _jar, _group, _artifact, _version, _packaging, args[5] + _repo])
        sys.exit()
