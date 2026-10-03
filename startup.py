## GENERAL IMPORTS FOR EVERY PY FILE

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import chess      # i want to use this for chess generation if possible
import pygame                 # Windows built-in support for playing WAV files
from pathlib import Path
# creating starting window https://www.youtube.com/watch?v=lyoyTlltFVU&list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T&index=1
pygame.mixer.init() # for sounds
pygame.init()
pygame.font.init()   # for fonts
import os  # file proper imports
import customtkinter as ctk
import hashlib

## IMPORTING OTHER PY FILE DATA

from chessboardmoves import mouse_click, draw_board


## MAIN CODE
## Chess board generation to use chess import (putting a chess board on the screen)

board = chess.Board()
BOARD_SIZE = 640
SQUARE_SIZE = BOARD_SIZE // 8
board = chess.Board()
selected_square = None

## function to start the game


def start(chesswindow, canvas, mouse_click, draw_board, piece_images):
    canvas.pack(pady=50)
    canvas.bind("<Button-1>", mouse_click)
    draw_board(canvas, piece_images)
    pygame.mixer.music.load(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "sounds",
            "game-start.mp3"
        )
    )
    pygame.mixer.music.play()
    chesswindow.mainloop()
    print("Created by DrFrostij")

