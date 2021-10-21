"""
 __                     ___  __              ___       __   __
/ _` |  | |    |       |__  |__)  /\   |\/| |__  |  | /  \ |__) |__/
\__> \__/ |___ |___    |    |  \ /~~\  |  | |___ |/\| \__/ |  \ |  \
                                                    Version: 1.015c

This file stores very simple functions with the sole purpose of de-bloating the Main.py file (used to be)
This file is also makes stating certain things faster and possibly easier.
"""
# IMPORTS---------------------------------------------------------------------------------------------------------------------
import os
import gc
import sys
import pdb
import subprocess
import platform as pt
import getpass as gp
from importlib import util
from pygame import *
from datetime import *
from random import *
from configparser import *

# ;VARIABLES-------------------------------------------------------------------------------------------------------------------
load = mixer.music
# ;Today's Date
td = date.today()
td_c_s = str(td)  # Converts the current date into a String
td_c_s_yo = td_c_s[0:4]  # Get year only
# ;Today's Time
tt = datetime.now()
GF_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
GF_XTN_FOLDER_PATH = f"{GF_FILE_PATH}/EXT/"


# ;FUNCTIONS-------------------------------------------------------------------------------------------------------------------

def p(t="passed"):
    """
    Print
    Make print statements faster than python's print("Hello World")

    Example: p("Hello World")
    Output: Hello World
    """
    # CODE
    print(t)


def ptry(cmd, errNum):
    """
    PrintTry is a conditional function that use try and except conditionals
    :param cmd:
    :param errNum:
    :return:
    """
    # sa
    en = errNum
    # dict
    errStrs = {
        0: {
            0: "PermissionError",
            1: "OSError",
            2: "RuntimeError"
        },
        1: {
            0: "notAbleToCreateFolderOrFileAtGivenDir",
            1: "cantRunProcessDueToNotBeingInstalled",
            2: "pythonErr",
        },
        2: {
            0: f"GULL FRAMEWORK: <{tt}> An error has occured (err code: {errNum})\n\tPermission to this '{cmd}' has been denied",
            1: f"GULL FRAMEWORK: <{tt}> An error has occured (err code: {errNum})\n\tRunning '{cmd}' returned as 'Unknown Command'",
            2: f"GULL FRAMEWORK: <{tt}> An error has occured (err code: {errNum})\n\tAccess to this path '{cmd}' doesn't exist",
            3: f"GULL FRAMEWORK: <{tt}> An error has occured (err code: {errNum}\n\tPython has ran into an error\n\t\tPython: {cmd}"
        }
    }
    # code
    def runt(str1,  # ;Command
             errType,  # ;Error Type
             var1,  # ;Variable
             errNumRef  # ;String From Dict Refrence (but takes int)
             ):
        e = en
        # code
        exec(f"if e == {errNumRef}:\n\ttry:\n\t\t{str1}\n\texcept {errType} as {var1}:\n\t\tp(f'{{errStrs[2][errNumRef]}}{{var1}}')\n\t\tsys.exit(2)")
        # ;if e == errNumRef:
        # ; try:
        # ;     str1
        # ; execpt errType as var1:
        # ;     p('{errStrs[2][errNumRef]}{var1}')
        # ;     sys.exit(2)

    runt(cmd, errStrs[0][0], errStrs[1][0], 0)  # ;Permission Error
    runt(f"subprocess.run({cmd}, shell=True)", errStrs[0][1], errStrs[1][1], 1)  # ;Subprocess Unknown Error
    runt(cmd, errStrs[0][2], errStrs[1][2], 3) # ;Python Error


