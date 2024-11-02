
# Copyright (c) Meta Platforms, Inc. and affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import json
import sys

from dram_model import Fab_DRAM
from hdd_model  import Fab_HDD
from ssd_model  import Fab_SSD
from logic_model  import Fab_Logic

debug = False

# Main Fairphone integrated circuits

# Main Fairphone integrated circuits' areas in mm^2
# https://www.fairphone.com/wp-content/uploads/2020/07/Fairphone_3_LCA.pdf
# Look at page 22 (Table 3-5)
fairphone3_IC_areas = []
# IC areas:
'''
fairphone3_IC_areas = [0.85,
         1.2,
         1.2,
         35,
         0.89,
         0.08,
         0.25,
         18,
         11.6,
         1.44,
         12.96,
         1.61,
         6.3,
         26.88,
         0.77,
         11.36,
         7,
         8.69,
         11,
         9.6]
'''

fairphone_cpu_area = 0 #mm^2
fairphone_ram      = 0 # GB
fairphone_storage  = 0 # GB
ic_yield           = 0

##################################
# Estimated process technology node to mimic fairphone LCA process node
# This initializes ACT with an older technology node.
##################################

# IC Logic node
IC_Logic = Fab_Logic()

# CPU Application processor node
CPU_Logic = Fab_Logic()

# DRAM Logic node
DRAM  = Fab_DRAM()

# SSD Logic node
SSD   = Fab_SSD()

##################################
# Computing the IC footprint
##################################
IC_Logic.set_area(0/100.)
CPU_Logic.set_area(0/100.)
DRAM.set_capacity(0)
SSD.set_capacity(0)


##################################
# Computing the packaging footprint
##################################
packaging_intensity = 0 # gram CO2

print("--------------------------------")
ram_flash = (DRAM.get_carbon() + SSD.get_carbon() + packaging_intensity * 2) / 1000.
fairphone_ram_flash = 11
print("ACT RAM + Flash", ram_flash, "kg CO2 vs. LCA", fairphone_ram_flash, "kg CO2")

cpu = (CPU_Logic.get_carbon() + packaging_intensity) / 1000.
fairphone_cpu = 1.07
print("ACT CPU", cpu, "kg CO2 vs. LCA", fairphone_cpu, "kg CO2")

ics = (IC_Logic.get_carbon() + packaging_intensity * len(fairphone3_IC_areas)) / 1000.
fairphone_ics = 5.3
print("ACT ICs", ics, "kg CO2 vs. LCA", fairphone_ics, "kg CO2")
