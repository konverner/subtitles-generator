## Multilingual Subtitles Generator

It allows to generate subtitles from a video or an audio and save it in `.srt` file. For now, 99 languages are available including all major language such as English, Mandarin, Spanich, etc.

## Get Started

The script can be run on CPU or GPU. It is recommended to use base or medium models to run the script on CPU. Besides, one can use Google Colab (see [notebook](https://github.com/konverner/subtitles-generator/blob/main/subtitles_generator.ipynb)).

Run the `main.py` passing the following arguments:

1) `model_size` (optional) : size of model to use (`large`, `medium`, `base`), larger the model is, better the quality would be
2) `lang` : language of speech in your video (e.g. `english`, `german`, `french`, see the list below).
3) `input_path` : path to an audio (`.wav`) or a video (`.mp4`, `.avi`, `.webm`).
4) `output_path` (optional) : path to result .srt file.

e.g.

`!python main.py large german /content/test.mp4`

`.srt` file with subtitles will be located in `output_path` if the optional argument was passed or in `input_path` with `.srt` extension otherwise.

The list of supported languages:

```
"english",
"chinese",
"german",
"spanish",
"russian",
"korean",
"french",
"japanese",
"portuguese",
"turkish",
"polish",
"catalan",
"dutch",
"arabic",
"swedish",
"italian",
"indonesian",
"hindi",
"finnish",
"vietnamese",
"hebrew",
"ukrainian",
"greek",
"malay",
"czech",
"romanian",
"danish",
"hungarian",
"tamil",
"norwegian",
"thai",
"urdu",
"croatian",
"bulgarian",
"lithuanian",
"latin",
"maori",
"malayalam",
"welsh",
"slovak",
"telugu",
"persian",
"latvian",
"bengali",
"serbian",
"azerbaijani",
"slovenian",
"kannada",
"estonian",
"macedonian",
"breton",
"basque",
"icelandic",
"armenian",
"nepali",
"mongolian",
"bosnian",
"kazakh",
"albanian",
"swahili",
"galician",
"marathi",
"punjabi",
"sinhala",
"khmer",
"shona",
"yoruba",
"somali",
"afrikaans",
"occitan",
"georgian",
"belarusian",
"tajik",
"sindhi",
"gujarati",
"amharic",
"yiddish",
"lao",
"uzbek",
"faroese",
creole",
"pashto",
"turkmen",
"nynorsk",
"maltese",
"sanskrit",
"luxembourgish",
"myanmar",
"tibetan",
"tagalog",
"malagasy",
"assamese",
"tatar",
"hawaiian",
"lingala",
"hausa",
"bashkir",
"javanese",
"sundanese"
```
