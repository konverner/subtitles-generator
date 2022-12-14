import argparse

from pathlib import Path
from spellchecker import SpellChecker

from src.core import Wav2vec
from src.utils import create_srt, extract_audio, text_likelihood
from src.config import MODEL_NAMES, CHUNK_SIZE, BATCH_SIZE, SAMPLING_RATE, \
                       SUPPORTED_LANGS, SUPPORTED_FORMATS, LIKELIHOOD_TRESHOLD


def parse_args():
    parser = argparse.ArgumentParser(description='It creates subtitles from a video or an audio')

    parser.add_argument('lang', type=str,
                        help='language of speech in an audio or video')
    parser.add_argument('input_file', type=str,
                        help='path to an audio or video file')
    parser.add_argument('--output_file', type=str,
                        help='path to a result file with subtitles')

    # Sanity checks
    args = parser.parse_args()
    lang = args.lang
    input_file = Path(args.input_file)

    try:
        output_file = Path(args.output_file)
    except:
        output_file = input_file.parents[0] / (input_file.stem + '.srt')

    if lang not in SUPPORTED_LANGS:
        raise ValueError(f'Language {lang} is not supported. Supported languages are {SUPPORTED_LANGS}')
    if not input_file.is_file():
        raise(OSError(f"Input file {input_file} does not exists"))
    if input_file.suffix not in SUPPORTED_FORMATS:
        raise ValueError('A file must be a video (mp4, avi, webm) or an audio (wav)')

    return input_file, output_file, lang


def main():
    input_file, output_file, lang = parse_args()

    if input_file.suffix in {'.mp4', '.avi', '.webm'}:
        input_file = extract_audio(input_file)

    model = Wav2vec(MODEL_NAMES[lang])
    print("transcribing audio ...")
    predicted_texts = model.transcribe(
        audio_path=input_file,
        sampling_rate=SAMPLING_RATE,
        batch_size=BATCH_SIZE,
        chunk_size=CHUNK_SIZE
    )

    # remove transcriptions that are not likely to be true
    # such transcriptions are usually generated from non-speech content (e.g. music)

    dictionary = SpellChecker(language=lang)
    for i in range(len(predicted_texts)):
        if text_likelihood(predicted_texts[i], dictionary) < LIKELIHOOD_TRESHOLD:
            predicted_texts[i] = None

    print(f"writing subtitles into {output_file} ...")
    create_srt(output_file, predicted_texts, CHUNK_SIZE)


if __name__ == '__main__':
    main()
