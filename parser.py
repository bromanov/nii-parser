#!/usr/bin python
# -*- coding: UTF-8 -*-

import re


class NaiveParser():
    def __init__(self):
        self.score = 0.0
        self.history = {}

    def recalculate_score(self):
        return True

    def _parse_exclamation_question(self, line):
        regex = re.compile(r"[\?\!]")
        res = re.search(regex, line)
        if res:
            return 0.1
        else:
            return 0.0

    def score(self):
        return self.score

    def parse(self, line):
        local_score = 0.0
        local_score += self._parse_exclamation_question(line)
        return local_score