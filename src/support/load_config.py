import os
from dotenv import load_dotenv


def load():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    stage_config = {
        "local": ".env",
        "dev": "dev.env",
        "hmg": "hmg.env",
        "prd": "prd.env"
    }

    dotenv_config = {
        "local": True,
        "dev": True,
        "hmg": False,
        "prd": False
    }

    stage_setted = os.getenv("STAGE", 'local')

    dotenv_path = os.path.join(BASE_DIR, stage_config[stage_setted])

    override_environment_variables = dotenv_config[stage_setted]

    load_dotenv(dotenv_path=dotenv_path, override=override_environment_variables)