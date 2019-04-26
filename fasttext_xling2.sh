#!/usr/bin/env bash

#for similarity_type in "cosine" ; do
for similarity_type in "cosine" "euclidean" ; do
    for targets_language in "en" "de" "hr" "it" "ru" "tr" ; do
        for attributes_language in "en" "de" "hr" "it" "ru" "tr" ; do
            for test_number in 6 7 8 9 10 1 2 ; do
                echo $targets_language
                echo $attributes_language
                echo $similarity_type
                echo $test_number

                dir_1="/work/gglavas/data/word_embs/yacle/mappings/new/smith/fasttext/${targets_language}-${attributes_language}"
                dir_2="/work/gglavas/data/word_embs/yacle/mappings/new/smith/fasttext/${attributes_language}-${targets_language}"

                if [ -d "$dir_1" ]; then
                    embedding_dir=$dir_1

                    echo $embedding_dir

                    python xweat.py \
                        --test_number $test_number \
                        --permutation_number 1000000 \
                        --output_file ./results/ft_xling2_space-${targets_language}-${attributes_language}_ta-${targets_language}-${attributes_language}_${similarity_type}_${test_number}.res \
                        --lower True \
                        --use_glove False \
                        --targets_lang $targets_language \
                        --attributes_lang $attributes_language \
                        --targets_embedding_vocab \
                        ${embedding_dir}/vocab_${targets_language}-${attributes_language}.${targets_language}.yacle.train.freq.5k.pkl \
                        --targets_embedding_vectors \
                        ${embedding_dir}/vectors_${targets_language}-${attributes_language}.${targets_language}.yacle.train.freq.5k.np \
                        --attributes_embedding_vocab \
                        ${embedding_dir}/vocab_${targets_language}-${attributes_language}.${attributes_language}.yacle.train.freq.5k.pkl \
                        --attributes_embedding_vectors \
                        ${embedding_dir}/vectors_${targets_language}-${attributes_language}.${attributes_language}.yacle.train.freq.5k.np \
                        --similarity_type $similarity_type |& tee ./results/ft_xling2_space-${targets_language}-${attributes_language}_ta-${targets_language}-${attributes_language}_${similarity_type}_${test_number}.out
                fi
                if [ -d "$dir_2" ]; then
                    embedding_dir=$dir_2
                    echo $embedding_dir
                    python xweat.py \
                        --test_number $test_number \
                        --permutation_number 1000000 \
                        --output_file ./results/ft_xling2_space-${attributes_language}-${targets_language}_ta-${targets_language}-${attributes_language}_${similarity_type}_${test_number}.res \
                        --lower True \
                        --use_glove False \
                        --targets_lang $targets_language \
                        --attributes_lang $attributes_language \
                        --targets_embedding_vocab \
                        ${embedding_dir}/vocab_${attributes_language}-${targets_language}.${targets_language}.yacle.train.freq.5k.pkl \
                        --targets_embedding_vectors \
                        ${embedding_dir}/vectors_${attributes_language}-${targets_language}.${targets_language}.yacle.train.freq.5k.np \
                        --attributes_embedding_vocab \
                        ${embedding_dir}/vocab_${attributes_language}-${targets_language}.${attributes_language}.yacle.train.freq.5k.pkl \
                        --attributes_embedding_vectors \
                        ${embedding_dir}/vectors_${attributes_language}-${targets_language}.${attributes_language}.yacle.train.freq.5k.np \
                        --similarity_type $similarity_type |& tee ./results/ft_xling2_space-${attributes_language}-${targets_language}_ta-${targets_language}-${attributes_language}_${similarity_type}_${test_number}.out
                fi
            done
        done
    done
done