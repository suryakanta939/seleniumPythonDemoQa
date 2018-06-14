import os

class GetFile():

    def filePath(self,fileName):
        wrkingDir=os.path.dirname(__file__)
        destiNationFile="../"+fileName
        destinationDir=os.path.join(wrkingDir,destiNationFile)
        print(destinationDir)
        return destinationDir

