import types
import textwrap
from docopt import docopt
import inspect
import sys
import importlib
from cmd3.shell import command
from cloudmesh_common.util import path_expand
from cloudmesh_common.util import banner
from cloudmesh.user.cm_user import cm_user
from cloudmesh.config.cm_config import cm_config
from cloudmesh.user.cm_template import cm_template
from cloudmesh_common.util import yn_choice
from cloudmesh.config.ConfigDict import ConfigDict
from sh import less
import os
from pprint import pprint
import yaml
import json
import ast

from cloudmesh.util.logger import LOGGER

log = LOGGER(__file__)

def shell_command_storm(arguments):
    """
    Usage:
      storm list
      storm ID
      storm register ID [--kind=KIND] [ARGUMENTS...]

    Arguments:

      list       list the available high level services to be provisioned.
      ID         list the user with the given ID
      ARGUMENTS  The name of the arguments that need to be passed

    Options:
      --kind=KIND  the kind of the storm. It can be chef, puppet, or other
                   frameworks. At this time we will focus on chef [default: chef].

       -v          verbose mode

    Description:
    
      Command to invoce a provisioning of high level services such as
      provided with chef, puppet, or other high level DevOps Tools. If
      needed the machines can be provisioned prior to a storm with
      rain. Together this forms a rain storm.

    """

    user = cm_user()

    if (arguments["list"]):

        print "not implemented"
        print "list"

    elif not (arguments["list"] or arguments["register"]):

        id = arguments["ID"]
        print "ID", id

    elif (arguments["register"]):

        id = arguments["ID"]
        kind = arguments['--kind']
        print arguments


    else:
        print "WRONG PARAMETERS"

    return

def main():
    arguments = docopt(shell_command_storm.__doc__)
    shell_command_storm(arguments)

if __name__ == '__main__':
    main()
