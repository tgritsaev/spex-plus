import argparse
import json
import logging
from typing import Dict

import src.datasets
from src.base.base_text_encoder import BaseTextEncoder
from src.utils.mixture_generator import MixtureGenerator
from src.text_encoder import CTCCharTextEncoder


logger = logging.getLogger(__name__)


def main(config: Dict, text_encoder: BaseTextEncoder):
    for split, params in config["data"].items():
        # create and join datasets
        index = []
        for ds in params["datasets"]:
            kwargs = dict(ds["args"])
            kwargs.update({"text_encoder": text_encoder})
            kwargs.update({"config_parser": config})
            dataset = getattr(src.datasets, ds["type"])(**kwargs)
            index += dataset._index
            # wave_augs=wave_augs, spec_augs=spec_augs)
        assert len(index) > 0

        logging.info("Creating " + split + " starts: " + str(len(index)))
        mixture_generator = MixtureGenerator(index, **params["mixture_generator_init"])
        mixture_generator.generate_mixes(**params["mixture_generator_generate_mixes"])
        logging.info("Creating " + split + " finished.")


if __name__ == "__main__":
    args = argparse.ArgumentParser(description="PyTorch Template")
    args.add_argument(
        "-c",
        "--config",
        default=None,
        type=str,
        help="config file path (default: None)",
    )
    args = args.parse_args()
    with open(args.config, "r") as rfile:
        config = json.load(rfile)

    text_encoder = CTCCharTextEncoder()
    main(config, text_encoder)
