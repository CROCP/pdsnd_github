'''
Adding a docstring to the Python file...
'''

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
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nPlease enter one of the three cities (Chicago, New York City, or Washington):\n')
    
    while type(city) != str or city.lower() not in CITY_DATA.keys():
        city = input('\nOops, not a valid input! Please enter one of the three cities (Chicago, New York City, or Washington):\n')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nPlease enter a month between January and June, or "All" to apply no month filter:\n')
    
    while type(month) != str or month.lower() not in ['january','february','march','april','may','june','all']:
        month = input('\nOops, not a valid input! Please enter a month between January and June, or "All" to apply no month filter:\n')
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nPlease enter a day of week between Monday and Sunday, or "All" to apply no day of week filter:\n')
    
    while type(day) != str or day.lower() not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
        day = input('\nOops, not a valid input! Please enter a day of week between Monday and Sunday, or "All" to apply no day of week filter:\n')

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    # Return the data frame and the selected city to be used in another helper function
    return df, city


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}
    popular_month_num = df['Start Time'].dt.month.mode()[0]
    popular_month = months[popular_month_num]
    print("\nThe most common month is: %s.\n" % (popular_month))

    # TO DO: display the most common day of week
    popular_dow = df['day_of_week'].mode()[0]
    print("\nThe most common DOW is: %s.\n" % (popular_dow))

    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('\nThe most common hour is: ', popular_hour, '.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('\nThe most popular start station is: ', popular_start, '.\n')

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('\nThe most popular end station is: ', popular_end, '.\n')
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combo'] = df['Start Station'] + ' - ' + df['End Station']
    popular_combo = df['Station Combo'].mode()[0]
    print('\nThe most popular start & end station combo is: ', popular_combo, '.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum().round()
    print('\nThe total travel time is: ', str(total_travel_time), ' seconds.\n')
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean().round(2)
    print('\nThe mean travel time is: ', str(mean_travel_time), ' seconds.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, selected_city):
    """Displays statistics on bikeshare users.
    
    Args:
        df:              Pandas DataFrame
        selected_city:   The city of interest as a str. Must be in ('Chicago','New York City','Washington'), case insensitive.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nThe number of Subscribers is: ', str(user_types['Subscriber']), '.\n')
    print('\nThe number of Customers is: ', str(user_types['Customer']), '.\n')

    # TO DO: Display counts of gender
    # Produce a different output if city is 'Washington' because it has no "Gender" column.
    if selected_city == 'washington':
        print('\nOops! Washington has no gender data available!\n')
    else:
        genders = df['Gender'].value_counts()
        print('\nThe number of men is: ', str(genders['Male']), '.\n')
        print('\nThe number of women is: ', str(genders['Female']), '.\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    # Produce a different output if city is 'Washington' because it has no "Birth Year" column.
    if selected_city == 'washington':
        print('\nOops! Washington has no birth year data available!\n')
    else:
        birth_year_non_null = df['Birth Year'].dropna()
        dob_earliest = birth_year_non_null.min()
        dob_recent = birth_year_non_null.max()
        dob_popular = birth_year_non_null.mode()[0]
        print('\nThe earliest birth year is: ', str(int(dob_earliest)), '.\n')
        print('\nThe most recent birth year is: ', str(int(dob_recent)), '.\n')
        print('\nThe most popular birth year is: ', str(int(dob_popular)), '.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    city, month, day = get_filters()
    df, selected_city = load_data(city, month, day)

    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df, selected_city)

    # While Loop to continously loop through five rows of the data until end of file is reached or canceled by user.  
    data_loop = input('\nWould you like to display the first 5 lines of raw data? Enter yes or no.\n').lower()
    row = 0
    while data_loop == 'yes':
        print('\nThe data in rows %s and %s out of %s are:\n' % (row+1, min(row+5, df['Start Time'].size), df['Start Time'].size), df.iloc[row:min(row+5,df['Start Time'].size)])
        
        # If the end of data is reached, break loop
        if min(row+5,df['Start Time'].size) == df['Start Time'].size:
            break
        else:
            row += 5
            data_loop = input('\nWould you like to display up to the next 5 lines of raw data? Enter yes or no.\n').lower()

    '''
    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
        break
    '''

if __name__ == "__main__":
    main()
