import os
import argparse
import logging
import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import hydra
from omegaconf import DictConfig

from src.core import Model
from src.utils import create_srt, extract_audio
from src.config import MODEL_NAMES, CHUNK_SIZE, BATCH_SIZE, SAMPLING_RATE, \
                       SUPPORTED_LANGS, SUPPORTED_FORMATS, LIKELIHOOD_TRESHOLD


logger = logging.getLogger(__name__)


def parse_args(config_path):
    cfg = compose(parsed.name, overrides=args.overrides)
    parser = argparse.ArgumentParser(
      description='It creates subtitles from a video or an audio'
    )

    parser.add_argument('--model_size', type=str, default='medium',
                        help='model size')
    parser.add_argument('--lang', type=str, default='english',
                        help='language of speech in an audio or video: english, german, french')
    parser.add_argument('--input_file', type=str, required=True,
                        help='path to an audio or video file')
    parser.add_argument('--output_file', type=str,
                        help='path to a result file with subtitles')

    args = parser.parse_args()
    lang = args.lang
    input_file = Path(args.input_file)
    model_size = args.model_size

    # Sanity checks
    try:
        output_file = Path(args.output_file)
    except:
        output_file = input_file.parents[0] / (input_file.stem + '.srt')

    if lang not in cfg.supported_languages:
        raise ValueError(
          f"Language {lang} is not supported. Supported languages are {cfg.supported_languages}"
        )
    
    if not input_file.is_file():
        raise(OSError(f"Input file {input_file} does not exists"))
    
    if input_file.suffix not in cfg.supported_media_formats.video or \
       input_file.suffix not in cfg.supported_media_formats.audio:
        raise ValueError(
          f"""A file must be a video: {cfg.supported_media_formats.video}
          or an audio {cfg.supported_media_formats.audio}"""
        )

    return input_file, output_file, lang, model_size


@hydra.main(version_base=None, config_path="src/conf", config_name="config")
def app(input_file, output_file, lang, model_size, cfg: DictConfig) -> None:
  

  # if an input is video then we extract the audio from it
  if input_file.suffix in cfg.supported_media_formats.video:
      logger.info("Extracting audio ...")
      input_file = extract_audio(input_file)

  model = Model(cnf.model_names[model_size], lang)
  logger.info("Generating subtitles ...")
  predicted_texts = model.transcribe(
      audio_path=input_file,
      sampling_rate=cfg.processing.sampling_rate,
      chunk_size=cfg.processing.chunk_size
  )

  logger.info(f"Writing subtitles into {output_file} ...")
  create_srt(output_file, predicted_texts, CHUNK_SIZE)
  os.remove(input_file)


if __name__ == '__main__':
  input_file, output_file, lang, model_size = parse_args()
  app(input_file, output_file, lang, model_size)