def sps(t: str, **sargs):
    """
    Same thing as p() but adds in "passed"

    sargs is KWARGS
    --------------
    replacePassed(str)
        Commands:
            |_____"<tt>" = Includes current time when executed
    addCond(bool or int)
        conditionals:
            |____bool = if the "condition" arg is bool and that bool is set to true, then print the statement
            |____int = same as bool but if the value is greater than 1, then print the statement

    Example: sps("it")
    Output: passed it
    """
    # sargs
    replacePassed = sargs.get("rp", None)
    addCond = sargs.get("condition", None)
    # lists
    replacePassedCMDS = ["<tt>", "<exec>"]
    # CODE
    if replacePassed is not None and type(replacePassed) is str:
        if type(addCond) is int:
            if addCond >= 1:
                if replacePassed in replacePassedCMDS:
                    if replacePassed.__contains__(replacePassedCMDS[0]):
                        p(f"{replacePassed[len(replacePassedCMDS[0]):]}<{tt}> {t}")
                    elif replacePassed.__contains__(replacePassedCMDS[1]):
                        exec(f"{replacePassed[len(replacePassedCMDS[1]):]}")
                    else:
                        p(f"{replacePassed} {t}")
        elif type(addCond) is bool:
            if addCond is True:
                if replacePassed in replacePassedCMDS:
                    if replacePassed.__contains__(replacePassedCMDS[0]):
                        p(f"{replacePassed[len(replacePassedCMDS[0]):]}<{tt}> {t}")
                    elif replacePassed.__contains__(replacePassedCMDS[1]):
                        exec(f"{replacePassed[len(replacePassedCMDS[1]):]}")
                    else:
                        p(f"{replacePassed} {t}")
        elif addCond is None:
            if replacePassed in replacePassedCMDS:
                if replacePassed.__contains__(replacePassedCMDS[0]):
                    p(f"{replacePassed[len(replacePassedCMDS[0]):]}<{tt}> {t}")
                elif replacePassed.__contains__(replacePassedCMDS[1]):
                    exec(f"{replacePassed[len(replacePassedCMDS[1]):]}")
                else:
                    p(f"{replacePassed} {t}")
    else:
        p(f"passed {t}")


def flp(l: dict, **kwargs):
    """
    For in Loop Print From Dictionary

    kwargs
    -----------------
    additions(str)
        Commands(additionsCommander):
            |_____"<addfirst>" = puts the additions first before "key" or "value" (if type is list)
            |_____"<addinbetween>" =  puts the additions in between "key" and "l.get(key)" (not availible if the type is a list)
            |_____"<counter> = adds a counter

    :param l:
    :param kwargs:
    :return:
    """
    # kwargs
    additions = kwargs.get("add", None)
    # lists
    additionsCommander = ["<addfirst>", "<addinbetween>", "<counter>"]
    # abs
    add = additions
    # code
    if add is not None and type(add) is str:
        if add.__contains__(additionsCommander[2]):
            additionsCommanderCounter = 0

    if type(l) is dict:
        for key in l:
            if add is not None and type(add) is str:
                if add.__contains__(additionsCommander[0]):
                    p(f"{add[len(additionsCommander[0]):]} {key}: {l.get(key)}")
                elif add.__contains__(additionsCommander[1]):
                    p(f"{key}: {add[len(additionsCommander[1]):]} {l.get(key)}")
                elif add.__contains__(additionsCommander[2]):
                    additionsCommanderCounter += 1
                    p(f"{key}: {l.get(key)} {add[len(additionsCommander[2]):]}<{additionsCommander}>")
                else:
                    p(f"{key}: {l.get(key)} {add}")
            else:
                p(f"{key}: {l.get(key)}")
    elif type(l) is list:
        for value in l:
            if add is not None and type(add) is str:
                if add.__contains__(additionsCommander[0]):
                    p(f"{add[len(additionsCommander[0]):]} {value}")
                elif add.__contains__(additionsCommander[2]):
                    additionsCommanderCounter += 1
                    p(f"{value} {add[len(additionsCommander[2]):]}<{additionsCommander}>")
                else:
                    p(f"{value} {add}")
            else:
                p(value)


