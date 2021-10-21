"""
FFFFF FFFFF M   M PPPP  EEEEE  GGG        DDDD  IIIII RRRR  L      OOO   OOO  PPPP
F     F     MM MM P   P E     G   G       D   D   I   R   R L     O   O O   O P   P
F     F     MM MM P   P E     G           D   D   I   R   R L     O   O O   O P   P
FFF   FFF   M M M PPPP  EEE   GGGGG ----- D   D   I   RRRR  L     O   O O   O PPPP
F     F     M   M P     E     G   G       D   D   I   R R   L     O   O O   O P
F     F     M   M P     E     G   G       D   D   I   R  R  L     O   O O   O P
F     F     M   M P     EEEEE  GGG        DDDD  IIIII R   R LLLLL  OOO   OOO  P
                                                                    By: SeagullisLearningToCode
===============================================================================================
NOTE: CODE REQUIRES FFMPEG
Documentation here: https://ffmpeg.org/ffmpeg.html

Optional Programs
------------------
Pygame (this is only a requirement because some functions use it): https://www.pygame.org/news
mpv: https://mpv.io/
"""
# Imports
import subprocess

try:
    from data.frw.GF import *
except ImportError as gfNotFound:
    p(f"Gull Framework or in it is not found \n{gfNotFound}")

# vars
default = f"{GF_FILE_PATH[len('/users/') + len(gp.getuser()) + len('/'):-len('frw/')]}/samples"

# classes

