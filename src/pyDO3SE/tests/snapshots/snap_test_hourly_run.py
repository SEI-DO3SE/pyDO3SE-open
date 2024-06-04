# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestHourlyRun.test_compare_initial_to_final[examples/hourly_runs/setup_01] Changes'] = {
    'changes': [
        'model_state.canopy.PM.precip_acc_dd: 0.12000000000000004 -> 0.005',
        'model_state.canopy.SMD.ASW: 0.0 -> 0.06607020548895037',
        'model_state.canopy.SMD.SMD: 0.06607020548895037 -> 0.0',
        'model_state.canopy.SMD.SWP: -4.0000000000000036 -> -0.015600329309258809',
        'model_state.canopy.SMD.Sn: 0.12482448627762405 -> 0.29',
        'model_state.canopy.Vd: 0.0013543010790158256 -> 0.001961302478903924',
        'model_state.canopy.canopy_height: 0.025925654029286063 -> 0.001',
        'model_state.canopy.met.micro_u: 0.11976331223257562 -> 0.2767320103608877',
        'model_state.canopy.rmodel_O3.Ra: 478.47710653827994 -> 283.95976783284624',
        'model_state.canopy.rmodel_O3.Ra_c: 538.4282392639461 -> 309.90525284542986',
        'model_state.canopy.rmodel_O3.Rb: 135.86093693405007 -> 58.79751962566096',
        'model_state.canopy_component.0.c_harv: 0.00022679394715261733 -> 0',
        'model_state.canopy_component.0.c_leaf: 7.57226264391933e-05 -> 0',
        'model_state.canopy_component.0.c_resv: 3.893774435538178e-07 -> 0',
        'model_state.canopy_component.0.c_root: 0.00047376085355725297 -> 0',
        'model_state.canopy_component.0.c_stem: 2.333319540738253e-05 -> 0',
        'model_state.canopy_component.0.dvi: 1.8653445640616693 -> -1',
        'model_state.canopy_component.0.g_bv_H2O: 1972211.9561548147 -> 3540228.8061649348',
        'model_state.canopy_component.0.growing_populations.0: False -> True',
        'model_state.canopy_component.0.phyllochron: 82.37721258036147 -> 10.133731524802753',
        'model_state.canopy_component.0.plant_height: 0.025925654029286063 -> 0.0',
        'model_state.canopy_component.0.t_eff: 13.78916666666666 -> 18.692500000000006',
        'model_state.canopy_component.0.td_dd: 0.0 -> 18.69250000000011',
        'model_state.canopy_component.0.td_dd_leaf_pops.0: 0 -> 18.69250000000011',
        'model_state.canopy_component.0.total_emerged_leaf_populations: 0 -> 1',
        'model_state.canopy_component_population.0.0.has_emerged: False -> True',
        'model_state.canopy_component_population.0.0.is_growing: False -> True',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.0: 79.78434069082402 -> 52.48677161523322',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.1: 79.78434069082402 -> 52.48677161523322',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.2: 79.78434069082402 -> 52.48677161523322',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.3: 79.78434069082402 -> 52.48677161523322',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.0: 79.78434069082402 -> 52.48677161523322',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.1: 79.78434069082402 -> 52.48677161523322',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.2: 79.78434069082402 -> 52.48677161523322',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.3: 79.78434069082402 -> 52.48677161523322',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.0: 79.78434069082402 -> 52.48677161523322',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.1: 79.78434069082402 -> 52.48677161523322',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.2: 79.78434069082402 -> 52.48677161523322',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.3: 79.78434069082402 -> 52.48677161523322',
        'model_state.canopy_layer_component.0.0.Tleaf_C_estimate: 14.54 -> 5.36',
        'model_state.canopy_layer_component.0.0.gsto_params.f_SW: 0.01 -> 1.0',
        'model_state.canopy_layer_component.0.0.gsto_params.f_phen: 0.03854316188197903 -> 0',
        'model_state.canopy_layer_component.0.0.gsto_params.leaf_f_phen: 0.06407800662879015 -> 0',
        'model_state.canopy_layer_component.1.0.Tleaf_C_estimate: 14.54 -> 5.36',
        'model_state.canopy_layer_component.1.0.gsto_params.f_SW: 0.01 -> 1.0',
        'model_state.canopy_layer_component.1.0.gsto_params.f_phen: 0.03854316188197903 -> 0',
        'model_state.canopy_layer_component.1.0.gsto_params.leaf_f_phen: 0.06407800662879015 -> 0',
        'model_state.canopy_layer_component.2.0.Tleaf_C_estimate: 14.54 -> 5.36',
        'model_state.canopy_layer_component.2.0.gsto_params.f_SW: 0.01 -> 1.0',
        'model_state.canopy_layer_component.2.0.gsto_params.f_phen: 0.03854316188197903 -> 0',
        'model_state.canopy_layer_component.2.0.gsto_params.leaf_f_phen: 0.06407800662879015 -> 0',
        'model_state.canopy_layer_component.3.0.Tleaf_C_estimate: 14.54 -> 5.36',
        'model_state.canopy_layer_component.3.0.gsto_params.f_SW: 0.01 -> 1.0',
        'model_state.canopy_layer_component.3.0.gsto_params.f_phen: 0.03854316188197903 -> 0',
        'model_state.canopy_layer_component.3.0.gsto_params.leaf_f_phen: 0.06407800662879015 -> 0',
        'model_state.canopy_layers.0.layer_depth: 0.006481413507321516 -> 0.00025',
        'model_state.canopy_layers.0.layer_height: 0.006481413507321516 -> 0.00025',
        'model_state.canopy_layers.0.micro_met.micro_O3: 46.08679955708794 -> 25.117948098341003',
        'model_state.canopy_layers.0.micro_met.micro_O3_nmol_m3: 1949.4084767142629 -> 1097.474483882952',
        'model_state.canopy_layers.0.micro_met.micro_u: 0.11976331223257562 -> 0.2767320103608877',
        'model_state.canopy_layers.1.layer_depth: 0.006481413507321516 -> 0.00025',
        'model_state.canopy_layers.1.layer_height: 0.012962827014643031 -> 0.0005',
        'model_state.canopy_layers.1.micro_met.micro_O3: 46.08679955708794 -> 25.117948098341003',
        'model_state.canopy_layers.1.micro_met.micro_O3_nmol_m3: 1949.4084767142629 -> 1097.474483882952',
        'model_state.canopy_layers.1.micro_met.micro_u: 0.11976331223257562 -> 0.2767320103608877',
        'model_state.canopy_layers.2.layer_depth: 0.006481413507321516 -> 0.00025',
        'model_state.canopy_layers.2.layer_height: 0.019444240521964546 -> 0.00075',
        'model_state.canopy_layers.2.micro_met.micro_O3: 46.08679955708794 -> 25.117948098341003',
        'model_state.canopy_layers.2.micro_met.micro_O3_nmol_m3: 1949.4084767142629 -> 1097.474483882952',
        'model_state.canopy_layers.2.micro_met.micro_u: 0.11976331223257562 -> 0.2767320103608877',
        'model_state.canopy_layers.3.layer_depth: 0.006481413507321516 -> 0.00025',
        'model_state.canopy_layers.3.layer_height: 0.025925654029286063 -> 0.001',
        'model_state.canopy_layers.3.micro_met.micro_O3: 46.08679955708794 -> 25.117948098341003',
        'model_state.canopy_layers.3.micro_met.micro_O3_nmol_m3: 1949.4084767142629 -> 1097.474483882952',
        'model_state.canopy_layers.3.micro_met.micro_u: 0.11976331223257562 -> 0.2767320103608877',
        'model_state.external_met.photoperiod: 16.097306086959733 -> 12.701908669196873',
        'model_state.external_met.t_acc: 448.6200000000001 -> 5.36',
        'model_state.met.O3_50: 46.10884678829408 -> 25.125080184178874',
        'model_state.met.u_50: 1.0756085231763632 -> 3.30541917407676',
        'model_state.met.ustar: 0.04469543852898771 -> 0.10327585574845156',
        'model_state.temporal.dd: 223 -> 71',
        'model_state.temporal.hr: 23 -> 0',
        'model_state.temporal.row_index: 3672 -> 1',
        'model_state.temporal.td: 2186.4704166666656 -> 2205.1629166666658'
    ],
    'total_changes': 84
}

