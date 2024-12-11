# Importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('results.csv')

# Filter the data for rows with p-values less than 0.05
filtered_data = data[data['p-value'] < 0.05]

# Create a colorblind-friendly bar plot to show the discrepancies
plt.figure(figsize=(10, 6))
sns.set_palette('colorblind')

# Melt the data for easier plotting
melted_data = filtered_data.melt(id_vars=['RS Number'], 
                                 value_vars=['% of Puerto Ricans with at least one copy of the variant', 
                                             '% of Non-PR with at least one copy of the variant'], 
                                 var_name='Group', 
                                 value_name='Percentage')

# Create the bar plot
sns.barplot(data=melted_data, x='RS Number', y='Percentage', hue='Group')

# Add labels and title
plt.title('Significant Genetic Variant Frequencies in Puerto Rican vs Non-Puerto Rican Populations\n(p < 0.05)', fontsize=12)
plt.xlabel('RS Number', fontsize=12)
plt.ylabel('Frequency (%)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Population')

# Show the plot
plt.tight_layout()
plt.show()