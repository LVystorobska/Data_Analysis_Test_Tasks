import pandas as pd
import numpy as np

prods_data = pd.read_csv('task_9_data.csv')
articles_ids = list(set(prods_data['ArticleId']))
article_id_averages = {}

for id_i in articles_ids:
    data_by_article = prods_data.loc[
        prods_data['ArticleId'] == id_i]
    article_id_averages.update(
        {id_i: round(np.average( data_by_article['Price'], 
        weights = data_by_article['Quantity']),2)})
    

print('Averages:', article_id_averages)
