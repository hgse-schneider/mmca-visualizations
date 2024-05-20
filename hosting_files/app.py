import dash
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State
import ast
import plotly.express as px
import json

########### MMCA LIB code 

"""
Source codes for pre-processing MMCA literature review dataset (data metrics)
author: Pankaj Chejara (pankajchejara23@gmail.com)
"""
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def reduce_intensity(c, intensity=.2):
    return c.replace('0.8', '0.2')


color = ["rgba(31, 119, 180, 0.8)",
         "rgba(255, 127, 14, 0.8)",
         "rgba(44, 160, 44, 0.8)",
         "rgba(214, 39, 40, 0.8)",
         "rgba(148, 103, 189, 0.8)",
         "rgba(140, 86, 75, 0.8)",
         "rgba(227, 119, 194, 0.8)",
         "rgba(127, 127, 127, 0.8)",
         "rgba(188, 189, 34, 0.8)",
         "rgba(23, 190, 207, 0.8)",
         "rgba(31, 119, 180, 0.8)",
         "rgba(255, 127, 14, 0.8)",
         "rgba(44, 160, 44, 0.8)",
         "rgba(214, 39, 40, 0.8)",
         "rgba(148, 103, 189, 0.8)",
         "rgba(140, 86, 75, 0.8)",
         "rgba(227, 119, 194, 0.8)",
         "rgba(127, 127, 127, 0.8)",
         "rgba(188, 189, 34, 0.8)",
         "rgba(23, 190, 207, 0.8)",
         "rgba(31, 119, 180, 0.8)",
         "rgba(255, 127, 14, 0.8)",
         "rgba(44, 160, 44, 0.8)",
         "rgba(214, 39, 40, 0.8)",
         "rgba(148, 103, 189, 0.8)",
         "rgba(140, 86, 75, 0.8)",
         "rgba(227, 119, 194, 0.8)",
         "rgba(127, 127, 127, 0.8)",
         "rgba(188, 189, 34, 0.8)",
         "rgba(23, 190, 207, 0.8)",
         "rgba(31, 119, 180, 0.8)",
         "rgba(255, 127, 14, 0.8)",
         "rgba(44, 160, 44, 0.8)",
         "rgba(214, 39, 40, 0.8)",
         "rgba(148, 103, 189, 0.8)",
         "magenta",
         "rgba(227, 119, 194, 0.8)",
         "rgba(127, 127, 127, 0.8)",
         "rgba(188, 189, 34, 0.8)",
         "rgba(23, 190, 207, 0.8)",
         "rgba(31, 119, 180, 0.8)",
         "rgba(255, 127, 14, 0.8)",
         "rgba(44, 160, 44, 0.8)",
         "rgba(214, 39, 40, 0.8)",
         "rgba(148, 103, 189, 0.8)",
         "rgba(140, 86, 75, 0.8)",
         "rgba(227, 119, 194, 0.8)",
         "rgba(127, 127, 127, 0.8)",
         "rgba(214, 39, 40, 0.8)",
         "rgba(148, 103, 189, 0.8)",
         "rgba(140, 86, 75, 0.8)",
         "rgba(227, 119, 194, 0.8)",
         "rgba(127, 127, 127, 0.8)",
         "rgba(188, 189, 34, 0.8)",
         "rgba(23, 190, 207, 0.8)",
         "rgba(31, 119, 180, 0.8)",
         "rgba(255, 127, 14, 0.8)",
         "rgba(44, 160, 44, 0.8)",
         "rgba(214, 39, 40, 0.8)",
         "rgba(148, 103, 189, 0.8)",
         "magenta",
         "rgba(227, 119, 194, 0.8)",
         "rgba(127, 127, 127, 0.8)",
         "rgba(188, 189, 34, 0.8)",
         "rgba(23, 190, 207, 0.8)",
         "rgba(31, 119, 180, 0.8)",
         "rgba(255, 127, 14, 0.8)",
         "rgba(44, 160, 44, 0.8)",
         "rgba(214, 39, 40, 0.8)",
         "rgba(148, 103, 189, 0.8)",
         "rgba(140, 86, 75, 0.8)",
         "rgba(227, 119, 194, 0.8)",
         "rgba(127, 127, 127, 0.8)",
         "rgba(214, 39, 40, 0.8)",
         "rgba(148, 103, 189, 0.8)",
         "rgba(140, 86, 75, 0.8)",
         "rgba(227, 119, 194, 0.8)",
         "rgba(127, 127, 127, 0.8)",
         "rgba(188, 189, 34, 0.8)",
         "rgba(23, 190, 207, 0.8)",
         "rgba(31, 119, 180, 0.8)",
         "rgba(255, 127, 14, 0.8)",
         "rgba(44, 160, 44, 0.8)",
         "rgba(214, 39, 40, 0.8)",
         "rgba(148, 103, 189, 0.8)",
         "magenta",
         "rgba(227, 119, 194, 0.8)",
         "rgba(127, 127, 127, 0.8)",
         "rgba(188, 189, 34, 0.8)",
         "rgba(23, 190, 207, 0.8)",
         "rgba(31, 119, 180, 0.8)",
         "rgba(255, 127, 14, 0.8)",
         "rgba(44, 160, 44, 0.8)",
         "rgba(214, 39, 40, 0.8)",
         "rgba(148, 103, 189, 0.8)",
         "rgba(140, 86, 75, 0.8)",
         "rgba(227, 119, 194, 0.8)",
         "rgba(127, 127, 127, 0.8)"]


