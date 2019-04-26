#!/usr/bin/env bash

#for similarity_type in "cosine" ; do
for similarity_type in "cosine" "euclidean" ; do
    targets_language="en"
    attributes_language="en"
    for xspace in "en-de" "en-hr" "en-it" "en-ru" "en-tr" "ru-en" "tr-en" "de-en"; do
        for test_number in 1 2 3 4 5 6 7 8 9 10 ; do
            echo $targets_language
            echo $attributes_language
            echo $similarity_type
            echo $test_number
            echo $xspace

            dir="/work/gglavas/data/word_embs/yacle/mappings/new/smith/fasttext/${xspace}"

            if [ -d "$dir" ]; then
                python xweat.py \
                    --test_number $test_number \
                    --permutation_number 1000000 \
                    --output_file ./results/ft_xling_space-${xspace}_ta-${targets_language}-${attributes_language}_${similarity_type}_${test_number}.res \
                    --lower True \
                    --use_glove False \
                    --targets_lang $targets_language \
                    --attributes_lang $attributes_language \
                    --targets_embedding_vocab \
                    ${dir}/vocab_${xspace}.${targets_language}.yacle.train.freq.5k.pkl \
                    --targets_embedding_vectors \
                    ${dir}/vectors_${xspace}.${targets_language}.yacle.train.freq.5k.np \
                    --attributes_embedding_vocab \
                    ${dir}/vocab_${xspace}.${attributes_language}.yacle.train.freq.5k.pkl \
                    --attributes_embedding_vectors \
                    ${dir}/vectors_${xspace}.${attributes_language}.yacle.train.freq.5k.np \
                    --similarity_type $similarity_type |& tee ./results/ft_xling_space-${xspace}_ta-${targets_language}-${attributes_language}_${similarity_type}_${test_number}.out
            fi
        done
    done
done