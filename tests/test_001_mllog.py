###############################################################
# pytest -v --capture=no tests/test_001_mllog.py
# pytest -v  tests/test_001_mllog.py
# pytest -v --capture=no  tests/test_001_mllog.py::Testmllog::<METHODNAME>
###############################################################
import pytest
from cloudmesh.common.Benchmark import Benchmark
from cloudmesh.common.Shell import Shell
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import HEADING
import os
from cloudmesh.mllog import MLLOG
from pprint import pprint

@pytest.mark.incremental
class TestConfig:

    def test_help(self):
        HEADING()
        Benchmark.Start()
        result = Shell.run("cms mllog help")
        Benchmark.Stop()
        VERBOSE(result)

        assert "mllog check" in result
        assert "mllog grep" in result

    def test_logfile(self):
        HEADING()
        Benchmark.Start()
        result = Shell.cat("tests/mlperf_cloudmask.log")
        Benchmark.Stop()
        VERBOSE(result)

        assert  result is not None
        assert ":::MLLOG" in result

    def test_grep(self):
        HEADING()
        Benchmark.Start()
        mllog = MLLOG()
        result = mllog.grep("tests/mlperf_cloudmask.log")
        Benchmark.Stop()
        print(result)

        assert ":::MLLOG" in result

    def test_list_of_dicts(self):
        HEADING()
        Benchmark.Start()
        mllog = MLLOG()
        entries = mllog.grep("tests/mlperf_cloudmask.log")
        list_of_dicts = mllog.content_to_list_of_dicts(entries)
        Benchmark.Stop()
        pprint(list_of_dicts)

        # assert ":::MLLOG" in result

    def test_org(self):
        HEADING()
        Benchmark.Start()
        mllog = MLLOG()
        success = mllog.find_org("tests/mlperf_cloudmask.log")
        Benchmark.Stop()
        assert success

    def test_intervalls(self):
        HEADING()
        Benchmark.Start()
        mllog = MLLOG()
        intervals = mllog.find_intervals("tests/mlperf_cloudmask.log")
        Benchmark.Stop()
        print(intervals)

    def test_benchmark(self):
        HEADING()
        Benchmark.print(csv=True, sysinfo=False, tag="mllog")
