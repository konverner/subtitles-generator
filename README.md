## Multilingual Subtitles Generator

It allows to generate subtitles from a video or an audio and save it in `.srt` file. For now, 2 languages are available: English and German.

![](https://github.com/konverner/subtitles-generator/blob/main/diagram.png?raw=true)

## Get Started

Run the `main.py` passing the following arguments:

1) `lang` : language of speech in your video (`en` or `de`).
2) `input_path` : path to an audio (`.wav`) or a video (`.mp4`, `.avi`, `.webm`).
3) `output_path` (optional) : path to result .srt file.

e.g.

`python main.py de /episodes/king_of_the_hill_de.mp4`

.srt file with subtitles will be located in `output_path` if the optional argument was passed or in `input_path` with `.srt` extension otherwise.
