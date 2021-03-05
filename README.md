# BMC
Code are for publication 'Establishing A Consensus Annotation for the Hallmarks of Cancer based on Gene Ontology and pathway annotations'.Data can be found at FairdomHub https://fairdomhub.org/programmes/137.

# workflow
## Literature source
4 different GO mapping methods are acquired from paper:
1)  Knijnenburg, T.A., Bismeijer, T., Wessels, L.F., Shmulevich, I.: A multilevel pan-cancer map links gene mutations to cancer hallmarks. Chinese journal of cancer 34(3), 48 (2015)
2)  Plaisier, C.L., Pan, M., Baliga, N.S.: A mirna-regulatory network explains how dysregulated mirnas perturb oncogenic processes across diverse cancers. Genome research 22(11), 2302–2314 (2012)
3)  Kiefer, J., Nasser, S., Graf, J., Kodira, C., Ginty, F., Newberg, L., Sood, A., Berens, M.E.: A systematic approach toward gene annotation of the hallmarks of cancer. AACR (2017)
4)   Hirsch, T., Rothoeft, T., Teig, N., Bauer, J.W., Pellegrini, G., De Rosa, L., Scaglione, D., Reichelt, J.,Klausegger, A., Kneisz, D., et al.: Regeneration of the entire human epidermis using transgenic stem cells. Nature 551(7680), 327–332 (2017)
1 pathway mapping method is retrieved from paper:
1)Uhlen, M., Zhang, C., Lee, S., Sjöstedt, E., Fagerberg, L., Bidkhori, G., Benfeitas, R., Arif, M., Liu, Z., Edfors, F., et al.: A pathology atlas of the human cancer transcriptome. Science 357(6352) (2017)
## Semantic similarity between GO methods
The semantic similarity between select GO terms sets were calculated by using R package 'GOSemSim':
```
mgoSim(GO1, GO2, semData, measure = "Wang", combine = "BMA")
```
GO1,GO2 are two of four sets of selected GO terms. semData is the GOSemSimDATA object. In our study, we used Genome wide annotation for Human(org.Hs.eg.db).
## Descendant/child GO terms
Child terms of select GO terms from each method are retrieved by using QUICKGO API(see [GO_descendant.py](https://github.com/chestnzu1/BMC/blob/main/GO_descendants.py)). Some selected terms are obsoleted.therefore, they are not included in this section. We only consider relation type 'is_a' and 'part_of'. 
## Gene annotated to selected pathways, GO terms and their descendants 
Gene products annotated to selected pathways were directly provided by the author. For other methods, gene products annotated to select GO terms and their descendant terms were retrieved by using QUICKGO API(see [GO_annotation](https://github.com/chestnzu1/BMC/blob/main/GO_annotation.py)). As it can only retrieve GO terms with less than 10000 annotations, while for selected GO terms, two GO terms(GO:0007155 and GO:0006955) have more than 10000 annotations. Therefore, we downloaded their annotations by using the QUICKGO webtool. Next, we converted retrieved gene products ID to Ensembl ID for each method by using Biomart-Ensembl webtool.



