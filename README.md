# Part 2: RFM Segmentation & Retention Strategy

RFM-based customer segmentation for a D2C personal care brand. Segments 2,400 customers into 6 groups using order history + behavioural signals, and recommends retention actions for each.

## How to Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook rfm_segmentation.ipynb
```

Or run all cells in Jupyter.

## Files

| File | Description |
|------|-------------|
| `rfm_segmentation.ipynb` | Main analysis notebook |
| `segments.csv` | Customer segments output |
| `retention_strategy.md` | Retention actions + budget allocation |
| `manual_review_cases.md` | 12 edge-case customers for manual review |
| `charts/` | Visualizations |
| `data/` | Source datasets |
| `requirements.txt` | Python dependencies |