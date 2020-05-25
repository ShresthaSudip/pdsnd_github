import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_LIST = ['january',
              'february',
              'march',
             'april',
             'may',
             'june',
             'all']

DAY_LIST = ['monday',
              'tuesday',
              'wednesday',
             'thursday',
             'friday',
             'saturday',
            'sunday',
            'all']

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
        city = input("Please provide city name (chicago, new york city, washington): ").lower()
        if city not in CITY_DATA:
            print('Sorry, please provide correct city name')
            continue
        else:
            break
 
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please provide mont name (all, january, february.....,june): ").lower()
        if month not in MONTH_LIST:
            print('Sorry, please provide correct month or all')
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please provide day of week (all, monday...sunday): ").lower()
        if day not in DAY_LIST:
            print('Sorry, please privde all or valid day name')
            continue
        else:
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
    # Loading data file as dataframe :df
    df = pd.read_csv(CITY_DATA[city])
    # Convert to date time format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    #Parsing month week name and hour from the start time 
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] =df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # when applicable filter by month
    if month !='all':
        month = MONTH_LIST.index(month) + 1 
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    
    # filter by day of week 
    if day !='all':
        # filter by day to create new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month of travel is:', common_month)


    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most frequent day of travel is:', common_day)


    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most frequent hour of travel is:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode().values[0]
    print('The most commonly used start station is:', start_station)


    # display most commonly used end station
    end_station = df['End Station'].mode().values[0]
    print('The most Commonly used end station is:', end_station)


    # display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+ " " + df['End Station']
    
    comb_start_end_station = df['routes'].mode().values[0]
    
    print("The most commonly used combination of both start station and end station trip is: {}".format(df['routes'].mode().values[0])) 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time for the passengers is:', total_travel_time/86400, " Days")


    # display mean travel time
    avg_trvl_time = df['Trip Duration'].mean()
    print('Mean travel time for the passengers is:', avg_trvl_time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print('\nThe counts of bikeshare user by types is:\n', user_type)


    # Display counts of gender
    try:
      gender_type = df['Gender'].value_counts()
      print('\nThe counts of bikeshare user by gender is:\n', gender_type)
    except KeyError:
      print("Gender Types:\nNo data for gender is available for this month.")


    # Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('Earliest year of birth is:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('Most Recent year of birth is:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('Most Common year of birth is :', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")


    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    option = input('Display raw data? yes/no ').lower()
    print()
    if option=='yes':
        option=True
    elif option=='no':
        option=False
    else:
        print('Please enter a valid option')
        display_raw_data(df)
        return

    if option:
        while 1:
            for i in range(5):
                print(df.iloc[i])
                print()
            option = input('Would like to take a look into five more observations? yes/no ').lower()
            if option=='yes':
                continue
            elif option=='no':
                break
            else:
                print('Please enter a valid option')
                return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
