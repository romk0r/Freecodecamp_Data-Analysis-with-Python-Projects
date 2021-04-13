import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male'].age.mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df[df['education'] == 'Bachelors'].education.count() / len(df) *100,1) 

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    df_high = df[(df['education'] == 'Doctorate') | (df['education'] == 'Bachelors') | (df['education'] == 'Masters')]
    
    # What percentage of people without advanced education make more than 50K?
    df_lower = df[(df['education'] != 'Doctorate') & (df['education'] != 'Bachelors') & (df['education'] != 'Masters')]

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round(len(df_high) / len(df) *100,1)
    lower_education = round(len(df_lower) / len(df) *100,1)

    # percentage with salary >50K
    higher_education_rich = round(len(df_high[df['salary'] == '>50K']) / len(df_high) *100,1)
    lower_education_rich = round(len(df_lower[df['salary'] == '>50K']) / len(df_lower) *100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[(df['hours-per-week'] == min_work_hours)])

    rich_percentage = round(len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]) / num_min_workers * 100,1)

    # What country has the highest percentage of people that earn >50K?
    table = pd.pivot_table(df,values='age',index='native-country', columns='salary', aggfunc='count')
    table['ratio'] = table['>50K']/ (table['<=50K'] + table['>50K'])
    table['country'] = table.index
    
    highest_earning_country = table['country'][table['ratio'] == table['ratio'].max()][0]
    highest_earning_country_percentage = round(table['ratio'][table['ratio'] == table['ratio'].max()][0]*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    rich_india = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    table2 = pd.pivot_table(rich_india, values='age', index='occupation', aggfunc='count')
    table2['occ'] = table2.index
    top_IN_occupation = table2['occ'][table2['age'] == table2['age'].max()][0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
