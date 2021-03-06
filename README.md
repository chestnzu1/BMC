Code are for publication 'Establishing A Consensus Annotation for the Hallmarks of Cancer based on Gene Ontology and pathway annotations'.Data can be found at FairdomHub https://fairdomhub.org/programmes/137.

## Literature source
4 different GO mapping methods are acquired from paper:
1)  Knijnenburg, T.A., Bismeijer, T., Wessels, L.F., Shmulevich, I.: A multilevel pan-cancer map links gene mutations to cancer hallmarks. Chinese journal of cancer 34(3), 48 (2015)
2)  Plaisier, C.L., Pan, M., Baliga, N.S.: A mirna-regulatory network explains how dysregulated mirnas perturb oncogenic processes across diverse cancers. Genome research 22(11), 2302–2314 (2012)
3)  Kiefer, J., Nasser, S., Graf, J., Kodira, C., Ginty, F., Newberg, L., Sood, A., Berens, M.E.: A systematic approach toward gene annotation of the hallmarks of cancer. AACR (2017)
4)   Hirsch, T., Rothoeft, T., Teig, N., Bauer, J.W., Pellegrini, G., De Rosa, L., Scaglione, D., Reichelt, J.,Klausegger, A., Kneisz, D., et al.: Regeneration of the entire human epidermis using transgenic stem cells. Nature 551(7680), 327–332 (2017)
1 pathway mapping method is retrieved from paper:
1)Uhlen, M., Zhang, C., Lee, S., Sjöstedt, E., Fagerberg, L., Bidkhori, G., Benfeitas, R., Arif, M., Liu, Z., Edfors, F., et al.: A pathology atlas of the human cancer transcriptome. Science 357(6352) (2017)

## Semantic similarity between GO methods
The semantic similarity between select GO terms sets were calculated by using R package *GOSemSim*:
```
mgoSim(GO1, GO2, semData, measure = "Wang", combine = "BMA")
```
GO1, GO2 are two of four sets of selected GO terms.  semData is the GOSemSimDATA object.  In our study,  we used Genome wide annotation for Human(org.Hs.eg.db).

