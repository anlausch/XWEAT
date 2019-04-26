#!/usr/bin/env bash
#for similarity_type in "cosine" "csls" ; do
for similarity_type in "euclidean" ; do
    for test_number in 1 2 3 4 5 6 7 8 9 10 ; do
        for language in "en" "de" "es" "hr" "it" "ru" "tr" ; do
            echo $language
            echo $similarity_type
            echo $test_number
            echo /work/gglavas/data/word_embs/yacle/fasttext/200K/npformat/ft.wiki.${language}.300.vocab
            python weat.py \
                --test_number $test_number \
                --permutation_number 1000000 \
                --output_file ./results/fasttext_${language}_${similarity_type}_${test_number}.res \
                --lower True \
                --use_glove False \
                --lang $language \
                --embedding_vocab \
                /work/gglavas/data/word_embs/yacle/fasttext/200K/npformat/ft.wiki.${language}.300.vocab \
                --embedding_vectors \
                /work/gglavas/data/word_embs/yacle/fasttext/200K/npformat/ft.wiki.${language}.300.vectors \
                --similarity_type $similarity_type |& tee ./results/fasttext_${language}_${similarity_type}_${test_number}.out
        done
    done
done