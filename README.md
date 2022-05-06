# Machine Project: Kobe Bryant Shot Selection

does exact location hurt or not, is shot zone good enough?

### What is test set
1 - Random 
2 - train on regular predict on playoff 
3 - train on data against 1 team in 1 season and then predict the match results against 
the same team in the next season.  (Suns or the clippers) Divide the suns's game by each season.


### Things to discuss
Do we need "game_event_id"? maybe it is useful maybe not.

- 

### References
Link to dataset: https://www.kaggle.com/competitions/kobe-bryant-shot-selection/overview


### ToDos
- Move "removing redundant columns section to notebook 2"
- p Analysis and remove redundant rows.

- Ask Prof: 
- Two styles of train/test split
1- Train: S1-regular, Test: S1-playoff. If we average shots made for S1-regular and then train
  and test on testset would it be okay. Techinically there is data leakage in training data
  but not in the test data. We'll be using season average from S1-regular in test rows. 
2- if we take MV of past 5 games, would it be a problem in regular season trining data. 
  if we do that, should we do the same for the testing data? in real life we would know data of 
  all the games before 
- Does keeping "date" column makes sense? what effect does dropping have if any. Given no 2 games 
  will have same date.

- Ask Prof Question) If this the distribution of a column (shot_distance)
  , can we normalize it to improve the results of linear regression on it? (done)
- How do outlier detection on categorical data (done)
- We have a categorical column wiht 2 different values "away" & "home". Question is, is it better apply one-hot encoding to it? 
  meaning we will get 2 different columns (match_away, match_home) and in each column "1" will denote true value. Or we use a 
  single column and have 1 denote "away" and 0 denote "home"? (done)
  
TODO 
Combine the notebooks into 1-EDA.
    - Resolve for in outliers game_event_id
Conclusion: divide dataset in 3 ways. as above.
Look into models regularized linear regression.

## ToDos Next tasks
- Complete the feature engineering in the same notebook. (convert categorical variables to numeric) (filip)
- Split the dataset as discussed above



### EDA on Columns Done: (22/22)
    game_event_id
    game_id
    lat, lon, loc_x, loc_y
    minutes_remaining, seconds_remaining - 8
    shot_distance
    period 
    playoffs
    season
    matchup
    shot_type
    shot_zone_area
    shot_zone_basic
    shot_zone_range
    combined_shot_type - 18
    action_type
    opponent
    game_date
    shot_made_flag
