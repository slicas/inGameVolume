from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import pythoncom
import keyboard
import time

class Start:
    def __init__(self):
        self.running = False
    def start(self,app_name,volume,sec):
        timer = 0
        normal = True
        def set_volume(volume, app_name):
            sessions = AudioUtilities.GetAllSessions()

            for session in sessions:
                volume_interface = session._ctl.QueryInterface(ISimpleAudioVolume)
                if session.Process and session.Process.name() == app_name:
                    volume_interface.SetMasterVolume(volume, None)

        def on_key(event):
            nonlocal normal
            nonlocal timer
            timer = 0
            if normal == True:
                normal = False
                set_volume(volume,app_name)
            return True

        # Inicializar o ambiente COM
        pythoncom.CoInitialize()


        keyboard.on_press(on_key)
        while self.running:
            if keyboard.is_pressed('esc'):
                break
            else:
                time.sleep(1)
                if timer < sec:
                    timer += 1
                else:
                    if normal == False:
                        normal = True
                        set_volume(1,app_name)

        # Parar a detecção de teclas
        keyboard.unhook_all()

