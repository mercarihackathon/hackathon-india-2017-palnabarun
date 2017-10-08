import sys
import argparse
import yaml
import web
from ewasf.app import app

def parse_arguments():
    p = argparse.ArgumentParser()
    p.add_argument("-c", "--config",
        help="config file",
        required=True)
    p.add_argument("-p", "--port",
        type=int,
        help="port to use to run the webapp",
        default=8080)
    return p.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    with open(args.config, "r") as f:
        web.config = yaml.safe_load(f)

    sys.argv = [sys.argv[0]] + [str(args.port)]
    app.run()