snapshots['TestHourlyRun.test_compare_initial_to_final[examples/hourly_runs/bangor_day_71_hr_01] Changes'] = {
    'changes': [
        'model_state.canopy.PM.precip_acc_dd: 0.005 -> 0.01',
        'model_state.canopy.Vd: 0.001961302478903924 -> 0.002117293899210453',
        'model_state.canopy.met.micro_u: 0.2767320103608877 -> 0.3149019428244583',
        'model_state.canopy.rmodel_O3.Ra: 283.95976783284624 -> 249.54040203492548',
        'model_state.canopy.rmodel_O3.Ra_c: 309.90525284542986 -> 272.34097977325655',
        'model_state.canopy.rmodel_O3.Rb: 58.79751962566096 -> 51.67054754982327',
        'model_state.canopy_component.0.g_bv_H2O: 3540228.8061649348 -> 3776498.3781275474',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.0: 52.48677161523322 -> 49.203034718891914',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.1: 52.48677161523322 -> 49.203034718891914',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.2: 52.48677161523322 -> 49.203034718891914',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.3: 52.48677161523322 -> 49.203034718891914',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.0: 52.48677161523322 -> 49.203034718891914',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.1: 52.48677161523322 -> 49.203034718891914',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.2: 52.48677161523322 -> 49.203034718891914',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.3: 52.48677161523322 -> 49.203034718891914',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.0: 52.48677161523322 -> 49.203034718891914',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.1: 52.48677161523322 -> 49.203034718891914',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.2: 52.48677161523322 -> 49.203034718891914',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.3: 52.48677161523322 -> 49.203034718891914',
        'model_state.canopy_layer_component.0.0.Tleaf_C_estimate: 5.36 -> 5.85',
        'model_state.canopy_layer_component.1.0.Tleaf_C_estimate: 5.36 -> 5.85',
        'model_state.canopy_layer_component.2.0.Tleaf_C_estimate: 5.36 -> 5.85',
        'model_state.canopy_layer_component.3.0.Tleaf_C_estimate: 5.36 -> 5.85',
        'model_state.canopy_layers.0.micro_met.micro_O3: 25.117948098341003 -> 24.76905137882568',
        'model_state.canopy_layers.0.micro_met.micro_O3_nmol_m3: 1097.474483882952 -> 1080.3295043651854',
        'model_state.canopy_layers.0.micro_met.micro_u: 0.2767320103608877 -> 0.3149019428244583',
        'model_state.canopy_layers.1.micro_met.micro_O3: 25.117948098341003 -> 24.76905137882568',
        'model_state.canopy_layers.1.micro_met.micro_O3_nmol_m3: 1097.474483882952 -> 1080.3295043651854',
        'model_state.canopy_layers.1.micro_met.micro_u: 0.2767320103608877 -> 0.3149019428244583',
        'model_state.canopy_layers.2.micro_met.micro_O3: 25.117948098341003 -> 24.76905137882568',
        'model_state.canopy_layers.2.micro_met.micro_O3_nmol_m3: 1097.474483882952 -> 1080.3295043651854',
        'model_state.canopy_layers.2.micro_met.micro_u: 0.2767320103608877 -> 0.3149019428244583',
        'model_state.canopy_layers.3.micro_met.micro_O3: 25.117948098341003 -> 24.76905137882568',
        'model_state.canopy_layers.3.micro_met.micro_O3_nmol_m3: 1097.474483882952 -> 1080.3295043651854',
        'model_state.canopy_layers.3.micro_met.micro_u: 0.2767320103608877 -> 0.3149019428244583',
        'model_state.external_met.t_acc: 5.36 -> 11.21',
        'model_state.met.O3_50: 25.125080184178874 -> 24.77523123700452',
        'model_state.met.u_50: 3.30541917407676 -> 3.761339060156313',
        'model_state.met.ustar: 0.10327585574845156 -> 0.11752080136892763'
    ],
    'total_changes': 39
}

