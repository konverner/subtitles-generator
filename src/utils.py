import datetime
import pathlib

import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import VideoFileClip


def extract_audio(input_path: pathlib.Path):

    if input_path.suffix == '.wav':
        return input_path

    print("extracting audio from video ...")
    video = VideoFileClip(str(input_path))
    audio_path = input_path.with_suffix('.wav')
    video.audio.write_audiofile(audio_path, logger=None)
    return audio_path


def create_srt(subtitles_path: pathlib.Path, texts: list, interval_size: int):

    if subtitles_path.suffix != '.srt':
        subtitles_path.rename(subtitles_path.with_suffix('.srt'))

    f = open(subtitles_path, 'w')
    timer = 0
    for i, text in enumerate(texts):
        start_time = str(datetime.timedelta(seconds=timer))+',000'
        end_time = str(datetime.timedelta(seconds=timer+interval_size))+',000'
        frame = f'{i+1}\n{start_time} -->  {end_time}\n{text}\n\n'
        f.write(frame)
        timer += interval_size
    print(f'{i} subtitle frames are recorded')
    f.close()
