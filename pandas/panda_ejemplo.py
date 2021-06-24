import pandas as pd
# Matplotlib pyplot provides plotting API
import matplotlib as mpl
from matplotlib import pyplot as plt
# For output plots inline in notebook:
# %matplotlib inline
# For interactive plot controls on MatplotLib output:
# %matplotlib notebook
# Set the default figure size for all inline plots
# (note: needs to be AFTER the %matplotlib magic)
plt.rcParams['figure.figsize'] = [28, 15]
data = pd.read_csv('chat_performance_clean.csv')

# Preview the first 5 lines of the loaded data
print(data.head())

# Group the data by user_id and round the number of chats that appear for each
chats_per_user = data.groupby('user_id')['chat_id'].count().reset_index()
# Rename the columns in the results
chats_per_user.columns = ['user_id', 'number_chats']
# Sort the results by the number of chats
chats_per_user = chats_per_user.sort_values(
    'number_chats',
    ascending=False
)
# Preview the results
print(chats_per_user.head())

# Plotting directly from DataFrames with Pandas
chats_per_user[0:20].plot(
    x='user_id',
    y='number_chats',
    kind='bar',
    legend=False,
    color='blue',
    width=0.8
)
# The plot is now created, and we use Matplotlib style
# commands to enhance the output.
plt.ylabel("Number of chats")
plt.xlabel("User")
plt.title("Chats per users for Top 20 users")
plt.gca().yaxis.grid(linestyle=':')
plt.savefig('chats.png')
