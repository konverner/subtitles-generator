import numpy as np
import torch
import librosa
from tqdm import tqdm
from transformers import WhisperProcessor, WhisperForConditionalGeneration


class Model:
    def __init__(
            self,
            model_name: str,
            lang: str
    ):
        self.model = WhisperForConditionalGeneration.from_pretrained(model_name)
        self.processor = WhisperProcessor.from_pretrained(model_name)
        self.forced_decoder_ids = self.processor.get_decoder_prompt_ids(
          language=lang, task="transcribe")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def get_features(
            self,
            path: str,
            chunk_size: int = 4,
            sampling_rate: int = 16000
    ):
        speech_array, sampling_rate = librosa.load(path, sr=sampling_rate)
        chunks = np.array_split(speech_array,
                                speech_array.shape[0] // (chunk_size * sampling_rate) + (
                                            speech_array.shape[0] % (chunk_size * sampling_rate) > 0))
        input_features_chunks = [
            self.processor(
                chunk, sampling_rate=sampling_rate, return_tensors="pt"
                ).input_features
            for chunk in chunks
        ]

        input_features_chunks = []
        for chunk in chunks:
            input_features_chunks.append(
              self.processor(
                  chunk, sampling_rate=sampling_rate, return_tensors="pt").input_features
            )
        return input_features_chunks


    def transcribe(
            self,
            audio_path: str,
            chunk_size: int = 4,
            sampling_rate: int = 16000,
    ) -> list[str]:
        input_features_chunks = self.get_features(audio_path, chunk_size, sampling_rate)
        transcriptions = []
        n = len(input_features_chunks)
        for i in tqdm(range(0, n, 4)):
            predicted_ids = self.model.generate(
              torch.concat(input_features_chunks[i:i+4]).to(self.device),
                forced_decoder_ids=self.forced_decoder_ids
            )
            transcription = self.processor.batch_decode(
              predicted_ids, skip_special_tokens=True
            )
            transcriptions.extend(transcription)

        return transcriptions