snapshots['TestHourlyRun.test_compare_initial_to_final[examples/hourly_runs/bangor_day_71_hr_12] Changes'] = {
    'changes': [
        'model_state.canopy.PM.precip_acc_dd: 0.05999999999999999 -> 0.06499999999999999',
        'model_state.canopy.Vd: 0.002907090934665732 -> 0.0028972921411461365',
        'model_state.canopy.met.micro_u: 0.595450946431703 -> 0.5906797048737569',
        'model_state.canopy.rmodel_O3.Ra: 131.9684818453933 -> 133.03446312039645',
        'model_state.canopy.rmodel_O3.Ra_c: 144.02647968777993 -> 145.18985997604952',
        'model_state.canopy.rmodel_O3.Rb: 27.325770338848848 -> 27.54649546274907',
        'model_state.canopy_component.0.g_bv_H2O: 5193075.389400775 -> 5172227.953213199',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.0: 35.78133704627189 -> 35.92555906191503',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.1: 35.78133704627189 -> 35.92555906191503',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.2: 35.78133704627189 -> 35.92555906191503',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.3: 35.78133704627189 -> 35.92555906191503',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.0: 35.78133704627189 -> 35.92555906191503',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.1: 35.78133704627189 -> 35.92555906191503',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.2: 35.78133704627189 -> 35.92555906191503',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.3: 35.78133704627189 -> 35.92555906191503',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.0: 35.78133704627189 -> 35.92555906191503',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.1: 35.78133704627189 -> 35.92555906191503',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.2: 35.78133704627189 -> 35.92555906191503',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.3: 35.78133704627189 -> 35.92555906191503',
        'model_state.canopy_layer_component.0.0.Tleaf_C_estimate: 10.61 -> 10.51',
        'model_state.canopy_layer_component.1.0.Tleaf_C_estimate: 10.61 -> 10.51',
        'model_state.canopy_layer_component.2.0.Tleaf_C_estimate: 10.61 -> 10.51',
        'model_state.canopy_layer_component.3.0.Tleaf_C_estimate: 10.61 -> 10.51',
        'model_state.canopy_layers.0.micro_met.PARshade: 54.797828952563236 -> 49.58663901924016',
        'model_state.canopy_layers.0.micro_met.PARsun: 57.911487556989734 -> 50.68219168679784',
        'model_state.canopy_layers.0.micro_met.micro_O3: 26.110416001756676 -> 26.0324031842174',
        'model_state.canopy_layers.0.micro_met.micro_O3_nmol_m3: 1119.7309488992387 -> 1116.7789763931587',
        'model_state.canopy_layers.0.micro_met.micro_u: 0.595450946431703 -> 0.5906797048737569',
        'model_state.canopy_layers.1.micro_met.PARshade: 54.797828952563236 -> 49.58663901924016',
        'model_state.canopy_layers.1.micro_met.PARsun: 57.911487556989734 -> 50.68219168679784',
        'model_state.canopy_layers.1.micro_met.micro_O3: 26.110416001756676 -> 26.0324031842174',
        'model_state.canopy_layers.1.micro_met.micro_O3_nmol_m3: 1119.7309488992387 -> 1116.7789763931587',
        'model_state.canopy_layers.1.micro_met.micro_u: 0.595450946431703 -> 0.5906797048737569',
        'model_state.canopy_layers.2.micro_met.PARshade: 54.797828952563236 -> 49.58663901924016',
        'model_state.canopy_layers.2.micro_met.PARsun: 57.911487556989734 -> 50.68219168679784',
        'model_state.canopy_layers.2.micro_met.micro_O3: 26.110416001756676 -> 26.0324031842174',
        'model_state.canopy_layers.2.micro_met.micro_O3_nmol_m3: 1119.7309488992387 -> 1116.7789763931587',
        'model_state.canopy_layers.2.micro_met.micro_u: 0.595450946431703 -> 0.5906797048737569',
        'model_state.canopy_layers.3.micro_met.PARshade: 54.797828952563236 -> 49.58663901924016',
        'model_state.canopy_layers.3.micro_met.PARsun: 57.911487556989734 -> 50.68219168679784',
        'model_state.canopy_layers.3.micro_met.micro_O3: 26.110416001756676 -> 26.0324031842174',
        'model_state.canopy_layers.3.micro_met.micro_O3_nmol_m3: 1119.7309488992387 -> 1116.7789763931587',
        'model_state.canopy_layers.3.micro_met.micro_u: 0.595450946431703 -> 0.5906797048737569',
        'model_state.external_met.t_acc: 99.66 -> 110.17',
        'model_state.met.O3_50: 26.11386213646197 -> 26.035867227074313',
        'model_state.met.u_50: 7.112350222841028 -> 7.055360237081086',
        'model_state.met.ustar: 0.22222115167942677 -> 0.22044053347686735',
        'model_state.temporal.row_index: 12 -> 1'
    ],
    'total_changes': 48
}

