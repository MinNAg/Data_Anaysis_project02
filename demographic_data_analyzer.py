import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    df.head(5)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    
    r=df.loc[df['sex']=='Male'].age.mean()
    average_age_men =round(r,1)
    
    # What is the percentage of people who have a Bachelor's degree?
    
    b=df.loc[df['education']=='Bachelors'].age.count() #number of bachelors people

    c=df.age.count()
    percentage_bachelors = round((b/c)*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    a=df['education']=='Bachelors' #condition 
    a1=df['education']=='Masters'  #condition
    a2=df['education']=='Doctorate'  #condition
    higher_education = df.loc[(a1 | a | a2) ]
    h=df.loc[(a1 | a | a2) & (df['salary']=='>50K') ] 


    lower_education = df.loc[~(a1 | a | a2) ]
    l=df.loc[~ (a1 | a | a2) & (df['salary']=='>50K') ] 

    # percentage with salary >50K
    higher_education_rich = round( (h.salary.count()/higher_education.salary.count() )*100 ,1)
    lower_education_rich = round( (l.salary.count()/lower_education.salary.count() )*100 ,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df.iloc[0:,12].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[(df.iloc[0:,12]==1) & (df['salary']=='>50K') ]# people who work the minimum number of hours per week have a salary of >50K?
    m=df.loc[(df.iloc[0:,12]==1)]# total of people who work the minimum number of hours per week with all salary

    rich_percentage = round((num_min_workers.age.count()/m.age.count())*100,1)


    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df.loc[df["salary"] == ">50K",
    "native-country"].value_counts() / df["native-country"].value_counts()
    ).sort_values(ascending=False).index[0]
    z=(df.loc[df["salary"] == ">50K","native-country"].value_counts() / df["native-country"].value_counts()
    ).sort_values(ascending=False)
    highest_earning_country_percentage = round(z[0]*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    p=df.loc[ (df['native-country']=='India') & (df ['salary'] == '>50K') ]['occupation'].value_counts()
      
    top_IN_occupation = p.index[0]

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
