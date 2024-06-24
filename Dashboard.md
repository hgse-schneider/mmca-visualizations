```python

```

# Dashboard Generator

Dashboard generator is a `Dash` application that uses the MMCA review library to get metric-outcome relationships and process the literature review dataset. The generator builds a dashboard that allows uses to interact with the visual representation of the metric-outcome relationship and explore the dataset.

The dashboard consists of two main components.

* 

![](figures/visualizer.gif)

* **Dataset Explorer**: This enables review dataset exploration as per the user's need. The explorer at the moment offers filtering of research papers based on the filter chosen by the users. The filters can be on metrics, outcomes, or instruments. 

![explorer.gif](figures/explorer.gif)

## How to run dashboard generator

Setup
```python
conda create -n "mmca-viz" python=3.9
conda activate mmca-viz
pip install -r requirements.txt
```

The dashboard generator can be started using the following command

```python
cd source_codes
python3 dashboard_mmca_cscw_v6.py
```