class Paper:
    """
    A class used to represent a paper record

    Attributes
    -----------
    paper_record : strt
        a string containing paper record for an individual paper
    paper_id : int
        an unique id of the paper
    pub_year : int
        publication year of the paper
    study_setting : str
        type of setting
    experimental_study : str
        type of research study (ecological or lab)
    sample_size : dict
        a dictionary containing number of groups and number of participants
    task : str
        learning task given to participants in the paper
    data : dict
        a dictionary containg types of data used in the paper
    sensor : dict
        a dictionary containg types of sensors used in the paper
    metrics_org : dict
        a dictionary containing metrics used in the paper
    metrics_sm : dict
        a dictionary containing first level grouping of original metrics (e.g., voice features -> speech features)
    metrics_lg : dict
        a dictionary containing second level grouping of original metrics (e.g., voice features -> verbal)
    outcome_org : dict
        a dictionary containing original outcome reported in the paper
    outcome_instrument : dict
        a dictionary containing outcome instrument used in the paper
    outcome_sm : dict
        a dictionary containing first level grouping of original outcome (e.g., collaboration quality -> coordination)
    outcome_lg : dict
        a dictionary containing second level grouping of original outcome (e.g., collaboration quality -> process)
    relationship : dict
        a dictionary mapping relationship between metrics and outcomes. Keys represent metric and values represent outcomes



    Functions
    -------
    get_paper_id ()
        Returns unique id of the paper
    get_pub_year ()
        Returns publication year of the paper
    get_metrics_org()
        Returns a dictionary of metrics used in the paper
    get_metrics_sm ()
        Returns a dictionary of first level grouping of metrics
    get_metrics_lg ()
        Returns a dictionary of second level grouping of metrics
    get_outcome_sm ()
        Returns a dictionary of first level grouping of outcomes
    get_outcome_lg ()
        Returns a dictionary of second level grouping of outcomes
    get_relationship ()
        Returns dictionary mapping metrics to outcomes
    get_data ()
        Returns a dictionary of data used in the paper
    parse_relationship ()
        Returns parsed relationship
    parsed_items()
        Returns a dictionary containing parsed items
    set_pub_year()
        Set publication year
    set_study_setting()
        Set study setting
    set_sample_size()
        Set sample size
    set_task()
        Set learning task


    """

    def __init__(self, paper_record):
        """
        Initialize LiteratureReview object

        Attributes
        ---------
        paper_record: record in a pandas DataFrame
            record from a DataFrame containing paper records
        """
        self.paper_record = paper_record
        self.paper_id = paper_record['paper_id']
        self.sample_size = None
        self.study_setting = None
        self.task = None
        self.experimental_study = None
        self.authors = None

        # Input
        self.data = self.parsed_items(paper_record['data'])
        self.sensor = self.parsed_items(paper_record['sensor'])
        self.data_metric = self.parsed_items(paper_record['data_per_metric'])
        self.metrics_org = self.parsed_items(paper_record['metric'])
        self.paper_title = paper_record['paper_title']
        self.pub_year = paper_record['year']
        self.metrics_sm = self.parsed_items(
            paper_record['metric_smaller_standardized']) # using metric_smaller_standardised
        self.metrics_lg = self.parsed_items(
            paper_record['metric_larger_category_corrected']) # using metric_larger_corrected

        # Outcome
        self.outcomes_org = self.parsed_items(paper_record['outcome_new']) # Using udpated outcome entries from Zoe data version 6 dataset
        self.outcomes_sm = self.parsed_items(
            paper_record['outcome_smaller_category_new'])
        self.outcomes_lg = self.parsed_items(
            paper_record['outcome_larger_category_new'])
        self.outcomes_instrument = self.parsed_items(
            paper_record['outcome_instrument'])

        # Relationship
        self.raw_relationship = paper_record['analysis_and_results mm-oo:analysis:resultsig']

    def set_pub_year(self, year):
        """
        Attributes
        ---------
        year: int
            set publication year
        """
        self.pub_year = year

    def set_paper_authors(self,authors):
        """
        Attributes
        ---------
        authors: str
            set authors for the publication
        """
        self.authors = authors

    def set_experimental_type(self, experimental_type):
        """
        Attributes
        ---------
        experimental_type: str
            Returns whether the study reported in the paper was experimental in nature.
        """
        self.experimental_study = experimental_type

    def set_study_setting(self, study_setting):
        """
        Attributes
        ---------
        year: str
            set setting type of research study
        """
        self.study_setting = study_setting

    def set_sample_size(self, sample):
        """
        Attributes
        ---------
        year: str
            set sample size
        """
        self.sample_size = sample

    def set_task(self, task):
        """
        Attributes
        ---------
        year: int
            set publication year
        """
        self.task = task

    def get_study_setting(self):
        """
        Returns
        ---------
        str
            type of study setting
        """
        return self.study_setting

    def get_sensor(self):
        """
        Returns
        ---------
        dict
            dictionary containing all sensors used in the reserach study
        """
        return self.sensor

    def get_paper_id(self):
        """
        Returns
        ---------
        int
            an unique id of the paper
        """
        return self.paper_id

    def get_pub_year(self):
        """
        Returns
        ---------
        int
            publication year of the paper
        """
        return self.pub_year

    def get_metrics_org(self):
        """
        Returns
        ---------
        dict
            Returns a dict of metrics used in the paper
        """
        return self.metrics_org

    def get_metrics_sm(self):
        """
        Returns
        ---------
        dict
            Returns a dict of metrics grouping (first level)
        """
        return self.metrics_sm

    def get_metrics_lg(self):
        """
        Returns
        ---------
        dict
            Returns a dict of metrics groupping (second level) used in the paper
        """
        return self.metrics_lg

    def get_outcomes_instrument(self):
        """
        Returns
        ---------
        dict
            Returns a dict of outcome instruments used in the paper
        """
        return self.outcomes_instrument

    def get_outcomes_sm(self):
        """
        Returns
        ---------
        dict
            Returns a dict of outcomes groupping (first level) used in the paper
        """
        return self.outcomes_sm

    def get_outcomes_lg(self):
        """
        Returns
        ---------
        dict
            Returns a dict of outcomes groupping (second level) used in the paper
        """
        return self.outcomes_lg

    def get_outcomes_org(self):
        """
        Returns
        ---------
        dict
            Returns a dict of types of outcomes used in the paper
        """
        return self.outcomes_org

    def get_data(self):
        """
        Returns
        ---------
        dict
            Returns a dict of data types used in the paper
        """
        return self.data

    def get_experimental_type(self):
        """
        Returns
        ---------
        str
            Returns a description of what type of experimental conditions were used in the study
        """
        return self.experimental_study

    def get_raw_relationship(self):
        """
        Returns
        ---------
        str
            Returns an original code string representing the relationships found the paper
        """
        return self.raw_relationship

    def parsed_items(self, text):
        """
        This function takes a string which contains data in a particular format (e.g.,  VI) EDA).
        The function then process the string, transforms the information in a dictionary data structure for later processing.

        Parameters
        ----------
        text : str
            string to parse

        Returns
        ---------
        dict
            dictionary with extracted information

        """
        # remove additional quotes
        if isinstance(text,float):
            print(text,self.paper_title)
        text_no_quotes = text.replace('\"', '')
        text_items = text_no_quotes.split('\n')

        pre_text_items = [item for item in text_items if item != '']

        # seperates index and data
        labels = [item.split(')')[1].strip() for item in pre_text_items]
        index = [item.split(')')[0].strip() for item in pre_text_items]

        # changing case of index
        index = [item.lower() for item in index]

        pre_met = {}
        for ind, lab in zip(index, labels):
            if ind in pre_met.keys():
                
                # coded added to process version 6 data where single outcome assigned to multiple different smaller categories
                if not isinstance(pre_met[ind],list):
                    tmp = pre_met[ind]
                    pre_met[ind] = [tmp]
                pre_met[ind].append(lab.lower())
            else:
                pre_met[ind] = lab.lower()
        return pre_met

    def parse_relationship(self, item_index=False):
        """
        This function processess relationship data and prepare a mapping between metrics and outcomes.

        Returns
        ---------
        list
            a list containing tuples of four items (metric,outcome,method,significance) representing found relationship in the paper.

        """
        data = self.raw_relationship

        data = data.replace('+', ',')
        data = data.replace('*', ',')

        if data.strip() == '':
            return []
        metrics_org = self.metrics_org
        metrics_sm = self.metrics_sm
        outcome_smaller = self.outcomes_sm
        text_no_quotes = data.replace('\"', '')
        text_items = text_no_quotes.split('\n')
        pre_text_items = [item for item in text_items if item != '']
        rel_tuples = []
        for rel in pre_text_items:
            parts = rel.split(':')
            rel_type = '' if len(parts) < 3 else parts[2]
            rel_method = parts[1]
            rel_parts = parts[0].split('-')
            metrics = rel_parts[0]
            outcomes = rel_parts[1]
            metrics = [item.strip() for item in metrics.split(',')]
            outcomes = [item.strip() for item in outcomes.split(',')]
            outcomes = [outcome.lower() for outcome in outcomes]
            for metric in metrics:
                for outcome in outcomes:
                    if item_index:
                        if isinstance(outcome_smaller[outcome],list):
                            for each_outcome in outcome_smaller[outcome]:
                                rel_tuples.append(
                                    (metric, f'{outcome}-{each_outcome}', rel_method, rel_type.strip()))
                        else:
                            rel_tuples.append(
                                    (metric, outcome, rel_method, rel_type.strip()))
                    else:
                        if isinstance(outcome_smaller[outcome],list):
                            for each_outcome in outcome_smaller[outcome]:
                                rel_tuples.append(
                                    (metrics_sm[metric], each_outcome, rel_method, rel_type.strip()))
                        else:
                            rel_tuples.append(
                                    (metrics_sm[metric], outcome_smaller[outcome], rel_method, rel_type.strip()))
        return rel_tuples

    def __str__(self):
        return 'Paper id:{} '.format(self.paper_id, self.data_types)

    def print_paper_record(self):
        """
            This function print the paper record.
        """
        print('\n####################   PAPER ID: {}     ####################\n'.format(
            self.paper_id))
        if self.pub_year:
            print('Year:', self.pub_year)
        print('Title:',self.paper_title)
        if self.study_setting:
            print('Study setting:', self.study_setting)
        if self.task:
            print('Learning task:', self.task)
        if self.sample_size:
            print('Study setting:', self.sample_size)
        print('Authors:',self.authors)
        print('Data:', self.data)
        print('Metrics:', self.metrics_org)
        print('Metrics smaller:', self.metrics_sm)
        print('Metrics larger:', self.metrics_lg)
        print('Outcomes:', self.outcomes_org)
        print('Outcomes smaller:', self.outcomes_sm)
        print('Outcomes larger:', self.outcomes_lg)
        print('Outcomes instrument:', self.outcomes_instrument)
        print('Experimental type:', self.experimental_study)
        print('Results:', self.raw_relationship)
        print('Results:', self.parse_relationship())
        print('\n############################################################\n')


