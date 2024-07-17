import os

MINECRAFT_ICON = "resource/image/core/minecraft.png"
FORGE_ICON = "resource/image/core/forge.png"
FABRIC_ICON = "resource/image/core/fabric.png"
MICROSOFT_ACCOUNT = "resource/image/account/Microsoft.png"
LEGACY_ACCOUNT = "resource/image/account/legacy.png"
THIRD_PARTY_ACCOUNT = "resource/image/account/third_party.png"
JAVA_RUNTIME = "resource/image/java.png"

DEFAULT_GAME_PATH = os.path.join(os.path.expanduser('~'), "AppData", "Roaming", ".minecraft")

LAUNCH_DATA = {}

PROCESS_DATA = []

def setLaunchData(data):
    global LAUNCH_DATA
    LAUNCH_DATA = data

def getLaunchData():
    global LAUNCH_DATA
    return LAUNCH_DATA
def setProcessData(data):
    global PROCESS_DATA
    PROCESS_DATA = data

def getProcessData():
    global PROCESS_DATA
    return PROCESS_DATA




