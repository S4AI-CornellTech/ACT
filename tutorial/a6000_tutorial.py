
# Copyright (c) Meta Platforms, Inc. and affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import json
import sys

from dram_model import Fab_DRAM
from hdd_model  import Fab_HDD
from ssd_model  import Fab_SSD
from logic_model  import Fab_Logic
from pdn_model import Fab_PDN
from pcb_model import Fab_PCB

debug = False

a6000_soc_area = 609 #mm^2
a6000_ram      = 48 # GB
a6000_pcb_area = 22960 # mm^2
a6000_power = 300 # W

ic_yield           = 0.875

##################################
# Estimated process technology node to mimic fairphone LCA process node
# This initializes ACT with an older technology node.
##################################

# IC Logic node
SoC_Logic = Fab_Logic(gpa = "95",
                     carbon_intensity = "loc_taiwan", # e.g. location: "loc_taiwan", source: "src_coal"
                     process_node = 5,
                     fab_yield=ic_yield)

# DRAM Logic node
DRAM  = Fab_DRAM(config = "ddr4_10nm", fab_yield=ic_yield)

PDN = Fab_PDN()

PCB = Fab_PCB()


##################################
# Computing the IC footprint
##################################
SoC_Logic.set_area(a6000_soc_area/100.) # area in cm^2
DRAM.set_capacity(a6000_ram)
PDN.set_power()
PCB.set_area() # area in cm^2

##################################
# Computing the packaging footprint
##################################
#Number of packages
nr = 1 + 24 # a6000 SoC + 24 DRAM chips
packaging_intensity = 150 # gram CO2

PackagingFootprint = nr * packaging_intensity

if debug:
    print("ACT SoC", SoC_Logic.get_carbon(), "g CO2")
    print("ACT DRAM", DRAM.get_carbon(), "g CO2")
    print("ACT PDN", PDN.get_carbon(), "g CO2")
    print("ACT PCB", PCB.get_carbon(), "g CO2")
    print("ACT Packaging", PackagingFootprint, "g CO2")

print("--------------------------------")
ram = (DRAM.get_carbon() + packaging_intensity * 24) / 1000.
print("ACT RAM", ram, "kg CO2")

soc = (SoC_Logic.get_carbon() + packaging_intensity) / 1000.
print("ACT CPU", soc, "kg CO2")

pdn = PDN.get_carbon() / 1000.
print("ACT PDN", pdn, "kg CO2")

pcb = PCB.get_carbon() / 1000.
print("ACT PCB", pcb, "kg CO2")

