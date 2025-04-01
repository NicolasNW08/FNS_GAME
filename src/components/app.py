import customtkinter as ctk
from FRAME import FRAMES
from src.assets.constant import constants


class App(ctk.CTk):
    
    def __init__(self, frame_initial, *args, **kwargs, ):
        super().__init__(*args, **kwargs)

        self.title("F*king Numbers")
        self.iconbitmap("src/assets/img/icon.ico")
        self.geometry("{}x{}+{}+{}".format(
            constants.WIDTH, constants.HEIGHT,
            int((self.winfo_screenwidth() - constants.WIDTH) / 2),
            int((self.winfo_screenheight() - constants.HEIGHT) / 2 - 30)
        ))
        self.resizable(False, False)
        
        

        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for name, frame_class in FRAMES.items():
            frame = frame_class(container, self)
            self.frames[name] = frame
        
        self.show_frame(frame_initial)

    def show_frame(self, container):
        # Handle both string and class references
        if isinstance(container, str):
            frame = self.frames[container]
        else:
            frame = self.frames[container.__name__]
        frame.tkraise()