snapshots['TestHourlyRun.test_compare_initial_to_final[examples/hourly_runs/bangor_day_100_hr_1] Changes'] = {
    'changes': [
        'model_state.canopy.PM.precip_acc_dd: 0.005 -> 0.01',
        'model_state.canopy.Vd: 0.0007386971179707586 -> 0.000662405052969135',
        'model_state.canopy.rmodel_O3.Ra: 1025.3080854391712 -> 1163.8632321201405',
        'model_state.canopy.rmodel_O3.Ra_c: 1153.7747984227412 -> 1309.6903117231122',
        'model_state.canopy.rmodel_O3.Rb: 291.1305791443929 -> 330.47254929904074',
        'model_state.canopy_component.0.g_bv_H2O: 1347277.2543170168 -> 1264541.814255266',
        'model_state.canopy_layer_component.0.0.Tleaf_C_estimate: 0.69 -> 0.12',
        'model_state.canopy_layer_component.1.0.Tleaf_C_estimate: 0.69 -> 0.12',
        'model_state.canopy_layer_component.2.0.Tleaf_C_estimate: 0.69 -> 0.12',
        'model_state.canopy_layer_component.3.0.Tleaf_C_estimate: 0.69 -> 0.12',
        'model_state.canopy_layers.0.micro_met.micro_O3: 25.10759441065602 -> 24.7561856667744',
        'model_state.canopy_layers.0.micro_met.micro_O3_nmol_m3: 1115.7304469413234 -> 1102.4092298706744',
        'model_state.canopy_layers.1.micro_met.micro_O3: 25.10759441065602 -> 24.7561856667744',
        'model_state.canopy_layers.1.micro_met.micro_O3_nmol_m3: 1115.7304469413234 -> 1102.4092298706744',
        'model_state.canopy_layers.2.micro_met.micro_O3: 25.10759441065602 -> 24.7561856667744',
        'model_state.canopy_layers.2.micro_met.micro_O3_nmol_m3: 1115.7304469413234 -> 1102.4092298706744',
        'model_state.canopy_layers.3.micro_met.micro_O3: 25.10759441065602 -> 24.7561856667744',
        'model_state.canopy_layers.3.micro_met.micro_O3_nmol_m3: 1115.7304469413234 -> 1102.4092298706744',
        'model_state.external_met.t_acc: 0.69 -> 0.8099999999999999',
        'model_state.met.O3_50: 25.133325479495205 -> 24.784984684219246',
        'model_state.met.u_50: 0.5019506441489696 -> 0.442194615083616',
        'model_state.met.ustar: 0.020857871313527603 -> 0.018374791395250504',
        'model_state.temporal.row_index: 697 -> 1'
    ],
    'total_changes': 23
}

