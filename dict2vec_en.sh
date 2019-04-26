#!/usr/bin/env bash
for similarity_type in "cosine" "euclidean" ; do
    for test_number in 6 7 8 9 10 1 2 3 4 5 ; do
        for language in "en" ; do
            echo $language
            echo $similarity_type
            echo $test_number
            python weat.py \
                --test_number $test_number \
                --permutation_number 1000000 \
                --output_file ./results/dict2vec_${language}_${similarity_type}_${test_number}_cased.res \
                --lower False \
                --use_glove False \
                --is_vec_format True \
                --lang $language \
                --embeddings \
                /work/anlausch/dict2vec-vectors-dim300.vec \
                --similarity_type $similarity_type |& tee ./results/dict2vec_${language}_${similarity_type}_${test_number}_cased.out
        done
    done
done