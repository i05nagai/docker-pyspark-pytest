[![Build Status](https://travis-ci.org/i05nagai/docker-pyspark-pytest.svg?branch=master)](https://travis-ci.org/i05nagai/docker-pyspark-pytest)

## Overviews
* [makoto-nagai/docker-pyspark: Docker image of Apache Spark with its Python interface, pyspark.](https://github.com/makoto-nagai/docker-pyspark)
    * Base docker image
* pytest
    * 3.1.2
* pytest-cov
    * latest
* pytest-mock
    * 1.6.2
* pytest-pep8
    * latest
* pytest-faker
    * 2.0.0
* pytest-env
    * 0.6.2

To run `pytest`, you need to replace `repository_name` with your name of repository (more specifically directory name).

```
docker run -it --rm \
  --volume $(pwd):/tmp/repository_name \
  --workdir /tmp/repository_name \
  i05nagai/pyspark-pytest:latest \
  pytest
```

or by using short option

```
docker run --rm -it \
  -v $(pwd):/tmp/repository_name \
  -w /tmp/repository_name \
  i05nagai/pyspark-pytest:latest \
  pytest
```

For instance, run the examples, 

```
docker run -it \
  --volume $(pwd):/opt/local/pyspark-pytest \
  --workdir /opt/local/pyspark-pytest \
  i05nagai/pyspark-pytest:latset \
  pytest --cov=. --pep8
```

See `docker_run_example.sh`.


## Notes
If you change the version of pytest, you need to add git-tag to the commit.
For instance, if the version of pytest is `3.1.2`, you need to execute the following commands.

```
git tag -a pytest-3.1.2
git push origin pytest-3.1.2
```

Then you can push your commits to the remote repository.