## Descendant/child GO terms
Child terms of select GO terms from each method are retrieved by using QUICKGO API(see [GO_descendant.py](https://github.com/chestnzu1/BMC/blob/main/GO_descendants.py)). Some selected terms are obsoleted.therefore, they are not included in this section. We only consider relation type 'is_a' and 'part_of'. 

## Gene annotated to selected pathways, GO terms and their descendants 
Gene products annotated to selected pathways were directly provided by the author. For other methods, gene products annotated to select GO terms and their descendant terms were retrieved by using QUICKGO API(see [GO_annotation](https://github.com/chestnzu1/BMC/blob/main/GO_annotation.py)). As it can only retrieve GO terms with less than 10000 annotations, while for selected GO terms, two GO terms(*GO:0007155* and *GO:0006955*) have more than 10000 annotations. Therefore, we downloaded their annotations by using the QUICKGO webtool. Next, we converted retrieved gene products ID to Ensembl ID for each method by using Biomart-Ensembl webtool. The full list of hallmark genes can be found at https://fairdomhub.org/data_files/4013?graph_view=tree.

## Upset plot
The upsetplot presents the intersections among 5 mapping methods. it was accomplished by using R package 'UpsetR'.
```
list_of_input<-list(GO1=GO1,GO2=GO2,GO3=GO3,GO4=GO4,PW1=PW1)
upset(fromList(list_of_input),order.by = 'freq',queries=list(list(query=intersects,params=list('GO1','GO2','GO3','GO4'),active=T),list(query=intersects,params=list('GO1','GO2','GO3','GO4','PW1'),active=T)))
```
GO1,GO2,GO3,GO4,PW1 represent the gene sets we get from the last step.

## prognostic-hallmark genes and 
The full list of prognostic genes can be found at https://fairdomhub.org/data_files/4046?graph_view=tree. The abbreviation of cancer names can be found at https://fairdomhub.org/data_files/4014?graph_view=tree. Prognostic-hallmark genes are the intersection of prognostic genes and hallmark genes. Prognostic-hallmarks genes shared by multiple cancers types are considered to be potential research targets. The overlap of prognostic-hallmark genes shared by the same combinations of cancers are calculated by using Jaccard index. Sets of genes with less than 5 members are removed.
```
score = len((set1 & set2)) / len((set1 | set2)) # set1,set2 represent two sets of genes shared by the same combination of cancers when applying two different mapping schemes.
```
## Co-expression network construction 
We used prognostic-hallmark genes of breast cancer to construct the network.The full breast cancer FPKM values data can be found at https://fairdomhub.org/data_files/4047. Prognostic-hallmark genes with log-transformed FPKM value belonging to GO1 to GO4 can be found at https://fairdomhub.org/assays/1392?graph_view=tree.
We used the Rpackage *WGCNA* to construct the co-expression network with aforementioned data(see [WGCNA](https://github.com/chestnzu1/BMC/blob/main/WGCNA_FPKM)) and genes are grouped  into different clusters. detailed information about WGCNA can be found at([WCGNA] https://horvath.genetics.ucla.edu/html/CoexpressionNetwork/Rpackages/WGCNA/Tutorials/index.html) 

## hub genes identification and functional similarities between modules 
Clusters were identified and export to cytoscape to find hub genes for each cluster. 5 genes with the highest intra-modular connectivity in each module were designated as hub genes. The closeness of the proteins encoded by hub genes of clusters which have a high overlap on hub genes are revealed by using String Database(https://string-db.org/cgi/input?sessionId=bKwPqj7oGzsF&input_page_show_search=on). For each cluster, a Gene Set Enrichement Analysis was conducted by using webtool 'g:propfiler'(https://biit.cs.ut.ee/gprofiler/gost). The output files can be found at https://fairdomhub.org/data_files/4012?graph_view=tree.
Next, clusters were paired and the functional similarity were calculated by using aforementioned R package GOSemSim using the same code.  The visualization of the functional similarity results and the comparison of enriched GO terms of clusters with high functional similarity were accomplished by using python Package *seaborn*.  Functional similarity data can be found at https://fairdomhub.org/data_files/4015?graph_view=tree.

## Gene Ontology archive data
Gene Ontology archive data was downloaded from http://archive.geneontology.org/full/. We downloaded go_xxxxxx_termdb-tables.tar.gz from subdirectory. Then we load the *term* and *term2term* file into sql and we constructed a edge file by using multi-queries in sql. We only consider GO terms whose type are *biological_process*.
```
 #term2term201206 and term201206 can be found in the downloaded zip file, they are named as term2term and term respectively in the zipped file.
 with term2term201206 as(select term1,term2,relationship from term2term201206),
 term201206 as (select * from term201206 where term_type='biological_process' or is_relation=1),
 t as (select s1.acc as name1,s2.acc as name2,s1.relationship from (select term2term201206.term1,term201206.acc,term2term201206.term2,term2term201206.relationship from term2term201206 left join term201206 on term2term201206.term1=term201206.id where term201206.acc!='all' and term201206.is_relation=0 and term201206.is_obsolete=0) as s1 inner join 
					  (select term2term201206.term1,term201206.acc,term2term201206.term2,term2term201206.relationship from term2term201206 left join term201206 on term2term201206.term2=term201206.id where term201206.acc!='all' and term201206.is_relation=0 and term201206.is_obsolete=0) as s2 on (s1.term1=s2.term1 and s2.term2=s1.term2))
select t.name1,t.name2,term201206.acc as relation from t inner join term201206 on t.relationship=term201206.id into outfile 'xxxx'; 
```
After getting the edge files, for each method ,we load edges files in cytoscape followed with selecting collected GO terms  and their first neighbors, edges between selected nodes are reserved. Then we use cytoscape app *DyNet analyzer* to compare constructed networks. 

Similarly, the annotation count data can be downloaded from the aforementioned URL. We should download go_xxxxxx_assocdb-tables.tar.gz and load file *species* and *gene_product_count* into sql and run multiqueries to retrieve the annotation counts of selected GO terms at different timepoints. 
```
with goterms as (select GO_ID from xxxx limit 100),	#xxxx represent the table contains selected GO terms for each GO mapping schemes.
final as (select gene_product_count.term_id,gene_product_count.product_count,species.common_name from species inner join gene_product_count on species.id=gene_product_count.species_id where species.ncbi_taxa_id=9606 and gene_product_count.term_id in (select id from termxxxxxx where acc in (select * from goterms)))
select termxxxxxx.acc,final.product_count,final.common_name as species from final inner join termxxxxxx on final.term_id=termxxxxxx.id;
```
The table presents the annotation counts of all selected GO terms at different time-points can be found at https://fairdomhub.org/data_files/4010?graph_view=tree.
the cytoscape file contains all networks can be found at https://fairdomhub.org/data_files/4007?graph_view=tree.

## Consensus between methods
Mapping from MSigDB pathways to GO terms can be seen at https://fairdomhub.org/data_files/4019?graph_view=tree. The consensus GO terms for each individual hallmark can be found at https://fairdomhub.org/data_files/4018?graph_view=tree.  
The visualization of consensus of individual cancer hallmarks were accomplished by using goa-tools. For more information about goa-tools, pls see [goa-tools](https://github.com/tanghaibao/goatools).