class LiteratureDataset:
    """
    A class used to represent a collection of objects of class:Paper type
    """

    def __init__(self, data_metric_file_path, paper_details_file_path, paper_meta_file_path):
        """
        Attributes
        -----------
        data_metric_file_path : str
            a string containing path of CSV file of data_metric sheet imported from MMCA literature review dataset

        paper_details_file_path : str
            a string containing path of CSV file of paper details sheet imported from MMCA literature review dataset

        paper_meta_file_path : str
            a string containing path of CSV file of paper meta sheet imported from MMCA literature review dataset
        """
        self.data_metric_file_path = data_metric_file_path
        self.paper_details_file_path = paper_details_file_path
        self.paper_meta_file_path = paper_meta_file_path
        self.paper_store = dict()
        self.paper_count = 0
        self.populate_dataset()

        try:
            self.update_setting_task_sample_experimental()
        except Exception as e:
            print(e)
            print('Literature dataset could not update contextual information, e.g., study setting, learning task, sample size, and  experimental type.')

    def get_record(self, df, index):
        """
        Function to parse data metric sheet. 

        Attributes
        -----------
            df : Pandas Dataframe containing data_metric sheet of MMCA literature review

        Returns
        -----------
            record 
                a record from df at specified index
        """

        return df.iloc[index, :].to_dict()

    def update_year(self):
        """
        This function adds year information to each paper record.

        """
        year = pd.read_csv(self.paper_meta_file_path,sep=';')
        pub_year = year[['ID updated', 'year']]
        pub_year.index = pub_year['ID updated']
        for ind in self.paper_store.keys():
            self.paper_store[ind].set_pub_year(
                pub_year.to_dict()['year'][int(ind)])


    def generate_sankey_data(self, year1=2000, year2=2005, selected_levels={'metrics_lg': 2, 'metrics_sm': 1, 'outcome_sm': 4, 'outcome_lg': 3}):
        """
        This function processes papers published in the specified interval (year1,year2) and generates data for plotting
        a sankey diagram.

        Attributes
        ----------
        year1 : int
            starting year for filtering
        year2 : int
            ending year for filtering
        selected_levels : dict
            dictionary containing levels for each node type to configure its position in the generated sankey diagram


        Returns
        ---------
        dataframe
            pandas dataframe containing record for sankey diagram generation (e.g., source, target)
        dict
            dictionary containing unique node labels for each level in sankey diagram (e.g., labels for smaller metrics)
        dict
            dictionary containing data for nodes to be used in sankey diagram
        dict
            dictionary containing data for links to be used in sakey diagram
        """
        linked_paper_ids = []
        available_color_index = 0

        # filter papers according to the interval
        papers = self.get_papers_between_interval(year1, year2)

        # dataframe to store information for sankey diagram generation
        sankey = pd.DataFrame(
            columns=['source', 'target', 'level', 'paper_id', 'year', 'color', 'edge_label'])

        full = pd.DataFrame(
            columns=['metrics_lg', 'metrics_sm', 'outcome_sm',
                     'outcome_lg', 'paper_id', 'year']
        )

        # position info for each node
        nodes_level = {}

        # color info for nodes
        nodes_color = {}

        # color info for links
        link_color = {}


        level_wise_nodes = {
            # store information what nodes are stored at different levels (e.g., metrics_lg at level 1, metrics_sm at level 2)
            1: list(),
            2: list(),
            3: list(),
            4: list()
        }
        for paper in papers:
            metrics_org = paper.get_metrics_org()
            metrics_sm = paper.get_metrics_sm()
            metrics_lg = paper.get_metrics_lg()
            outcome_sm = paper.get_outcomes_sm()
            outcome_lg = paper.get_outcomes_lg()
            outcome = paper.get_outcomes_org()
            rels = paper.parse_relationship(item_index=True)

            # process each relationship found in the paper
            for rel in rels:
                check = 0
                # the following check to only process entries where we have all the data from metric to outcome
                if rel[0] in metrics_org.keys():
                    check += 1
                if rel[0] in metrics_sm.keys():
                    check += 1
                if rel[0] in metrics_lg.keys():
                    check += 1
                if rel[1] in outcome_sm.keys():
                    check += 1
                if rel[1] in outcome_lg.keys():
                    check += 1
                if rel[1] in outcome.keys():
                    check += 1

                if check == 6:
                    # skip the cases where label in smaller and larger categories are same. This is to avoid circular linking in sankey diagram.
                    if metrics_lg[rel[0]] == metrics_sm[rel[0]] or outcome_sm[rel[1]] == outcome_lg[rel[1]]:
                        continue

                    # process metric_lg information of the current relationship
                    if metrics_lg[rel[0]] not in nodes_level.keys():

                        # set the position of the node
                        nodes_level[metrics_lg[rel[0]]
                                    ] = selected_levels['metrics_lg'] if selected_levels else .1
                        
                        # set the color of the node
                        nodes_color[metrics_lg[rel[0]]
                                    ] = color[available_color_index]
                        # append the node to the list 
                        level_wise_nodes[1].append(metrics_lg[rel[0]])
                        available_color_index += 1

                    if metrics_sm[rel[0]] not in nodes_level.keys():
                        # print('  adding metrics sm')
                        nodes_level[metrics_sm[rel[0]]
                                    ] = selected_levels['metrics_sm'] if selected_levels else .2
                        level_wise_nodes[2].append(metrics_sm[rel[0]])
                        nodes_color[metrics_sm[rel[0]]
                                    ] = nodes_color[metrics_lg[rel[0]]]

                    if outcome_lg[rel[1]] not in nodes_level.keys():
                        nodes_level[outcome_lg[rel[1]]
                                    ] = selected_levels['outcome_lg'] if selected_levels else .6
                        nodes_color[outcome_lg[rel[1]]
                                    ] = color[available_color_index]
                        level_wise_nodes[4].append(outcome_lg[rel[1]])
                        available_color_index += 1

                    if '-' in rel[1]:
                        outcome_sm_index =  rel[1].split('-')[1]
                    else:
                        outcome_sm_index = rel[1]

                    if outcome_sm[outcome_sm_index] not in nodes_level.keys():
                            nodes_level[outcome_sm[outcome_sm_index]
                                    ] = selected_levels['outcome_sm'] if selected_levels else .5
                            nodes_color[outcome_sm[outcome_sm_index]
                                    ] = nodes_color[outcome_lg[rel[1].split('-')[0]]]
                            level_wise_nodes[3].append(outcome_sm[outcome_sm_index])

                    """
                    if isinstance(outcome_sm[rel[1]],list):
                        for out_sm in outcome_sm[rel[1]]:
                            if out_sm[rel[1]] not in nodes_level.keys():
                                nodes_level[out_sm[rel[1]]
                                        ] = selected_levels['outcome_sm'] if selected_levels else .5
                                nodes_color[out_sm[rel[1]]
                                        ] = nodes_color[outcome_lg[rel[1]]]
                                level_wise_nodes[3].append(out_sm[rel[1]])
                    else:
                        if outcome_sm[rel[1]] not in nodes_level.keys():
                            nodes_level[outcome_sm[rel[1]]
                                    ] = selected_levels['outcome_sm'] if selected_levels else .5
                            nodes_color[outcome_sm[rel[1]]
                                    ] = nodes_color[outcome_lg[rel[1]]]
                            level_wise_nodes[3].append(outcome_sm[rel[1]])
                    """
                            
                    # for each relationship store the related paper id
                    linked_paper_ids.append(paper.paper_id)
                    sorted_order = sorted(
                        selected_levels.items(), key=lambda item: item[1])
                    node_type_names = [item[0] for item in sorted_order]

                    source = eval(node_type_names[0])[
                        rel[0]] if 'metric' in node_type_names[0] else eval(node_type_names[0])[rel[1]]
                    target = eval(node_type_names[1])[
                        rel[0]] if 'metric' in node_type_names[1] else eval(node_type_names[1])[rel[1]]
                    # adding label for edges
                    edge_label = '{}:{}-{}'.format(paper.paper_id,
                                                   source, target)
                    
                    # create a record for linking metrics_lg to metrics_sm
                    temp = pd.DataFrame({'source': source,
                                         'target': target,
                                         'level': 1,
                                         'paper_id': paper.paper_id,
                                         'year': paper.pub_year,
                                         'edge_label': edge_label,
                                         'color': reduce_intensity(nodes_color[source])},
                                        index=[0])
                    # concat the record with dataframe
                    sankey = pd.concat([sankey, temp], axis=0)

                    source = eval(node_type_names[1])[
                        rel[0]] if 'metric' in node_type_names[1] else eval(node_type_names[1])[rel[1]]
                    target = eval(node_type_names[2])[
                        rel[0]] if 'metric' in node_type_names[2] else eval(node_type_names[2])[rel[1]]
                    edge_label = '{}:{}-{}'.format(paper.paper_id,
                                                   source, target)
                    
                    # create a record for linking metrics_sm to outcomes_sm
                    temp = pd.DataFrame({'source': source, 'target': target,
                                         'level': 2,
                                         'paper_id': paper.paper_id,
                                         'year': paper.pub_year,
                                         'edge_label': edge_label,
                                         'color': reduce_intensity(nodes_color[source])},
                                        index=[0])
                    sankey = pd.concat([sankey, temp], axis=0)

                    source = eval(node_type_names[2])[
                        rel[0]] if 'metric' in node_type_names[2] else eval(node_type_names[2])[rel[1]]
                    target = eval(node_type_names[3])[
                        rel[0]] if 'metric' in node_type_names[3] else eval(node_type_names[3])[rel[1]]
                    edge_label = '{}:{}-{}'.format(paper.paper_id,
                                                   source, target)
                    
                    # create a record for linking outcomes_sm to outcomes_lg
                    temp = pd.DataFrame({'source': source, 'target': target,
                                         'level': 3,
                                         'paper_id': paper.paper_id,
                                         'year': paper.pub_year,
                                         'edge_label': edge_label,
                                         'color': reduce_intensity(nodes_color[target])},
                                        index=[0])
                    sankey = pd.concat([sankey, temp], axis=0)

                    # here we store the processed record for later processing (it is an addition feature)
                    temp_full = pd.DataFrame({'metrics_lg': metrics_lg[rel[0]],
                                              'metrics_sm': metrics_sm[rel[0]],
                                              'outcome_sm': outcome_sm[rel[1]],
                                              'outcome_lg': outcome_lg[rel[1]],
                                              'paper_id': paper.paper_id,
                                              'year': paper.pub_year},
                                             index=[0])
                    full = pd.concat([full, temp_full], axis=0)

        #sankey.drop_duplicates(subset=['paper_id','source','target'],inplace=True)
        nodes = list(nodes_level.keys())
        x_pos = list(nodes_level.values())
        link = []
        value = []
        label = []
        link_color = []

        ## Code to check number of features which found to be related with collaboration constructs ##
        feat_count = sankey.loc[sankey.level == 4, ['source']]

        ## End new code ##
        for row in sankey.itertuples():
            t_rel = (nodes.index(row.source), nodes.index(row.target))
            if t_rel in link:
                ind = link.index(t_rel)

                label[ind] = label[ind] + ',' + row.edge_label
                if row.edge_label not in str(linked_paper_ids[ind]):
                    linked_paper_ids[ind] = str(linked_paper_ids[ind]) + \
                    ',' + str(row.paper_id)
                value[ind] += 1
            else:
                link.append(t_rel)
                label.append(row.edge_label)
                value.append(1)
                linked_paper_ids.append(str(row.paper_id))
                link_color.append(row.color)
        source = [item[0] for item in link]
        target = [item[1] for item in link]

        return full, sankey, level_wise_nodes, {'pad': 15,
                                                'thickness': 15,
                                                'label': nodes,
                                                'x': x_pos,
                                                'color': list(nodes_color.values())
                                                }, {'source': source,
                                                    'target': target,
                                                    'value': value,
                                                    'color': link_color,
                                                    'label': label,
                                                    #'customdata': linked_paper_ids,
                                                    #'hovertemplate': 'Paper id:%{customdata}'
                                                    }

    def count_or_mean(self, year1=2000, year2=2010):
        """
        This function count frequencies for each characteristic of the papers

        Attributes
        ---------
        year1: int
            starting year
        year2: int
            end year
        
        Returns
        ---------
        dict
            dictionary containing frequency count for all attributes of the paper (e.g., number of papers used audio, video, gaze, etc)
        """
        attrs = {}
        papers = self.get_papers_between_interval(year1, year2)
        temp_data_store = []
        temp_sensor_store = []
        temp_metrics_store = []
        temp_metrics_sm_store = []
        temp_metrics_lg_store = []
        temp_outcomes_store = []
        temp_outcomes_sm_store = []
        temp_outcomes_lg_store = []
        temp_outcomes_instrument_store = []
        temp_setting_store = []
        for paper in papers:
            temp_data_store += list(paper.get_data().values())
            temp_sensor_store += list(paper.get_sensor().values())
            temp_metrics_store += list(paper.get_metrics_org().values())
            temp_metrics_sm_store += list(paper.get_metrics_sm().values())
            temp_metrics_lg_store += list(paper.get_metrics_lg().values())
            temp_outcomes_store += list(paper.get_outcomes_org().values())
            temp_outcomes_sm_store += list(paper.get_outcomes_sm().values())
            temp_outcomes_lg_store += list(paper.get_outcomes_lg().values())
            temp_outcomes_instrument_store += list(
                paper.get_outcomes_instrument().values())
            temp_setting_store.append(paper.get_study_setting())

        attrs['data_stats'] = Counter(temp_data_store)
        attrs['sensor_stats'] = Counter(temp_sensor_store)
        attrs['metrics_stats'] = Counter(temp_metrics_store)
        attrs['metrics_sm_stats'] = Counter(temp_metrics_sm_store)
        attrs['metrics_lg_stats'] = Counter(temp_metrics_lg_store)
        attrs['outcomes_stats'] = Counter(temp_outcomes_store)
        attrs['outcomes_sm_stats'] = Counter(temp_outcomes_sm_store)
        attrs['outcomes_lg_stats'] = Counter(temp_outcomes_lg_store)
        attrs['outcomes_instrument_stats'] = Counter(
            temp_outcomes_instrument_store)
        attrs['setting_stats'] = Counter(temp_setting_store)

        return attrs

    def update_setting_task_sample_experimental(self):
        """
        This function adds details of sample size, type of study settings, and learning task.

        """
        context_org = pd.read_csv(self.paper_details_file_path)

        context = context_org[['study_setting', 'task',
                               'sample_size', 'experimental_conditions']]
        context.index = context_org['ID updated']
        for ind in self.paper_store.keys():
            self.paper_store[ind].set_study_setting(
                context.to_dict()['study_setting'][int(ind)])
            self.paper_store[ind].set_task(context.to_dict()['task'][int(ind)])
            self.paper_store[ind].set_sample_size(
                context.to_dict()['sample_size'][int(ind)])
            self.paper_store[ind].set_experimental_type(
                context.to_dict()['experimental_conditions'][int(ind)])

        print('Updated paper records with study setting, learning task, sample size and experimental study type')

    def get_papers(self):
        """
        This function return a list containing all paper records.

        Returns
        ---------
        list
            list of all paper records

        """
        return self.paper_store


    def get_filtered_papers(self, start_year,end_year, data,metric,outcome,instrument):
        """
        This function return a list containing all paper records published between specified interval.

        Attributes
        ---------
        start_year: int
            start year
        end_year: int
            end year
        data: str
            selected type of data
        metric: str
            selected type of metric
        outcome
            selected type of outcome
        instrument
            selected type of instrument


        Returns
        ---------
        list
            list of all paper records between start_year and end_year, and satisfying selected options
        """
        papers = self.get_papers_between_interval(start_year,end_year)
        results = []
        for paper in papers:
            paper_add_flag = 0
            if data in paper.metrics_lg.values() or data == 'all':
                paper_add_flag += 1
            if metric in paper.metrics_sm.values() or metric == 'all':
                paper_add_flag += 1
            if outcome in paper.outcomes_sm.values() or outcome == 'all':
                paper_add_flag += 1
            else:
                for sm_val in paper.outcomes_sm.values():
                    if isinstance(sm_val,list) and outcome in sm_val:
                        paper_add_flag += 1
                        break
            if instrument in paper.outcomes_instrument or instrument == 'all':
                paper_add_flag += 1
            if paper_add_flag == 4:
                results.append(paper)
        #print('Total {} papers found for data options filter'.format(len(results)))
        return results

    def get_papers_between_interval(self, start_year, end_year):
        """
        This function return a list containing all paper records published between specified interval.

        Attributes
        ---------
        start_year: int
            start year
        end_year: int
            end year

        Returns
        ---------
        list
            list of all paper records between start_year and end_year
        """
        results = []
        for paper_id, paper in self.paper_store.items():
            pub_year = int(paper.pub_year)
            if pub_year >= start_year and pub_year < end_year:
                results.append(paper)

        #print('Total {} papers found between'.format(len(results)))
        return results

    def get_paper(self, id):
        """
        This function return a paper associated with specified id.

        Attributes
        ---------
        id: int
            paper id

        Returns
        ---------
        Paper object
            object containing paper record of specified id
        """
        if id in list(self.paper_store.keys()):
            return self.paper_store[id]
        else:
            print('There is no paper with given id.')
            return None

    def populate_dataset(self):
        """
        This function loads the paper record in the form of Paper class objects.
        """
        df = pd.read_csv(self.data_metric_file_path)
        df['paper_id'] = df['id'].copy()
        df.set_index('id',inplace=True)
        print('Populating with paper records ...')
        for paper_index in range(len(df.index)):
            try:
                record = self.get_record(df, paper_index)
                paper_object = Paper(record)
                self.paper_store[paper_object.paper_id] = paper_object
            except Exception as e:
                print(e)
                print('Excluding paper:',paper_id)
        print('Literature dataset is succefully populated. \n  Total papers:', len(
            self.paper_store))

    def get_unique_values(self,attribute_name):
        """
        This function returns the unique values of the specified attribute.
        Attributes
        -----------
        attribute_name : str
            name of attribute for which unique values are requested

        Returns
        -----------
        list
            a list of unique values
        """
        vals =[]
        for paper in self.paper_store.values():
            attr_vals = getattr(paper,attribute_name)

            if isinstance(attr_vals,str):
                vals.append(attr_vals)
            else:
                # this cases handles the cases where there are mutliple smaller outcomes linked to a single larger outcomes 
                # (updated in 6th version dataset)
                for attr_val in attr_vals.values():
                    if isinstance(attr_val,list):
                        for v in attr_val:
                            if v not in vals:
                                vals.append(v)
                    else:
                        if attr_val not in vals:
                            vals.append(attr_val)
        return list(set(vals))

    def plot_trends(self,attribute,skip_values=[],fig_title='',savefig=True):
        """
        This function prints the trend of specified attribute.

        @todo: there is an issue to plot trends for sensor

        Attributes
        -----------
        attribute: str
            name of attribute for which trend has to be plotted
        skip_values : list
            list containing attribute's values to skip
        fig_title : str
            title of the figure
        save_fig: boolean
            flag to save the figure
        """


        papers = self.paper_store
        years = list(range(1999,2023))

        attr_type = {}
        base_dict = {}

        for year in years:
            base_dict[year] = 0

        # types of data used
        attr_uniques = self.get_unique_values(attribute)

        # different markers for data types
        markers = ['o','D','v','^','*','p','s','h','x','d','1','2','3','4','5']
        
        if len(markers) > len(attr_uniques):
            attr_markers =  markers[:len(attr_uniques)]
        else:
            attr_markers = []

        # create an empty dictionary for each data type
        for data in attr_uniques:
            if data not in skip_values:
                attr_type[data] = base_dict.copy()

        # iterate over all papers
        for pid,paper in papers.items():
            year = paper.pub_year
            attr_vals = getattr(paper,attribute)
            # set for taking unique values per paper

            attribute_values = list(attr_vals.values())

            while True:
                if len(attribute_values) == 0:
                    break
                used_data = attribute_values.pop()
                if used_data in attribute_values:
                    continue
                if isinstance(used_data,list):
                    for v in used_data:
                        if v.lower() not in skip_values:
                            attr_type[v][year] += 1
                else:
                    if used_data.lower() not in skip_values:
                        attr_type[used_data][year] += 1

        for a in attr_type.keys():
            print(a,':',sum(list(attr_type[a].values())))
        
        plt.figure()
        
        for ind,dt in enumerate(attr_uniques):
            if dt not in skip_values:
                if len(attr_markers) == 0:
                    #@todo: place the legend outside the figure
                    plt.plot(list(attr_type[dt].keys()),np.cumsum(list(attr_type[dt].values())),linestyle='-',label=dt)
                else:
                    plt.plot(list(attr_type[dt].keys()),np.cumsum(list(attr_type[dt].values())),markers[ind],linestyle='-',label=dt)
        plt.legend()
        plt.title(fig_title)
        if savefig:
            plt.savefig('{}.png'.format(fig_title))
        plt.show()


