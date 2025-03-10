%------------------------------------
% Formula 1 Knowledgebase (Optimized)
%------------------------------------

% Teams and their countries
team(mercedes, germany).
team(red_bull, austria).
team(ferrari, italy).
team(mclaren, uk).
team(aston_martin, uk).
team(alpine, france).
team(toro_rosso, italy).  % Now AlphaTauri, kept for history

% Drivers and their teams
driver(hamilton, mercedes, british).
driver(verstappen, red_bull, dutch).
driver(leclerc, ferrari, monegasque).
driver(norris, mclaren, british).
driver(alonso, aston_martin, spanish).
driver(ocon, alpine, french).

% Transfers (career moves)
transfer(hamilton, mclaren, mercedes, 2013).
transfer(verstappen, toro_rosso, red_bull, 2016).
transfer(alonso, alpine, aston_martin, 2023).

% Efficient career path tracking using recursion
career_path(Driver, Start, End) :-
    transfer(Driver, Start, End, _).
career_path(Driver, Start, End) :-
    transfer(Driver, Start, Mid, _),
    career_path(Driver, Mid, End).

% Formula 1 Races and Results
race(monaco, 2023, verstappen, red_bull).
race(silverstone, 2023, hamilton, mercedes).
race(monza, 2023, leclerc, ferrari).

% Query if a driver won a specific race
race_winner(GrandPrix, Year, Winner) :-
    race(GrandPrix, Year, Winner, _).

% Check if a driver has won any race
driver_won_race(Driver) :-
    race(_, _, Driver, _).

% Check if a driver has won a race in a specific year
driver_won_race_in_year(Driver, Year) :-
    race(_, Year, Driver, _).

% Unified predicate to check if a driver has driven for a team (current or past)
driver_for_team(Driver, Team) :-
    driver(Driver, Team, _);
    transfer(Driver, Team, _, _);
    transfer(Driver, _, Team, _).

% Find all teams a driver has driven for
all_teams_for_driver(Driver, Teams) :-
    findall(Team, driver_for_team(Driver, Team), TeamList),
    sort(TeamList, Teams).  % Remove duplicates
