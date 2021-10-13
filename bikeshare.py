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
    city=input('Enter the city you want : ')
    if city in ['chicago', 'new york city', 'washington']:
         display = pd.read_csv(CITY_DATA[city])
    print('Here the first 5 rows from',city, ':\n', display.head(5))
    while city not in ['chicago', 'new york city', 'washington']:
        print('Not Valid')
        city = input ("CHOOSE BETWEEN chicago, new york city OR washington: ").lower()
        display = pd.read_csv(CITY_DATA[city])
        print('Here the first 5 rows from',city, ':\n', display.head(5))
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month =input('Enter the month you want : ')
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        print('Not Valid')
        month=input('Enter month you want as january, february, ... , june : ').lower()
        


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Enter the day of week you want as all, monday, tuesday, ... sunday : ')
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        print('Not Valid')
        day = input("Please Select the day of the week again: ").lower()
    

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
    #load city file into data frame
    df = pd.read_csv('{}.csv'.format(city))
     
    #convert Start Time and End Time to date format yyyy-mm-dd
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    #extract month from Start Time into new column called month
    df['month'] = df['Start Time'].dt.month
    
    #how to filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # extract day from Start Time into new column called month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: ", df['month'].value_counts().idxmax())

    # TO DO: display the most common day of week
    print("The most common day of week is: ", df['day_of_week'].value_counts().idxmax())

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is: ", df['hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is: ", df ['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print("The most common end station is: ", df ['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip")
    most_common_start_and_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(most_common_start_and_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum() / 3600.0
    print("total_travel_time in hours is: ", total_duration)

    # TO DO: display mean travel time
    mean_travel_duration = df['Trip Duration'].mean() / 3600.0
    print("mean_travel_time in hours is: ", mean_travel_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    types_of_user=df['User Type'].value_counts()
    print("types of user is : ",types_of_user)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_of_gender = df['Gender'].value_counts()
        print("cont of gender is :",count_of_gender)
    else:
        print('gender not found information')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
       earliest_year= int(df['Birth Year'].min())
       most_recent_year = int(df['Birth Year'].max())
       most_common_year = int(df['Birth Year'].value_counts().idxmax())
       print("The earliest year:",earliest_year,
          ", the most recent one is:",most_recent_year,
           "and the most common one is: ",most_common_year)
    else:
        print('birth year not found any information')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    user_input = input('Do you want to see raw data? Enter yes or no.\n')
    line_number = 0

    while 1 == 1 :
        if user_input.lower() != 'no':
            print(df.iloc[line_number : line_number + 5])
            line_number += 5
            user_input = input('\nDo you want to see more raw data? Enter yes or no.\n')
        else:
            break 


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