def getAllVars(**kwargs):
    """
    code inheirited and modified from the ASKII project

    :param kwargs:
    :return:
    """
    # kwargs
    test = kwargs.get("test", False)  # ;This is a test arg which will print after the varible has been changed only if the `reduceSpacing` kwarg has been set to 'True'
    printResult = kwargs.get("printResult", False)  # ;This a arg that will print the var's value before and after
    printDebugDispAllVars = kwargs.get("debugVars", "N")  # ;Prints all vars and globals
    # lists
    passArgStrings = ["NOP", "nop"]
    execArgStrings = ["all", "globals", "vars"]
    # dicts
    easSTDOUTDict = {
        "all": [f"GF All Vars:\n\tallVars\n\t---------------------------------------------------------", f" ---------------------------------------------------------\n<{tt}> Excuting allGlobals as {flp}...\n\tallGlobals\n\t---------------------------------------------------------", f"\nBelow this point is non debug executions\n================================================\n"],
        "vars": [f"GF All Vars:\n\tallVars\n\t---------------------------------------------------------", f"\nBelow this point is non debug executions\n================================================\n"],
        "globals": [f"GF All Vars:\n\tallGlobals\n\t---------------------------------------------------------", f"\nBelow this point is non debug executions\n================================================\n"]
    }
    # code
    if printDebugDispAllVars in passArgStrings:
        pass
    elif printDebugDispAllVars in execArgStrings:
        if printDebugDispAllVars in execArgStrings[0:1]:
            p(easSTDOUTDict["all"][0])
            flp(vars(), add="<addfirst>\t")
            p(easSTDOUTDict["all"][1])
            flp(globals(), add="<addfirst>\t")
            p(easSTDOUTDict["all"][2])
        elif printDebugDispAllVars in execArgStrings[1:2]:
            p(easSTDOUTDict["globals"][0])
            flp(globals(), add="<addfirst>\t")
            p(easSTDOUTDict["globals"][1])
        elif printDebugDispAllVars in execArgStrings[2]:
            p(easSTDOUTDict['vars'][0])
            flp(vars(), add='<addfirst>\t')
            p(easSTDOUTDict['vars'][1])


def getPresSpec(file: str, **kwargs):
    """
    Does the file exist

    Returns: None by default
    """
    # KWARGS
    GPS_RETURN_EXIST = kwargs.get('return_result', False)
    GPS_CREATE_FOLDER = kwargs.get("create_folder", False)
    # OSPATH
    getpres = os.path.exists
    # CODE
    if GPS_RETURN_EXIST is False:
        p(getpres(file))
    if GPS_CREATE_FOLDER is True:
        if getpres(file) is False:
            if GPS_RETURN_EXIST is False:
                p(f"Making File/Folder:\n\t\t{file}")
            os.makedirs(file)
        else:
            if GPS_RETURN_EXIST is False:
                p(f"Folder already exists:\n\t\t{file}")

    return getpres(file)


