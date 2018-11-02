import pandas

# ------------------------------
# constants
MIN_AF_SUPPORT = 0.05
COLUMN_HEADERS = (
    'sequence_name'       ,
    'position'            ,
    'ref_allele'          ,
    'alt_allele'          ,
    'total_read_depth'    ,
    'reads_supporting_ref',
    'reads_supporting_alt',
)

ROW_MAJOR_DATA = [
    ('1' , 10403    , 'ACCCTAACCCTAACCCTAACCCTAACCCTAACCCTAAC', 'A'    , 33, 27,  6),
    ('1' , 10409    , 'ACCCTAACCCTAACCCTAACCCTAACCCTAAC'      , 'A'    , 27, 20,  7),
    ('1' , 10492    , 'C'                                     , 'T'    , 44, 35,  9),
    ('1' , 10583    , 'G'                                     , 'A'    , 41, 32,  9),
    ('13', 53190918 , 'C'                                     , 'CAAA' ,  3,  1,  2),
    ('13', 53191123 , 'A'                                     , 'C'    , 35, 17, 18),
    ('16', 84403006 , 'CCCTT'                                 , 'C'    , 37,  0, 37),
    ('16', 84403110 , 'CT'                                    , 'C'    , 48, 21, 27),
    ('7' , 144427996, 'G'                                     , 'T'    , 37, 24, 13),
    ('Y' , 25592900 , 'C'                                     , 'CTATA',  8,  0,  8),
    ('Y' , 25592940 , 'C'                                     , 'A'    ,  7,  1,  6),
    ('Y' , 25593187 , 'T'                                     , 'C'    ,  4,  0,  4),
    ('Y' , 26716226 , 'G'                                     , 'T'    , 21,  0, 21),
]


# ------------------------------
# functions for DataFrame application
def is_short_allele_sequence(allele_seq):
    return len(allele_seq) < 50

def is_snv_calc(dfrow):
    return len(dfrow['ref_allele']) == len(dfrow['alt_allele'])

def is_snv(is_snv):
    return is_snv

def allelic_fraction_by_row(dfrow):
    afrac = float(dfrow['reads_supporting_alt'])/float(dfrow['total_read_depth'])
    return afrac

def is_supported_alt_allele(alt_allele_fraction, af_support=MIN_AF_SUPPORT):
    return alt_allele_fraction > af_support

# ------------------------------
# classes
class DataFrameProcessor(object):
    def __init__(self, dataframe, **kwargs):
        super(DataFrameProcessor, self).__init__(**kwargs)
        self.dataframe = dataframe

    def filter(self, col_to_filter, fn_filter_val):
        self.dataframe = self.dataframe[self.dataframe[col_to_filter].apply(fn_filter_val)]
        return self 
    
    def add_column_from_rows(self, new_col_name, fn_row_processor):
        self.dataframe[new_col_name] = self.dataframe.apply(fn_row_processor, axis=1)
        return self

    def get_result_dataframe(self):
        return self.dataframe

          
# ------------------------------
# Main code
test_dataframe = pandas.DataFrame(data=ROW_MAJOR_DATA, columns=COLUMN_HEADERS)

# Objective: In class DataFrameProcessor above, implement code to support the below
# interface.
result_dataframe = (
    DataFrameProcessor(test_dataframe).filter('ref_allele', is_short_allele_sequence)
                                      .add_column_from_rows('alt_allelic_fraction', allelic_fraction_by_row)
                                      .filter('alt_allelic_fraction', is_supported_alt_allele)
                                      .get_result_dataframe()
)

print(result_dataframe)

# BONUS:
# use DataFrameProcessor filter and add_column_from_rows methods to filter out
# SNVs from result_dataframe.


result_dataframe_snvs = (
    DataFrameProcessor(test_dataframe).filter('ref_allele', is_short_allele_sequence)
                                      .add_column_from_rows('alt_allelic_fraction', allelic_fraction_by_row)
                                      .filter('alt_allelic_fraction', is_supported_alt_allele)
                                      .add_column_from_rows('is_snv', is_snv_calc)
                                      .filter('is_snv', is_snv)
                                      .get_result_dataframe()
)

print(result_dataframe_snvs)