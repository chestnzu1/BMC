import os
path='E:/PHD/prognostic_gene/unzipped/'
lists=os.listdir(path)
filename_ID={}
n=0
namelist=[]
final_df=pd.DataFrame(fGO4_ensembl)
final_df=final_df.sort_values('Gene stable ID')
final_df.reset_index(inplace=True)
final_df.drop(['index'],inplace=True,axis=1)
for x in lists:
    if os.path.isfile(path+x):
        n+=1
        transit_df=pd.read_csv(path+x,header=None,names=['Gene','FPKM'],sep='\t')
        transit_df['Gene']=transit_df['Gene'].map(lambda x:x.split('.',1)[0])
        transit_df_usable=transit_df.loc[transit_df['Gene'].isin(fGO4_ensembl)]
        transit_df_usable=transit_df_usable.sort_values('Gene')
        final_df['BRAC_patient_{0}'.format(n)]=transit_df_usable['FPKM'].values
final_df.to_csv('WGCNA_GO4.csv')