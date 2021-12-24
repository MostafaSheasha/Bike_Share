import time
import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York': 'new_york_city.csv',
             'Washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('would you like to see Data for Chicago , New York or Washington').title()
        if city not in ('Chicago', 'New York', 'Washington'):
            print('Wrong Input... please enter city frome Chicago , New York or Washington')
            continue
        else:break

    #showing data
    df = pd.read_csv(CITY_DATA[city.title()])
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data.lower() == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month?\"January, February, March, April, May, June, all\"').title()
        if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
            print('Wrong Input...please enter a month frome January to June')
            continue
        else:break

        # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day?\", Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, all\"').title()
        if day not in ('Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'All'):
            print('Wrong input...please enter a day')
            continue
        else:break

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.title()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
    print('The most common month :', months.get(df['month'].mode()[0]))

    # display the most common day of week
    print('The most common day of week :', df['day_of_week'].mode()[0])

    # display the most common start hour
    if df['hour'].mode()[0] < 12:
        hour = str(df['hour'].mode()[0]) + ':00 am'
    else:
        hour = str(df['hour'].mode()[0] - 12) + ':00 pm'
    print('The most common start hour :', hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common used start station :' + df['Start Station'].mode()[0])

    # display most commonly used end station
    print('The most common used end station :' + df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    print('The most common trip :' + df['trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The total travel time :', (df['Trip Duration'].sum()/3600), ' hour')

    # display mean travel time
    print('The mean travel time :', (df['Trip Duration'].mean() / 60), ' min')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('The counts of user types :', df['User Type'].value_counts())

    # Display counts of gender
    print('The counts of gender :', df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    print('The most common year of birth :', int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats_2(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('The counts of user types :', df['User Type'].value_counts())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city in ('Chicago', 'New York'):
            user_stats(df)
        elif city in ('Washington'):
            user_stats_2(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

