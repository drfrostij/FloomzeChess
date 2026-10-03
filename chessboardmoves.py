## GENERAL IMPORTS

from tkinter import *
import tkinter as tk
from tkinter import messagebox

import chess
import pygame

from pathlib import Path
import os


## SOUND SETUP

pygame.init()
pygame.mixer.init()
pygame.font.init()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUNDS_DIR = os.path.join(BASE_DIR, "sounds")


def play_sound(filename):

    sound_path = os.path.join(
        SOUNDS_DIR,
        filename
    )

    if os.path.exists(sound_path):
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
    else:
        print(f"Sound not found: {sound_path}")


## GAME VARIABLES

board = chess.Board()

BOARD_SIZE = 640
SQUARE_SIZE = BOARD_SIZE // 8

selected_square = None

game_window = None
game_canvas = None
game_piece_images = None


## SETUP GAME

def setup_game(chesswindow, canvas, piece_images):

    global game_window
    global game_canvas
    global game_piece_images

    game_window = chesswindow
    game_canvas = canvas
    game_piece_images = piece_images


## DRAW CHESS BOARD

def draw_board(canvas, piece_images):

    canvas.delete("all")

    # Draw squares
    for row in range(8):

        for col in range(8):

            if (row + col) % 2 == 0:
                colour = "#F0D9B5"
            else:
                colour = "#B58863"

            canvas.create_rectangle(
                col * SQUARE_SIZE,
                row * SQUARE_SIZE,
                (col + 1) * SQUARE_SIZE,
                (row + 1) * SQUARE_SIZE,
                fill=colour,
                outline=""
            )

    # Draw pieces
    for square in chess.SQUARES:

        piece = board.piece_at(square)

        if piece is not None:

            file = chess.square_file(square)
            rank = chess.square_rank(square)

            col = file
            row = 7 - rank

            x = (
                col * SQUARE_SIZE
                + SQUARE_SIZE // 2
            )

            y = (
                row * SQUARE_SIZE
                + SQUARE_SIZE // 2
            )

            canvas.create_image(
                x,
                y,
                image=piece_images[piece.symbol()]
            )


## CHECKMATE POPUP

def show_checkmate(winner):

    messagebox.showinfo(
        "Checkmate",
        f"{winner} wins by Checkmate!"
    )


## CONVERT MOUSE POSITION TO CHESS SQUARE

def square_from_mouse(event):

    col = event.x // SQUARE_SIZE
    row = event.y // SQUARE_SIZE

    rank = 7 - row
    file = col

    return chess.square(
        file,
        rank
    )


## MOUSE CLICK

def mouse_click(event):

    global selected_square

    # ------------------------------
    # CHECKMATE
    # ------------------------------

    if board.is_checkmate():

        winner = (
            "White"
            if board.turn == chess.BLACK
            else "Black"
        )

        print(
            "CHECKMATE",
            "Winner:",
            winner
        )

        play_sound("game-end.mp3")

        show_checkmate(winner)

        return


    # ------------------------------
    # STALEMATE
    # ------------------------------

    elif board.is_stalemate():

        print("STALEMATE - Draw")

        play_sound("game-end.mp3")

        return


    # ------------------------------
    # INSUFFICIENT MATERIAL
    # ------------------------------

    elif board.is_insufficient_material():

        print(
            "INSUFFICIENT MATERIAL - Draw"
        )

        play_sound("game-end.mp3")

        return


    # ------------------------------
    # GET CLICKED SQUARE
    # ------------------------------

    square = square_from_mouse(event)


    # ------------------------------
    # SELECT PIECE
    # ------------------------------

    if selected_square is None:

        piece = board.piece_at(square)

        if (
            piece is not None
            and piece.color == board.turn
        ):

            selected_square = square

            print(
                "Selected:",
                chess.square_name(square)
            )

        return


    # ------------------------------
    # GET SELECTED PIECE
    # ------------------------------

    piece = board.piece_at(
        selected_square
    )


    # ------------------------------
    # PROMOTION
    # ------------------------------

    if piece and piece.piece_type == chess.PAWN:

        rank = chess.square_rank(square)

        if rank == 0 or rank == 7:

            promotion_piece = promotion_popup(
                game_window
            )

            # User closed popup
            if promotion_piece is None:

                selected_square = None

                return

            move = chess.Move(
                selected_square,
                square,
                promotion=promotion_piece
            )

            if move in board.legal_moves:

                board.push(move)

                selected_square = None

                draw_board(
                    game_canvas,
                    game_piece_images
                )

                play_sound("promote.mp3")

                print(
                    "Promotion accepted"
                )

            else:

                selected_square = None

                print(
                    "Illegal promotion move"
                )

                play_sound(
                    "illegal.mp3"
                )

            return


    # ------------------------------
    # NORMAL MOVE
    # ------------------------------

    move = chess.Move(
        selected_square,
        square
    )


    # ------------------------------
    # LEGAL MOVE
    # ------------------------------

    if move in board.legal_moves:

        # Capture
        if board.is_capture(move):

            sound = "capture.mp3"

        # Castling
        elif board.is_castling(move):

            sound = "castle.mp3"

        # Normal move
        else:

            sound = "move-self.mp3"


        board.push(move)

        selected_square = None

        draw_board(
            game_canvas,
            game_piece_images
        )

        print("Move accepted")

        play_sound(sound)


    # ------------------------------
    # ILLEGAL MOVE
    # ------------------------------

    else:

        selected_square = None

        print("Illegal move")

        play_sound(
            "illegal.mp3"
        )


## PROMOTION POPUP

def promotion_popup(chesswindow):

    popup = tk.Toplevel(chesswindow)

    popup.title("Promote Pawn")
    popup.geometry("300x250")

    popup.transient(chesswindow)
    popup.grab_set()

    promotion_piece = [None]


    ## TITLE

    tk.Label(
        popup,
        text="Promote Pawn",
        font=("Helvetica", 20, "bold")
    ).pack(
        pady=10
    )


    ## CHOOSE PIECE

    def choose(piece):

        promotion_piece[0] = piece

        popup.destroy()


    ## QUEEN

    tk.Button(
        popup,
        text="Queen",
        font=("Helvetica", 14),
        command=lambda: choose(
            chess.QUEEN
        )
    ).pack(
        fill="x",
        padx=40,
        pady=5
    )


    ## ROOK

    tk.Button(
        popup,
        text="Rook",
        font=("Helvetica", 14),
        command=lambda: choose(
            chess.ROOK
        )
    ).pack(
        fill="x",
        padx=40,
        pady=5
    )


    ## BISHOP

    tk.Button(
        popup,
        text="Bishop",
        font=("Helvetica", 14),
        command=lambda: choose(
            chess.BISHOP
        )
    ).pack(
        fill="x",
        padx=40,
        pady=5
    )


    ## KNIGHT

    tk.Button(
        popup,
        text="Knight",
        font=("Helvetica", 14),
        command=lambda: choose(
            chess.KNIGHT
        )
    ).pack(
        fill="x",
        padx=40,
        pady=5
    )


    ## WAIT FOR POPUP

    chesswindow.wait_window(
        popup
    )

    return promotion_piece[0]