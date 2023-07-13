# How to access formatted paper records

This tutorial is targetted at providing information on accessing mmca literature review data ( data metric sheet) in a formatted version.



* step-1: first import LiteratureDataset from mmcalib
* step-2: create an object of LiteratureDataset class by specify file_path of data_metric csv file.
* step-3: call populate_dataset function on Literature dataset class object.


```python
# import required classes
from mmcalib import LiteratureDataset

# instantiating LiteratureDataset
lit = LiteratureDataset('./data_metric_constructs.csv')

# populating the dataset with papers information
lit.populate_dataset()
```

    1. Record parsing begins...
    2. Record parsing completed
       Total 155 records are parsed
    3. Populating literature dataset
    4. Literature dataset is succefully populated


### Accessing paper record
Once you have created Literature Dataset object and populated it with papers record, you can access paper records.


```python
# fetching a paper with a particular id
paper = lit.get_paper(11)

# printing paper details
paper.print_paper_record()
```

    
    ####################   PAPER ID: 11     ####################
    
    Data: {'II': 'video', 'IV': 'kinesiology', 'V': 'log data'}
    Metrics: {'1': 'dialogue acts', '2': 'facial expression', '3': 'gesture', '4': 'task actions'}
    Metrics smaller: {'1': 'speech content', '2': 'facial expressions', '3': 'hand motion', '4': 'task-related'}
    Metrics larger: {'1': 'verbal', '2': 'head', '3': 'body', '4': 'log data'}
    Outcomes smaller: {'A': 'engagement', 'B': 'frustration', 'c': 'learning gains'}
    Outcomes larger: {'A': 'cognitive engagement', 'B': 'affective', 'c': 'learning'}
    Outcomes type: {'A': 'process', 'B': 'process', 'c': 'product'}
    Results: [('dialogue acts', 'engagement', ' regression'), ('facial expression', 'engagement', ' regression'), ('gesture', 'engagement', ' regression'), ('dialogue acts', 'frustration', ' regression'), ('facial expression', 'frustration', ' regression'), ('gesture', 'frustration', ' regression')]
    
    ############################################################
    


### Accessing particular details of the paper
You can access information like data, metrics, outcomes, relationship in a structured way once you have paper obejct.


```python
import pprint as pp
```


```python
# accessing metrics

# original metrics reported in the paper
metrics_org = paper.get_metrics_org()

# smaller metrics codes
metrics_sm = paper.get_metrics_sm()

# larger metrics codes
metrics_lg = paper.get_metrics_lg()
```


```python
pp.pprint(metrics_org)
```

    {'1': 'dialogue acts',
     '2': 'facial expression',
     '3': 'gesture',
     '4': 'task actions'}


In a similar way you can access the outcomes investigated in the paper.



```python
outcomes_sm = paper.get_outcomes_sm
outcomes_lg = paper.get_outcomes_lg
```

### Accessing relationship data
Each paper object has relationship mapping in the form of a dictionary.


```python
# accessing raw relationship codes
relationship = paper.get_relationship()
pp.pprint(relationship)
```

    '"1,2,3-A: regression: sig;1,2,3-B: regression: sig;1,2,3-C: regression: sig"'



```python
# accessing parsed relationship codes
# each tuple consist of three items, (metric,outcome,method)

relationship = paper.parse_relationship()
pp.pprint(relationship)
```

    [('dialogue acts', 'engagement', ' regression'),
     ('facial expression', 'engagement', ' regression'),
     ('gesture', 'engagement', ' regression'),
     ('dialogue acts', 'frustration', ' regression'),
     ('facial expression', 'frustration', ' regression'),
     ('gesture', 'frustration', ' regression')]


For example the first tuple ('dialogue acts', 'engagement', ' regression') represents that the paper has found a relationship between dialogue acts and engagment through regression method.


```python

```
