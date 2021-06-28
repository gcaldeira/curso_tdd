import argparse
import json
import os
import re
import sys
from glob import glob

import pytest

# Args
_CAPABILITIES_PYTEST_ARG = '--capabilities'
_CONFIG_FILE_PYTEST_ARG = '--config-file'
_PROJECT_PYTEST_ARG = '--project'

# Caps
_PLATFORM_NAME_CAPABILITY = 'platformName'

# Session info
_SESSION_INFO_CONFIG = 'session'
_PROJECT_SESSION_INFO = 'project'

# Patterns
_PLATFORM_NAME_PATTERN_GROUP = 'platform'
_PLATFORM_NAME_PATTERN = rf'{_PLATFORM_NAME_CAPABILITY}=(?P<{_PLATFORM_NAME_PATTERN_GROUP}>\w+)'

# Folders
_TESTS_FOLDER = 'tests'


def _get_args():
    parser = argparse.ArgumentParser(
        description='A script for collecting and running tests within a project using pytest.',
        epilog='All other arguments will be interpreted as pytest arguments for the test suite run.'
    )
    parser.add_argument(
        '--pytest-help', action='store_true', help='Show the "pytest --help" output for the given test suite.'
    )
    return parser.parse_known_args()


# def _get_arg_value(arg, args):
#     try:
#         project = args[args.index(arg) + 1]
#     except IndexError:
#         raise ValueError(f'The provided parameter "{arg}" has no value.')
#     else:
#         return project
#
#
# def _get_platform(pytest_args, cfg_file_session_data):
#     if _CAPABILITIES_PYTEST_ARG in pytest_args:
#         capabilities = _get_arg_value(arg=_CAPABILITIES_PYTEST_ARG, args=pytest_args)
#         platform_match = re.search(_PLATFORM_NAME_PATTERN, capabilities)
#         if platform_match:
#             return platform_match.group(_PLATFORM_NAME_PATTERN_GROUP)
#     if cfg_file_session_data:
#         return cfg_file_session_data.get(_PLATFORM_NAME_CAPABILITY)
#     raise ValueError(f'The "{_PLATFORM_NAME_CAPABILITY}" must be provided via command line or capabilities file...')
#
#
# def _get_project(pytest_args, cfg_file_session_data):
#     if _PROJECT_PYTEST_ARG in pytest_args:
#         return _get_arg_value(arg=_PROJECT_PYTEST_ARG, args=pytest_args)
#     elif cfg_file_session_data:
#         return cfg_file_session_data.get(_PROJECT_SESSION_INFO)
#     raise ValueError(f'The "{_PROJECT_SESSION_INFO}" must be provided via command line or capabilities file...')
#
#
# def _load_config_file_session_data(pytest_args):
#     if _CONFIG_FILE_PYTEST_ARG in pytest_args:
#         try:
#             config_file = _get_arg_value(arg=_CONFIG_FILE_PYTEST_ARG, args=pytest_args)
#             with open(config_file) as f:
#                 config = json.load(f)
#         except (IndexError, FileNotFoundError):
#             raise ValueError(f'The provided parameter "{_CONFIG_FILE_PYTEST_ARG}" has no value.')
#         else:
#             return config[_SESSION_INFO_CONFIG]
#     return {}


def main():
    args, pytest_args = _get_args()
    # Required base args
    pytest_base_command = ['--verbose',  # Increase verbosity
                           '--capture', 'tee-sys']  # Allows output to be "live printed" and captured for a plugin
    # try:
    #     cfg_file_session_data = _load_config_file_session_data(pytest_args=pytest_args)
    #     project_name = _get_project(pytest_args=pytest_args, cfg_file_session_data=cfg_file_session_data)
    #     project_metadata = distribution(project_name)
    #     project_tests_path = os.path.abspath(project_metadata.locate_file(_TESTS_FOLDER))
    #     tests_root_path = _get_tests_root_path(pytest_args=pytest_args, project_tests_path=project_tests_path,
    #                                            cfg_file_session_data=cfg_file_session_data)
    #     pytest_base_command += [tests_root_path, '--pyargs', project_name]
    # except ValueError:
    #     if not args.pytest_help:
    #         raise
    if args.pytest_help:
        exit_code = pytest.main([*pytest_base_command, '--help'])
    else:
        reporting_args = ['--html', 'report.html', '--self-contained-html'] if '--html' not in pytest_args else []
        exit_code = pytest.main([*pytest_base_command, *pytest_args, *reporting_args])
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
