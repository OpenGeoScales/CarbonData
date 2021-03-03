#!/usr/bin/env python
# coding: utf-8

# In[86]:


import os
import pandas as pd


# ## Files loading

# In[87]:


data_path = '../../datasets/raw/ademe/beges'
os.listdir(data_path)


# In[88]:


tests = pd.read_csv(data_path + '/texts.csv')
legal_units = pd.read_csv(data_path + '/legal_units.csv')
emissions = pd.read_csv(data_path + '/emissions.csv')
scope_items = pd.read_csv(data_path + '/scope_items.csv')
assessments = pd.read_csv(data_path + '/assessments.csv')


# In[99]:


scope_items


# ## Files preprocessing definitions

# In[89]:


# Assessments mapping definition
assessments_cols_mapping = {
    'id': 'assessment_id'
}

assessments_cols = [
    'assessment_id',
    'organization_name',
    'organization_description',
    'organization_type',
    'collectivity_type',
    'reporting_year'
]

# Scope Items mapping definition
scope_items_cols_mapping = {
    'id': 'scope_item_id'
}

scope_items_cols = [
    'scope_item_id',
    'label',
    'scope_id',
    'scope_label'
]

# Legl Units mapping definition
legal_units = legal_units.loc[legal_units['legal_unit_id_type'] == 'SIREN']


# # Processing
# 
# ## Dataframes merging
# 
# Merge everything left side of emission

# In[90]:


clean_emissions = emissions

clean_emissions = clean_emissions.merge(
    assessments.rename(assessments_cols_mapping, axis=1)[assessments_cols],
    on='assessment_id',
    how='left'
)

clean_emissions = clean_emissions.merge(
    scope_items.rename(scope_items_cols_mapping, axis=1)[scope_items_cols],
    on='scope_item_id',
    how='left'
)

# clean_emissions = clean_emissions.merge(
#     legal_units,
#     on='assessment_id',
#     how='left'
# )


# ## Explode gas values as rows

# In[91]:


gas_cols = [
    'co2',
    'ch4',
    'n2o',
    'other',
    'total',
    'co2_biogenic'
]

id_cols = [
    col for col in clean_emissions.columns
    if col not in gas_cols
]

clean_emissions = pd.melt(
    frame=clean_emissions,
    id_vars=id_cols,
    value_vars=gas_cols,
    var_name='gas'
)


# In[103]:


def mapping(row):
    return {
        'data_provider': {
            'name': 'ademe',
        },
        'data_source:': {
            'name': 'ademe',
            'link': 'url'
        },
        'geo': {
        },
        'time': {
            'scale': 'year',
            'value': row['reporting_year']
        },
        'emission': {
            'gas': row['gas'],
            'value': row['value'],
            'scope_name': row['scope_label'],
            'sub_scope_name': row['label']
        }
    }


# In[104]:


clean_emissions['output'] = clean_emissions.apply(
    lambda row: mapping(row),
    axis=1
)


# In[106]:


clean_emissions['output'].values