#########################


"""
Source codes for pre-processing MMCA literature review dataset (data metrics)

author: Pankaj Chejara (pankajchejara23@gmail.com)


"""
data_metric_file = "https://raw.githubusercontent.com/pankajchejara23/harvard-mmca/main/dataset/6.2023%20CSCW%20dataset_data_metrics_constructs.csv"
paper_detail_file = "https://raw.githubusercontent.com/pankajchejara23/harvard-mmca/main/dataset/6.2023%20CSCW%20dataset%20-%20paper_details.csv"
paper_meta_file = "https://raw.githubusercontent.com/pankajchejara23/harvard-mmca/main/dataset/6.2023%20CSCW%20dataset%20-%20paper_meta.csv"

lit = LiteratureDataset(data_metric_file,
                       paper_detail_file,
                       paper_meta_file)


def generate_table(year1,year2,data,metric,outcome,instrument):
    papers = lit.get_filtered_papers(
            year1, year2,data,metric,outcome,instrument)

    table_header = [
            html.Thead(html.Tr([html.Th("Year"), html.Th("Title"),html.Th("Data"),html.Th("Metric"),html.Th("Outcome"),html.Th("Instrument")]))
        ]

    rows_list = []

    for paper in papers:
        outcomes_sm_values = []

        for key in paper.outcomes_sm.keys():
            if isinstance(paper.outcomes_sm[key],list):
                outcomes_sm_values = outcomes_sm_values + paper.outcomes_sm[key]
            else:
                outcomes_sm_values.append(paper.outcomes_sm[key])


        rows_list.append(html.Tr([html.Td(paper.pub_year),
                                  html.Td(paper.paper_title),
                              html.Td(', '.join(list(set(list(paper.metrics_lg.values()))))),
                              html.Td(', '.join(list(set(list(paper.metrics_sm.values()))))),
                              html.Td(', '.join(outcomes_sm_values)),
                              html.Td(', '.join(list(set(list(paper.outcomes_instrument.values())))))]))

    table_body = [html.Tbody(rows_list)]
    print('Rows added to table:',len(rows_list))
    table = dbc.Table(table_header + table_body)
    return table


