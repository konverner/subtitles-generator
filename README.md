## Multilingual Subtitles Generator

It allows to generate subtitles from a video or an audio and save it in `.srt` file. For now, 3 languages are available: English, French and German.

## Get Started

The script can run on CPU or GPU. It is recommended to use base or medium models to run the script on CPU. Besides, one can use Google Colab (see [notebook](https://github.com/konverner/subtitles-generator/blob/main/subtitles_generator.ipynb)).

Run the `main.py` passing the following arguments:

1) `model_size` (optional) : size of model to use (`large`, `medium`, `base`)
2) `lang` : language of speech in your video (`english`, `german`, 'french').
3) `input_path` : path to an audio (`.wav`) or a video (`.mp4`, `.avi`, `.webm`).
4) `output_path` (optional) : path to result .srt file.

e.g.

`!python main.py large german /content/test.mp4`

.srt file with subtitles will be located in `output_path` if the optional argument was passed or in `input_path` with `.srt` extension otherwise.
