##################################
### if,elif, else Statements #####
##################################



# %% Now let's show some examples of if, elif, and else statements:

if 1 < 2:
    print('Yep!')

if 1 < 2:
    print('yep!')


# %% If Else - Make sure to line up the else with the if statement to "connect" them

if 1 < 2:
    print('first')
else:
    print('last')

# %%
###

if 1 > 2:
    print('first')
else:
    print('last')


# %% To add more conditions (like else if) you just use a single phrase "elif"

if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')