def hexValFromFile(dirname: str,
                   filename: str,
                   destination: str,
                   printresults: bool,
                   outputresulttofile: bool):  # ;True = 1, False = 0
    """
    Hex Values From File To Array Of Hex Values
    This Function converts the hex values inside a text document and prints the values as an array
    """
    """
    Unfortunately what sucks about this function as of now is that I can possibly figure out a way to convert it into an actual hex value.
    """
    # STRINGS
    dfn = dirname  # ;Shortens dirname arg
    fn = filename  # ;Shortens and filename arg
    dtn = destination  # ;Shortens destination arg
    # BOOLEANS
    orf = outputresulttofile  # ;Shortens outputresulttofile arg (this makes it to where if you don't want the results made into a file, the function prints the result instead)
    pr = printresults  # ;Shortens the printresults arg
    # MISC
    gun = gp.getuser()  # ;Shortens and gets the current username
    # CODE
    gdn = (dfn + fn)  # ;Combine and Shortens dfn and fn which creates the full path
    gun_gdn = (gun + gdn)  # ;Combines and shortens gun and gdn which will do something
    fp_uni = ("/Users/" + gun + "/" + dtn + fn)  # ;Combines and shortens gun and dtn and fn
    pat = open(gdn, "r")  # ;Opens the file and gives python read and write access
    dat = pat.read()

    void_names = ["none", "null", "0"]
    preres = []
    res = []

    pat.close()  # ;Prevents memory leakage
    r = dat.split(' ')
    if orf is True:
        if dtn == void_names[0] or void_names[0].upper() or void_names[1] or void_names[1].upper() or void_names[2]:
            pass
        else:
            if os.path.exists(dtn) is False:  # ;if directory doesn't exist then create it
                os.makedirs(dtn)
    if os.path.exists(gdn) is False:
        ptry(f"os.makedirs({gdn})", 0)
    else:
        for i in r:
            preres.append(i)
        if len(preres[-1]) >= 4:
            if preres[-1].__contains__(preres[-2]):
                preres.pop(-1)
                preres.append(preres[-1])
            else:
                preres[-1][-1].rindex("\n")

    for fi in preres:
        pointer_hex_string = f"0x{fi}"
        translator = int(pointer_hex_string, 16)
        real_hex_value = translator
        res.append(real_hex_value)
    if orf is True:
        if dtn == void_names[0] or void_names[0].upper() or void_names[1] or void_names[1].upper() or void_names[2]:
            pass
            if os.path.exists(f"{dtn}{fn}") is False:
                destfile = open(f"{dtn}{fn}", "w+")
            destfile = open(f"{dtn}{fn}", "w+")
            destfile.write(str(f"Pre-result_001: {preres} {len(preres)}\n\nResult: {res} {len(res)}"))
        destfile.close()  # ;Prevent memory leakage
    if pr is True:
        p(f"pre-result_001: {preres}")
        p(f"Result: {res}")
    return res


def imgDict(targetpath: str, **kwargs):
    """
    Takes the files within a folder and translate the paths to a dictionary (targetname --> returnname)

    :param targetpath:
    :param kwargs:
    :return: Dict
    """
    # INT
    counter = 0
    # STRINGS
    t_path = targetpath
    # DICTIONARIES
    d = {}
    # OSPATH
    g_fit = os.listdir(t_path)
    # KWARGS_BOOLEANS
    v_names = kwargs.get("EVerboseResults", False)  # ;prints the process
    # CODE
    for file in g_fit:
        if file.__contains__(".jpg") or file.__contains__(".bmp") or file.__contains__(".png") or file.__contains__(".gif"):
            counter += 1
            d.update({counter: t_path + file})
    if v_names is True:
        flp(d)
    return d


