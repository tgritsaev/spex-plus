from src.base.base_metric import BaseMetric
from torchmetrics.audio import ScaleInvariantSignalDistortionRatio


class SISDRMetric(BaseMetric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.metric = ScaleInvariantSignalDistortionRatio()

    def __call__(self, s1, target_wav, **kwargs):
        return self.metric.to(s1.device)(s1, target_wav).item()


class SegmentedSISDRMetric(BaseMetric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.metric = ScaleInvariantSignalDistortionRatio()

    def __call__(self, segmented_s, cut_target_wav, **kwargs):
        return self.metric.to(segmented_s.device)(segmented_s, cut_target_wav).item()
