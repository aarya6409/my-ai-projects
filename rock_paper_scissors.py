import random

VALID_MOVES = ("rock", "paper", "scissors")

def counter_move(pred):
    """Return the move that beats 'pred'."""
    if pred == "rock":
        return "paper"
    if pred == "paper":
        return "scissors"
    return "rock"

def winner(user, comp):
    """Return 'win", 'lose", or 'tie' from the user's prespective."""
    if user == comp:
        return "tie"
    if (user == "rock" and comp == "scissors") or (user == "paper" and comp == "rock") or (user == "scissors" and comp == "paper"):
        return "win"
    return "lose"

def predict_next_move(freqs):
    """Predict the user's next move based on frequency counts (simple learning).
    freqs is a dict like {'rock': n1, 'paper':n2, 'scissors': n3}
    If all are zero (start of game), pick a random move.
    """
    total = sum(freqs.values())
    if total == 0:
        return random.choice(VALID_MOVES), 0.0 
    most_move = max(freqs, key=freqs.get)
    confidence = freqs[most_move] / total
    return most_move, confidence

def play():
    print("=== Rock , Paper , Scissors Predictor - Part 1 ===")
    print("Type rock / paper / scissors. Type 'exit' to stop.")

    freqs = {"rock": 0, "paper": 0, "scissors": 0}
    rounds = 0
    user_wins = 0
    comp_wins = 0
    ties = 0

    while True:
        user = input("\nYour move: ").strip().lower()
        if user == "exit":
            break
        if user not in VALID_MOVES:
            print("I didn't understand that. Please type Rock, Paper, or Scissors.")
            continue

        predicted_user, conf = predict_next_move(freqs)
        comp = counter_move(predicted_user)

        result = winner(user, comp)

        freqs[user] += 1
        rounds += 1
        if result == "win":
            user_wins += 1
        elif result == "lose":
            comp_wins += 1
        else:
            ties += 1

        print(f"AI predicted you might play:{predicted_user}")
        print(f"Computer played: {comp}")
        print(f"Result this round: You {result}!")

        conf_pct = int(round(conf * 100))
        print(f"AI Confidence: {conf_pct}%")
        if conf_pct < 70:
            print("Tip: Try to surprise me if my confidence is high! 😉")

    print("\n=== Game Summary (Part 1) ===")
    print(f"Rounds: {rounds} | You won: {user_wins} | Computer won: {comp_wins} | Ties: {ties}")
    if rounds > 0:
        most = max(freqs, key=freqs.get)
        print(f"Your most frequent move was: {most} ({freqs[most]} times)")
        print(f"Next time, my counter would be: {counter_move(most)}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play()