def getDirectory(targetpath: str, **kwargs):
    """
    Takes the files within a folder and translate the paths to a dictionary (targetname --> returnname)

    Rules
    -------
    1. there must not be any more than 1 "." containing in the dir name

    if these rules are broken they go into a "unusable list"
    :param targetpath:
    :param kwargs:
    :return: Dict
    """
    # KWARGS
    GD_FILTER = kwargs.get("filter", None)  # ;acts like the search or find option you most likely find in a file manager
    GD_PRINT_DICT = kwargs.get("print_dict", True)
    GD_ALSO_INCLUDE_FILENAME = kwargs.get("alsoIncludeFileName", True)
    # INT
    counter = 0
    # STRINGS
    t_path = targetpath
    # DICTIONARIES
    d = {}
    # LISTS
    nmi = []
    mi = []
    # BOOLEANS
    tooManyFalseFlagsAlreadyChecked = False
    # CODE
    for file in os.listdir(t_path):  # ;Loop through directory
        if GD_FILTER is not None:  # ;if argument is not a NONE type
            try:
                if type(GD_FILTER) is str:
                    if file.__contains__(GD_FILTER):  # ;if filename contains a word, number or file type
                        counter += 1
                        if GD_ALSO_INCLUDE_FILENAME is True:
                            d.update({counter: [t_path + file, file[:-4]]})
                        else:
                            d.update({counter: t_path + file})
                elif type(GD_FILTER) is list:
                    onlyExt = file[file.find("."):]
                    if onlyExt in GD_FILTER:
                        counter += 1
                        if GD_ALSO_INCLUDE_FILENAME is True:
                            d.update({counter: [t_path + file, file[:file.find('.')]]})
                            mi.append(counter)
                        else:
                            d.update({counter: t_path + file})
                            mi.append(counter)
                    else:
                        nmi.append(t_path+file)
                        p(f"Get in the Gull-lag '{onlyExt}'\n\t\tReason: {file}")
                        if len(nmi) > len(mi) and tooManyFalseFlagsAlreadyChecked is False:
                            p("Getting too many possible False Flags")
                            tooManyFalseFlagsAlreadyChecked = True
            except TypeError as valueTypeIsInvalid:
                p(f"<{tt}> Filter arg type error: {valueTypeIsInvalid}")
                sys.exit(2)
        else:
            counter += 1
            if GD_ALSO_INCLUDE_FILENAME is True:
                d.update({counter: [t_path + file, file[:-4]]})
            else:
                d.update({counter: t_path + file})
    if GD_PRINT_DICT is True:
        flp(d)
        if len(nmi) != 0:
            p(f"--------------------\n\tMissing\n--------------------")
        flp(nmi)
    del mi, nmi # ;These aren't needed anymore when the loop is done
    return d


def merge(target_list, **kwargs):
    """
    Takes a nested list into a single list

    :param target_list:
    :param kwargs:
    :return:
    """
    # LISTS
    tl = target_list
    i = []  # ;result var
    # KWARGS_BOOLEANS
    show_result = kwargs.get("show_result", False)
    # CODE

    for cat in tl:
        for value in cat:
            i.append(value)

    if show_result is True:
        p(i)

    return i


def remDupesLst(target, **kwargs):
    # LIST
    new_list = []
    # KWARGS
    print_result = kwargs.get("print_result", False)
    sender = kwargs.get("send", None)
    # CODE
    if sender is not None:
        for i in target:
            if i not in target:
                sender.append(i)
    else:
        for i in target:
            if i not in target:
                new_list.append(i)

    if print_result is True:
        p(new_list)

    return new_list


def genIterList(amount, **kwargs):
    # KWARGS
    GIL_PRINTRESULT = kwargs.get('print_result', False)
    GIL_LISTNAME = kwargs.get('listname', None)
    # ABS
    a = amount
    ln = GIL_LISTNAME
    pr = GIL_PRINTRESULT
    # LIST
    l = []
    # CODE
    if GIL_LISTNAME is not None:
        for i in range(a):
            ln.append(0)
        if pr is True:
            p(ln)
        return ln
    else:
        for i in range(a):
            l.append(0)
        if pr is True:
            p(f"gen_iter_list <print_result>: {l}")
        return l

