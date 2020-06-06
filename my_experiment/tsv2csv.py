import pandas as pd

tsv_dev='dev.tsv'
csv_dev=pd.read_table(tsv_dev,sep='\t')
csv_dev.to_csv('dev.csv',index=False)

tsv_invalidated='invalidated.tsv'
csv_invalidated=pd.read_table(tsv_invalidated,sep='\t')
csv_invalidated.to_csv('invalidated.csv',index=False)

tsv_other='other.tsv'
csv_other=pd.read_table(tsv_other,sep='\t')
csv_other.to_csv('other.csv',index=False)

tsv_test='test.tsv'
csv_test=pd.read_table(tsv_test,sep='\t')
csv_test.to_csv('test.csv',index=False)

tsv_train='train.tsv'
csv_train=pd.read_table(tsv_train,sep='\t')
csv_train.to_csv('train.csv',index=False)

tsv_val='validated.tsv'
csv_val=pd.read_table(tsv_val,sep='\t')
csv_val.to_csv('validated.csv',index=False)   