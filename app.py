from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt
import spycone as spy
from pyfedappwrap.engine.config.system_config import system_settings
from pyfedappwrap.learning.app_types import BaseSelfLearnedApp

from config import MyAppConfig, MyAppInputConfig, MyAppOutputConfig


class MyAPP(BaseSelfLearnedApp[MyAppConfig, MyAppInputConfig, MyAppOutputConfig]):
    """Main application class for Spycone analysis."""

    def __init__(self):
        super().__init__()

    def run_algorithm(self, data: MyAppInputConfig) -> MyAppOutputConfig:
        self.logger.info("Running prediction")
        genes = data.gene_ids.iloc[:, 0].tolist()
        flu_dset = spy.dataset(ts=data.data,
                               gene_id=genes,
                               symbs=genes,
                               species=self.config.data_num_species,
                               reps1=self.config.reps1,
                               timepts=self.config.timepts, )

        self.logger.info("Preprocessing data")
        spy.preprocess(flu_dset)
        self.logger.info("Initialized clustering")
        asclu = spy.clustering(
            flu_dset,
            algorithm=self.config.clustering_algorithm,  # hierarchical
            metrics="correlation",
            input_type="expression",
            n_clusters=self.config.n_clusters,
            composite=False,
        )
        self.logger.info("Running clustering")
        c = asclu.find_clusters()
        self.logger.info("Clustering completed")
        spy.vis_all_clusters(asclu, col_wrap=5)

        path = Path(system_settings.data_dir) / "outputgene_level_cluster_visualization.png"
        self.logger.info(f"Saving visualization")
        plt.savefig(str(path))
        return MyAppOutputConfig(image=path)

    def get_test_data(self) -> Optional[dict[str, Path]]:
        return {"data": Path("data/flu_ts.csv"),
                "gene_ids": Path("data/gene_list.csv")}
