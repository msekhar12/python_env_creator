def read_arguments():
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('--name', '-n', type=str, required=True,
                        help='Name of the project')
    parser.add_argument('--location', '-l', type=str, required=False,
                        help='Directory or location of the project.'
                        'Defaults to current directory', default='./')

    parser.add_argument('--requirements', '-r', type=str, required=False,
                        help='Requirements file path, if any')

    parser.add_argument('--overwrite', '-o', action='store_true',
                        help='If supplied overwrites the project directory')

    args = parser.parse_args()

    return args
        