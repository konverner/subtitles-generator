import argparse

from pathlib import Path

from src.core import Wav2vec
from src.utils import create_srt, extract_audio
from src.config import MODEL_NAME, CHUNK_SIZE, BATCH_SIZE, SAMPLING_RATE


def parse_args():
    parser = argparse.ArgumentParser(description='It creates subtitles from a video or an audio')

    parser.add_argument('input_file', type=str,
                        help='path to an audio or video file')
    parser.add_argument('--output_file', type=str,
                        help='path to a result file with subtitles')

    # Sanity checks
    args = parser.parse_args()
    input_file = Path(args.input_file)

    try:
        output_file = Path(args.output_file)
    except:
        output_file = input_file.parents[0] / (input_file.stem + '.srt')

    if not input_file.is_file():
        raise(OSError(f"Input file {input_file} does not exists"))
    if input_file.suffix not in {'.wav', '.mp4', '.avi', '.webm'}:
        raise ValueError('A file must be a video (mp4, avi, webm) or an audio (wav)')

    return input_file, output_file


def main():
    input_file, output_file = parse_args()

    if input_file.suffix in {'.mp4', '.avi', '.webm'}:
        input_file = extract_audio(input_file)

    model = Wav2vec(MODEL_NAME)
    print("transcribing audio ...")
    predicted_texts = model.transcribe(
        audio_path=input_file,
        sampling_rate=SAMPLING_RATE,
        batch_size=BATCH_SIZE,
        chunk_size=CHUNK_SIZE
    )

    print(f"writing subtitles into {output_file} ...")
    create_srt(output_file, predicted_texts, CHUNK_SIZE)


if __name__ == '__main__':
    main()
