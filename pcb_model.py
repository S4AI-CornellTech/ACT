
# Copyright (c) Meta Platforms, Inc. and affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import json
import sys

class Fab_PCB():
    def __init__(self,  config = "lca_dellr740"):

        ###############################
        # Carbon per area (gCO2e/cm^2)
        ###############################
        if "lca" in config:
            with open("pcb/lca.json", 'r') as f:
                lca_configs = json.load(f)

                lca = config.replace("lca_", "")

                assert lca in lca_configs.keys()

                fab_cpa = lca_configs[lca]

        self.carbon_per_area = fab_cpa
        self.carbon        = 0

    def get_cpa(self, ):
        return self.carbon_per_area

    def set_area(self, area):
        self.area = area
        self.carbon = self.carbon_per_area * self.area

        return

    def get_carbon(self, ):
        return self.carbon

