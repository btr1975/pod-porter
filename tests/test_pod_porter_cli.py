from pod_porter.pod_porter_cli import cli_argument_parser


def test_cli_argument_parser_run_job_template():
    arg_parser = cli_argument_parser()
    args = arg_parser.parse_args(
        [
            "template",
            "-n",
            "some-release",
            "-m",
            "some-map",
        ]
    )

    assert args.which_sub == "template"
    assert args.name == "some-release"
    assert args.map == "some-map"
