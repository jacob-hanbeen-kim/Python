def mixtapeFire(timesPlayed, rating):
    msg = ""
    # ---- your code goes here ----
    if (rating > 5):
        msg = "Invalid input. Try again."
    elif (timesPlayed >= 1000 and rating >= 3):
        msg = "Your mix tape is fire!"
    else:
        msg = "You should quit the rap game."
    # -----------------------------
    return msg