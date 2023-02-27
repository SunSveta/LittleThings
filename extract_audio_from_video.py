import moviepy.editor
from pathlib import Path

#Извлекает аудио дорожку из видео файла, сохраняет в мр3 с таким же названием

video_file = Path('cat.mp4')

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'{video_file.stem}.mp3')

