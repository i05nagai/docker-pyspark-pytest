"""
Sample module depending on another module.
In this case, this module depends on `wordcount.py`.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pyspark
import sys

from . import wordcount


def word_counts(sc, filename):
    """word_counts

    :param filename:

    :return: word and counts.
    :rtype: dict
    """

    lines = sc.textFile(filename, 1)
    results = wordcount.do_word_counts(lines)
    return results


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: wordcount file}")

    sc = pyspark.SparkContext(appName="PythonWordCount")

    print(word_counts(sc, sys.argv[1]))
