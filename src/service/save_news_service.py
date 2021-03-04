from src.support.config import Config

import os


class SaveNewsService:

    def __init__(self):
        self.config = Config()

    def save(self):
        raise NotImplemented

    def _check_is_workdir_empty(self):
        workdir = os.listdir('../../workdir')
        if len(workdir) is 0:
            return True
        else:
            return False

    def _get_save_option(self):
        raise NotImplemented

    def _associate_save_option(self):
        raise NotImplemented

    def _dissociate_save_option(self):
        raise NotImplemented

    def _both_save_option(self):
        raise NotImplemented
