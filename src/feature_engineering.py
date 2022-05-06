import pandas as pd
import datetime
from collections import deque

def last_5_average(df):
    """
    Create a "moving average" for the points scored in the last 5 games.
    :param df:
    :return:
    """
    df = df.sort_values(by=['game_date'])
    df['last_5_games_avg'] = ""

    average_per_game = df.groupby(['game_id'], sort=False)['shot_made_flag'].mean().reset_index(name="avg")
    avg_pts = deque(maxlen=5) # using a queue with a max number of elements

    prev_res = 0
    for i, game, avg in average_per_game.itertuples():
        avg_pts.append(avg)
        res = round(sum(avg_pts) / len(avg_pts),2) # max size will be 5. for the first 5 we divide by the length of the array.
        if i == 0:
            # we skip the first
            df.loc[df['game_id'] == game, ['last_5_games_avg']] = 0
        else:
            df.loc[df['game_id'] == game, ['last_5_games_avg']] = prev_res

        prev_res = res

    return df


# shot id is needed. we can delete it later
def before_current_shot_features(df):
    """
    Adding the statistics for the shots taken before the current shot
    :param df:
    :return:
    """
    df['streak_before_shot'] = ""
    df['points_before_shot'] = ""
    df['fgp_before_shot'] = ""

    for game in df.game_id.unique():
        fgp = [0,0]
        streak = 0
        shots = df[df['game_id'] == game]['shot_id'].sort_values()
        prev_streak = 0
        points = 0
        prev_points = 0
        for num, shot in enumerate(shots):

            row = df[(df['game_id'] == game) & (df['shot_id'] == shot)]

            flag = row['shot_made_flag'].item()
            shot_type = row['shot_type'].item()
            period = row['period'].item()

            # TODO divide per period somehow and multiply by the time remaining
            if num == 0:
                df.loc[(df['game_id']==game) & (df['shot_id'] == shot), ['fgp_before_shot'] ] = 0.00
            else:
                df.loc[(df['game_id']==game) & (df['shot_id'] == shot), ['fgp_before_shot'] ] = round(fgp[0]/fgp[1],2)

            fgp[1] += 1
            if flag == 1.0:
                fgp[0] += 1
                prev_streak = streak
                prev_points = points
                streak += 1

                if shot_type == '2PT Field Goal':
                    points += 2
                else:
                    points += 3
            else:
                prev_streak = streak
                prev_points = points
                streak = 0

            # df.loc[(df['game_id']==game) & (df['shot_id'] == shot), ['current_streak'] ] = streak
            df.loc[(df['game_id']==game) & (df['shot_id'] == shot), ['streak_before_shot'] ] = prev_streak
            df.loc[(df['game_id']==game) & (df['shot_id'] == shot), ['points_before_shot'] ] = prev_points

    return df

def extract_from_date(df):
    """
    Extract the month from the datetime format.
    :param df: dataframe
    :return: modified df with the month feature
    """
    df['month'] = df.game_date.apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").month)
    df['weekday'] = df.game_date.apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").weekday())
    return df



# get points scored per game
# shot_type = '2PT Field Goal'
# shot_made_flag 1.0 0.0
# df[df.game_id == 20000012].apply(lambda x: x['shot_type'], axis=1)

def feature_engineering(df):
    """
    Do the feature engineering on the dataframe
    :param df: original dataset
    :return: copy of the original but with modificaiton.
    """
    df_new = df.copy(deep=True)
    df_new = last_5_average(df_new)
    df_new = before_current_shot_features(df_new)
    df_new = extract_from_date(df_new)
    return df_new

