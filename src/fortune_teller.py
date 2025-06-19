import random
import os
from datetime import datetime

def generate_fortune():
    # Get GitHub Actions environment variables
    actor = os.getenv('GITHUB_ACTOR', 'coder')
    event = os.getenv('GITHUB_EVENT_NAME', 'push')
    
    # Get current time
    now = datetime.now()
    time_str = now.strftime("%H:%M")
    
    # Fun fortunes
    fortunes = [
        f"🌟 {actor}, your code will sparkle brighter than a supernova!",
        f"🧠 At {time_str}, your debugging skills will reach legendary status!",
        f"🚀 This {event} event will launch your career to new heights!",
        f"🎯 {actor}, your next commit will be pure perfection!",
        f"💡 At exactly {time_str}, a brilliant idea will strike!",
        f"🌈 {actor}, your code is about to make the world more colorful!",
        f"🦸‍♂️ Your coding superpowers will awaken during this {event} event!",
        f"🍀 Luck is on your side today, {actor}! Merge with confidence!"
    ]
    
    return random.choice(fortunes)

if __name__ == "__main__":
    print(generate_fortune())