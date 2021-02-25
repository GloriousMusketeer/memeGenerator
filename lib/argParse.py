import argparse


class argParse:
    def get_arg_parse(self) -> argparse.Namespace:

        argp = argparse.ArgumentParser(
            description='llego por quien lloraban MemeGenerator 0.1 alpha')
        argp.add_argument(
            "-i",
            "--image",
            help='la ruta de la imagen',
            required=True
        )
        argp.add_argument(
            "-t",
            "--top",
            type=str,
            help='agregar texto arriba',
            required=True
        )
        argp.add_argument(
            "-b",
            "--bottom",
            type=str,
            help='agregar texto abajo',
            required=True
        )
        arg = argp.parse_args()

        return arg
