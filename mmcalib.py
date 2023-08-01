"""
Source codes for pre-processing MMCA literature review dataset (data metrics)

author: Pankaj Chejara (pankajchejara23@gmail.com)


"""
"""
Source codes for pre-processing MMCA literature review dataset (data metrics)

author: Pankaj Chejara (pankajchejara23@gmail.com)


"""



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
    def  __init__(self,paper_record):
        self.paper_record = paper_record
        self.paper_id = paper_record['id']
        self.pub_year = None
        self.sample_size = None
        self.study_setting = None
        self.task = None

        # Input
        self.data = self.parsed_items(paper_record['data'])
        self.sensor = self.parsed_items(paper_record['sensor'])
        self.data_metric = self.parsed_items(paper_record['data_per_metric'])
        self.metrics_org = self.parsed_items(paper_record['metric'])
        self.metrics_sm = self.parsed_items(paper_record['metric_smaller_category'])
        self.metrics_lg = self.parsed_items(paper_record['metric_larger_category'])

        # Outcome
        self.outcomes_org = self.parsed_items(paper_record['outcome'])
        self.outcomes_sm = self.parsed_items(paper_record['outcome_smaller_category'])
        self.outcomes_lg = self.parsed_items(paper_record['outcome_larger_category'])
        self.outcomes_instrument = self.parsed_items(paper_record['outcome_instrument'])

        # Relationship
        self.raw_relationship = paper_record['analysis_and_results mm-oo:analysis:resultsig']


    def set_pub_year(self,year):
        """
        Attributes
        ---------
        year: int
            set publication year
        """
        self.pub_year = year

    def set_study_setting(self,study_setting):
        """
        Attributes
        ---------
        year: str
            set setting type of research study
        """
        self.study_setting = study_setting

    def set_sample_size(self,sample):
        """
        Attributes
        ---------
        year: str
            set sample size
        """
        self.sample_size = sample

    def set_task(self,task):
        """
        Attributes
        ---------
        year: int
            set publication year
        """
        self.task = task


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
        return self.get_metrics_org

    def get_metrics_sm(self):
        """
        Returns
        ---------
        list
            Returns a list of metrics grouping (first level)
        """
        return self.get_metrics_sm

    def get_metrics_lg(self):
        """
        Returns
        ---------
        list
            Returns a list of metrics groupping (second level) used in the paper
        """
        return self.get_metrics_lg

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
        return self.get_outcomes_sm

    def get_outcomes_lg(self):
        """
        Returns
        ---------
        list
            Returns a list of outcomes groupping (second level) used in the paper
        """
        return self.get_outcomes_lg

    def get_outcomes(self):
        """
        Returns
        ---------
        list
            Returns a list of types of outcomes used in the paper
        """
        return self.get_outcomes

    def get_data(self):
        """
        Returns
        ---------
        list
            Returns a list of data types used in the paper
        """
        return self.data

    def get_raw_relationship(self):
        """
        Returns
        ---------
        dict
            Returns a mapping between metrics and outcomes
        """
        return self.raw_relationship


    def parsed_items(self,text):
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
        text_no_quotes = text.replace('\"','')
        text_items = text_no_quotes.split('\n')

        pre_text_items = [item for item in text_items if item != '' ]
        labels = [item.split(')')[1].strip() for item in pre_text_items]
        index = [item.split(')')[0].strip() for item in pre_text_items]

        # changing case of index
        index = [item.lower() for item in index]

        pre_met = {}
        for ind,lab in zip(index,labels):
            pre_met[ind] = lab.lower()
        return pre_met


    def parse_relationship(self):
        """
        This function processess relationship data and prepare a mapping between metrics and outcomes.

        Returns
        ---------
        list

            a list containing tuples of three items (metrics,outcomes,method) representing relationship

        """
        data = self.raw_relationship

        data = data.replace('+',',')
        data = data.replace('*',',')

        if data.strip() == '':
            return []

        metrics_org = self.metrics_org
        metrics_sm = self.metrics_sm
        outcome_smaller = self.outcomes_sm

        print(metrics_org)

        text_no_quotes = data.replace('\"','')
        text_items = text_no_quotes.split('\n')

        pre_text_items = [item for item in text_items if item != '' ]

        rel_tuples = []

        print(pre_text_items)


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
                    rel_tuples.append((metrics_sm[metric],outcome_smaller[outcome],rel_method))

        return rel_tuples

    def __str__(self):
        return 'Paper id:{} '.format(self.paper_id,self.data_types)

    def print_paper_record(self):
        """
            This function print the paper record.
        """
        print('\n####################   PAPER ID: {}     ####################\n'.format(self.paper_id))
        if self.pub_year:
            print('Year:',self.pub_year)
        if self.study_setting:
            print('Study setting:',self.study_setting)
        if self.task:
            print('Learning task:',self.task)
        if self.sample_size:
            print('Study setting:',self.sample_size)
        print('Data:',self.data)
        print('Metrics:',self.metrics_org)
        print('Metrics smaller:',self.metrics_sm)
        print('Metrics larger:',self.metrics_lg)
        print('Outcomes:',self.outcomes_org)
        print('Outcomes smaller:',self.outcomes_sm)
        print('Outcomes larger:',self.outcomes_lg)
        print('Outcomes instrument:',self.outcomes_instrument)
        print('Results:',self.raw_relationship)
        print('Results:',self.parse_relationship())
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
    def  __init__(self,data_metric_file_path,paper_details_file_path,paper_meta_file_path):
        self.data_metric_file_path = data_metric_file_path
        self.paper_details_file_path = paper_details_file_path
        self.paper_meta_file_path = paper_meta_file_path
        self.paper_store = dict()
        self.paper_count = 0
        self.populate_dataset()

        try:
            self.update_year()
        except:
            print('Literature dataset could not update publication year.')

        try:
            self.update_setting_task_sample()
        except:
            print('Literature dataset could not update contextual information, e.g., study setting, learning task, and sample size.')


    def get_record(self,df,index):
        """
        Function to parse data metric sheet. This function combines record expanding over multiple lines into a single record.
        The proper exeuction of this function requires adding '#' in the last column of the sheet.

        params:

            df: Dataframe containing data_metric sheet of literature review

        returns:

            record    : parsed record in a single line
            line_index: line number for the next record

        """
        return df.iloc[index,:].to_dict()

    def update_year(self):
        """
        This function adds year information to each paper record.

        """
        year = pd.read_csv(self.paper_meta_file_path)
        pub_year = year[['ID_updated','year']]
        pub_year.index = pub_year.ID_updated
        for ind in self.paper_store.keys():
            self.paper_store[ind].set_pub_year(pub_year.to_dict()['year'][int(ind)])



    def update_setting_task_sample(self):
        """
        This function adds details of sample size, type of study settings, and learning task.

        """
        context_org = pd.read_csv(self.paper_details_file_path)
        context = context_org[['study_setting','task','sample_size']]
        context.index = context_org.ID_updated
        for ind in self.paper_store.keys():
            self.paper_store[ind].set_study_setting(context.to_dict()['study_setting'][int(ind)])
            self.paper_store[ind].set_task(context.to_dict()['task'][int(ind)])
            self.paper_store[ind].set_sample_size(context.to_dict()['sample_size'][int(ind)])

        print('Updates paper records with study setting, learning task and sample size')

    def get_papers(self):
        """
        This function return a list containing all paper records.

        Returns
        ---------
        list
            list of all paper records

        """
        return self.paper_store

    def get_papers_between_interval(self,start_year,end_year):
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
        for paper_id,paper in self.paper_store.items():

            pub_year = int(paper.pub_year)

            if pub_year > start_year and pub_year <= end_year:
                results.append(paper)
        print('Total {} papers found between'.format(len(results)))
        return results

    def get_paper(self,id):
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
        if str(id) in list(self.paper_store.keys()):
            return self.paper_store[str(id)]
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
            record = self.get_record(df,paper_id)
            paper_object = Paper(record)
            self.paper_store[paper_object.paper_id] = paper_object

        print('Literature dataset is succefully populated. \n  Total papers:',len(self.paper_store))


    
