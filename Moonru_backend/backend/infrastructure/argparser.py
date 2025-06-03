import argparse

def parse_args(argv):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--env", type=str, default="dev")
    return parser.parse_args(argv)