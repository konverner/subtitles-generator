from pathlib import Path

MODEL_NAMES = {'de': "jonatasgrosman/wav2vec2-large-xlsr-53-german",
               'eng': 'facebook/wav2vec2-base-960h'}

SAMPLING_RATE = 16000
CHUNK_SIZE = 6  # a size in seconds of one piece of audio used for one subtitles frame
BATCH_SIZE = 5  # how many chunks are passed to a model at once

SUPPORTED_LANGS = {'eng', 'de'}
SUPPORTED_FORMATS = {'.wav', '.mp4', '.avi', '.webm'}
