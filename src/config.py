MODEL_NAMES = {'large': "openai/whisper-large-v2",
               'medium': 'openai/whisper-medium',
               'base': 'openai/whisper-base'}

SAMPLING_RATE = 16000
CHUNK_SIZE = 2  # a size in seconds of one piece of audio used for one subtitles frame
BATCH_SIZE = 30  # how many chunks are passed to a model at once
LIKELIHOOD_TRESHOLD = 0.5  # threshold value for eliminating phrases that contains out-of-dictionary words

SUPPORTED_LANGS = {'english', 'german', 'french'}
SUPPORTED_FORMATS = {'.wav', '.mp4', '.avi', '.webm'}