snapshots['TestHourlyRun.test_compare_initial_to_final[examples/hourly_runs/bangor_day_110_hr_12] Changes'] = {
    'changes': [
        'model_state.canopy.PM.precip_acc_dd: 0.05999999999999999 -> 0.06499999999999999',
        'model_state.canopy.Vd: 0.0025592356356389117 -> 0.0027200772157524532',
        'model_state.canopy.met.micro_u: 0.3379986811897135 -> 0.3845733026134929',
        'model_state.canopy.rmodel_O3.Ra: 169.5391322379732 -> 149.00671137870307',
        'model_state.canopy.rmodel_O3.Ra_c: 190.78165958171314 -> 167.676614303651',
        'model_state.canopy.rmodel_O3.Rb: 48.139702063246084 -> 42.309634339323544',
        'model_state.canopy_component.0.g_bv_H2O: 3313211.734857885 -> 3534119.692370364',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.0: 47.492174728495435 -> 44.523571446680435',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.1: 47.492174728495435 -> 44.523571446680435',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.2: 47.492174728495435 -> 44.523571446680435',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.3: 47.492174728495435 -> 44.523571446680435',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.0: 47.492174728495435 -> 44.523571446680435',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.1: 47.492174728495435 -> 44.523571446680435',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.2: 47.492174728495435 -> 44.523571446680435',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.3: 47.492174728495435 -> 44.523571446680435',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.0: 47.492174728495435 -> 44.523571446680435',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.1: 47.492174728495435 -> 44.523571446680435',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.2: 47.492174728495435 -> 44.523571446680435',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.3: 47.492174728495435 -> 44.523571446680435',
        'model_state.canopy_layer_component.0.0.Tleaf_C_estimate: 12.87 -> 13.19',
        'model_state.canopy_layer_component.1.0.Tleaf_C_estimate: 12.87 -> 13.19',
        'model_state.canopy_layer_component.2.0.Tleaf_C_estimate: 12.87 -> 13.19',
        'model_state.canopy_layer_component.3.0.Tleaf_C_estimate: 12.87 -> 13.19',
        'model_state.canopy_layers.0.micro_met.PARshade: 74.52170803412098 -> 60.109864817582526',
        'model_state.canopy_layers.0.micro_met.PARsun: 233.34933992496894 -> 249.9845242721574',
        'model_state.canopy_layers.0.micro_met.micro_O3: 26.110206817975268 -> 26.03253597044386',
        'model_state.canopy_layers.0.micro_met.micro_O3_nmol_m3: 1110.8744441809324 -> 1106.3321237167086',
        'model_state.canopy_layers.0.micro_met.micro_u: 0.3379986811897135 -> 0.3845733026134929',
        'model_state.canopy_layers.1.micro_met.PARshade: 74.52170803412098 -> 60.109864817582526',
        'model_state.canopy_layers.1.micro_met.PARsun: 233.34933992496894 -> 249.9845242721574',
        'model_state.canopy_layers.1.micro_met.micro_O3: 26.110206817975268 -> 26.03253597044386',
        'model_state.canopy_layers.1.micro_met.micro_O3_nmol_m3: 1110.8744441809324 -> 1106.3321237167086',
        'model_state.canopy_layers.1.micro_met.micro_u: 0.3379986811897135 -> 0.3845733026134929',
        'model_state.canopy_layers.2.micro_met.PARshade: 74.52170803412098 -> 60.109864817582526',
        'model_state.canopy_layers.2.micro_met.PARsun: 233.34933992496894 -> 249.9845242721574',
        'model_state.canopy_layers.2.micro_met.micro_O3: 26.110206817975268 -> 26.03253597044386',
        'model_state.canopy_layers.2.micro_met.micro_O3_nmol_m3: 1110.8744441809324 -> 1106.3321237167086',
        'model_state.canopy_layers.2.micro_met.micro_u: 0.3379986811897135 -> 0.3845733026134929',
        'model_state.canopy_layers.3.micro_met.PARshade: 74.52170803412098 -> 60.109864817582526',
        'model_state.canopy_layers.3.micro_met.PARsun: 233.34933992496894 -> 249.9845242721574',
        'model_state.canopy_layers.3.micro_met.micro_O3: 26.110206817975268 -> 26.03253597044386',
        'model_state.canopy_layers.3.micro_met.micro_O3_nmol_m3: 1110.8744441809324 -> 1106.3321237167086',
        'model_state.canopy_layers.3.micro_met.micro_u: 0.3379986811897135 -> 0.3845733026134929',
        'model_state.external_met.t_acc: 78.71000000000001 -> 91.9',
        'model_state.met.O3_50: 26.11463330411124 -> 26.036413567004523',
        'model_state.met.u_50: 3.0356062765199585 -> 3.4538984799774335',
        'model_state.met.ustar: 0.12614045984847644 -> 0.1435220192764161',
        'model_state.temporal.row_index: 948 -> 1'
    ],
    'total_changes': 48
}

