# Machine Project: Kobe Bryant Shot Selection

does exact location hurt or not, is shot zone good enough?

### What is test set
1 - Random 
2 - train on regular predict on playoff 
3 - train on data against 1 team in 1 season and then predict the match results against 
the same team in the next season.  (Suns or the clippers) Divide the suns's game by each season.


### Things to discuss
Do we need "game_event_id"? maybe it is useful maybe not.

### Project Structure
src/
├── 1-EDA.ipynb
├── 2-feature-engineering.ipynb
|-- feature_engineering.py
(In `feature_engineering.py` we are mainting copy of some funtions from the `2-feature-engineering.ipynb` )
├── 4-models.ipynb
|-- 5-random-forrest.ipynb
├── ml03-linear-regression.ipynb
├── modeling_prep.ipynb
└── shots_made_and_missed.png

**Important Note** If you make changes to the functions in `2-feature-engineering.ipynb` make sure to sync that with `feature_engineering.py` 

### References
Link to dataset: https://www.kaggle.com/competitions/kobe-bryant-shot-selection/overview


## ToDos Next tasks
- Complete the feature engineering in the same notebook. (convert categorical variables to numeric) (filip)
- Split the dataset as discussed above
  
### ToDos
- More statistics, by Filip ( 2-feature-engineering )
- Move "removing redundant columns section to notebook 2"
- p Analysis and remove redundant rows.
- 
- Ask Prof: 
- Two styles of train/test split
1- Train: S1-regular, Test: S1-playoff. If we average shots made for S1-regular and then train
  and test on testset would it be okay. Techinically there is data leakage in training data
  but not in the test data. We'll be using season average from S1-regular in test rows. 
2- If we take MV of past 5 games, would it be a problem in regular season trining data. 
  if we do that, should we do the same for the testing data? in real life we would know data of 
  all the games before 
3- Do we remove duplicates usually? If yes why and happens if we don't?
- Does keeping "date" column makes sense? what effect does dropping have if any. Given no 2 games 
  will have same date.
- Move Section 2 remove redundant columns to Notebook-3


### ToDos that are Done
- Ask Prof Question) If this the distribution of a column (shot_distance)
  , can we normalize it to improve the results of linear regression on it? (done)
- How do outlier detection on categorical data (done)
- We have a categorical column wiht 2 different values "away" & "home". Question is, is it better apply one-hot encoding to it? 
  meaning we will get 2 different columns (match_away, match_home) and in each column "1" will denote true value. Or we use a 
  single column and have 1 denote "away" and 0 denote "home"? (done)



### EDA on Columns Done: (22/22)
Eventual status of columns
    game_event_id - drop
    game_id - drop
    lat, lon, - drop
    loc_x, loc_y
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
