"""
Source codes for pre-processing MMCA literature review dataset (data metrics)

author: Pankaj Chejara (pankajchejara23@gmail.com)


"""



class Paper:
    """
    A class used to represent a paper record

    Attributes
    -----------
    paper_record : str
        a string containing raw paper record for an individual paper
    paper_id : int
        an unique id of the paper
    pub_year : int
        publication year of the paper
    metrics_org : dict
        a dict containing metrics used in the paper. 
    metrics_sm : dict
        a dict containing first level grouping of original metrics (e.g., voice features -> speech features).
    metrics_lg : dict
        a dict containing second level grouping of original metrics (e.g., voice features -> verbal).
    outcome_sm : dict
        a dict containing first level grouping of original outcome (e.g., collaboration quality -> coordination)
    outcome_lg : dict
        a dict containing second level grouping of original outcome (e.g., collaboration quality -> process)
    relationship : dict
        a list of tuples mapping relationship between metrics and outcomes. 
    data_types : dict
        a dict containg types of data used in the paper.


    Methods
    -------
    get_paper_id ()
        Returns unique id of the paper
    get_pub_id ()
        Returns publication year of the paper
    get_metrics_org()
        Returns a dict of metrics used in the paper
    get_metrics_sm ()
        Returns a dict of first level grouping of metrics
    get_metrics_lg ()
        Returns a dict of second level grouping of metrics   
    get_outcome_sm ()
        Returns a dict of first level grouping of outcomes
    get_outcome_lg ()
        Returns a dict of second level grouping of outcomes
    get_relationship ()
        Returns list of tuples mapping metrics to outcomes
    get_data_types ()
        Returns a list of data used in the paper

    """
    def  __init__(self,paper_record):
        self.paper_record = self.parse_record(paper_record)
        self.paper_id = self.get_paper_id()
        self.pub_year = self.get_pub_year()
        self.metrics_org = self.get_metrics_org()
        self.metrics_sm = self.get_metrics_sm()
        self.metrics_lg = self.get_metrics_lg()
        self.outcomes_sm = self.get_outcomes_sm()
        self.outcomes_lg = self.get_outcomes_lg()
        self.relationship = self.parse_relationship()
        self.outcomes_type = self.get_outcomes_type()
        self.data_types = self.get_data_types()


    def parse_record(self,paper_record):
        """
        Returns
        ---------
        list
            return formatted paper record in a list
        """
        processed = paper_record.split('#')[0]
        items = processed.split(';')
        items_processed = []    
        for ind,item in enumerate(items):
            items_processed.append(item.replace('\n',';'))
        return items_processed


    def get_paper_id(self):
        """
        Returns
        ---------
        int
            an unique id of the paper
        """
        return self.paper_record[0]

    def get_pub_year(self):
        """
        Returns
        ---------
        int
            publication year of the paper
        """
        return self.paper_record[3]

    def get_metrics_org(self):
        """
        Returns
        ---------
        list
            Returns a list of metrics used in the paper
        """
        return self.get_parsed_items(self.paper_record[7])

    def get_metrics_sm(self):
        """
        Returns
        ---------
        list
            Returns a list of metrics grouping (first level) 
        """
        return self.get_parsed_items(self.paper_record[9])

    def get_metrics_lg(self):
        """
        Returns
        ---------
        list
            Returns a list of metrics groupping (second level) used in the paper
        """
        return self.get_parsed_items(self.paper_record[8])

    def get_outcomes_sm(self):
        """
        Returns
        ---------
        list
            Returns a list of outcomes groupping (first level) used in the paper
        """
        return self.get_parsed_items(self.paper_record[13])

    def get_outcomes_lg(self):
        """
        Returns
        ---------
        list
            Returns a list of outcomes groupping (second level) used in the paper
        """
        return self.get_parsed_items(self.paper_record[15])
    
    def get_outcomes_type(self):
        """
        Returns
        ---------
        list
            Returns a list of types of outcomes used in the paper
        """
        return self.get_parsed_items(self.paper_record[16])

    def get_data_types(self):
        """
        Returns
        ---------
        list
            Returns a list of data types used in the paper
        """
        return self.get_parsed_items(self.paper_record[3])
    
    def get_relationship(self):
        """
        Returns
        ---------
        dict
            Returns a mapping between metrics and outcomes
        """
        return self.paper_record[17]
    

    def get_parsed_items(self,text):
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
        text_items = text_no_quotes.split(';')
    
        pre_text_items = [item for item in text_items if item != '' ]        
        labels = [item.split(')')[1].strip() for item in pre_text_items]
        index = [item.split(')')[0].strip() for item in pre_text_items]
    
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
        
        data = self.get_relationship()
        
        if data.strip() == '':
            return []
        
        metrics_org = self.get_metrics_org()
        outcome_smaller = self.get_outcomes_sm()
        
        text_no_quotes = data.replace('\"','')
        text_items = text_no_quotes.split(';')
    
        pre_text_items = [item for item in text_items if item != '' ]
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
            for metric in metrics:
                for outcome in outcomes:
                    try:
                        rel_tuples.append((metrics_org[metric],outcome_smaller[outcome],rel_method))
                    except:
                        pass
        return rel_tuples  
    
    def __str__(self):
        return 'Paper id:{} Data:{}'.format(self.paper_id,self.data_types)

    def print_paper_record(self):
        print('\n####################   PAPER ID: {}     ####################\n'.format(self.paper_id))
        print('Data:',self.data_types)
        print('Metrics:',self.metrics_org)
        print('Metrics smaller:',self.metrics_sm)
        print('Metrics larger:',self.metrics_lg)
        print('Outcomes smaller:',self.outcomes_sm)
        print('Outcomes larger:',self.outcomes_lg)
        print('Outcomes type:',self.outcomes_type)
        print('Results:',self.relationship)
        print('\n############################################################\n')
    

