from torch import Tensor
from hw_asr.augmentations.base import AugmentationBase
from torchaudio import transforms


class FrequencyMasking(AugmentationBase):
    def __init__(self, *args, **kwargs):
        self._aug = transforms.FrequencyMasking(*args, **kwargs)

    def __call__(self, spectogram: Tensor):
        return self._aug(spectogram).squeeze(1)
