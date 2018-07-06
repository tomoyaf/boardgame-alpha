import boardgame_alpha

if __name__ == "__main__":
    game = boardgame_alpha.BoardgameAlpha()

    while True:
        i = input()
        if i == "quit":
            break
        else:
            x, y = [int(j) for j in i.split(",")]
            is_input_valid = game.update(x, y)
            if not is_input_valid:
                print("Input is invalid.\n")