def list_to_select_options(values):
    results = []
    for val in values:
        results.append({'label':val,'value':val})
    results.append({'label':'---','value':'all'})
    return results


metric_larger_unique = lit.get_unique_values('metrics_lg')
metric_smaller_unique = lit.get_unique_values('metrics_sm')
outcome_smaller_unique = lit.get_unique_values('outcomes_sm')
instruments_unique = lit.get_unique_values('outcomes_instrument')

metric_smaller_options = list_to_select_options(metric_smaller_unique)
metric_larger_options = list_to_select_options(metric_larger_unique)
outcome_smaller_options = list_to_select_options(outcome_smaller_unique)
instruments_options = list_to_select_options(instruments_unique)

def reduce_intensity(c, intensity=.2):
    return c.replace('0.8', '0.2')


year_options = list(range(1999, 2023, 1))

marks = {}
for year in year_options:
    marks[year] = year
full, sankey, _, node, link = lit.generate_sankey_data(2000, 2010)
# creating dash app
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


start_year = []

overview_content = [dbc.Row([
    html.Hr(),
    html.H5('Start and End year selection'),
    html.P('Select duration which you are interested to explore.')]),
    dbc.Row([
        dcc.RangeSlider(1999, 2023, 1, value=[
                        2000, 2005], marks=marks, id='year_range')
    ]),
    dbc.Row(
        dcc.Graph(id='sankey',
                  style={'padding': '2em', 'width': '100%', 'height': '150%'},
                  figure=go.Figure(
                      data=[
                          go.Sankey(
                              node=node,
                              link=link,
                          )
                      ]
                  ))
)]

