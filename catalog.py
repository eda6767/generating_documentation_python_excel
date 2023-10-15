# -*- coding: utf-8 -*-

class Catalog:
    
    def __init__(self, area, user=None, tables=None, data=None, file_name=None, columns= None, extra_columns=None):
        self.area = area
        self.data = data
        self.tables = tables
        self.file_name = file_name
        self.columns = columns
        self.extra_columns = extra_columns
        self.user = user
        
        
    def __str__(self):
        return 'Area for object : {}'.format(self.area)
        
    def choose_metrics(self, input):
        self.data = input.data[input.data['AREA_NAME']==self.area]
        
        
    def pick_tables(self, data):
        l=self.data['TABLE'].unique()
        self.tables = l
    
        
    def pick_columns(self, data):
        m = self.data.columns
        self.columns = m
        
    def pick_extra_columns(self):
        ec = ["Metric's name", "Area's name", 'Target table', "Metric's ID",
                              'Metric description', 'Metric type', 'Metric version', 'Function', 'Grouping key',
                              'Target table synonym', 'File name for metrics custom/sql', 'Main expression',
                              ' Aggregation period', 'Where condition', "Metric's status : PROD/TEST/DEV"]
        self.extra_columns = ec


if __name__ == "__catalog__":
    pass

