# def checkIf(statement_1, newvalue, **oper):
#    """
#    *EXPERIMENTAL*
#    it's complicated (read code below) *NOT YET DONE*
#    this may compare multiple values
#    **oper
#    --------------------------------------------------------
#    addStatement(list)
#        Examples:
#            |____[[statement:str, neededValue:any]]
#            |____[["player.IsDead", True]]
#            |____[["npc.jellyfish.variant", "Jurassic"]]
#            |____[["ep.resolution["internal"][0], 320]]
#    :param statement_1:
#    :param value:
#    :param oper:
#    :return:
#    """
#    # oper
#    addStatement = oper.get("addStatment", None)
#    # code
#    if addStatement is not None: # ;if addstatment kwarg has no value
#        if type(value) is str: # ;if the type 'value' is text
#            if value is not "</p/a/s/@000000n>": # ;this acts as a no-operation
#                cmd = oper.get("cmd", str) # ;add conditional kwarg
#        addStatementValueDict = {} # ;Create Dictionary
#        if addStatement is list: # ;if addstatement kwarg is this "[[statement, value]]" quotes aren't included
#            for statment in range(len(addStatement)): # ;loop through nested list
#                getNV = addStatement[statment][1] # ;Get needed value
#                addStatementValueDict.update({f"{addStatement[statment][0]}": getNV}) # ;define the nested strings and add a value to it
#                if type(addStatementValueDict[f"{statment}"]) is bool: # ; if executable name has the value type "boolean"
#                    exec(f"if {addStatementValueDict[f'{addStatement[statment]}']} is {addStatementValueDict.get(f'{addStatement[statment]}')}:") # ;if ^ is equal to the statement that matches the targeted value
#                    if value is "<p0000>": # ;if value arg is a passed or no-operation value (I know it's long)
#                        exec(f"if {statement_1} is True:\n\texec({cmd})") # ;make an if statement and if the if statement returns true then execute command
#                    else:
#                        exec(f"{statement_1} = {value}") # ;if not value arg is not the passed nor the no-operation value then this will execute
#    else:
#        exec(f"if type({statement_1}) is bool"
#             f"")

def sysDetect(**sdopt):
    """
    Inherited From EccoPY
    :return:
    """
    # sdopt
    printResult = sdopt.get("getResults", False)
    # code
    p("Detecting Operating System and Hardware...")
    compinfo = {
        "Machine".lower(): pt.machine(),
        "System".lower(): pt.system(),
        "OS".lower(): pt.platform(),
        "CPU".lower(): pt.processor(),
        "Username".lower(): gp.getuser(),
    }
    if printResult is True:
        flp(compinfo)

    return compinfo


# CLASSES------------------------------------------------------------------------------------------------------------------------------------------------------------------

class GF_GET_FILE_INFO(object):
    def __init__(self, target, types, **gfKwargs):
        # gfkwargs
        self.printDict = gfKwargs.get("pDict", False)
        # str
        self.target = target
        # double
        self.types = types
        # gd
        self.dir = getDirectory(target, filter=types, alsoIncludeFileName=False, print_dict=self.printDict)

    def createDummyFiles(self, tar, types, **cdf):
        # cdf
        add = cdf.get("add", None)
        # list
        deleteMeAfter = []
        # code
        if add is None:
            for file in self.dir:
                if self.dir[file][self.dir[file].find('.'):] in types:
                    f = open(f"{tar}{file}.{self.dir[file][self.dir[file].find('.'):]}", "w+")
                    f.close()
                    deleteMeAfter.append(f"{tar}{file}.{self.dir[file][self.dir[file].find('.'):]}")
        else:
            for file in self.dir:
                if self.dir[file][self.dir[file].find('.'):] in types:
                    f = open(f"{tar}{file}{add}.{self.dir[file][self.dir[file].find('.'):]}", "w+")
                    f.close()
                    deleteMeAfter.append(f"{tar}{file}{add}.{self.dir[file][self.dir[file].find('.'):]}")
        return deleteMeAfter

    def getResolution(self):
        # int
        c = 0
        # dict
        r = {}
        # code
        for indFileSize in self.dir:
            c += 1
            p(indFileSize)
            f = image.load(indFileSize)
            r.update({c: [f.get_width(), f.get_height()]})
        sps("", rp=f"<exec>flp(r)", condition=self.printDict)
        return r

class GF_MATH_CONVERT_FROM_LIST(object):
    def __init__(self):
        pass

    def hextoint(self, tl: list, dl: list):
        # INT
        nothexval = 0
        # CODE
        for hexchecker in tl:
            for i in range(len(tl)):
                if type(hexchecker) != hex:
                    nothexval += 1
        for value in tl:
            dl.append(int(value))


