from maze_game import player, create_background, create_maze, create_ghost, get_barrier, display_text
import pytest

def test_player():
    assert player() == 'player'

def test_create_background():
    assert create_background(black) == 'black'

def test_create_maze():
    assert create_maze(blue) == 'blue'
    
def test_create_ghost():
    assert create_ghost(redImgUrl, orangeImgUrl, pinkImgUrl, tealImgUrl) == 'red'
    assert create_ghost(redImgUrl, orangeImgUrl, pinkImgUrl, tealImgUrl) == 'orange'
    assert create_ghost(redImgUrl, orangeImgUrl, pinkImgUrl, tealImgUrl) == 'pink'
    assert create_ghost(redImgUrl, orangeImgUrl, pinkImgUrl, tealImgUrl) == 'teal'

    # red = pygame.image.load(redImgUrl)
    # orange = pygame.image.load(orangeImgUrl)
    # pink = pygame.image.load(pinkImgUrl)
    # teal = pygame.image.load(tealImgUrl)

def test_get_barrier():
    assert get_barrier(playerX, playerY) == 'True'

def test_display_text():
    assert display_text('The Maze', title_font, orange, (screen_width/2), 50) == 'The Maze'
    assert display_text('You Did It!', cel_font, orange, (screen_width/2), (screen_height/2)) == 'You Did It!'

pytest.main(['-v', '--tb=line', '-rN', 'test_maze_game.py'])