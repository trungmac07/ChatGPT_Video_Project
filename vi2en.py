from multiprocessing import shared_memory
import subprocess
import time

class Vi2En():
    def __init__(self, command=["translate_vietnamese/translate_vietnamese.exe", "--input=original_vietnamese", "--output=translated_vietnamese", "--wait=5", "--errorsharedmemory=translation_error", "--errorlog=translation_error_log.txt"]):
        self.command = command

        self.input_path = ""
        self.output_path = ""
        self.error_shm_name = ""
        self.error_log_path = ""
        self.wait = -1

        args = command[1:]

        for arg in args:
            if arg[0] == "-" and arg[1] == "-": # is a command
                cmd = arg[2:].lower()
                if "input" == cmd[0:5]:
                    self.input_path = cmd[6:]
                if "output" == cmd[0:6]:
                    self.output_path = cmd[7:]
                if "wait" == cmd[0:4]:
                    self.wait = int(cmd[5:])
                if "errorsharedmemory" == cmd[0:17]:
                    self.error_shm_name = cmd[18:]
                if "errorlog" == cmd[0:8]:
                    self.error_log_path = cmd[9:]

    def translateVi2En(self, text, timeout=15):
        translated_text = ""
        error_text = ""
        shm_list = []

        encoded_text = text.encode('utf-8')
        encoded_text_size = len(encoded_text)

        shm = shared_memory.SharedMemory(name=self.input_path, create=True, size=encoded_text_size)
        shm.buf[:encoded_text_size] = encoded_text

        shm_list.append(shm)

        subprocess.Popen(self.command)

        start_time = time.time()

        while True:
            if time.time() - start_time >= timeout:
                raise Exception(f"Processing time has exceeded {timeout}.")
            else:
                try:
                    tv_shm = shared_memory.SharedMemory(name=self.output_path)
                    translated_text = tv_shm.buf.tobytes().decode('utf-8')

                    translated_text = translated_text.rstrip('\x00')

                    shm_list.append(tv_shm)

                except Exception as e:
                    try:
                        e_shm = shared_memory.SharedMemory(name=self.error_shm_name)
                        error_text = e_shm.buf.tobytes().decode('utf-8')

                        error_text = error_text.rstrip('\x00')

                        shm_list.append(e_shm)

                    except Exception as e:
                        continue
            
            break

        # Close and release shared memory when done
        for shm in shm_list:
            shm.close()
            shm.unlink()

        return True, translated_text if translated_text != "" else False, error_text