from pathlib import Path

MODEL_NAME = "jonatasgrosman/wav2vec2-large-xlsr-53-german"
SAMPLING_RATE = 16000
CHUNK_SIZE = 10  # a size in seconds of one piece of audio used for one subtitles frame
BATCH_SIZE = 5  # how many chunks are passed to a model at once
