#!/usr/bin/env bash
#parser.add_argument("--test_number", type=int, help="Number of the weat test to run", required=False)
#parser.add_argument("--permutation_number", type=int, default=None,
#                     help="Number of permutations (otherwise all will be run)", required=False)
#  parser.add_argument("--output_file", type=str, default=None, help="File to store the results)", required=False)
#  parser.add_argument("--lower", type=bool, default=False, help="Whether to lower the vocab", required=False)
#  parser.add_argument("--similarity_type", type=str, default="cosine", help="Which similarity function to use",
#                      required=False)
#  parser.add_argument("--embedding_file", type=str)

for similarity_type in "cosine" "csls" ; do
    for test_number in 1 2 3 4 5 6 7 8 9 10 ; do
        echo $similarity_type
        echo $test_number
        python weat.py \
            --test_number $test_number \
            --permutation_number 1000000 \
            --output_file ./results/glove_${similarity_type}_${test_number}.res \
            --lower True \
            --use_glove True \
            --similarity_type $similarity_type > ./results/glove_${similarity_type}_${test_number}.out
    done
done