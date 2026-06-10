from pydantic import BaseModel
import json
import hashlib


class IrisFlower(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

    def to_list(self):

        return [
            self.SepalLengthCm,
            self.SepalWidthCm,
            self.PetalLengthCm,
            self.PetalWidthCm,
        ]

    def cache_key(self):

        raw = json.dumps(self.model_dump(), sort_keys=True)
        return f"Predict: {hashlib.sha256(raw.encode()).hexdigest()}"