first_table = generate_table(2000,2010,'verbal','all','all','all')

filter_component =dbc.Card(
                    dbc.CardBody([
                        html.H5('MMCA literature dataset explorer'),
                        html.P('You can search through MMCA reserach dataset by selecting values for data types, metric, collaboration outcomes, type of study'),
                        dbc.Row([
                            dbc.Col([
                                html.P('Data type'),
                                dbc.Select(options= metric_larger_options, value='verbal', id='data'),
                            ]),
                            dbc.Col([
                                html.P('Metric type'),
                                dbc.Select(options= metric_smaller_options, value='all', id='metric'),
                            ]),
                            dbc.Col([
                                html.P('Outcome type'),
                                dbc.Select(options= outcome_smaller_options, value='all', id='outcome'),
                            ]),
                            dbc.Col([
                                html.P('Instrument type'),
                                dbc.Select(options= instruments_options, value='all', id='instrument'),
                            ])
                        ]),
                        dbc.Button("Apply filter", id="filter",color="primary", className="p-2 my-3"),
                        dbc.Row([
                        html.Div(children=[first_table],id='paper_list')
                            ])]),className="mt-3",)


sankey_component = dbc.Card(
    dbc.CardBody([dbc.Row([
        dbc.Col([
            dcc.Graph(id='sankey',
                      style={'padding': '3em',
                             'width': '100%', 'height': '100%'},
                      figure=go.Figure(
                          data=[
                              go.Sankey(
                                  node=node,
                                  link=link,
                              )
                          ]
                      )
                      )
        ])
    ])]),className="mt-3")

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([

                html.H1("MMCA"),
                html.H4(
                    "Relationship between data metrics and collaboration aspects"),
                html.P("This visualisation gives an overview of the field of Multiomdal Collaboration Analytics" +
                       ". In particular, it provides overview of relationship between data-metrics and collaboration aspects found in past two decades."),
                ])
    ]),
    dbc.Button(
        "Configure metric-outcome graph",
        id="collapse-button",
        className="mb-3",
        color="primary",
        n_clicks=0,
    ),
    dbc.Collapse([
        html.Div([
            html.H3('Configure sankey dashboard'),
            html.P('Configure order of sankey diagram.'),
            dbc.Row([
                dbc.Col([
                    html.P('Larger metrics'),
                    dbc.Select([
                        {'label': '1', 'value': '1'},
                        {'label': '2', 'value': '2'},
                        {'label': '3', 'value': '3'},
                        {'label': '4', 'value': '4'}
                    ], 1, id='larger_metric')
                ]),
                dbc.Col([
                    html.P('Smaller metrics'),
                    dbc.Select([
                        {'label': '1', 'value': '1'},
                        {'label': '2', 'value': '2'},
                        {'label': '3', 'value': '3'},
                        {'label': '4', 'value': '4'}
                    ], 2, id='smaller_metric')
                ]),
                dbc.Col([
                    html.P('Smaller outcome'),
                    dbc.Select([
                        {'label': '1', 'value': '1'},
                        {'label': '2', 'value': '2'},
                        {'label': '3', 'value': '3'},
                        {'label': '4', 'value': '4'}
                    ], 3, id='smaller_outcome')
                ]),
                dbc.Col([
                    html.P('Larger outcome'),
                    dbc.Select([
                        {'label': '1', 'value': '1'},
                        {'label': '2', 'value': '2'},
                        {'label': '3', 'value': '3'},
                        {'label': '4', 'value': '4'}
                    ], 4, id='larger_outcome')
                ])
            ]),
            dbc.Button("Update layout", id="enter",
                       color="primary", className="p-2 my-3"),
            html.Div(id='error', className="p-2 my-3"),
        ], style={'padding': '3em', 'margin-bottom': '2em'}, className='border rounded-top rounded-bottom')], id='collapse', is_open=False
    ),

    dbc.Row([
        dbc.Card([
            dbc.CardBody([
                html.H3('Start and End year selection'),
                html.P('Select duration which you are interested to explore.')]),
            dbc.Row([
                    dcc.RangeSlider(1999, 2023, 1, value=[
                                    2000, 2005], marks=marks, id='year_range')
                    ]),
        ], style={'padding': '1em', 'margin-bottom': '1em'})
    ]),
    dbc.Modal(
        [
            dbc.ModalHeader("Details", id='modalheader'),
            dbc.ModalBody(dcc.Graph(id='node_details')),
            dbc.ModalFooter(
                dbc.Button("Close", id="close", className="ml-auto")
            ),
        ],
        size="xl",
        id="modal",
    ),
    dbc.Tabs(
    [
        dbc.Tab(sankey_component, label="Metric-Outcome Relationship"),
        dbc.Tab(filter_component, label="MMCA literature dataset"),
    ]
)
])



