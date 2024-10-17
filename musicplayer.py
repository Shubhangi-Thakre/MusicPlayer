# Music Player

from tkinter import *
import pygame
import os

# Defining the AudioPlayer class
class AudioPlayer:
    def __init__(self, root):
        self.root = root
        # Title of the window
        self.root.title("AudioPlayer")
        # Window Geometry
        self.root.geometry("900x250+200+150")
        # Initiating Pygame
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring song_title variable
        self.song_title = StringVar()
        # Declaring play_status variable
        self.play_status = StringVar()

        # Creating the frame for song title & status display
        display_frame = LabelFrame(self.root, text="Now Playing", font=("Helvetica", 14, "bold"), bg="SlateBlue", fg="white", bd=5, relief=RIDGE)
        display_frame.place(x=0, y=0, width=550, height=100)
        # Song Title Label
        song_title_lbl = Label(display_frame, textvariable=self.song_title, width=25, font=("Helvetica", 18, "bold"), bg="LightSteelBlue", fg="white").grid(row=0, column=0, padx=10, pady=10)
        # Play Status Label
        status_lbl = Label(display_frame, textvariable=self.play_status, font=("Helvetica", 18, "bold"), bg="LightSteelBlue", fg="white").grid(row=0, column=1, padx=10, pady=10)

        # Creating Control Buttons Frame
        control_frame = LabelFrame(self.root, text="Controls", font=("Helvetica", 14, "bold"), bg="DimGrey", fg="white", bd=5, relief=RIDGE)
        control_frame.place(x=0, y=100, width=550, height=150)
        # Play Button
        play_btn = Button(control_frame, text="PLAY", command=self.play_song, width=10, height=1, font=("Helvetica", 14, "bold"), fg="DarkBlue", bg="LightCoral").grid(row=0, column=0, padx=10, pady=10)
        # Pause Button
        pause_btn = Button(control_frame, text="PAUSE", command=self.pause_song, width=8, height=1, font=("Helvetica", 14, "bold"), fg="DarkBlue", bg="LightCoral").grid(row=0, column=1, padx=10, pady=10)
        # Resume Button
        resume_btn = Button(control_frame, text="RESUME", command=self.resume_song, width=10, height=1, font=("Helvetica", 14, "bold"), fg="DarkBlue", bg="LightCoral").grid(row=0, column=2, padx=10, pady=10)
        # Stop Button
        stop_btn = Button(control_frame, text="STOP", command=self.stop_song, width=10, height=1, font=("Helvetica", 14, "bold"), fg="DarkBlue", bg="LightCoral").grid(row=0, column=3, padx=10, pady=10)

        # Creating Playlist Frame
        playlist_frame = LabelFrame(self.root, text="Playlist", font=("Helvetica", 14, "bold"), bg="DimGrey", fg="white", bd=5, relief=RIDGE)
        playlist_frame.place(x=550, y=0, width=350, height=250)
        # Scrollbar
        scroll_y = Scrollbar(playlist_frame, orient=VERTICAL)
        # Playlist Listbox
        self.playlist = Listbox(playlist_frame, yscrollcommand=scroll_y.set, selectbackground="LightGreen", selectmode=SINGLE, font=("Helvetica", 12, "bold"), bg="SlateGray", fg="White", bd=5, relief=RIDGE)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

        # Change Directory to your music folder
        os.chdir("E:/music")
        # Fetch Songs
        song_list = os.listdir()
        # Insert Songs into Playlist
        for song in song_list:
            self.playlist.insert(END, song)

    def play_song(self):
        # Display selected song title
        self.song_title.set(self.playlist.get(ACTIVE))
        # Display play status
        self.play_status.set("Playing")
        # Load and play song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

    def stop_song(self):
        # Display stop status
        self.play_status.set("Stopped")
        # Stop song
        pygame.mixer.music.stop()

    def pause_song(self):
        # Display pause status
        self.play_status.set("Paused")
        # Pause song
        pygame.mixer.music.pause()

    def resume_song(self):
        # Display playing status
        self.play_status.set("Playing")
        # Resume song
        pygame.mixer.music.unpause()


# Creating Tkinter window
root = Tk()
# Passing Root to AudioPlayer Class
app = AudioPlayer(root)
# Running the app
root.mainloop()



