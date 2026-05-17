import pytest
from unittest.mock import Mock, patch
import pygame

from src import main
from src import start_screen
from src import instructions_screen
from src import base_dino
from src import scrolling_background
from src import scoreboard


def test_start_screen(mock_load, mock_display):
    display = start_screen.Display()
    assert isinstance(display.start_button)
    assert display.screen_size == (800, 600)

def test_background(mock_dispay, mock_load):

    mock_load.return_value = Mock()
    game = scrolling_background.Game()
    bg = scrolling_background(x=0) #Intializing background object x= 0
    speed = 5.0 #testing background movement

def test_scoreboard():

    mock_screen = Mock()
    mock_font = Mock()
    scoreboard.draw_score_counter(100, mock_font, mock_screen)
    assert mock_screen.blit.called
    assert scoreboard.meter_moved == 5.0 # tracking absolute distance

def test_base_dino_exist(mock_display):
    assert callable(base_dino.run_game)