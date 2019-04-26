#!/usr/bin/env bash
#for similarity_type in "cosine" "csls" ; do
for similarity_type in "cosine" "euclidean" ; do
    for test_number in 3 4 5 ; do
        for language in "en" ; do # "de" "es" "hr" "it" "ru" "tr" ; do
            echo $language
            echo $similarity_type
            echo $test_number
            python weat.py \
                --test_number $test_number \
                --permutation_number 1000000 \
                --output_file ./results/fasttext_cc_${language}_${similarity_type}_${test_number}.res \
                --lower True \
                --use_glove False \
                --is_vec_format True \
                --lang $language \
                --embeddings \
                /work/anlausch/fasttext_cc/cc.${language}.300.vec \
                --similarity_type $similarity_type |& tee ./results/fasttext_cc_${language}_${similarity_type}_${test_number}.out
        done
    done
done