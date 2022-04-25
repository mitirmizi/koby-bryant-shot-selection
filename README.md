# Machine Project: Kobe Bryant Shot Selection

does exact location hurt or not, is shot zone good enough?

### What is test set
1 - Random 
2 - train on regular predict on playoff 
3 - train on data against 1 team in 1 season and then predict the match results against 
the same team in the next season.  (Suns or the clippers) Divide the suns's game by each season.


### Things to discuss

In model 1 I'm getting
Train MSE with y_pred_bin: 0.40113847583643125
Test Mean Squared Error (MSE): 163.421316639007
MSE is 163 which is very huge, don't know why.

### References
Link to dataset: https://www.kaggle.com/competitions/kobe-bryant-shot-selection/overview


### ToDos
TODO 
Combine the notebooks into 1-EDA.
    - Resolve for in outliers game_event_id
Conclusion: divide dataset in 3 ways. as above.
Look into models regularized linear regression.

- Ask Prof Question) If this the distribution of a column (shot_distance)
  , can we normalize it to improve the results of linear regression on it?

