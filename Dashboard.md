```python

```

# Dashboard Generator
Dashboard generator is a `Dash` application that uses the MMCA review library to get metric-outcome relationships and process the literature review dataset. The generator builds a dashboard that allows uses to interact with the visual representation of the metric-outcome relationship and explore the dataset.

The dashboard consists of two main components.

* **Relationship Visualizer**: This component represents the metric-outcome relationships found in all the papers published between a particular time interval. The visualizer allows users to change the time interval. The relationships are plotted using a Sankey diagram. <br> The diagram comes with an interactive feature that allows uses to gain further information with a single click on nodes.

![](./visualizer.gif)

* **Dataset Explorer**: This enables review dataset exploration as per the user's need. The explorer at the moment offers filtering of research papers based on the filter chosen by the users. The filters can be on metrics, outcomes, or instruments. 

![explorer.gif](./explorer.gif)

## How to run dashboard generator
The dashboard generator can be started using the following command


```python
python3 dashboard_mmca_cscw_v6.py
```


```python

```
