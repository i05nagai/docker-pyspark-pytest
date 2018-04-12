import pytest
import my_pyspark_lib.wordcount_use as target


@pytest.mark.usefixtures("spark_context")
def test_word_counts(spark_context, mocker):
    """ test word couting
    Args:
        spark_context: test fixture SparkContext
    """
    # noqa
    # this is for package dependecies issues. See
    # https://www.cloudera.com/documentation/enterprise/5-5-x/topics/spark_python.html
    # spark_context.addPyFile(target.__file__)

    filename = ''
    read_data = [
        ' hello spark ',
        ' hello again spark spark'
    ]
    mock = mocker.mock_open(read_data=read_data)
    mocker.patch.object(target, 'open', mock)
    # mock().write.assert_called_once_with(expected_text)
    # mock().read.assert_called_once()
    results = target.word_counts(spark_context, filename)

    expected_results = {
        'hello': 2,
        'spark': 3,
        'again': 1
    }
    assert results == expected_results