class GF_MUSICPLAYER_DICT_FORM(object):
    def __init__(self):
        pass

    def play(self, target: dict, name: str, loop: int):
        # DICTIONARIES
        filename = target.get(name)
        # CODE
        load.load(filename)
        if loop != 1 or 0:
            if randint(0, 100) == 1:
                p(f"Gull: Sorry I can't do that option {loop}, maybe tell me a yes or a no, or in what I can read a 1 or a 0 (representing on or off).")
            raise ValueError
        load.play(loop)

    def que(self,
            target: dict,
            name: str):
        # DICTIONARIES
        filename = target.get(name)
        # CODE
        load.queue(filename)

    def queFromDict(self, target: dict):  # takes the values from the target and qeues them
        # DICTIONARIES
        names = target
        # CODE
        for i in names:
            self.que(names, i)


class GF_DEVLOG(object):
    """
    This deals with Logging stuff into a file

    Functions Avaible
    ---------------------------
    RECORD_CONSOLE(self, what: sys.stderr, sys.stdout, sys.stdin)
    """

    def __init__(self, filepath: str = "/Documents/SIS/EccoPY/LOGS/", textfile: str = "DEVELOPERLOG", filetype: str = ".log", limit_fs: float = 0x164210, isThisEnabled: bool = True):
        # STRINGS
        self.fp = filepath
        self.tf = textfile
        self.ft = filetype
        # FLOATS
        self.lfs = limit_fs
        # BOOLEANS
        self.ise = isThisEnabled
        # STATEMENTS
        self.gun = gp.getuser()

    def RECORD_CONSOLE(self, what):
        # CODE
        if what is not sys.stderr or sys.stdout or sys.stdin:
            p(f"Gull: ARGUMENT OF RECORD WHICH IS {what} ISN'T 'sys.stderr', 'sys.stdout OR 'sys.stdin'\n SOLUTION: Try changing 'what' to one of those options")
            raise ValueError
        if os.path.exists(f"/Users/{self.gun}{self.fp}") is False:
            os.makedirs(
                f"/Users/{self.gun}{self.fp}"
            )
        if os.path.exists(f"/Users/{self.gun}{self.fp}{self.tf}{str(what)}{self.ft}") is False:
            what = open(f"/Users/{self.gun}{self.fp}{self.tf}{str(what)}", "w+")
        if self.ise is True:
            if not os.path.getsize(f"/Users/{self.gun}{self.fp}{self.tf}") >= self.lfs:
                what = open(f"/Users/{self.gun}{self.fp}{self.tf}", "w+")
                if os.path.getsize(f"/Users/{self.gun}{self.fp}/{self.tf}") >= self.lfs:
                    what.close()
        else:
            p("Ok")


class GF_WRITE_SETTING_FILES(object):
    """
    This deals with writing non-existant settings file/s (mainly uses '.ini' files ATM)

    Functions Avaible
    ---------------------------
    writeSettingsFile(self, dir: str *optional*, name: str *optional*, **kwargs)
    """

    def __init__(self):
        super().__init__()
        # USERNAME
        self.gun = gp.getuser()  # ;Get Current Username
        # DIRECTORIES
        self.subdir = f"{self.gun}/EP_S/"
        self.user_settings_folder = f"/Documents/Seagulls/EccoPY/"

    def writeSettingsFile(self, dir: str = "/Documents/Seagulls/EccoPY/", name: str = "Settings", **kwargs):
        # KWARGS
        WSF_RETURN_FILEPATH = kwargs.get('return_path', True)
        # STRINGS
        d = dir
        n = name
        getdir = f"/Users/{self.gun}{d}{self.subdir}"
        # CODE
        if os.path.exists(getdir) is False:
            os.makedirs(getdir)
        if os.path.exists(f"{getdir}{n}.ini") is False:
            newfile = open(f"{getdir}{n}.ini", "w+")  # Creates new file
            newfile.close()

        if WSF_RETURN_FILEPATH is True:
            path_name = f"{getdir}{n}.ini"
            p(path_name)
            return path_name