snapshots['TestHourlyRunNetCDF.test_compare_initial_to_final[examples/net_cdf/wrfchem] Changes'] = {
    'changes': [
        'model_state.canopy.Vd: 0.0013543010790158256 -> 0.0022883314956318444',
        'model_state.canopy.met.micro_u: 0.11976331223257562 -> 0.2720387030631548',
        'model_state.canopy.rmodel_O3.Ra: 478.47710653827994 -> 210.6465089755263',
        'model_state.canopy.rmodel_O3.Ra_c: 538.4282392639461 -> 237.03961461260798',
        'model_state.canopy.rmodel_O3.Rb: 135.86093693405007 -> 59.811915095277804',
        'model_state.canopy_component.0.g_bv_H2O: 1972211.9561548147 -> 2972398.516396024',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.0: 79.78434069082402 -> 52.937595600457385',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.1: 79.78434069082402 -> 52.937595600457385',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.2: 79.78434069082402 -> 52.937595600457385',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.3: 79.78434069082402 -> 52.937595600457385',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.0: 79.78434069082402 -> 52.937595600457385',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.1: 79.78434069082402 -> 52.937595600457385',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.2: 79.78434069082402 -> 52.937595600457385',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.3: 79.78434069082402 -> 52.937595600457385',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.0: 79.78434069082402 -> 52.937595600457385',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.1: 79.78434069082402 -> 52.937595600457385',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.2: 79.78434069082402 -> 52.937595600457385',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.3: 79.78434069082402 -> 52.937595600457385',
        'model_state.canopy_layer_component.0.0.Tleaf_C_estimate: 14.54 -> 295.37158203125',
        'model_state.canopy_layer_component.1.0.Tleaf_C_estimate: 14.54 -> 295.37158203125',
        'model_state.canopy_layer_component.2.0.Tleaf_C_estimate: 14.54 -> 295.37158203125',
        'model_state.canopy_layer_component.3.0.Tleaf_C_estimate: 14.54 -> 295.37158203125',
        'model_state.canopy_layers.0.micro_met.micro_O3: 46.08679955708794 -> 0.03773722312416794',
        'model_state.canopy_layers.0.micro_met.micro_O3_nmol_m3: 1949.4084767142629 -> 745.1954261404694',
        'model_state.canopy_layers.0.micro_met.micro_u: 0.11976331223257562 -> 0.2720387030631548',
        'model_state.canopy_layers.1.micro_met.micro_O3: 46.08679955708794 -> 0.03773722312416794',
        'model_state.canopy_layers.1.micro_met.micro_O3_nmol_m3: 1949.4084767142629 -> 745.1954261404694',
        'model_state.canopy_layers.1.micro_met.micro_u: 0.11976331223257562 -> 0.2720387030631548',
        'model_state.canopy_layers.2.micro_met.micro_O3: 46.08679955708794 -> 0.03773722312416794',
        'model_state.canopy_layers.2.micro_met.micro_O3_nmol_m3: 1949.4084767142629 -> 745.1954261404694',
        'model_state.canopy_layers.2.micro_met.micro_u: 0.11976331223257562 -> 0.2720387030631548',
        'model_state.canopy_layers.3.micro_met.micro_O3: 46.08679955708794 -> 0.03773722312416794',
        'model_state.canopy_layers.3.micro_met.micro_O3_nmol_m3: 1949.4084767142629 -> 745.1954261404694',
        'model_state.canopy_layers.3.micro_met.micro_u: 0.11976331223257562 -> 0.2720387030631548',
        'model_state.external_met.t_acc: 448.6200000000001 -> 743.9915820312501',
        'model_state.met.O3_50: 46.10884678829408 -> 0.03774517092549319',
        'model_state.met.u_50: 1.0756085231763632 -> 2.4432118834551066',
        'model_state.met.ustar: 0.04469543852898771 -> 0.10152432246239727',
        'model_state.temporal.hr: 23 -> 11',
        'model_state.temporal.row_index: 3672 -> 1',
        'model_state.temporal.td: 2186.4704166666656 -> None'
    ],
    'total_changes': 41
}

