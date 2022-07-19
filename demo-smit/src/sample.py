import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.types import *
from pyspark.sql import Row
from awsglue.job import Job
from awsglue.utils import getResolvedOptions


class GluePythonSampleTest:
    def __init__(self):
        params = []
        if '--JOB_NAME' in sys.argv:
            params.append('JOB_NAME')
        args = getResolvedOptions(sys.argv, params)

        self.context = GlueContext(SparkContext.getOrCreate())
        self.job = Job(self.context)

        if 'JOB_NAME' in args:
            jobname = args['JOB_NAME']
        else:
            jobname = "test"
        self.job.init(jobname, args)

    def run(self, path):
        dyf = read_json(self.context, path)
        dyf_applyMapping = ApplyMapping.apply( frame = dyf, mappings = [ 
     ("col0","String","order_id","Long"), 
     ("col1","String","customer_id","Long"),
     ("col2","String","essential_item","String"),
     ("col3","String","timestamp","Long"),
     ("col4","String","zip","Long")
    ])
        dyf_filter = Filter.apply(frame = dyf_applyMapping, f = lambda x: x["essential_item"] == 'YES') 
        return dyf_filter

        self.job.commit()


def read_json(glue_context, path):
    dynamicframe = glue_context.create_dynamic_frame.from_options(
        connection_type='s3',
        connection_options={
            'paths': [path],
            'recurse': True
        },
        format='csv'
    )
    return dynamicframe


if __name__ == '__main__':
    GluePythonSampleTest().run("s3://smit-test-july/df_sample.csv")
    




# from test.test_sample import test_file1_method1

# def add(x, y):
#     return x+y

# import sys
# from pyspark.context import SparkContext
# from awsglue.context import GlueContext
# from awsglue.job import Job
# from awsglue.utils import getResolvedOptions


# class GluePythonSampleTest:
#     def __init__(self):
#         params = []
#         if '--JOB_NAME' in sys.argv:
#             params.append('JOB_NAME')
#         args = getResolvedOptions(sys.argv, params)

#         self.context = GlueContext(SparkContext.getOrCreate())
#         self.job = Job(self.context)

#         if 'JOB_NAME' in args:
#             jobname = args['JOB_NAME']
#         else:
#             jobname = "test"
#         self.job.init(jobname, args)

#     def run(self):
#         dyf = read_json(self.context, "s3://smit-test-july/test.json")
#         dyf.printSchema()

#         self.job.commit()


# def read_json(glue_context, path):
#     dynamicframe = glue_context.create_dynamic_frame.from_options(
#         connection_type='s3',
#         connection_options={
#             'paths': [path],
#             'recurse': True
#         },
#         format='json'
#     )
#     return dynamicframe


# if __name__ == '__main__':
#     GluePythonSampleTest().run()