class GF_MAPPING(object):
    """
    This deals with mapping

    Functions Avaible
    ---------------------------
    LoadMap(self, filepath)
    """

    def __init__(self):
        pass

    def loadMap(self, filepath):
        """
        This function is now mainly used for either basic maps or static HUD
        """
        # DIRECTORIES
        f = open(filepath, "r")
        # CODE
        data = f.read()
        f.close()
        data = data.split('\n')
        gmap = []
        for bit in data:
            gmap.append(list(bit))
        return gmap


class GF_INIT(object):
    """
    Gull Framework Root class
    """

    def __init__(self, **kwargs):
        # KWARGS_BOOLEANS
        self.enable_assembly_mode = kwargs.get("assembly_mode", True)
        self.init_all_classes = kwargs.get("init_all", False)  # ;Runs all initilized classes
        self.load_all_palm_trees = kwargs.get("load_all_palm_trees", False)  # ;Loads all "Palm Trees"
        self.no_start_print = kwargs.get("no_print", True)
        #   CODE
        if self.no_start_print is not True:
            p("\nGull Framework\n\t\t\tBy SeagullinSeagulls\n\t\t\t\tCode: https://github.com/SeagullisLearningToCode/Gull-Framework (Might be outdated)\n\nBELOW HERE MIGHT BE PALM TREES\n------------------------------------------------------------------------------------------------------------")
        if self.init_all_classes is True:
            if self.enable_assembly_mode is True:
                self.m = GF_MAPPING()
                self.dl = GF_DEVLOG()
                self.wsf = GF_WRITE_SETTING_FILES()
                self.mpdf = GF_MUSICPLAYER_DICT_FORM()
                self.cl = GF_MATH_CONVERT_FROM_LIST()
                self.gef = GF_GET_FILE_INFO()
            else:
                self.map = GF_MAPPING()
                self.log = GF_DEVLOG()
                self.set = GF_WRITE_SETTING_FILES()
                self.musicPlayer = GF_MUSICPLAYER_DICT_FORM()
                self.convert = GF_MATH_CONVERT_FROM_LIST()
                self.getFileInfo = GF_GET_FILE_INFO()
        if self.enable_assembly_mode is True:  # ;gives it somewhat of an assembly feel
            self.m = GF_MAPPING  # ;Deals with mapping
            self.dl = GF_DEVLOG  # ;Logs stuff
            self.wsf = GF_WRITE_SETTING_FILES  # ;Writes INI files
            self.mpdf = GF_MUSICPLAYER_DICT_FORM  # ;Deals with playing music from dicts
            self.cl = GF_MATH_CONVERT_FROM_LIST  # ;Deals with converting lists/dicts to differnt types of values inside them
            self.gef = GF_GET_FILE_INFO  # ;This is very limited as of now, this deals with getting the size of a file (as in resolution)
        else:  # ;New age stuff
            self.map = GF_MAPPING
            self.log = GF_DEVLOG
            self.set = GF_WRITE_SETTING_FILES
            self.musicPlayer = GF_MUSICPLAYER_DICT_FORM
            self.convert = GF_MATH_CONVERT_FROM_LIST
            self.getFileInfo = GF_GET_FILE_INFO
        # ;Palm Trees (TEST)
        if getPresSpec(GF_XTN_FOLDER_PATH) is False:
            os.makedirs(GF_XTN_FOLDER_PATH)
        if self.load_all_palm_trees is True:
            pt_dir_dict = getDirectory(targetpath=GF_XTN_FOLDER_PATH, filter='.py', print_dict=False)
            for palm_tree in range(len(pt_dir_dict)):
                ext = util.spec_from_file_location("*", pt_dir_dict[palm_tree + 1])
                ext_mod = util.module_from_spec(ext)
                ext.loader.exec_module(ext_mod)


# INIT_GULL_FRAMEWORK----------------------------------------------------------------------------------------------------------------------------------------------------------------

GF = GF_INIT(assembly_mode=True)
