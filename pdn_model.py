
# Copyright (c) Meta Platforms, Inc. and affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import json
import sys

class Fab_PDN():
    def __init__(self,  config = "lca_dellr740"):

        ###############################
        # Carbon per watt (gCO2e/W)
        ###############################
        if "lca" in config:
            with open("pdn/lca.json", 'r') as f:
                lca_configs = json.load(f)

                lca = config.replace("lca_", "")

                assert lca in lca_configs.keys()

                fab_cpw = lca_configs[lca]

        self.carbon_per_watt = fab_cpw
        self.carbon        = 0

    def get_cpa(self, ):
        return self.carbon_per_watt

    def set_power(self, power):
        self.power = power
        self.carbon = self.carbon_per_watt * self.power

        return

    def get_carbon(self, ):
        return self.carbon

