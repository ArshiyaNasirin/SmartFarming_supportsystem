from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from src.config import DATASET_FILE, RANDOM_STATE, RECORD_ID_COLUMN, TARGET_COLUMN
from src.crop_profiles import CROP_PROFILES, REGION_STATE_MAP
from src.schema import FEATURE_COLUMNS


def _sample_numeric(rng: np.random.Generator, bounds: tuple[float, float], precision: int = 1) -> float:
    low, high = bounds
    midpoint = (low + high) / 2.0
    span = max(high - low, 1.0)
    sigma = span / 4.8
    lower_bound = low - (span * 0.18)
    upper_bound = high + (span * 0.18)
    value = float(rng.normal(midpoint, sigma))
    value = min(max(value, lower_bound), upper_bound)
    return round(value, precision)


def _choose_state(rng: np.random.Generator, region: str) -> str:
    return str(rng.choice(REGION_STATE_MAP[region]))


def generate_dataset(records_per_crop: int = 120, random_state: int = RANDOM_STATE) -> pd.DataFrame:
    rng = np.random.default_rng(random_state)
    rows: list[dict[str, object]] = []
    record_counter = 1

    for crop_name, profile in CROP_PROFILES.items():
        for _ in range(records_per_crop):
            region = str(rng.choice(profile.regions))
            row = {
                RECORD_ID_COLUMN: f"SF-{record_counter:05d}",
                "nitrogen_kg_ha": _sample_numeric(rng, profile.nitrogen),
                "phosphorus_kg_ha": _sample_numeric(rng, profile.phosphorus),
                "potassium_kg_ha": _sample_numeric(rng, profile.potassium),
                "temperature_c": _sample_numeric(rng, profile.temperature),
                "humidity_pct": _sample_numeric(rng, profile.humidity),
                "soil_ph": _sample_numeric(rng, profile.soil_ph),
                "rainfall_mm": _sample_numeric(rng, profile.rainfall),
                "soil_moisture_pct": _sample_numeric(rng, profile.soil_moisture),
                "organic_matter_pct": _sample_numeric(rng, profile.organic_matter, precision=2),
                "sunlight_hours": _sample_numeric(rng, profile.sunlight_hours, precision=1),
                "altitude_m": _sample_numeric(rng, profile.altitude, precision=0),
                "soil_type": str(rng.choice(profile.soil_types)),
                "region": region,
                "state": _choose_state(rng, region),
                "season": str(rng.choice(profile.seasons)),
                "irrigation_method": str(rng.choice(profile.irrigation_methods)),
                TARGET_COLUMN: crop_name,
            }
            rows.append(row)
            record_counter += 1

    frame = pd.DataFrame(rows)
    frame = frame.sample(frac=1.0, random_state=random_state).reset_index(drop=True)
    ordered_columns = [RECORD_ID_COLUMN] + FEATURE_COLUMNS + [TARGET_COLUMN]
    return frame[ordered_columns]


def save_dataset(path: Path = DATASET_FILE, records_per_crop: int = 120, random_state: int = RANDOM_STATE) -> pd.DataFrame:
    path.parent.mkdir(parents=True, exist_ok=True)
    dataset = generate_dataset(records_per_crop=records_per_crop, random_state=random_state)
    dataset.to_csv(path, index=False, float_format="%.2f")
    return dataset


def load_dataset(path: Path = DATASET_FILE) -> pd.DataFrame:
    return pd.read_csv(path)