class LiteratureDataset:
    """
    A class used to represent a collection of objects of class:Paper type
    
    Attributes
    -----------
    file_path : str
        a string containing path of CSV file of data_metric_sheet imported from MMCA literature review dataset
        
    """
    def  __init__(self,file_path):
        self.file_path = file_path
        self.paper_store = dict()
        self.paper_count = 0
        
    def getRecord(self,lines,index):
        """
        Function to parse data metric sheet. This function combines record expanding over multiple lines into a single record. 
        The proper exeuction of this function requires adding '#' in the last column of the sheet.
    
        params:
        
            lines: lines read from csv file.
            index: line number from where parsing starts for the new record
        
        returns:
    
            record    : parsed record in a single line
            line_index: line number for the next record
        
        """
    
        line = lines[index]
    

        line_index = index
        record = ''
        # adding line until stop symbol occurs
        while line_index < len(lines):
            record += lines[line_index]
            if '#' in lines[line_index]:
                break
            line_index += 1
        return record,line_index+1

    def get_all_papers(self):
        return self.paper_store
        
    def get_paper(self,id):
        if str(id) in list(self.paper_store.keys()):
            return self.paper_store[str(id)]
        else:
            print('There is no paper with given id.')
            return None



        
    def populate_dataset(self):
        try:
            file = open(self.file_path)
            lines = file.readlines()

            records = []
            current_record_index = 1
            
            print('1. Record parsing begins...')
            
            while current_record_index < len(lines):
                record,next_record_index = self.getRecord(lines,current_record_index)
    
                if record != '': # to address cases when empty line occurs
                    current_record_index = next_record_index
                    records.append(record)
                else:
                    current_record_index += 1
    
            print('2. Record parsing completed')
            print('   Total {} records are parsed'.format(len(records)))
            
            print('3. Populating literature dataset')
            
            for record in records:
                paper_object = Paper(record)
                self.paper_store[paper_object.paper_id] = paper_object
            
            print('4. Literature dataset is succefully populated')
            
        except:
            print('Error occurred while reading file from given path')
        
    