@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("error", "children"),
    [Input("enter", "n_clicks"), Input('year_range', 'value')],
    [State("larger_metric", "value"), State("smaller_metric", "value"),
     State("smaller_outcome", "value"), State("larger_outcome", "value")]
)
def func(n_clicks, value, lg_metric, sm_metric, sm_outcome, lg_outcome):
    print('Inside function')
    year_range = value
    year1 = year_range[0]
    year2 = year_range[1]
    error_text = ''
    if len(list(set([str(lg_metric), str(sm_metric), str(sm_outcome), str(lg_outcome)]))) != 4:
        error_text = 'Each node type needs a different level. Please specify a unique level for each type of nodes.'

    return html.P(error_text, className='text-danger')


@app.callback(Output('modal', 'is_open'),
              [Input('sankey', 'clickData'), Input(
                  'close', 'n_clicks')],
              [State("modal", "is_open")],)
def open_modal(clickData, n1, is_open):
    if n1:
        return not is_open
    elif clickData['points'][0]['label'] and ':' not in clickData['points'][0]['label']:
        return True
    else:
        return False

@app.callback(Output('paper_details', 'children'),
              [Input('sankey', 'clickData'), Input('year_range', 'value')])
def display_value(clickData, value):
    print('Click Data:=======>', clickData)
    year_range = value
    year1 = year_range[0]
    year2 = year_range[1]
    full, sankey, level_wise_nodes, node, link = lit.generate_sankey_data(
        year_range[0], year_range[1])

    node_label = clickData['points'][0]['label']
    if ':' in node_label:
        papers = [item.split(':')[0] for item in node_label.split(',')]

        return [html.H3('Related papers'), html.H6((',').join(set(papers)))]

