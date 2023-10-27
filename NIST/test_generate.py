import monobit_test
import frequency_within_block_test
import runs_test
import longest_run_ones_in_a_block_test
import binary_matrix_rank_test
import dft_test
import non_overlapping_template_matching_test
import overlapping_template_matching_test
import maurers_universal_test
import linear_complexity_test
import serial_test
import approximate_entropy_test
import cumulative_sums_test
import random_excursion_test
import random_excursion_variant_test

import numpy as np
import os

num_0 = 0
num_1 = 0
i = 0
e = 0
while i < 8000:
    rand = np.random.randint(2, size=1024)
    rand = ''.join(map(str, rand))
    
    p_value = 0

    #p_value += monobit_test.test(rand, len(rand))[-2]
    #p_value += frequency_within_block_test.test(rand, len(rand))[-2]
    #p_value += runs_test.test(rand, len(rand))[-2]
    #p_value += longest_run_ones_in_a_block_test.test(rand, len(rand))[-2]
    #p_value += binary_matrix_rank_test.test(rand, len(rand))[-2]
    #p_value += dft_test.test(rand, len(rand))[-2]
    #p_value += non_overlapping_template_matching_test.test(rand, len(rand))[-2]
    #overlapping_template_matching_test.test(rand, len(rand))
    #maurers_universal_test.test(rand, len(rand))[-2]
    #linear_complexity_test.test(rand, len(rand))[-2]
    #p_value += serial_test.test(rand, len(rand))[-2]
    #p_value += approximate_entropy_test.test(rand, len(rand))[-2]
    #p_value += cumulative_sums_test.test(rand, len(rand))[-2]
    #p_value += random_excursion_test.test(rand, len(rand))[-2]
    #p_value += random_excursion_variant_test.test(rand, len(rand))[-2]


    
    p_value = monobit_test.test(rand, len(rand))[-2]
    
    
    f = open("C:/Users/alida/Desktop/article/dataset2/data/" + str(i) + "_rand.txt", "w")
    f.write(''.join(map(str, rand)))
    f.close()

    #p_value /= 12

    f = open("C:/Users/alida/Desktop/article/dataset2/label/" + str(i) + "_lbl.txt", "w")
    if p_value >= 0.1 and num_1 < 4000:
        f.write(str(1))
        num_1 += 1
        i += 1
    elif p_value < 0.1 and num_0 < 4000:
        f.write(str(0))
        num_0 += 1
        i += 1
    f.close()

    os.system('cls')
    print("e: ", e, " i: ", i, " num_0: ", num_0, " num_1: ", num_1)
    e += 1
    