# XWEAT
Cross-lingual version of WEAT, which includes the tests in English, German, Spanish, Croation, Italian, Russian, and Turkish.

Example usage:
This example would test monolingual bias in seven languages.
```
for similarity_type in "cosine" "euclidean" ; do
    for language in "en" "de" "es" "hr" "it" "ru" "tr" ; do
        for test_number in 3 4 5 6 10; do
            python weat.py \
                --test_number $test_number \
                --permutation_number 1000000 \
                --output_file ./results/w2v_wiki_${language}_${similarity_type}_${test_number}_cased.res \
                --lower False \
                --use_glove False \
                --is_vec_format True \
                --lang $language \
                --embeddings \
                <PATH TO YOUR EMBEDDINGS>/cbow.wiki.${language}.300w5.vec \
                --similarity_type $similarity_type |& tee ./results/w2v_wiki_${language}_${similarity_type}_${test_number}_cased.out
        done
    done
done
```

This example tests bias in cross-lingual embedding spaces. Here, Spanish is tested in bilingual spaces with each of the other six languages.
```
for similarity_type in "cosine" ; do
    targets_language="es"
    for attributes_language in "en" "de" "hr" "it" "ru" "tr" ; do
        for test_number in 6 7 8 9 10 1 2 ; do
            xspace=${targets_language}-${attributes_language}
            embedding_dir="/smith/fasttext/${xspace}" # be aware that you need to have trained the bilingual embedding space first

            python xweat.py \
                --test_number $test_number \
                --permutation_number 1000000 \
                --output_file ./results/ft_xling_space-${xspace}_ta-${targets_language}-${attributes_language}_${similarity_type}_${test_number}.res \
                --lower False \
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
        done
    done
done
```
For more information on our approach, experiments, and results we refer to our paper:

Lauscher A. and Glavas G. (2019). Are We Consistently Biased? Multidimensional Analysis of Biases in DistributionalWord Vectors. To appear at *SEM 2019.
