## GENERAL IMPORTS FOR EVERY PY FILE

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import chess
import pygame
from pathlib import Path
import os
import customtkinter as ctk
import hashlib


## PYGAME SETUP

pygame.mixer.init()
pygame.init()
pygame.font.init()


## IMPORTING OTHER PY FILE DATA

from chessboardmoves import mouse_click, draw_board, setup_game
from piecesimages import load_piece_images


## MAIN CODE
## Chess board generation

board = chess.Board()

BOARD_SIZE = 640
SQUARE_SIZE = BOARD_SIZE // 8

selected_square = None


## FILE PATHS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

icon_path = os.path.join(
    BASE_DIR,
    "icons",
    "chessicon.png"
)


## CREATING MAIN WINDOW

chesswindow = Tk()

icon = PhotoImage(file=icon_path)

chesswindow.geometry("1000x1000")
chesswindow.title("Floomze Chess")
chesswindow.iconphoto(True, icon)
chesswindow.config(background="#1d3b24")


## LOAD PIECES

piece_images = load_piece_images(chesswindow)


## CREATE CHESS CANVAS

canvas = Canvas(
    chesswindow,
    width=BOARD_SIZE,
    height=BOARD_SIZE
)

canvas.pack(pady=50)


## SETUP GAME

setup_game(
    chesswindow,
    canvas,
    piece_images
)


## DRAW INITIAL BOARD

draw_board(
    canvas,
    piece_images
)


## MOUSE CONTROLS

canvas.bind(
    "<Button-1>",
    mouse_click
)


## MENU BAR

menubar = Menu(chesswindow)

chesswindow.config(menu=menubar)


## EXIT MENU

exitbar = Menu(
    menubar,
    tearoff=0
)

menubar.add_cascade(
    label="Exit Area",
    menu=exitbar
)

exitbar.add_command(
    label="Exit",
    command=chesswindow.destroy
)


## CREDITS MENU

creditsbar = Menu(
    menubar,
    tearoff=0
)

menubar.add_cascade(
    label="Credits",
    menu=creditsbar
)

creditsbar.add_command(
    label="About",
    command=lambda: messagebox.showinfo(
        "About",
        "Floomze Chess\n\nCreated by DrFrostij"
    )
)


## RUN PROGRAM

print("Created by DrFrostij")

chesswindow.mainloop()