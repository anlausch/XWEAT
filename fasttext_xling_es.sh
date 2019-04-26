#!/usr/bin/env bash
#!/usr/bin/env bash

#for similarity_type in "cosine" ; do
for similarity_type in "cosine" "euclidean" ; do
    targets_language="es"
    for attributes_language in "en" "de" "hr" "it" "ru" "tr" ; do
        for test_number in 6 7 8 9 10 1 2 ; do
            xspace=${targets_language}-${attributes_language}
            echo $targets_language
            echo $attributes_language
            echo $similarity_type
            echo $test_number

            dir_1="/work/gglavas/data/word_embs/yacle/mappings/new/smith/fasttext/${xspace}"

            if [ -d "$dir_1" ]; then
                embedding_dir=$dir_1
                echo $embedding_dir

                python xweat.py \
                    --test_number $test_number \
                    --permutation_number 1000000 \
                    --output_file ./results/ft_xling_space-${xspace}_ta-${targets_language}-${attributes_language}_${similarity_type}_${test_number}.res \
                    --lower True \
                    --use_glove False \
                    --targets_lang $targets_language \
                    --attributes_lang $attributes_language \
                    --targets_embedding_vocab \
                    ${embedding_dir}/${targets_language}.vocab \
                    --targets_embedding_vectors \
                    ${embedding_dir}/${targets_language}.vectors \
                    --attributes_embedding_vocab \
                    ${embedding_dir}/${attributes_language}.vocab \
                    --attributes_embedding_vectors \
                    ${embedding_dir}/${attributes_language}.vectors \
                    --similarity_type $similarity_type |& tee ./results/ft_xling_space-${xspace}_ta-${targets_language}-${attributes_language}_${similarity_type}_${test_number}.out
            fi
        done
    done
done

for similarity_type in "cosine" "euclidean" ; do
    attributes_language="es"
    for targets_language in "en" "de" "hr" "it" "ru" "tr" ; do
        for test_number in 6 7 8 9 10 1 2 ; do
            xspace=${attributes_language}-${targets_language}
            echo $targets_language
            echo $attributes_language
            echo $similarity_type
            echo $test_number

            dir_1="/work/gglavas/data/word_embs/yacle/mappings/new/smith/fasttext/${xspace}"

            if [ -d "$dir_1" ]; then
                embedding_dir=$dir_1
                echo $embedding_dir

                python xweat.py \
                    --test_number $test_number \
                    --permutation_number 1000000 \
                    --output_file ./results/ft_xling_space-${xspace}_ta-${targets_language}-${attributes_language}_${similarity_type}_${test_number}.res \
                    --lower True \
                    --use_glove False \
                    --targets_lang $targets_language \
                    --attributes_lang $attributes_language \
                    --targets_embedding_vocab \
                    ${embedding_dir}/${targets_language}.vocab \
                    --targets_embedding_vectors \
                    ${embedding_dir}/${targets_language}.vectors \
                    --attributes_embedding_vocab \
                    ${embedding_dir}/${attributes_language}.vocab \
                    --attributes_embedding_vectors \
                    ${embedding_dir}/${attributes_language}.vectors \
                    --similarity_type $similarity_type |& tee ./results/ft_xling_space-${xspace}_ta-${targets_language}-${attributes_language}_${similarity_type}_${test_number}.out
            fi
        done
    done
done