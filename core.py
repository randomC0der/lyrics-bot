#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class LyricsBot:
    __line_count = 0

    # a cycle of 8 means the lyrics file is read once a day if get_lyrics() is called every 3h
    def __init__(self, cycle = 8, filename = "lyrics.txt"):
        self.__cache_count = cycle
        self.__cycle = cycle
        self.__filename = filename

    # cache the line count
    def __get_lines(self, lyrics) -> int:
        self.__cache_count += 1

        if self.__cache_count > self.__cycle:
            self.__cache_count = 0
            self.__line_count = sum(1 for _ in lyrics)
            lyrics.seek(0) # to the beginning

        return self.__line_count

    def get_lyrics(self) -> str:
        with open(self.__filename, encoding="utf-8") as lyrics:

            # depending on how many songs there are, the file could turn out quite big so it gets read line by line
            # unfortunately, this means the file could be read two times
            
            selected = random.randrange(0, self.__get_lines(lyrics))

            # there is no need to cache the lines
            for i, line in enumerate(lyrics):
                if i == selected:
                    return line
        
        raise IndexError
