# spycone

Analyzes time-course expression and splicing patterns with Spycone and exports clusters and plots.

## Runtime inputs

Supply input files according to the schemas in `app.yml`.

## Inputs and outputs

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `data` | CSV | time series data values with columns as each sample e.g. the order of the columns should be sample1_rep1, sample1_rep2, sample2_rep1, sample2_rep2 and so on…. |
| `gene_ids` | CSV | list of gene id (can be entrez gene id or ensembl gene id) |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `image` | IMAGE |  |

## Configuration

| Name | Default | Description |
| --- | --- | --- |
| `data_num_species` | `9606` | specify the species ID |
| `clustering_algorithm` | `hierarchical` | Type of clustering algorithm to use |
| `reps1` | `5` | Number of replicates |
| `timepts` | `9` | Number of time points |
| `n_clusters` | `10` | Number of cluster |

## Development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
# Set APP_ID and platform URLs before connecting.
python main.py
```

The Docker base image provides the FL-Net API. `requirements.txt` lists additional
runtime dependencies; `requirements-dev.txt` includes the API for local development.
Runtime datasets and trained models must be supplied separately; see `data/README.md`.

Build with `docker build -t tool-spycone .`.
