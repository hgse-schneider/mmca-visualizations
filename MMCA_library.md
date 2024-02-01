# MMCA Review Library

MMCA library is developed to allow easier access to the MMCA literature review dataset. The library offers a systematic way to access reviewed papers and their information which were coded during the review process.

## Setting up environment

First, you need to install the required python packages and for that, we recommend you set up a virtual environment. 
You can use the `requirement.txt` file which contains the python packages list. You can use that file to set your envrionment

## Initialization

To start using MMCA library, we first need to initiaze it. The steps are given below

* Step-1: first import LiteratureDataset from mmcalib
* Step-2: create an object of LiteratureDataset class by specify file_paths of data_metric, paper details, and paper meta CSV files.

```python
# import required classes
from mmcalib_cscw_v6dataset import LiteratureDataset

# create an object of LiteratureDataset class
lit = LiteratureDataset('../dataset/6.2023 CSCW dataset_data_metrics_constructs.csv',
                       '../dataset/6.2023 CSCW dataset - paper_details.csv',
                       '../dataset/6.2023 CSCW dataset - paper_meta.csv')
```

    Populating with paper records ...
    Literature dataset is succefully populated. 
      Total papers: 140
    Updated paper records with study setting, learning task, sample size and experimental study type

Here, we are using the 6th version of the review dataset consisting of a total of 140 papers.

### Accessing paper record

Once you have created a Literature Dataset object, you can access any paper record using its paper id. For example, let's say we want to access a paper with id 10. 

```python
# fetching a paper with a particular id
paper = lit.get_paper(10)

# printing paper details
paper.print_paper_record()
```

    ####################   PAPER ID: 10     ####################
    
    Year: 2018
    Title: A Network Analytic Approach to Gaze Coordination during a Collaborative Task
    Study setting: lab
    Learning task: Each dyad was assigned a sandwich-building task: one participant made verbal references to visible ingredients they would like added to their sandwich, while the other participant assembled those ingredients into a sandwich.
    Study setting: G=13; I=26
    Authors: None
    Data: {'i': 'eye gaze'}
    Metrics: {'1': 'gaze fixations', '2': 'gaze saccades'}
    Metrics smaller: {'1': 'visual attention', '2': 'eye motion'}
    Metrics larger: {'1': 'gaze', '2': 'gaze'}
    Outcomes: {'a': 'task performance'}
    Outcomes smaller: {'a': 'performance'}
    Outcomes larger: {'a': 'product'}
    Outcomes instrument: {'a': 'human evaluation'}
    Experimental type: NS
    Results: 1+2-A: correlation: nonsig
    Results: [('visual attention', 'performance', ' correlation', 'nonsig'), ('eye motion', 'performance', ' correlation', 'nonsig')]
    
    ############################################################

### Accessing particular details of the paper

You can access information like data, metrics, outcomes, relationship in a structured way once you have the paper obejct.

```python
# original metrics reported in the paper
metrics_org = paper.get_metrics_org()

# smaller metrics codes
metrics_sm = paper.get_metrics_sm()

# larger metrics codes
metrics_lg = paper.get_metrics_lg()

# original outcomes reported in the paper
outcomes_org = paper.get_outcomes_org()

# smaller outcomes codes
outcomes_sm = paper.get_outcomes_sm()

# larger outcomes codes
outcomes_lg = paper.get_outcomes_lg()
```

```python
print('Metrics')
print('--------')
print('  original:',metrics_org)
print('  smaller:',metrics_sm)
print('  larger:',metrics_lg)

print('\nOutcomes')
print('--------')
print('  original:',outcomes_org)
print('  smaller:',outcomes_sm)
print('  larger:',outcomes_lg)
```

    Metrics
    --------
      original: {'1': 'gaze fixations', '2': 'gaze saccades'}
      smaller: {'1': 'visual attention', '2': 'eye motion'}
      larger: {'1': 'gaze', '2': 'gaze'}
    
    Outcomes
    --------
      original: {'a': 'task performance'}
      smaller: {'a': 'performance'}
      larger: {'a': 'product'}

### Accessing relationship data

Each paper object has relationship mappings in the form of a string and a dictionary. The string version is what is available in the review dataset. While the dictionary version is a processed version.

```python
# accessing raw relationship data
raw_relationship = paper.get_raw_relationship()
print('Raw relationship:',raw_relationship)

# accessing processed relationship data
relationship = paper.parse_relationship()
print('\n\nProcessed relationshp:')
print(relationship)
```

    Raw relationship: 1+2-A: correlation: nonsig
    
    
    Processed relationshp:
    [('visual attention', 'performance', ' correlation', 'nonsig'), ('eye motion', 'performance', ' correlation', 'nonsig')]

Parsed relationships are in `tuple` form. For example the first tuple `('visual attention', 'performance', ' correlation')` represents that the paper has found a relationship between visual attention and performance using correlation analysis and the relationship was significant.

### Fetching unique values for attributes

The MMCA library offers a function `get_unique_values` which returns all unique values for a specified attribute. For example, let's say we want to see what different values are there in the dataset for the data attribute. 

```python
# getting unique values
data_unique = lit.get_unique_values('data')
print(data_unique)
```

    ['video', 'log data', 'eeg', 'audio', 'ecg', 'bvp', 'other', 'eda', 'eye gaze', 'kinesiology']

### Filtering papers

namely `get_filtered_papers` which can be used to filter papers based on time intervals, larger metrics, smaller metrics, smaller outcomes, and instruments used for collaboration constructs.

Let's take an example. We want to fetch all the papers published between 2000 and 2010 which used audio data.

```python
# get papers between 2000 and 2010 using audio
# 'all' representing no filtering for metrics, outcomes, instruments.
audio_papers = lit.get_filtered_papers(2000,2010,'verbal','all','all','all')

print('Total papers using verbal metrics between 2000 and 2010:',len(audio_papers))
```

    Total papers using verbal metrics between 2000 and 2010: 19

### Plotting trends for different attributes

The library also offers a basic functionality of plotting trends for different attributes (e.g., metrics, and instruments).

Below, we show the trends in terms of different types of metrics used over the years.

```python
lit.plot_trends('metrics_lg',fig_title='Metrics usages over the years')
```

    physiological : 21
    head : 14
    verbal : 69
    log data : 26
    gaze : 59
    body : 42

![png](output_19_1.png)

```python
lit.plot_trends('outcomes_sm',fig_title='Outcomes investigated over the years')
```

    interpersonal relationship : 31
    communication : 30
    coordination : 56
    engagement : 27
    group composition : 18
    learning : 37
    affective : 10
    performance : 42

![png](output_20_1.png)

```python
lit.plot_trends('outcomes_instrument',fig_title='Instruments used over the years')
```

    task outcome : 18
    human evaluation : 78
    task performance : 2
    log data : 13
    mixed - human evaluation & survey : 1
    research coded : 2
    learning test : 12
    survey : 49
    assigned : 3
    computation : 5
    mixed - human evaluation & tests : 1

![png](output_21_1.png)

```python

```