class ffdir(object):
    def __init__(self, idir, odir, **fdAddArgs):
        # kwargs
        self.debugPrint = fdAddArgs.get("debugMode", False)  # ;Prints
        self.outputFileNameAsOutputFile = fdAddArgs.get("outputNameBeInput", True)
        self.useUserDirectory = fdAddArgs.get("useUserDir", True)
        self.addExtenstions = fdAddArgs.get("addExt", None)
        self.clearDefaultExtensions = fdAddArgs.get("clearExt", None)
        # initargs
        self.inputDirectory = idir
        self.outputDirectory = odir
        # list
        self.fileExtList = [
            [".jpg", ".png", ".jpeg", ".webp", ".gif", ".JPG", ".PNG", ".JPEG", ".WEBP", ".GIF"],
            ["jpeg", "jpg", "png", "JPEG", "JPG", "PNG"]  # ;For refrenced files
        ]
        # dict
        self.compInfo = sysDetect()
        # code

        if self.useUserDirectory is True:
            if self.compInfo["os"].__contains__("macOS") or self.compInfo["os"].__contains__("Linux"):
                self.inputDirectory = f"/Users/{gp.getuser()}/{idir}/"
                self.outputDirectory = f"/Users/{gp.getuser()}/{odir}/"
            elif self.compInfo["os"].__contains__("Windows"):
                self.inputDirectory = f"C:/Users/{gp.getuser()}/{idir}/"
                self.outputDirectory = f"C:/Users/{gp.getuser()}/{odir}/"

        sps(f"idir: '{self.inputDirectory}'", rp="<tt>", condition=self.debugPrint)
        sps(f"odir: '{self.outputDirectory}'", rp="<tt>", condition=self.debugPrint)

        if type(self.clearDefaultExtensions) is bool:
            if self.outputFileNameAsOutputFile is True:
                self.fileExtList.clear()
                sps(self.fileExtList, rp="<tt>", condition=self.debugPrint)
        elif type(self.clearDefaultExtensions) is int:
            self.fileExtList[self.clearDefaultExtensions].clear()
            sps(self.fileExtList[self.clearDefaultExtensions], rp="<tt>", condition=self.debugPrint)

        if type(self.addExtenstions) is list:
            for extentsion in self.addExtenstions:
                if extentsion.islower():
                    dumString = ""
                    for letter in extentsion:
                        dumString += letter.upper()
                    self.fileExtList[0].append(dumString)
                    self.fileExtList[1].append(dumString[1:])
                self.fileExtList[0].append(extentsion)
                self.fileExtList[1].append(extentsion[1:])
            sps(self.fileExtList, rp="<tt>", condition=self.debugPrint)

        self.dirList = getDirectory(self.inputDirectory, filter=self.fileExtList[0], alsoIncludeFileName=self.ouputFileNameAsOutputFile, print_dict=self.debugPrint)

        getPresSpec(self.outputDirectory, create_folder=True, return_result=self.debugPrint)  # ;Check if directory exists, if not, create it

    def runProc(self, **rp):
        """
        abstract
        :param rp:
        :return:
        """
        # rp
        rpAdd = rp.get("cmds", "")
        rpOut = rp.get("out", "")
        rpOutExt = rp.get("outE", "jpg")
        # code
        if self.outputFileNameAsOutputFile is False:
            counter = 0
        crdufi = GF.gef(self.inputDirectory, self.fileExtList[1], pDict=self.debugPrint).createDummyFiles(self.outputDirectory, self.fileExtList[1], add=rpOut)
        for file in self.dirList:
            path = self.dirList.get(file)
            if self.outputFileNameAsOutputFile is True:
                path = self.dirList.get(file)[0]
                name = self.dirList.get(file)[1]
                subprocess.run(f"ffmpeg -y -hide_banner -nostats -i '{path}' {rpAdd} '{self.outputDirectory}{name}{rpOut}{rpOutExt}'", shell=True)
            else:
                subprocess.run(f"ffmpeg -y -hide_banner -nostats -i '{path}' {rpAdd} '{self.outputDirectory}{counter}{rpOut}{rpOutExt}'", shell=True)
                counter += 1
                sps(f"counter: {counter}", rp="<tt>", condition=self.debugPrint)
        for deletion in crdufi:  # ;Delete dummy files from directory that has been cached
            subprocess.run(f"rm {deletion}", shell=True)
            sps(f"Deleted: {deletion}", rp="<tt>", condition=self.debugPrint)

    def setResolution(self, x, y, **sargs):
        """
        Beginner Users, takes the input and makes copies of listed files and places it at the ouput directory

        sargs
        ---------------------------
        printList(bool) = prints the list

        :param x: int
        :param y: int
        :param sargs:
        :return:
        """
        # sargs
        fileType = sargs.get("fileType", "jpg")
        # code
        self.runProc(cmds=f"-s {x}x{y}", outE=fileType)

    def setBitRate(self, **sbrargs):
        """
        Beginner Users, takes the input and makes copies of listed files and places it at the ouput directory

        sargs
        ---------------------------
        printList(bool) = prints the list
        :return:
        """
        # sargs
        setBitRateVideo = sbrargs.get("Video", None)
        setBitRateAudio = sbrargs.get("Audio", None)
        # code
        if type(setBitRateVideo) is str:
            self.runProc(cmds=f"-c:v={setBitRateVideo}")
        if type(setBitRateAudio) is str:
            self.runProc(cmds=f"-c:a={setBitRateAudio}")

    def advancedSettings(self, add, ext, **aS):
        """
        FOR ADVANCED FFMPEG USERS ONLY
        FOR DOCUMENTATION PLEASE REFER TO THE BEGGINING OF THIS CODE

        :param ext:
        :param add:
        :return:
        """
        # aS
        addOutput = aS.get("addOut", None)
        # code
        if addOutput is None:
            self.runProc(cmds=add, outE=ext)
        else:
            self.runProc(cmds=add, out=addOutput, outE=ext)

    def playinmpv(self):
        """
        This is optional
        if you want to use this install mpv (https://mpv.io/)

        This plays each file in ouputDirectory
        :return:
        """
        # code
        ptry(f"'mpv {self.outputDirectory}'", 1)

# ;ffdir(default, f"{default}/results", outputNameBeInput=False, addRes=True, addExt=[".wav"]).advancedSettings("-ar 2048", ".wav")
