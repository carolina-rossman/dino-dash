import pytest
from unittest.mock import Mock, patch
import pygame

import main
import start_screen
import instructions_screen
import base_dino
import scrolling_background
import scoreboard
import powers_screen
import death_screen
import game

@patch('pygame.display.set_mode')
@patch('pygame.image.load')
def test_start_screen(mock_load, mock_display):
    #testing to see if start screen work without crashing
    mock_load.return_value = pygame.Surface((800, 600))
    mock_display.return_value = Mock()

    display = start_screen.Display()
    assert isinstance(display.start_button, pygame.Rect)
    assert display.screen_size == (800, 600)

@patch('pygame.display.set_mode')
@patch('pygame.image.load')
def test_instructions_screen(mock_load, mock_display):
    #testing to see if instruction works poperly and imports layout work 
    mock_load.return_value = pygame.Surface((800, 600))
    mock_display.return_value = Mock()

    display = instructions_screen.Display()
    assert isinstance(display.start_button, pygame.Rect)
    assert display.screen_size == (800, 600)

@patch('pygame.display.set_mode')
@patch('pygame.image.load')
def test_power_screen(mock_load, mock_display):
    mock_load.return_value = pygame.Surface((800, 600))
    mock_display.return_value = Mock()

    display = powers_screen.Display()
    assert isinstance(display.quit_button, pygame.Rect)
    assert display.screen_size == (800,600)

@patch('pygame.display.set_mode')
@patch('pygame.image.load')
def test_scrolling_background(mock_load, mock_display):
#testing background making sure it scrolls properly
    mock_load.return_value = pygame.Surface((623, 150))#from chatgpt
    mock_display.return_value = Mock()#from chatgpt
    # game = scrolling_background.Game()
    # bg = scrolling_background(x=0) #Intializing background object x= 0
    # speed = 5.0 #testing background movement

    game_bg = scrolling_background.Game()
    assert len(game_bg.bg) == 2 #from chatgpt 

@patch('pygame.display.set_mode') #this code is from chaptgpt
@patch('pygame.freetype.SysFont') #this code is from chaptgpt
def test_death_screen(mock_font, mock_display): #this code is from chaptgpt
    mock_window = Mock()
    mock_window.get_size.return_value = (800, 600)
    mock_display.return_value = mock_window

    mock_font_instance = Mock()#from chatgpt
    mock_font_instance.render.return_value = (pygame.Surface((100, 50)), (0,0,100, 50)) # from chatgpt
    mock_font.return_value = mock_font_instance #from chatgpt

    display = death_screen.Display() #this code is from chaptgpt
    assert isinstance(display.restart_button, pygame.Rect) #this code is from chaptgpt
    assert display.red == [128, 0, 0]#this code is from chaptgpt

@patch('pygame.display.set_mode')
@patch('pygame.image.load')
def test_game_obstacles(mock_load, mock_display):
# verify game.py can spawn ostacles and randomizes
    mock_load.return_value = pygame.Surface((50, 50))
    mock_display.return_value = Mock()
    obstacle_item = game.Obstacles(800, 150)
    assert obstacle_item.speed == 5
    assert hasattr(obstacle_item, 'rect')

def test_scoreboard():
# testing the scoreboard 
    mock_screen = Mock()
    mock_font = Mock()
    scoreboard.draw_score_counter(100, mock_screen, mock_font)
    assert mock_screen.blit.called
    # assert scoreboard.meter_moved == 5.0 # tracking absolute distance

# @patch('pygame.display.set_mode')    
def test_main_callable():
    assert callable(main.main)
    