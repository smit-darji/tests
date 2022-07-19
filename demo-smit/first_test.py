import pytest
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
import sys
from src import sample


@pytest.fixture(scope="module", autouse=True)
def glue_context():
    sys.argv.append('--JOB_NAME')
    sys.argv.append('test_count')

    args = getResolvedOptions(sys.argv, ['JOB_NAME'])
    context = GlueContext(SparkContext.getOrCreate())
    job = Job(context)
    job.init(args['JOB_NAME'], args)

    yield(context)

    job.commit()


def test_counts(glue_context):
    dyf = sample.read_json(glue_context, "s3://smit-test-july/df_sample.csv")
    assert dyf.toDF().count() == 5
    dyf.toDF().show()

def test_transformation(glue_context):
    dyf = sample.GluePythonSampleTest().run("s3://smit-test-july/df_sample.csv")
    assert dyf.toDF().count() == 5   

def test_transformation2(glue_context):
    dyf = sample.GluePythonSampleTest().run("s3://smit-test-july/df_sample.csv")
    df =  dyf.toDF()  
    df.order_id.dtype == "Long"















# from src import sample

# def test_file1_method1():
#     x=6
#     y=6
#     z = sample.add(x, y)
#     print(">>>", z)

#     assert z < 10,"test fail"

# def test_file1_method2():
#     x=5
#     y=6
#     z = sample.add(x, y)
#     print(">>>", z)
#     assert x+y == z,"test Success"

# import pytest
# from pyspark.context import SparkContext
# from awsglue.context import GlueContext
# from awsglue.job import Job
# from awsglue.utils import getResolvedOptions
# import sys
# from src import sample


# @pytest.fixture(scope="module", autouse=True)
# def glue_context():
#     sys.argv.append('--JOB_NAME')
#     sys.argv.append('test_count')

#     args = getResolvedOptions(sys.argv, ['JOB_NAME'])
#     context = GlueContext(SparkContext.getOrCreate())
#     job = Job(context)
#     job.init(args['JOB_NAME'], args)

#     yield(context)

#     job.commit()


# def test_counts(glue_context):
#     dyf = sample.read_json(glue_context, "s3://smit-test-july/test.json")
#     assert dyf.toDF().count() == 1961
