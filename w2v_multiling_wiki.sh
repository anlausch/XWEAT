#!/usr/bin/env bash
#for similarity_type in "cosine" "csls" ; do
for similarity_type in "cosine" "euclidean" ; do
    for language in "en" "de" "es" "hr" "it" "ru" "tr" ; do
        for test_number in 3 4 5 6 10; do
            echo $language
            echo $similarity_type
            echo $test_number
            python weat.py \
                --test_number $test_number \
                --permutation_number 1000000 \
                --output_file ./results/w2v_wiki_${language}_${similarity_type}_${test_number}_cased.res \
                --lower False \
                --use_glove False \
                --is_vec_format True \
                --lang $language \
                --embeddings \
                /work/gglavas/data/word_embs/yacle/cbow/cbow.wiki.${language}.300w5.vec \
                --similarity_type $similarity_type |& tee ./results/w2v_wiki_${language}_${similarity_type}_${test_number}_cased.out
        done
    done
done