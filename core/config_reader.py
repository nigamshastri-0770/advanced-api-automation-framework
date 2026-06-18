import os
import yaml


class ConfigReader:

    @staticmethod
    def load():

        env = (
            os.getenv(
                "ENV",
                "dev"
            )
        )

        path = (
            f"config/{env}.yaml"
        )

        with open(
            path,
            "r"
        ) as file:

            config = (
                yaml.safe_load(
                    file
                )
            )

        print(
            f"\nRunning Environment → {env.upper()}"
        )

        return config


config = (
    ConfigReader.load()
)