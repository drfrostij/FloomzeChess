## GENERAL IMPORTS FOR EVERY PY FILE
from tkinter import *
import chess      # i want to use this for chess generation if possible
import os
from tkinter import PhotoImage

# The chess pieces to be used (PNGs)

def load_piece_images(chesswindow):   # chess pieces icons
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pieces_dir = os.path.join(base_dir, "pieces")
    return {
        "P": PhotoImage(
            file=os.path.join(pieces_dir, "wP.png"),
            master=chesswindow
        ),

        "N": PhotoImage(
            file=os.path.join(pieces_dir, "wN.png"),
            master=chesswindow
        ),

        "B": PhotoImage(
            file=os.path.join(pieces_dir, "wB.png"),
            master=chesswindow
        ),

        "R": PhotoImage(
            file=os.path.join(pieces_dir, "wR.png"),
            master=chesswindow
        ),

        "Q": PhotoImage(
            file=os.path.join(pieces_dir, "wQ.png"),
            master=chesswindow
        ),

        "K": PhotoImage(
            file=os.path.join(pieces_dir, "wK.png"),
            master=chesswindow
        ),

        "p": PhotoImage(
            file=os.path.join(pieces_dir, "bP.png"),
            master=chesswindow
        ),

        "n": PhotoImage(
            file=os.path.join(pieces_dir, "bN.png"),
            master=chesswindow
        ),

        "b": PhotoImage(
            file=os.path.join(pieces_dir, "bB.png"),
            master=chesswindow
        ),

        "r": PhotoImage(
            file=os.path.join(pieces_dir, "bR.png"),
            master=chesswindow
        ),

        "q": PhotoImage(
            file=os.path.join(pieces_dir, "bQ.png"),
            master=chesswindow
        ),

        "k": PhotoImage(
            file=os.path.join(pieces_dir, "bK.png"),
            master=chesswindow
        )
    }

## setting piece values for chess bot 

piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 1000
}

## other icons

def load_icons_images(chesswindow):   # chess pieces icons
    base_dir = os.path.dirname(os.path.abspath(__file__))  #this was taken as it kept on taking from the wrong file area
    pieces_dir = os.path.join(base_dir, "icons")

    return {
        "mainguiicon": PhotoImage(
            file=os.path.join(pieces_dir, "chessicon.png"),
            master=chesswindow
        ),
        "shopguiicon": PhotoImage(
            file=os.path.join(pieces_dir, "chessshopicon"),
            master=chesswindow
        ),
        "othericon1": PhotoImage(
            file=os.path.join(pieces_dir, "wB.png"),
            master=chesswindow
        ),
        "othericon2": PhotoImage(
            file=os.path.join(pieces_dir, "bK.png"),
            master=chesswindow
        )
    }