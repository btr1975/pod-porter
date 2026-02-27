"""
CLI for pod_porter
"""

import json
from pathlib import Path
from argparse import ArgumentParser
from importlib.metadata import version

from yaml import safe_load
from pod_porter.pod_porter import PorterMapsRunner, validate_json_against_schema
from pod_porter.util.file_read_write import write_file, create_tar_gz_file, extract_tar_gz_file, create_new_map


def common_sub_parser_map_arguments(sub_arg_parser: ArgumentParser) -> None:
    """Add common arguments to a sub parser

    :type sub_arg_parser: ArgumentParser
    :param sub_arg_parser: The sub parser to add the arguments to

    :rtype: None
    :returns: Nothing it appends the arguments to the sub parser
    """
    sub_arg_parser.add_argument("-m", "--map", required=True, help="Path to the map")


def common_sub_parser_arguments(sub_arg_parser: ArgumentParser) -> None:
    """Add common arguments to a sub parser

    :type sub_arg_parser: ArgumentParser
    :param sub_arg_parser: The sub parser to add the arguments to

    :rtype: None
    :returns: Nothing it appends the arguments to the sub parser
    """
    sub_arg_parser.add_argument("-n", "--name", required=True, help="Release name")
    common_sub_parser_map_arguments(sub_arg_parser=sub_arg_parser)
    sub_arg_parser.add_argument(
        "-f",
        "--file-values",
        required=False,
        default=None,
        help="Path to the values you want to use instead of the map values",
    )


def common_sub_parser_output_path(sub_arg_parser: ArgumentParser) -> None:
    """Add common arguments to a sub parser

    :type sub_arg_parser: ArgumentParser
    :param sub_arg_parser: The sub parser to add the arguments to

    :rtype: None
    :returns: Nothing it appends the arguments to the sub parser
    """
    sub_arg_parser.add_argument("-o", "--output", required=True, help="Path to output file/files")


def cli_argument_parser() -> ArgumentParser:
    """Function to create the argument parser

    :rtype: ArgumentParser
    :returns: The argument parser
    """
    arg_parser = ArgumentParser(description=f"pod-porter version: {version('pod-porter')}")
    subparsers = arg_parser.add_subparsers(
        title="commands",
        description="Valid commands: a single command is required",
        help="CLI Help",
        dest="a single command please see the -h option",
    )
    subparsers.required = True

    # This is the sub parser to print the rendered compose file
    arg_parser_template = subparsers.add_parser("template", help="View the rendered compose file")
    arg_parser_template.set_defaults(which_sub="template")
    common_sub_parser_arguments(sub_arg_parser=arg_parser_template)

    # This is the sub parser to write the rendered compose file
    arg_parser_template_write = subparsers.add_parser("write", help="Write the rendered compose file")
    arg_parser_template_write.set_defaults(which_sub="template_write")
    common_sub_parser_arguments(sub_arg_parser=arg_parser_template_write)
    common_sub_parser_output_path(sub_arg_parser=arg_parser_template_write)

    # This is the sub parser to package the map
    arg_parser_map_package = subparsers.add_parser("package", help="Package the map (tar.gz) the map")
    arg_parser_map_package.set_defaults(which_sub="package")
    common_sub_parser_map_arguments(sub_arg_parser=arg_parser_map_package)
    common_sub_parser_output_path(sub_arg_parser=arg_parser_map_package)

    # This is the sub parser to un-package the map
    arg_parser_map_unpackage = subparsers.add_parser("un-package", help="Un-Package the map extract (tar.gz)")
    arg_parser_map_unpackage.set_defaults(which_sub="un-package")
    common_sub_parser_map_arguments(sub_arg_parser=arg_parser_map_unpackage)
    common_sub_parser_output_path(sub_arg_parser=arg_parser_map_unpackage)

    # This is the sub parser to create a new map
    arg_parser_map_create = subparsers.add_parser("create", help="Create a new map, with some examples")
    arg_parser_map_create.set_defaults(which_sub="create")
    common_sub_parser_map_arguments(sub_arg_parser=arg_parser_map_create)

    # This is the sub parser to validate a compose file
    arg_parser_validate_compose = subparsers.add_parser("validate-compose", help="Validate a compose file")
    arg_parser_validate_compose.set_defaults(which_sub="validate-compose")
    arg_parser_validate_compose.add_argument("-f", "--file", required=True, help="Path to the compose file")

    # This is the sub parser to validate values file against schema
    arg_parser_validate_values = subparsers.add_parser(
        "validate-values", help="Validate a values file against a schema"
    )
    arg_parser_validate_values.set_defaults(which_sub="validate-values")
    arg_parser_validate_values.add_argument("-f", "--file", required=True, help="Path to the values file")
    arg_parser_validate_values.add_argument("-s", "--schema", required=True, help="Path to the values-schema.json")

    return arg_parser


def cli() -> None:  # pragma: no cover # pylint: disable=too-many-branches,too-many-statements
    """Function to run the command line

    :rtype: None
    :returns: Nothing it is the CLI
    """
    arg_parser = None

    try:
        arg_parser = cli_argument_parser()
        args = arg_parser.parse_args()

        if args.which_sub == "template":
            obj = PorterMapsRunner(path=args.map, release_name=args.name, values_override=args.file_values)
            print(obj.render_compose())

        if args.which_sub == "template_write":
            obj = PorterMapsRunner(path=args.map, release_name=args.name, values_override=args.file_values)
            map_name = obj.get_map_data().name
            map_version = obj.get_map_data().version
            file_name = f"{args.name}-{map_name}-{map_version}.yaml"
            write_file(path=args.output, file_name=file_name, data=obj.render_compose())

        if args.which_sub == "package":
            obj = PorterMapsRunner(path=args.map)
            map_name = obj.get_map_data().name
            map_version = obj.get_map_data().version
            file_name = f"{map_name}-{map_version}.tar.gz"
            create_tar_gz_file(path=args.map, file_name=file_name, output_path=args.output)

        if args.which_sub == "un-package":
            extract_tar_gz_file(path=args.map, output_path=args.output)

        if args.which_sub == "create":
            create_new_map(map_name_and_path=args.map)

        if args.which_sub == "validate-compose":
            compose_file_path: Path = Path(args.file)

            if not compose_file_path.is_file():
                raise FileNotFoundError(f"File not found: {compose_file_path}")

            data = safe_load(compose_file_path.read_text(encoding="utf-8"))

            try:
                PorterMapsRunner.validate_compose_json_schema(compose_data=data)

            except ValueError as error:
                print(error)

        if args.which_sub == "validate-values":
            values_file = Path(args.file)

            if not values_file.is_file():
                raise FileNotFoundError(f"File not found: {values_file}")

            values_file_data = safe_load(values_file.read_text(encoding="utf-8"))

            values_schema_file = Path(args.schema)

            if not values_schema_file.is_file():
                raise FileNotFoundError(f"File not found: {values_schema_file}")

            values_schema_data = json.loads(values_schema_file.read_text(encoding="utf-8"))

            try:
                validate_json_against_schema(values_data=values_file_data, json_schema=values_schema_data)

            except ValueError as error:
                print(error)

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
