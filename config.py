from pathlib import Path
from typing import Any

from pydantic.dataclasses import dataclass
from pyfedappwrap.learning.run_runfig import AppConfig, AppInputConfig, AppOutputConfig


@dataclass
class MyAppConfig(AppConfig):
    data_num_species: int = 9606
    clustering_algorithm: str = "hierarchical"
    reps1: int = 5
    timepts: int = 9
    # network_path: str = "human"
    n_clusters: int = 10


@dataclass
class MyAppInputConfig(AppInputConfig):
    data: Any = None
    gene_ids: Any = None


@dataclass
class MyAppOutputConfig(AppOutputConfig):
    image: Path = None