snapshots['TestHourlyRunNetCDF.test_compare_initial_to_final[examples/net_cdf/emep] Changes'] = {
    'changes': [
        'model_state.canopy.PM.precip_acc_dd: 0.12000000000000004 -> 0.00021260802447795868',
        'model_state.canopy.Vd: 0.0013543010790158256 -> 0.004006889400329333',
        'model_state.canopy.canopy_height: 0.025925654029286063 -> 0.001',
        'model_state.canopy.met.micro_u: 0.11976331223257562 -> 1.728692869937762',
        'model_state.canopy.rmodel_O3.Ra: 478.47710653827994 -> 45.456748726466145',
        'model_state.canopy.rmodel_O3.Ra_c: 538.4282392639461 -> 49.6101448283307',
        'model_state.canopy.rmodel_O3.Rb: 135.86093693405007 -> 9.41240407315888',
        'model_state.canopy_component.0.c_harv: 0.00022679394715261733 -> 0',
        'model_state.canopy_component.0.c_leaf: 7.57226264391933e-05 -> 0',
        'model_state.canopy_component.0.c_resv: 3.893774435538178e-07 -> 0',
        'model_state.canopy_component.0.c_root: 0.00047376085355725297 -> 0',
        'model_state.canopy_component.0.c_stem: 2.333319540738253e-05 -> 0',
        'model_state.canopy_component.0.dvi: 1.8653445640616693 -> -1',
        'model_state.canopy_component.0.g_bv_H2O: 1972211.9561548147 -> 8848314.546275448',
        'model_state.canopy_component.0.phyllochron: 82.37721258036147 -> 5.0317580235508315',
        'model_state.canopy_component.0.plant_height: 0.025925654029286063 -> 0.0',
        'model_state.canopy_component.0.t_eff: 13.78916666666666 -> 18.692500000000006',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.0: 79.78434069082402 -> 21.000065022899136',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.1: 79.78434069082402 -> 21.000065022899136',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.2: 79.78434069082402 -> 21.000065022899136',
        'model_state.canopy_component_population.0.0.leaf_rmodel_O3.Rb.3: 79.78434069082402 -> 21.000065022899136',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.0: 79.78434069082402 -> 21.000065022899136',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.1: 79.78434069082402 -> 21.000065022899136',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.2: 79.78434069082402 -> 21.000065022899136',
        'model_state.canopy_component_population.0.1.leaf_rmodel_O3.Rb.3: 79.78434069082402 -> 21.000065022899136',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.0: 79.78434069082402 -> 21.000065022899136',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.1: 79.78434069082402 -> 21.000065022899136',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.2: 79.78434069082402 -> 21.000065022899136',
        'model_state.canopy_component_population.0.2.leaf_rmodel_O3.Rb.3: 79.78434069082402 -> 21.000065022899136',
        'model_state.canopy_layer_component.0.0.Tleaf_C_estimate: 14.54 -> 14.314202880859398',
        'model_state.canopy_layer_component.0.0.gsto_params.f_phen: 0.03854316188197903 -> 0.016183712121213348',
        'model_state.canopy_layer_component.0.0.gsto_params.leaf_f_phen: 0.06407800662879015 -> 0.026905421401517193',
        'model_state.canopy_layer_component.1.0.Tleaf_C_estimate: 14.54 -> 14.314202880859398',
        'model_state.canopy_layer_component.1.0.gsto_params.f_phen: 0.03854316188197903 -> 0.016183712121213348',
        'model_state.canopy_layer_component.1.0.gsto_params.leaf_f_phen: 0.06407800662879015 -> 0.026905421401517193',
        'model_state.canopy_layer_component.2.0.Tleaf_C_estimate: 14.54 -> 14.314202880859398',
        'model_state.canopy_layer_component.2.0.gsto_params.f_phen: 0.03854316188197903 -> 0.016183712121213348',
        'model_state.canopy_layer_component.2.0.gsto_params.leaf_f_phen: 0.06407800662879015 -> 0.026905421401517193',
        'model_state.canopy_layer_component.3.0.Tleaf_C_estimate: 14.54 -> 14.314202880859398',
        'model_state.canopy_layer_component.3.0.gsto_params.f_phen: 0.03854316188197903 -> 0.016183712121213348',
        'model_state.canopy_layer_component.3.0.gsto_params.leaf_f_phen: 0.06407800662879015 -> 0.026905421401517193',
        'model_state.canopy_layers.0.layer_depth: 0.006481413507321516 -> 0.00025',
        'model_state.canopy_layers.0.layer_height: 0.006481413507321516 -> 0.00025',
        'model_state.canopy_layers.0.micro_met.micro_O3: 46.08679955708794 -> 38.48227424896322',
        'model_state.canopy_layers.0.micro_met.micro_O3_nmol_m3: 1949.4084767142629 -> 16077.430703906426',
        'model_state.canopy_layers.0.micro_met.micro_u: 0.11976331223257562 -> 1.728692869937762',
        'model_state.canopy_layers.1.layer_depth: 0.006481413507321516 -> 0.00025',
        'model_state.canopy_layers.1.layer_height: 0.012962827014643031 -> 0.0005',
        'model_state.canopy_layers.1.micro_met.micro_O3: 46.08679955708794 -> 38.48227424896322',
        'model_state.canopy_layers.1.micro_met.micro_O3_nmol_m3: 1949.4084767142629 -> 16077.430703906426',
        'model_state.canopy_layers.1.micro_met.micro_u: 0.11976331223257562 -> 1.728692869937762',
        'model_state.canopy_layers.2.layer_depth: 0.006481413507321516 -> 0.00025',
        'model_state.canopy_layers.2.layer_height: 0.019444240521964546 -> 0.00075',
        'model_state.canopy_layers.2.micro_met.micro_O3: 46.08679955708794 -> 38.48227424896322',
        'model_state.canopy_layers.2.micro_met.micro_O3_nmol_m3: 1949.4084767142629 -> 16077.430703906426',
        'model_state.canopy_layers.2.micro_met.micro_u: 0.11976331223257562 -> 1.728692869937762',
        'model_state.canopy_layers.3.layer_depth: 0.006481413507321516 -> 0.00025',
        'model_state.canopy_layers.3.layer_height: 0.025925654029286063 -> 0.001',
        'model_state.canopy_layers.3.micro_met.micro_O3: 46.08679955708794 -> 38.48227424896322',
        'model_state.canopy_layers.3.micro_met.micro_O3_nmol_m3: 1949.4084767142629 -> 16077.430703906426',
        'model_state.canopy_layers.3.micro_met.micro_u: 0.11976331223257562 -> 1.728692869937762',
        'model_state.external_met.photoperiod: 16.097306086959733 -> 8.853548521210024',
        'model_state.external_met.t_acc: 448.6200000000001 -> 14.314202880859398',
        'model_state.met.O3_50: 46.10884678829408 -> 38.48402309059567',
        'model_state.met.u_50: 1.0756085231763632 -> 20.64833248213798',
        'model_state.met.ustar: 0.04469543852898771 -> 0.6451448650130652',
        'model_state.temporal.dd: 223 -> 1',
        'model_state.temporal.hr: 23 -> 0',
        'model_state.temporal.row_index: 3672 -> 1',
        'model_state.temporal.td: 2186.4704166666656 -> -1036.1851259867367'
    ],
    'total_changes': 70
}