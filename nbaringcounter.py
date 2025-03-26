while True:
    print("NBA Ring Counter")
    user_input = input("Enter a current NBA Team: ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break


    if user_input == 'Boston Celtics':
        print("18 rings (1957, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1968, 1969,1974, 1976, 1981, 1984, 1986, 2008, 2024")
    elif user_input == 'Brooklyn Nets':
        print("0 rings")
    elif user_input == 'New York Knicks':
        print("2 rings (1970, 1973)")
    elif user_input == 'Philadelphia 76ers':
        print("3 rings (1955, 1967, 1983)")
    elif user_input == 'Toronto Raptors':
        print("1 ring (2019)")
    elif user_input == 'Chicago Bulls':
        print("6 rings (1991, 1992, 1993, 1996, 1997, 1998)")
    elif user_input == 'Cleveland Cavaliers':
        print("1 ring (2016)")
    elif user_input == 'Detroit Pistons':
        print("3 rings (1989, 1990, 2004)")
    elif user_input == 'Indiana Pacers':
        print("0 rings")
    elif user_input == 'Milwaukee Bucks':
        print("2 rings (1971, 2021)")
    elif user_input == 'Atlanta Hawks':
        print("1 ring (1958)")
    elif user_input == 'Charlotte Hornets':
        print("0 rings")
    elif user_input == 'Miami Heat':
        print("3 rings (2006, 2012, 2013)")
    elif user_input == 'Orlando Magic':
        print("0 rings")
    elif user_input == 'Washington Wizards':
        print("1 ring (1978)")
    elif user_input == 'Denver Nuggets':
        print("1 ring (2023)")
    elif user_input == 'Minnesota Timberwolves':
        print("0 rings")
    elif user_input == 'Oklahoma City Thunder':
        print("1 ring (1979)")
    elif user_input == 'Portland Trail Blazers':
        print("1 ring (1977)")
    elif user_input == 'Utah Jazz':
        print("0 rings")
    elif user_input == 'Golden State Warriors':
        print("7 rings (1947, 1956, 1975, 2015, 2017, 2018, 2022)")
    elif user_input == 'Los Angeles Clippers':
        print("0 rings")
    elif user_input == 'Los Angeles Lakers':
        print("17 rings (1949, 1950, 1952, 1953, 1954, 1972, 1980, 1982, 1985, 1987, 1988, 2000, 2001, 2002, 2009, 2010, 2020)")
    elif user_input == 'Phoenix Suns':
        print("0 rings")
    elif user_input == 'Sacromento Kings':
        print("1 ring (1951)")
    elif user_input == 'Dallas Mavericks':
        print("1 ring (2011)")
    elif user_input == 'Houston Rockets':
        print("2 rings (1994, 1995)")
    elif user_input == 'Memphis Grizzlies':
        print("0 rings")
    elif user_input == 'New Orleans Pelicans':
        print("0 rings")
    elif user_input == 'San Antonio Spurs':
        print("5 rings (1999, 2003, 2005, 2007, 2014)")

        
    
    else:
        print("Invalid Choice. Try Again!")
