import pygame
import random
pygame.init()

_songs = ['song_1.mp3', 'song_2.mp3', 'song_3.mp3']
done = False
screen = pygame.display.set_mode((300, 300))
_currently_playing_song = _songs[0]
_previously_played_song = None
key_states = {
    pygame.K_SPACE: False,
    pygame.K_RIGHT: False,
    pygame.K_LEFT: False,
    pygame.K_s: False
}

def play_next_song():
    global _currently_playing_song, _songs, _previously_played_song
    index = _songs.index(_currently_playing_song)
    next_index = (index + 1) % len(_songs) 
    next_song = _songs[next_index]
    _previously_played_song = _currently_playing_song  
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()
def play_previous_song():
    global _currently_playing_song, _songs, _previously_played_song
    index = _songs.index(_currently_playing_song)
    prev_index = (index - 1) % len(_songs)  
    prev_song = _songs[prev_index]
    _previously_played_song = _currently_playing_song  
    _currently_playing_song = prev_song
    pygame.mixer.music.load(prev_song)
    pygame.mixer.music.play()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_SPACE] and not key_states[pygame.K_SPACE]: 
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(_currently_playing_song)
            pygame.mixer.music.play(-1)
        key_states[pygame.K_SPACE] = True
    elif not pressed[pygame.K_SPACE]:
        key_states[pygame.K_SPACE] = False

    if pressed[pygame.K_RIGHT] and not key_states[pygame.K_RIGHT]:
        play_next_song()
        key_states[pygame.K_RIGHT] = True
    elif not pressed[pygame.K_RIGHT]:
        key_states[pygame.K_RIGHT] = False

    if pressed[pygame.K_LEFT] and not key_states[pygame.K_LEFT]:
        play_previous_song()
        key_states[pygame.K_LEFT] = True
    elif not pressed[pygame.K_LEFT]:
        key_states[pygame.K_LEFT] = False

    if pressed[pygame.K_s] and not key_states[pygame.K_s]:
        pygame.mixer.music.stop()
        key_states[pygame.K_s] = True
    elif not pressed[pygame.K_s]:
        key_states[pygame.K_s] = False

