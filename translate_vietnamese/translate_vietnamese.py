import os
import sys
from multiprocessing import shared_memory
import time
from googletrans import Translator


# Command line arguments
# translate_vietnamese.exe
# --input=original_vietnamese/input.txt
# --output=translated_vietnamese/output.txt
# --wait=10
# --errorsharedmemory=translation_error
# --errorlog=translation_error_log.txt


# ---------------------------------------------------- Functions ----------------------------------------------------
def writeErrorLog(file_path, error):
    current_time = time.strftime("%Y/%m/%d %H:%M:%S")
    with open(file_path, 'a') as error_file:
        error_file.write(f'{current_time}: {error}\n')

def getCommandLineArguments(default_error_log_path):
    if len(sys.argv) >= 4:
        input_path = ""
        output_path = ""
        error_shm_name = ""
        error_log_path = ""
        wait = -1

        args = sys.argv[1:]

        for arg in args:
            if arg[0] == "-" and arg[1] == "-": # is a command
                cmd = arg[2:].lower()
                if "input" == cmd[0:5]:
                    input_path = cmd[6:]
                if "output" == cmd[0:6]:
                    output_path = cmd[7:]
                if "wait" == cmd[0:4]:
                    wait = int(cmd[5:])
                if "errorsharedmemory" == cmd[0:17]:
                    error_shm_name = cmd[18:]
                if "errorlog" == cmd[0:8]:
                    error_log_path = cmd[9:]

        if input_path == "":
            raise Exception("Invalid Syntax: Input path not found")
        if output_path == "":
            raise Exception("Invalid Syntax: Output path not found")
        if wait < 0:
            raise Exception("Invalid Syntax: Wait time must be a number equal or greater than 0")
        if error_log_path == "":
            error_log_path = default_error_log_path
        
        return input_path, output_path, wait, error_shm_name, error_log_path
    
    else:
        raise Exception("Invalid Syntax: Not enough arguments")

def getVietnameseText(input_path):
    if os.path.splitext(input_path)[1]:
        with open(input_path, "r", encoding="utf-8") as file:
            vietnamese_text = file.read()
        return vietnamese_text
    else:
        global shm_list

        shm = shared_memory.SharedMemory(name=input_path)
        vietnamese_text = shm.buf.tobytes().decode("utf-8")
        shm_list.append(shm)

        return vietnamese_text

def translateViToEn(text):
    translator = Translator()
    translated_text = translator.translate(text, src="vi", dest="en")
    return translated_text.text

def setSharedMemory(name, text):
    global shm_list

    encoded_text = text.encode("utf-8")
    encoded_text_size = len(encoded_text)

    shm = shared_memory.SharedMemory(name=name, create=True, size=encoded_text_size)
    shm.buf[:encoded_text_size] = encoded_text

    shm_list.append(shm)

def yieldTranslatedText(output_path, text):
    if os.path.splitext(output_path)[1]:
        current_time = time.strftime("%Y/%m/%d %H:%M:%S")
        with open(output_path, "a", encoding="utf-8") as output_file:
            output_file.write(f'{current_time}: {text}\n')

    else:
        setSharedMemory(name=output_path, text=text)

def closeSharedMemory():
    global shm_list

    for shm in shm_list:
        shm.close()
        shm.unlink()
# -------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------- Processing ----------------------------------------------------
DEFAULT_ERROR_LOG_PATH = 'translation_error_log.txt'

shm_list = []
error_shm_name = ""
error_log_path = DEFAULT_ERROR_LOG_PATH

try:
    input_path, output_path, wait, error_shm_name, error_log_path = getCommandLineArguments(default_error_log_path=DEFAULT_ERROR_LOG_PATH)

    vietnamese_text = getVietnameseText(input_path=input_path)
    
    translated_text = translateViToEn(vietnamese_text)

    yieldTranslatedText(output_path=output_path, text=translated_text)

    time.sleep(wait)

    closeSharedMemory()
except Exception as e:    
    error = str(e)

    writeErrorLog(file_path=error_log_path, error=error)

    try:
        if error_shm_name != "" and wait >= 0:
            setSharedMemory(name=error_shm_name, text=error)

            time.sleep(wait)
    except Exception as e:
        pass

    closeSharedMemory()
# -------------------------------------------------------------------------------------------------------------------