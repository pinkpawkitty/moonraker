# Example Component
#
# Copyright (C) 2022  pinkpawkitty <git@lara.uber.space>
#
# This file may be distributed under the terms of the GNU GPLv3 license.

import logging
import os

class DryRunEstimate:
    def __init__(self, config):
        self.server = config.get_server()
        self.name = config.get_name()

        self.server.register_endpoint("/server/dry_run_estimate", ['GET'],
                                      self._handle_dry_run_estimate_request)

    async def _handle_dry_run_estimate_request(self, web_request):
        kinfo = self.server.get_klippy_info()
        if not kinfo:
            logging.info("No valid klippy info received")
            return
        kpath: str = kinfo['klipper_path']
        executable: str = kinfo['python_path']
        gcode_file_path: str = self.parse_url_path()
        return {"estimate": state}

def load_component(config):
    return DryRunEstimate(config)
