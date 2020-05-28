import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! refactor 1')
    print('refactoring 2')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please pick which city to explore, type c for  chicago, n for  new york city and w for washington : ").lower()
    if city == 'c':
        city = 'chicago'
    if city == 'n':
        city = 'new york city'
    if city == 'w':
        city = 'washington'
    while city !='chicago' and city != 'new york city' and city != 'washington':
        city = input("Please pick which city to explore, type c for  chicago, n for  new york city and w for washington : ").lower()
        if city == 'c':
            city = 'chicago'
        if city == 'n':
            city = 'new york city'
        if city == 'w':
            city = 'washington'        
        if city == 'washington' or city == 'chicago' or city == 'new york city':
            break
   

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please pick which month to explore : january or february or march or april or may or june or all : ").lower()
    while month !='january' and month != 'february' and month != 'march' and month !='april' and month != 'may' and month != 'june' and month != 'all' :
        month = input("Please pick which month to explore : january or february or march or april or may or june or all : ").lower()
        if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all':
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please pick which day to explore : monday or tuesday or wednesday or thursday or friday or saturday or sunday or all : ").lower()
    while day !='monday' and day != 'tuesday' and day != 'wednesday' and day !='thursday' and day != 'friday' and day != 'saturday' and day != 'sunday' and day != 'all':
        day = input("Please pick which day to explore : monday or tuesday or wednesday or thursday or friday or saturday or sunday or all : ").lower()
        if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all':
            break

    print('-'*40)
    
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    print ("Most common month is : ")
    print(popular_month)
    print ("Most common day is : ")
    print(popular_day)
    print ("Most common start hour is : ")
    print(popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]


    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = "(Start Station:) " + df['Start Station'] + " (End Station:) " +  df['End Station']
    popular_combination = df['combination'].mode()[0]

    print ("Most common start station is : ")
    print(popular_start_station)
    print ("Most common end station is : ")
    print(popular_end_station)
    print ("Most common combination of start station and end station is : ")
    print(popular_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum1 = df['Trip Duration'].sum().sum()

    # TO DO: display mean travel time
    mean1 = df['Trip Duration'].mean()
    print ("Total travel time is : ")
    print(sum1)
    print ("Mean travel time is : ")
    print(mean1)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types :" )
    print(user_types)
    

    # TO DO: Display counts of gender
    genderColumn = 0
    for col_name in df.columns:
        if col_name == 'Gender':
            gender = df['Gender'].value_counts()
            print ("Counts of gender : ")
            print(gender)
            genderColumn=1
    
    if genderColumn == 0:
        print("There is no gender info in this CSV")
    

    # TO DO: Display earliest, most recent, and most common year of birth
        birthYearColumn = 0
        for col_name in df.columns:
            if col_name == 'Birth Year':
                min1 = df['Birth Year'].min()
                mostrecent= df['Birth Year'].max()
                mostcommon = df['Birth Year'].mode()[0]
                print ("Earliest year of birth is : ")
                print(min1)
                print ("Most recent year of birth is : ")
                print(mostrecent)
                print ("Most common year of birth is : ")
                print(mostcommon)
                birthYearColumn = 1
        if birthYearColumn == 0:
            print ("There is no birth year info in this CSV")
    
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city,month,day = get_filters()
        df = load_data(city, month, day)
        counter = 0
        while True:
            wantToSee = input('\nWould you like to see couple of rows (5 rows at a time) from loaded data ? Print yes or no.\n')
            if wantToSee.lower() == 'yes':
                print(df.iloc[counter:counter + 5])
                counter = counter + 5
                if counter >= df.shape[0]:
                    print('End of dataframe has arrived, now passing to statistics.\n')
                    break
            else:
                break
            

        time_stats(df)
        print('*'*40)
        station_stats(df)
        print('*'*40)
        trip_duration_stats(df)
        print('*'*40)
        user_stats(df)
        print('*'*40)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
