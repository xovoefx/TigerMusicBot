#
# Copyright (C) 2021-2022 by TigerNetwork@Github, < https://github.com/TigerNetwork >.
#
# This file is part of < https://github.com/TigerNetwork/TigerMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TigerNetwork/TigerMusicBot/blob/master/LICENSE >
#
# All rights reserved.


class AssistantErr(Exception):
    def __init__(self, errr: str):
        super().__init__(errr)
