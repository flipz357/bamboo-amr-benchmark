# Bamboo AMR Similarity Benchmark

## What do you need?

You need a metric that can input two files with n parallel AMR graphs each (in ususal AMR SemBank Penman format) and output n scores of meaning similarity (one per line). That's it.

## Evaluation example based on simple BOW toy metric

We have prepared an example that shows how to test your AMR metric on the full benchmark.

See `evaluation-suite/README.md`

Alternatively, metrics can be tested on parts of benchmark, such as, e.g., STS MAIN.

## Version notes

- 0.1: release
- 0.2: Changed default evaluation of role switch, since using Pearsonr is not ideal for evaluating pairwise classification. Recall that role switch makes two equivalent graphs (in meaning, not necessarily in structure) different in meaning. Previous evaluation calculates Pearsonr of predictions and [0, 1, 0, 1, 0, 1, 0...] where 0 stands for a SRL switch pair (foil) and 1 is the original pair. Old evaluation is not ideal since the metric shouldn't be expected to predict either 0 or 1 it should just assign a score to the foil that is lower than the true paraphrase. This is solved now by calculating accuracy of pairs, e.g. if gold pair is [0, 1] and pred pair is [x, y] with y > x then it is a correct pair, otherwise not. Accuarcy is sum of correct divided by all pairs.

## Benchmark Results of Current Metrics and Evaluation Setup

latest update: 07/12/2023, using metrics with recent updates, with improved role confusion evaluation (see above), reporting arithmetic mean as average 

| Metric        | STS   | SICK  | PARA  | STS(reify) | SICK(reify) | PARA(reify)| STS(Syno) | SICK(Syno) | PARA(Syno) | STS(role) | SICK(role) | PARA(role) | AMEAN |
|---------------|-------|-------|-------|------------|-------------|------------|------------|------------|-----------|-----------|------------|------------|-------|
| Smatch        | 58.39 | 59.75 | 41.32 | 58.03      | 61.79       | 39.47      | 56.13      | 57.37      | 39.54     | 89.87     | 98.32      | 88.14      | 62.34 | 
| SmatchPP      | 58.54 | 59.75 | 41.38 | 58.35      | 59.75       | 41.39      | 56.28      | 57.37      | 39.66     | 89.87     | 98.32      | 88.31      | 62.41 | 
| S2match(def)  | 56.39 | 58.11 | 42.40 | 55.78      | 59.97       | 40.67      | 56.04      | 57.15      | 40.93     | 93.67     | 98.32      | 91.26      | 62.56 | 
| S2match       | 58.70 | 60.47 | 42.52 | 58.19      | 62.37       | 40.55      | 56.62      | 57.88      | 41.15     | 89.87     | 98.32      | 92.24      | 63.24 |  
| Sema          | 55.90 | 53.32 | 33.43 | 55.51      | 56.16       | 32.33      | 50.16      | 48.87      | 29.11     | 78.48     | 90.76      | 74.93      | 54.91 | 
| SemBleu(k3)   | 56.54 | 58.06 | 32.82 | 54.96      | 58.53       | 33.66      | 53.19      | 53.72      | 28.96     | 81.01     | 93.28      | 77.79      | 56.88 |  
| WLK-k2        | 65.57 | 61.36 | 36.21 | 63.77      | 62.55       | 36.23      | 60.14      | 56.40      | 32.51     | 79.75     | 90.76      | 77.61      | 60.24 |  
| WWLK-k2       | 67.31 | 67.53 | 38.37 | 64.56      | 67.16       | 37.17      | 62.10      | 61.89      | 34.30     | 92.41     | 99.16      | 86.53      | 64.87 | 
| WWLK-k2-train | 67.90 | 67.89 | 38.62 | 64.95      | 67.38       | 37.78      | 62.42      | 62.25      | 34.44     | 92.41     | 100.00     | 91.26      | 65.61 |  
| WWLK-k4 e2n   | 64.07 | 66.73 | 37.24 | 63.65      | 66.77       | 37.15      | 60.14      | 61.63      | 33.62     | 92.41     | 100.00     | 92.95      | 64.70 | 

## Citation

```
@article{10.1162/tacl_a_00435,
    author = {Opitz, Juri and Daza, Angel and Frank, Anette},
    title = "{Weisfeiler-Leman in the Bamboo: Novel AMR Graph Metrics and a Benchmark for AMR Graph Similarity}",
    journal = {Transactions of the Association for Computational Linguistics},
    volume = {9},
    pages = {1425-1441},
    year = {2021},
    month = {12},
    abstract = "{Several metrics have been proposed for assessing the similarity of (abstract) meaning representations (AMRs), but little is known about how they relate to human similarity ratings. Moreover, the current metrics have complementary strengths and weaknesses: Some emphasize speed, while others make the alignment of graph structures explicit, at the price of a costly alignment step.In this work we propose new Weisfeiler-Leman AMR similarity metrics that unify the strengths of previous metrics, while mitigating their weaknesses. Specifically, our new metrics are able to match contextualized substructures and induce n:m alignments between their nodes. Furthermore, we introduce a Benchmark for AMR Metrics based on Overt Objectives (Bamboo), the first benchmark to support empirical assessment of graph-based MR similarity metrics. Bamboo maximizes the interpretability of results by defining multiple overt objectives that range from sentence similarity objectives to stress tests that probe a metric’s robustness against meaning-altering and meaning- preserving graph transformations. We show the benefits of Bamboo by profiling previous metrics and our own metrics. Results indicate that our novel metrics may serve as a strong baseline for future work.}",
    issn = {2307-387X},
    doi = {10.1162/tacl_a_00435},
    url = {https://doi.org/10.1162/tacl\_a\_00435},
    eprint = {https://direct.mit.edu/tacl/article-pdf/doi/10.1162/tacl\_a\_00435/1979290/tacl\_a\_00435.pdf},
}

```



