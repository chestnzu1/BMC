import pandas as pd
import requests, sys
GO1=['0008283', '0016049', '0007049', '0051301', '0008284', '0030307', '0045787', '0051781', '0009968',
     '0008285', '0030308', '0045786', '0051782', '0012501', '0043067', '0090398', '0032200', '0000723',
     '0032204', '0001302', '1900062', '2000772', '0001525', '0045765', '0001570', '2001212', '0008015',
     '0007155', '0001837', '0016477', '0030030', '0030036', '0034330', '0042330', '0007163', '0006281',
     '0031570', '0045005', '0006282', '0006954', '0002367', '0002718', '0042060', '0061041', '0050727',
     '0006006', '0046323', '0006096', '0071456', '0006955', '0002418', '0002837', '0006897', '0020012',
     '0042533', '0030155'] 
GO2=['0009967', '0030307', '0008284', '0045787', '0007165', '0009968', '0030308', '0008285', '0045786',     
     '0043069', '0043066', '0045768', '0001302', '0032206', '0090398', '0045765', '0045766', '0030949',
     '0001570', '0042060', '0007162', '0033631', '0044331', '0001837', '0016477', '0048870', '0007155',
     '0051276', '0045005', '0006281', '0002419', '0002420', '0002857', '0002842', '0002367', '0050776',
     '0006096', '0071456', '0002837', '0002418']
GO3=['0008283', '0042127', '0008284', '0008285', '0007049', '0051726', '0045787', '0045786', '0051301',
     '0051302', '0051781', '0051782', '0012501', '0043067', '0043068', '0043069', '0090398', '2000772',
     '0007569', '0090342', '0000723', '0032204', '0032200', '0045446', '0045601', '0045603', '0045602',
     '0043542', '0010594', '0010595', '0010596', '0001944', '1901342', '1904018', '1901343', '0001935',
     '0001936', '0001938', '0001937', '0034330', '0030030', '0031344', '0031346', '0031345', '0001837',
     '0010717', '0010718', '0010719', '0007155', '0030155', '0045785', '0007162', '0016477', '0030334',
     '0030335', '0030336', '0031570', '0006281', '0006282', '0045739', '0045738', '0050900', '0002685',
     '0006955', '0050776', '0050778', '0050777']
GO4=['0070265', '0010939', '0097300', '2001233', '0006282', '0006298', '0006302', '0006289', '0036297',
     '0001525', '0045765', '0090130', '0090132', '0010631', '0010632', '0051546', '0001667', '0002526',
     '0002544', '0050727', '0000723', '0007004', '0032204', '0051972', '0000075', '1901976', '1901987',
     '0045786', '0050673', '0050678', '0043616', '0010837', '0072089', '0006096', '0006110']#select terms of each method
method_name=['GO1','GO2','GO3','GO4']
saving_names=['pancancer','SupS9','Poster','newGO']
def clean(x):
    try:
        if x[0]=='!':
           return 'shanchu'
    except IndexError:
        return 'shanchu'
    else:
        full_element=x.split('\t')
        gene_id=full_element[0]+':'+full_element[1]
        return gene_id
for method in method_name:
    number=method_name.index(method)
    exec('GO_'+str(number+1)+'annotation=pd.DataFrame(columns=["source","geneid"])')
    intermediates_df=eval('GO_'+str(number+1)+'annotation')
    golist=eval(method)
#### retrieve annotations of go terms.
    for goid in golist:
        link = "https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch?selectedFields=symbol&goId=GO%3A{}&goUsage=descendants&goUsageRelationships=is_a%2Cpart_of&taxonId=9606&aspect=biological_process".format(goid)#0007165,0006955 can not be directly downloaded as it containes more than 10000 annotations. 
        response = requests.get(link, headers={ "Accept" : "text/gpad"})
        if not response.ok:
            continue
        responsebody = response.text
####  data clean
        r=responsebody.split('\n')
        results=[x for x in list(map(clean,r))]
        results=set(results)
        results.remove('shanchu')
        results_df=pd.DataFrame(results,columns=['gene'])
        results_df['source']=results_df['gene'].map(lambda x:x.split(':')[0])
        results_df['geneid']=results_df['gene'].map(lambda x:x.split(':')[1])
        results_df=results_df.drop(['gene'],axis=1)
        results_df.to_csv(saving_path+goid+'.csv') #  data export 
