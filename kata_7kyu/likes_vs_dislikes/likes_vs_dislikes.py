from preloaded import Like, Dislike, Nothing


def like_or_dislike(lst):
    state = Nothing
    for button in lst:
        state = Nothing if button == state else button
    return state
