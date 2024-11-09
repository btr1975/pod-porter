"""
CLI for pod_porter
"""

from argparse import ArgumentParser
from pod_porter.pod_porter import PorterMap


def cli_argument_parser() -> ArgumentParser:
    """Function to create the argument parser

    :rtype: ArgumentParser
    :returns: The argument parser
    """
    arg_parser = ArgumentParser(description="pod-porter")
    subparsers = arg_parser.add_subparsers(
        title="commands",
        description="Valid commands: a single command is required",
        help="CLI Help",
        dest="a single command please see the -h option",
    )
    subparsers.required = True

    # This is the sub parser to print hello
    arg_parser_template = subparsers.add_parser("template", help="View the rendered compose file")
    arg_parser_template.set_defaults(which_sub="template")
    arg_parser_template.add_argument("-n", "--name", required=True, help="Release name")
    arg_parser_template.add_argument("-m", "--map", required=True, help="Path to the map")

    return arg_parser


def cli() -> None:
    """Function to run the command line
    :rtype: None
    :returns: Nothing it is the CLI
    """
    arg_parser = None

    try:
        arg_parser = cli_argument_parser()
        args = arg_parser.parse_args()

        if args.which_sub == "template":
            obj = PorterMap(args.map, args.name)
            print(obj.render_compose())


    except AttributeError as error:
        print(f"\n !!! {error} !!! \n")
        arg_parser.print_help()

    except FileNotFoundError as error:
        print(f"\n !!! {error} !!! \n")
        arg_parser.print_help()

    except FileExistsError as error:
        print(f"\n !!! {error} !!! \n")
        arg_parser.print_help()

    except Exception as error:  # pylint: disable=broad-exception-caught
        print(f"\n !!! {error} !!! \n")
        arg_parser.print_help()
