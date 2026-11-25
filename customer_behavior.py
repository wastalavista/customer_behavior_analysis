import pandas as pd

csb = pd.read_csv('customer_shopping_behavior.csv')
csb.head()
csb.info()
csb.describe(include='all')

# median rating of each category
csb['Review Rating'] = csb.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
csb.isnull().sum()

csb.columns = csb.columns.str.lower()
csb.columns = csb.columns.str.replace(' ', '_')
csb = csb.rename(columns={'purchase_amount(usd)': 'purchase_amount'})
csb.columns

# column of age group
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
csb['age_group'] = pd.qcut(csb['age'], q=4, labels = labels)

# column of pucrchase frequency days
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

csb['purchase_frequency_days'] = csb['frequency_of_purchases'].map(frequency_mapping)

(csb['discount_applied'] == csb['promo_code_used']).all()
csb = csb.drop('promo_code_used', axis=1)


csb.to_csv('customer_shopping_behavior_cleaned.csv', index=False)


