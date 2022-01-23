import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

months = ['january', 'february', 'march', 'april', 'may', 'june']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("What city do you want to know about (chicago, new york city, washington) ?").lower()
        if city.lower() in CITY_DATA:
            break
        else:
            print("Invalid input !")
    # ask the user to input the city,month,day with avoiding wrong inputs using the while loops
    while True:

        month = input("What month do you want to know about "
                      "(all, january, february, march, april, may, june) ?").lower()

        if month.lower() in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Invalid input !")

    while True:
        day = input("What day do you want to know about (all, monday, tuesday, ... sunday) ?").lower()
        if day.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Invalid input !")

    print('-' * 40)
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
    # reading the chosen file
    df = pd.read_csv(CITY_DATA[city])
    # converting 'Start Time' column into a date column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extracting a month, day, and hour column from 'Start Time' column
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filtering months and days
    if month != 'all':
        # converting the user string input to int input like the date in the data yy-mm-dd
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # printing the most common month and day of the week in a non-filtered data
    if month == 'all':
        print('The most common month is: ', months[df['month'].mode()[0] - 1], '\n')

    if day == 'all':
        print('The most common day of week is: ', df['day'].mode()[0], '\n')

    # printing the most common hour in the day
    print('The most common start hour is: ', df['hour'].mode()[0], '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most commonly used **Start Station** is: ", df['Start Station'].mode()[0], '\n')
    # display most commonly used end station
    print("Most commonly used **End Station** is: ", df['End Station'].mode()[0], '\n')
    # display most frequent combination of start station and end station trip
    print("Most frequent (combination of start station and end station) Trip is: ",
          (df['Start Station'] + " To " + df['End Station']).mode()[0], '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time is: ", df['Trip Duration'].sum(), '\n')

    # display mean travel time
    print("Mean travel time is: ", df['Trip Duration'].mean(), '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types\n", df['User Type'].value_counts(), '\n')

    # checking if the city is 'chicago' or 'new york city' to show only related data of them
    if city == 'chicago' or city == 'new york city':
        # Display counts of gender
        print('Counts of gender:\n', df['Gender'].value_counts(), '\n')
        # Display earliest, , and most common year of birth
        print("Earliest year of birth is: ", df['Birth Year'].min(), '\n')
        print("Most recent year of birth is: ", df['Birth Year'].max(), '\n')
        print("Most common **year of birth** is: ", df['Birth Year'].mode(), '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        rd = pd.read_csv(CITY_DATA[city])

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        input()

        data = input('\nWould you like to see raw data? Enter yes or no.\n')
        a = 0
        b = 5
        while data == 'yes' or b == rd.count:
            print(rd[a:b][0:])
            a = b
            b += 5
            data = input('\nWould you like to see raw data? Enter yes or no.\n')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
