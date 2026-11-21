from datetime import datetime

def safe_int(prompt: str, tries: int = 2, default:int = 0) -> int:
    """
    Ask the user fro a number and safely convert to int.
    If the user makes mistakes, let them try again a few times.
    Return a default value if all tries fail.
    """

    for attempt in range(tries):
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Oops! That wans't a number. Please try again.")
    print(f"Using default value {default}.")
    return default

def mood_to_tag(mood_text: str) -> str:
    """
    Turn a short mood phrase into a tiny tag/emoji label.
    This is NOT real sentiment analysis - just simple word checks.
    """
    m = mood_text.lower()   
    if any(w in m for w in ["happy", "good", "great", "awesome", "fun", "amazing"]):
        return "🙂 positive"
    if any(w in m for w in ["sad", "down", "unhappy", "upset", "depressing", "not happy"]):
            return "☹️ negative"
    if any(w in m for w in ["tired", "sleepy", "exhausted"]):
            return "😴 tired"
    if any(w in m for w in ["excited", "thrilled", "eager"]):
            return "🤩 excited"
    return "🤔 mixed"

def box(lines, pad=1, border_char="*"):
    """
    Make a simple ASCII box around a list of text lines.
    Example:
      ***************
      *    Hello    *
      *    World    *
      ***************
      """
    width = max(len(line) for line in lines) + (pad * 2)
    top_bottom = border_char * (width + 2)
    content = [top_bottom]
    for line in lines:
        content.append(border_char + " " * pad + line.ljust(width - pad * 2) + " " * pad + border_char)
    content.append(top_bottom)
    return "\n".join(content)

def main():
     print("=== Profile Card Program ===\n")

     name = input("Enter your name: ").strip().title()
     age = safe_int("Enter your age: ")
     mood = input("How are you feeling today? ").strip()
     mood_tag = mood_to_tag(mood)

     lines = [
          "Profile Card",
          f"Name : {name}",
          f"Age  : {age}",
          f"Mood : {mood} ({mood_tag})",
          "Thanks for sharing!"
     ]

     print("\n" + box(lines, pad=2, border_char="#") + "\n")

     color = input("What is your favorite color? ").strip().title()

     lines_with_color = [
          "Profile Card",
          f"Name  : {name}",
          f"Age   : {age}",
          f"Mood  : {mood} ({mood_tag})",
          f"Color : {color}",
          "------------------"
          "Summary saved to log files!"
     ]

     print("\n" + box(lines_with_color, pad=2, border_char="#") + "\n")

     ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

     txt_block = (
          f"[{ts}]\n"
          f"Name  : {name}\n"
          f"Age   : {age}\n"
          f"Mood  : {mood} ({mood_tag})\n"
          f"Color : {color}\n"
          f"{'-'*28}\n"
     )
     with open("profile_log.txt", "a", encoding="utf-8") as f:
          f.write(txt_block)

     csv_row = f'{ts},"{name}","{age}","{mood}","{mood_tag}","{color}"'
     header = "timestamp,name,age,mood,mood_tag,color\n"
     try:
          need_header = False
          try:
               with open("profile_log.csv", "r", encoding="utf-8") as check:
                    first = check.read(1)
                    if first == "":
                         needs_header = True
          except FileNotFoundError:
               needs_header = True

          with open("profile_log.csv", "a", encoding="utf-8") as f:
               if needs_header:
                    f.write(header)
               f.write(csv_row)
     except Exception as e:
          print("Couldn't update profile_log.csv", e)

     print("Log saved to: profile_log.txt and profile_log.csv")
     print("Great job! Try running again with different moods/colors to build a data log.\n")

if __name__ == "__main__":
     main()