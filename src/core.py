import librosa
import torch
from tqdm import tqdm
import numpy as np
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor


class Wav2vec:
    def __init__(
            self,
            model_name: str
    ):
        self.model = Wav2Vec2ForCTC.from_pretrained(model_name)
        self.processor = Wav2Vec2Processor.from_pretrained(model_name)

    def get_features(
            self,
            path: str,
            chunk_size: int = 10,
            sampling_rate: int = 16000
    ):
        speech_array, sampling_rate = librosa.load(path, sr=sampling_rate)
        chunks = np.array_split(speech_array,
                                speech_array.shape[0] // (chunk_size * sampling_rate) + (
                                            speech_array.shape[0] % (chunk_size * sampling_rate) > 0))
        features = self.processor(chunks, sampling_rate=sampling_rate, return_tensors="pt", padding=True)
        return features

    def transcribe(
            self,
            audio_path: str,
            chunk_size: int = 10,
            sampling_rate: int = 16000,
            batch_size: int = 5
    ) -> list[str]:
        features = self.get_features(audio_path, chunk_size, sampling_rate)
        n = features.input_values.shape[0]

        with torch.no_grad():
            if n > batch_size:
                logits = []
                for i in tqdm(range(0, n - batch_size, batch_size)):
                    logits.append(
                        self.model(features.input_values[i:i + batch_size]).logits)
                logits = torch.cat(logits, axis=0)

            else:
                logits = self.model(features.input_values).logits

        predicted_ids = torch.argmax(logits, dim=-1)
        predicted_texts = self.processor.batch_decode(predicted_ids, clean_up_tokenization_spaces=False)
        return predicted_texts
