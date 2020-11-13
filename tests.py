### PART 1

# Question 1.1

assert df.shape == (550, 14), "Shape of loaded DataFrame is incorrect."
assert df.index.name == 'RespondentID', "Index is not RespondentID"

# Question 1.2

patched_df = patch(df)
assert patched_df.loc[patched_df['Do you eat steak?'] == 'No', 'How do you like your steak prepared?'].isna().sum() == 0, "NaNs still exist."

# Question 1.3

cutoff_df = remove_rows_with_excess_of_missing(df, 5)
assert sum(cutoff_df.isnull().sum(axis=1) > 5) == 0, "Relevant NaNs not removed"

# Question 1.4

assert len(select_rows_with_missing(df).index) == 219, 'Not all missing value rows extracted'

# Question 1.5

assert sum(df['Age']=='&gt; 60') == 0
assert sum(df['Lottery Type']=='Lottery A') == 0
assert sum(df['Lottery Type']=='Lottery B') == 0

# Question 1.6

k1 = find_k_most_similar(df, 3234761827, 1)
assert k1.index.item() == 3234761827, "Wrong instance returned for k=1 (expected same entry as query)"

k2 = find_k_most_similar(df, 3234780649, 3)
assert (similar_df.index.values == 3234893368).any(), "Exact matching row not found"

###### N.B: returned subset and order of k_rows possibly depend on tie-break implementation???  
k3 = find_k_most_similar(df, 3234761827, 5)
assert np.array_equal(k3.index.values, [3234761827, 3234833617, 3234797258, 3234781654, 3234862267])

# Question 1.7

replaced_df = replace_missing(df, 6)
assert replaced_df.loc[3234925465, 'Household Income'] == '$50,000 - $99,999'

# Question 1.8

select_df = select(df, 'Do you ever gamble?', 'Household Income')
assert select_df.loc['No'].values.sum() == 1, "Group fractions do not sum to 1"
assert select_df.loc['Yes'].values.sum() == 1, "Group fractions do not sum to 1"

# Question 1.9

# Check visually.

### PART 2

# Question 2.1 - check visually against q2-1.png

Xs = [np.array([[1, 0, 0],[1, 0, 0],[0, 0, 0],[0, 0, 0]]),np.array([[0, 0, 1, 0],[0, 1, 0, 0],\
[0, 1, 0, 0]]),np.array([[1, 0, 0, 1, 1, 1],[1, 0, 0, 0, 0, 1],[1, 0, 0, 0, 1, 0],[1, 1, 0, 1, 1, 1]]\
),np.array([[0, 0, 0, 0, 0],[0, 1, 0, 1, 0],[0, 0, 0, 0, 0],[1, 0, 0, 0, 1],[0, 1, 1, 1, 0]])]
plot_list(Xs, n_per_row=2)

# Question 2.2

test_grid = make_initial_configuration(nrows=40, ncols=40, border_width=10, sparsity=0)
assert test_grid[10, 10] == 1
assert test_grid[9, 9] == 0

# Question 2.3

X = np.arange(18).reshape(6, 3)
n1 = extract(X, 1, 1, s=1)
assert np.array_equal(n1, [[0, 1, 2],[3, 4, 5],[6, 7, 8]]), "Incorrect neighbourhood"
n2 = extract(X, 1, 0, s=1)
assert np.array_equal(n2, [[2, 0, 1],[5, 3, 4],[8, 6, 7]]), "Incorrect neighbourhood - check left-right wrap"

# Question 2.4 - check visually against glider example

X = np.array([[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0]])

# Question 2.5 - NEEDS UPDATING

# X_test = np.array([[0, 0, 1, 1, 0],[0, 0, 0, 0, 0],[0, 1, 1, 1, 0],[0, 0, 0, 1, 1],[0, 0, 0, 0, 0]])
# X=conway_game(X_test, 15)

### PART 3

# Question 3.1

fund_data = make_data()
assert len(fund_data.index) == 5110, "incorrect number of rows returned"
assert set(['DJIA', 'NASDAQ100']) == set(fund_data.columns.values), "Incorrect index funds returned."

# Question 3.2

clean_fund_df = remove_missing(fund_data)
assert sum(clean_fund_df.isnull().sum(axis=1)) == 0, "NaN rows not removed"

# Question 3.3
assert all(coarser_df.reset_index()['DATE'].diff()[1:] == np.timedelta64(7, 'D')) == True, "Not resampled to 7 day intervals."

# Question 3.4

assert np.around(adjusted_df.min().min(), 3) == 1.00, "Minimum value across all arrays is not 1."

# Question 3.5

assert smooth_df.iloc[-2] == 2.469826635724209, "Wrong smoothed value, should be 2.469826635724209"

# Question 3.6

date_range = pd.date_range(start='1/1/2018', periods = 20)
s = pd.Series(np.sin(np.arange(0, 20, 1)), index = date_range)
intervals = find_intervals(s, 0)
assert np.array_equal(intervals.values, [3, 3, 2, 2])


