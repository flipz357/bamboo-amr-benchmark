# Bamboo AMR Similarity Benchmark

## What do you need?

You need a metric that can input two files 
with n parallel AMR graphs each (in ususal AMR SemBank Penman format) 
and output n scores of meaning similarity (one per line). That's it.

## Evaluation example based on simple BOW toy metric

We have prepared an example that shows how to test your AMR metric on the full benchmark.

See `evaluation-suite/README.md`

Alternatively, metrics can be tested on parts of benchmark, such as, e.g., STS MAIN.

## Version notes

- 0.1: release
- 0.2: Changed default evaluation of role switch. Recall that role switch makes two equivalent graphs (in meaning, not necessarily in structure) different. Previous evaluation calculates Pearsonr of predictions and [0, 1, 0, 1, 0, 1, 0...] where 0 stands for a SRL switch pair and 1 is the original pair. Old evaluation is not ideal since the metric shouldn't be expected to predict 0 (which implies totally different graphs). Instead, the metric should assign just a score that is lower. This is solved now by calculating accuracy of pairs, e.g. if gold pair is [0, 1] and pred pair is [x, y] with y > x then it is a correct pair, otherwise not. Accuarcy is sum of correct divided by all pairs.

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



