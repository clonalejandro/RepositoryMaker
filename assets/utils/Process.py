# -*- coding=utf-8 -*-

from subprocess import call

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
# * All rights reserved for clonalejandro ©Repository 2017 / 2018
# */


class Process(object):

    # SMALL CONSTRUCTORS

    __i = 0; __mvn = 'mvn'; __slash = 6
    __plugin = 'org.apache.maven.plugins:maven-install-plugin:2.5.2:install-file'
    __args = ["-Dfile=", "-DgroupId=", "-DartifactId=", "-Dversion=", "-Dpackagin=", "-DlocalRepositoryPath=", " /"]

    # REST

    def makeRepo(self, jar, group, artifact, version):
        # Make vars
        repo = "/Users/alejandrorioscalera/" + jar.replace(".jar", "")
        i = self.__setIterator(); mvn = self.__mvn; plugin = self.__plugin; args = self.__args; slash = self.__slash
        jar += slash; group += slash; artifact += slash; version += slash; repo += slash

        call([mvn, plugin, args[i] + jar,
              args[i] + group, args[i] + artifact,
              args[i] + version, args[i] + "jar",
              args[i] + repo])

    # OTHERS

    def getIterator(self):
        return self.__i

    def __setIterator(self):
        n = self.__i
        self.__i += 1
        return n
