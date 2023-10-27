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

f = open("result2.txt", "r")
data = f.read()
f.close()

print("1- monobit: " , monobit_test.test(data, len(data))[-2])
print("2- frequency within block: " , frequency_within_block_test.test(data, len(data))[-2])
print("3- runs: ", runs_test.test(data, len(data))[-2])
print("4- longest run ones in a block: ", longest_run_ones_in_a_block_test.test(data, len(data))[-2])
print("5- binary matrix rank: ", binary_matrix_rank_test.test(data, len(data))[-2])
print("6- dft: ", dft_test.test(data, len(data))[-2])
print("7- non overlapping template matching: ", non_overlapping_template_matching_test.test(data, len(data))[-2])
print("8- overlapping template matching: ", overlapping_template_matching_test.test(data, len(data)))
print("9- maurers universal: ", maurers_universal_test.test(data, len(data))[-2])
print("10- linear complexity: ", linear_complexity_test.test(data, len(data))[-2])
print("11- serial: ", serial_test.test(data, len(data))[-2])
print("12- approximate entropy: ", approximate_entropy_test.test(data, len(data))[-2])
print("13- cumulative sums: ", cumulative_sums_test.test(data, len(data))[-2])
print("14- random excursion: ", random_excursion_test.test(data, len(data))[-2])
print("15- random excursion variant: ", random_excursion_variant_test.test(data, len(data))[-2])