@app.callback(Output('paper_list', 'children'),
              [Input("filter", "n_clicks"), Input('year_range', 'value')],
              [State("data", "value"), State("metric", "value"), State("outcome", "value"), State("instrument", "value")])
def display_value(f1, value,data,metric,outcome,instrument):
    print('Paper list update called:=======>')
    if f1:
        table = generate_table(value[0],value[1],data,metric,outcome,instrument)
        return [html.H3('Related papers'), table]


@app.callback(Output('node_details', 'figure'),
              [Input('sankey', 'clickData'), Input('year_range', 'value')])
def display_value(clickData, value):
    print('Click Data:=======>', clickData)
    year_range = value
    year1 = year_range[0]
    year2 = year_range[1]
    full, sankey, level_wise_nodes, node, link = lit.generate_sankey_data(
        year_range[0], year_range[1])

    node_label = clickData['points'][0]['label']

    if node_label:
        for key in level_wise_nodes.keys():
            if node_label in level_wise_nodes[key]:
                clicked_node_level = key
                break
        msg = ''
        labels = []
        values = []
        title = ''
        if clicked_node_level == 1:
            targets = full.loc[full['metrics_lg'] == node_label, :]
            print('clicked data in full', targets.shape)
            total_papers = len(targets['paper_id'].unique())
            msg = '{} data has been used in {} papers'.format(
                node_label, total_papers)
            pie_data = targets['metrics_sm'].value_counts().to_dict()
            title = 'Type of features extracted from {} data'.format(
                node_label)
        elif clicked_node_level == 2:
            targets = full.loc[full['metrics_sm'] == node_label, :]
            total_papers = len(targets['paper_id'].unique())
            msg = '{} data has been used in {} papers'.format(
                node_label, total_papers)
            pie_data = targets['outcome_sm'].value_counts().to_dict()
            title = 'Type of outcomes found to associated with {}'.format(
                node_label)
        elif clicked_node_level == 3:
            targets = full.loc[full['outcome_sm'] == node_label, :]
            total_papers = len(targets['paper_id'].unique())
            msg = '{} construct has been used in {} papers'.format(
                node_label, total_papers)
            pie_data = targets['metrics_sm'].value_counts().to_dict()
            title = 'Type of metrics found to associated with {}'.format(
                node_label)
        elif clicked_node_level == 4:
            targets = full.loc[full['outcome_lg'] == node_label, :]
            total_papers = len(targets['paper_id'].unique())
            msg = '{} type of construct has been used in {} papers'.format(
                node_label, total_papers)
            pie_data = targets['outcome_sm'].value_counts().to_dict()
            title = 'Type of outcomes grouped under {}'.format(node_label)
        print_data = {}
        labels = [key for key in pie_data.keys()]
        values = [value for value in pie_data.values()]

        if clicked_node_level:
            print_data['level'] = clicked_node_level
        print_data['text'] = msg

        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
        fig.update_layout(title={'text': title, 'xanchor': 'left'})
        return fig
    else:
        return None


@app.callback(Output('sankey', 'figure'),
              [Input("enter", "n_clicks"), Input('year_range', 'value')],
              [State("larger_metric", "value"), State("smaller_metric", "value"), State("smaller_outcome", "value"), State("larger_outcome", "value")])
def display_value(n_clicks, value, lg_metric, sm_metric, sm_outcome, lg_outcome):
    print('===> Update-sankey-figure function called !!!!!-------------8')
    year_range = value
    year1 = year_range[0]
    year2 = year_range[1]
    selected_levels = {'metrics_lg': int(lg_metric),
                       'metrics_sm': int(sm_metric),
                       'outcome_sm': int(sm_outcome),
                       'outcome_lg': int(lg_outcome)
                       }
    full, sankey, _, node, link = lit.generate_sankey_data(
        year_range[0], year_range[1], selected_levels)

  
    figure = go.Figure(
        data=[
            go.Sankey(
                node=node,
                link=link,
            )
        ]
    )

    print('############        ######### New Sankey data:',sankey.shape)

    figure.update_layout(height=1100,
                         font_size=14)
    return figure

if __name__ == '__main__':
    app.run_server(debug=False)