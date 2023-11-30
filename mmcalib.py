
"""
Source codes for pre-processing MMCA literature review dataset (data metrics)
author: Pankaj Chejara (pankajchejara23@gmail.com)
"""
from collections import Counter
import pandas as pd


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



    Methods
    -------
    get_paper_id ()
        Returns unique id of the paper
    get_pub_id ()
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
    dparsed_items()
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
        self.paper_record = paper_record
        self.paper_id = paper_record['id']
        self.pub_year = None
        self.sample_size = None
        self.study_setting = None
        self.task = None
        self.experimental_study = None

        # Input
        self.data = self.parsed_items(paper_record['data'])
        self.sensor = self.parsed_items(paper_record['sensor'])
        self.data_metric = self.parsed_items(paper_record['data_per_metric'])
        self.metrics_org = self.parsed_items(paper_record['metric'])
        self.metrics_sm = self.parsed_items(
            paper_record['metric_smaller_category'])
        self.metrics_lg = self.parsed_items(
            paper_record['metric_larger_category'])

        # Outcome
        self.outcomes_org = self.parsed_items(paper_record['outcome'])
        self.outcomes_sm = self.parsed_items(
            paper_record['outcome_smaller_category'])
        self.outcomes_lg = self.parsed_items(
            paper_record['outcome_larger_category'])
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

    def set_experimental_type(self, experimental_type):
        """
        Returns
        ---------
        list
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
        return self.study_setting

    def get_sensor(self):
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
        list
            Returns a list of metrics used in the paper
        """
        return self.metrics_org

    def get_metrics_sm(self):
        """
        Returns
        ---------
        list
            Returns a list of metrics grouping (first level)
        """
        return self.metrics_sm

    def get_metrics_lg(self):
        """
        Returns
        ---------
        list
            Returns a list of metrics groupping (second level) used in the paper
        """
        return self.metrics_lg

    def get_outcomes_instrument(self):
        """
        Returns
        ---------
        list
            Returns a list of outcome instruments used in the paper
        """
        return self.outcomes_instrument

    def get_outcomes_sm(self):
        """
        Returns
        ---------
        list
            Returns a list of outcomes groupping (first level) used in the paper
        """
        return self.outcomes_sm

    def get_outcomes_lg(self):
        """
        Returns
        ---------
        list
            Returns a list of outcomes groupping (second level) used in the paper
        """
        return self.outcomes_lg

    def get_outcomes_org(self):
        """
        Returns
        ---------
        list
            Returns a list of types of outcomes used in the paper
        """
        return self.outcomes_org

    def get_data(self):
        """
        Returns
        ---------
        list
            Returns a list of data types used in the paper
        """
        return self.data

    def get_experimental_type(self):
        """
        Returns
        ---------
        list
            Returns whether the study reported in the paper was experimental in nature.
        """
        return self.experimental_study

    def get_raw_relationship(self):
        """
        Returns
        ---------
        dict
            Returns a mapping between metrics and outcomes
        """
        return self.raw_relationship

    def parsed_items(self, text):
        """
        This general function takes a string which contains data in a particular format (e.g.,  VI) EDA).
        The function then process the string, extract the information in dictionary data structure.

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
        text_no_quotes = text.replace('\"', '')
        text_items = text_no_quotes.split('\n')

        pre_text_items = [item for item in text_items if item != '']
        labels = [item.split(')')[1].strip() for item in pre_text_items]
        index = [item.split(')')[0].strip() for item in pre_text_items]

        # changing case of index
        index = [item.lower() for item in index]

        pre_met = {}
        for ind, lab in zip(index, labels):
            pre_met[ind] = lab.lower()
        return pre_met

    def parse_relationship(self, item_index=False):
        """
        This function processess relationship data and prepare a mapping between metrics and outcomes.

        Returns
        ---------
        list

            a list containing tuples of three items (metrics,outcomes,method) representing relationship

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
                        rel_tuples.append(
                            (metric, outcome, rel_method, rel_type.strip()))
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
        if self.study_setting:
            print('Study setting:', self.study_setting)
        if self.task:
            print('Learning task:', self.task)
        if self.sample_size:
            print('Study setting:', self.sample_size)
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

    Attributes
    -----------
    data_metric_file_path : str
        a string containing path of CSV file of data_metric sheet imported from MMCA literature review dataset

    paper_details_file_path : str
        a string containing path of CSV file of paper details sheet imported from MMCA literature review dataset

    paper_meta_file_path : str
        a string containing path of CSV file of paper meta sheet imported from MMCA literature review dataset
    """

    def __init__(self, data_metric_file_path, paper_details_file_path, paper_meta_file_path):
        self.data_metric_file_path = data_metric_file_path
        self.paper_details_file_path = paper_details_file_path
        self.paper_meta_file_path = paper_meta_file_path
        self.paper_store = dict()
        self.paper_count = 0
        self.populate_dataset()

        try:
            self.update_year()
        except Exception as e:
            print(e)
            print('Literature dataset could not update publication year.')

        try:
            self.update_setting_task_sample_experimental()
        except Exception as e:
            print(e)
            print('Literature dataset could not update contextual information, e.g., study setting, learning task, sample size, and  experimental type.')

    def get_record(self, df, index):
        """
        Function to parse data metric sheet. This function combines record expanding over multiple lines into a single record.
        The proper exeuction of this function requires adding '#' in the last column of the sheet.

        params:

            df: Dataframe containing data_metric sheet of literature review

        returns:

            record    : parsed record in a single line
            line_index: line number for the next record

        """
        return df.iloc[index, :].to_dict()

    def update_year(self):
        """
        This function adds year information to each paper record.

        """
        year = pd.read_csv(self.paper_meta_file_path)
        pub_year = year[['ID updated', 'year']]
        pub_year.index = pub_year['ID updated']
        for ind in self.paper_store.keys():
            self.paper_store[ind].set_pub_year(
                pub_year.to_dict()['year'][int(ind)])

    def generate_sankey_data(self, year1=2000, year2=2005, selected_levels={'metrics_lg': 2, 'metrics_sm': 1, 'outcome_sm': 4, 'outcome_lg': 3}):
        """
        This general function takes a string which contains data in a particular format (e.g.,  VI) EDA).
        The function then process the string, extract the information in dictionary data structure.

        Parameters
        ----------
        year1 : int
            starting year for filtering
        year2 : int
            ending year for filtering
        selected_levels : dict
            dictionary containing levels for each node type to configure sankey diagram


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
        papers = self.get_papers_between_interval(year1, year2)
        sankey = pd.DataFrame(
            columns=['source', 'target', 'level', 'paper_id', 'year', 'color', 'edge_label'])

        full = pd.DataFrame(
            columns=['metrics_lg', 'metrics_sm', 'outcome_sm',
                     'outcome_lg', 'paper_id', 'year']
        )
        nodes_level = {}
        nodes_color = {}
        link_color = {}
        level_wise_nodes = {
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
            for rel in rels:
                check = 0

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
                    if metrics_lg[rel[0]] == metrics_sm[rel[0]] or outcome_sm[rel[1]] == outcome_lg[rel[1]]:
                        continue

                    if metrics_lg[rel[0]] not in nodes_level.keys():
                        nodes_level[metrics_lg[rel[0]]
                                    ] = selected_levels['metrics_lg'] if selected_levels else .1
                        nodes_color[metrics_lg[rel[0]]
                                    ] = color[available_color_index]
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

                    if outcome_sm[rel[1]] not in nodes_level.keys():
                        nodes_level[outcome_sm[rel[1]]
                                    ] = selected_levels['outcome_sm'] if selected_levels else .5
                        nodes_color[outcome_sm[rel[1]]
                                    ] = nodes_color[outcome_lg[rel[1]]]
                        level_wise_nodes[3].append(outcome_sm[rel[1]])

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

                    temp = pd.DataFrame({'source': source,
                                         'target': target,
                                         'level': 1,
                                         'paper_id': paper.paper_id,
                                         'year': paper.pub_year,
                                         'edge_label': edge_label,
                                         'color': reduce_intensity(nodes_color[source])},
                                        index=[0])
                    sankey = pd.concat([sankey, temp], axis=0)

                    source = eval(node_type_names[1])[
                        rel[0]] if 'metric' in node_type_names[1] else eval(node_type_names[1])[rel[1]]
                    target = eval(node_type_names[2])[
                        rel[0]] if 'metric' in node_type_names[2] else eval(node_type_names[2])[rel[1]]
                    edge_label = '{}:{}-{}'.format(paper.paper_id,
                                                   source, target)

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

                    temp = pd.DataFrame({'source': source, 'target': target,
                                         'level': 3,
                                         'paper_id': paper.paper_id,
                                         'year': paper.pub_year,
                                         'edge_label': edge_label,
                                         'color': reduce_intensity(nodes_color[target])},
                                        index=[0])
                    sankey = pd.concat([sankey, temp], axis=0)

                    temp_full = pd.DataFrame({'metrics_lg': metrics_lg[rel[0]],
                                              'metrics_sm': metrics_sm[rel[0]],
                                              'outcome_sm': outcome_sm[rel[1]],
                                              'outcome_lg': outcome_lg[rel[1]],
                                              'paper_id': paper.paper_id,
                                              'year': paper.pub_year},
                                             index=[0])
                    full = pd.concat([full, temp_full], axis=0)

        # sankey.drop_duplicates(inplace=True)
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
                                                    'customdata': linked_paper_ids,
                                                    'hovertemplate': 'Paper id:%{customdata}'}

    def count_or_mean(self, year1=2000, year2=2010):
        """
        This function count frequencies for each characteristic of the papers

        Returns
        ---------
        dict
            dictionary containing frequency count for all attributes of Paper class
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
        context.index = context_org.ID_updated
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
            print('year:',paper.pub_year)
            pub_year = int(paper.pub_year)

            if pub_year > start_year and pub_year <= end_year:
                results.append(paper)
        print('Total {} papers found between'.format(len(results)))
        return results

    def get_paper(self, id):
        """
        This function return a list containing all paper records published between specified interval.

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
        print('Populating with paper records ...')
        for paper_id in df.index:
            record = self.get_record(df, paper_id)
            paper_object = Paper(record)
            self.paper_store[paper_object.paper_id] = paper_object

        print('Literature dataset is succefully populated. \n  Total papers:', len(
            self.paper_store))
