from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import map_parameters
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.variables import Variables
from cloudmesh.common.util import banner

class MllogCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_mllog(self, args, arguments):
        """
        ::

          Usage:
                mllog check --file=FILE [--benchmark=BENCHMARK]
                mllog check --dir=DIRECTORY [--benchmark=BENCHMARK]
                mllog grep --file=FILE [--benchmark=BENCHMARK]

          This command checks the science mllog format before submission.

          Arguments:
              FILE        a log file containing mlcommons logging events
              DIRECTORY   the mlcommons root directory in which the log files are located

          Options:
              --file=FILE      a log file containing mlcommons logging events
              --dir=DIRECTORY  the root directory to be checked
              --benchmark=BENCHMARK  the name of the benchmark. IF not specified it is the directory name

          Description:

            TBD

        """

        banner("arguments", color="RED")


        map_parameters(arguments,
                       "file",
                       "benchmark")
        arguments.directory = arguments["--dir"]

        VERBOSE(arguments)

        if arguments.check and arguments.file:
            raise NotImplementedError

        elif arguments.check and arguments.directory:
            raise NotImplementedError

        elif arguments.grep and arguments.file:
            raise NotImplementedError

        return ""
