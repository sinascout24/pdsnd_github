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
        (str) month - name of the month to filter by, or "all" to apply no 
                      month filter
        (str) day - name of the day of week to filter by, or "all" to apply no 
                    day filter
    """

    print('\n        __o\n      _ \<_\n.....(_)/(_)\n')
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('First of all: Which city do you want to look at? \
(Chicago, New York City, Washington): ')
        if city.lower() in CITY_DATA:
            break
        else:
            print('I\'m sorry but this was not a valid input, try again!')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Now: Which month would you like to filter for? \
(January, February, ... , June OR \'all\' for no filter): ')
        if month.lower() in (
            'all', 'january', 'february', 'march', 'april', 'may', 'june'):
            break
        else:
            print('I\'m sorry but this was not a valid input, try again!')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Lastly: Which weekday would you like to filter for? \
(Monday, Tuesday, ... , Sunday OR \'all\' for no filter): ')
        if day.lower() in (
            'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 
            'saturday', 'sunday'):
            break
        else:
            print('I\'m sorry but this was not a valid input, try again!')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city
    and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, 
                      or "all" to apply no month filter
        (str) day - name of the day of week to filter by,
                    or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Month: ' + str(df['month'].mode()[0]))

    # display the most common day of week
    print('Day of week: ' + str(df['day_of_week'].mode()[0]))

    # display the most common start hour
    print('Start hour: ' + str(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Start station: ' + str(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('End station: ' + str(df['Start Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print('Combination: ' + str((df['Start Station']+' & '+
    df['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total: ' + str(df['Trip Duration'].sum()))

    # display mean travel time
    print('Average: ' + str(df['Trip Duration'].sum()/
    df['Trip Duration'].count()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Types:\n' + str(df['User Type'].value_counts()))

    # Display counts of gender
    if city.lower() == 'washington':
        print('[No gender data available for Washington.]')
    else:
        print('Gender:\n' + str(df['Gender'].value_counts()))

    # Display earliest, most recent, and most common year of birth
    if city.lower() == 'washington':
        print('[No birth year data available for Washington.]')
    else:
        print('Oldest: ' + str(df['Birth Year'].min()))
        print('Youngest: ' + str(df['Birth Year'].max()))
        print('Most common: ' + str(df['Birth Year'].mode()[0]))

        print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_print(df):
    """Displays 5 lines of raw data at a time, at user request."""

    start_line = 0
    stop_line = 5
    more_raw = 'yes'

    # Display raw data if user wants to see it
    pd.set_option("display.max_columns", 11)
    while True:
        if more_raw == 'yes':
            if stop_line >= df.shape[0]:
                print('\nYou have reached the end of the data set.\n')
                pd.reset_option("display.max_columns")
                break
            else:
                print(df[start_line:stop_line])
                start_line += 5
                stop_line += 5
                more_raw = input('\nDo you want to see some more lines? \
Enter yes or no.\n')
        elif more_raw == 'no':
            pd.reset_option("display.max_columns")
            break
        else:
            print('\nSorry, I didn\'t catch that, come again.')
            more_raw = input('\nDo you want to see some more lines? \
Enter yes or no.\n')





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        while True:
            show_raw = input('\nCheck out the first lines of raw data? \
Enter yes or no.\n')
            if show_raw == 'yes':
                raw_print(df)
                break
            elif show_raw == 'no':
                break
            else:
                print('\nSorry, I didn\'t catch that, come again.')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
