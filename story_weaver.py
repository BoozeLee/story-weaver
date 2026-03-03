#!/usr/bin/env python3
"""
🎪✨ STORY-WEAVER: The Cosmic Joy Carnival ✨🎪
Where Stories Dance, Laughter Sparkles, and Every Word is a Celebration!

NO DARK TIMES - ONLY BRIGHT ONES! 🌈
"""

import random
import time
from datetime import datetime

# 🎵 The Eccentric Guest List
ECCENTRIC_GUESTS = {
    "🎺 Captain Funkatron": {
        "role": "Chief Joy Officer",
        "catchphrase": "Drop that bass and raise that story!",
        "specialty": "Plot twists that groove",
        "music": "Funk/Fusion"
    },
    "📚 Madame Plottwist": {
        "role": "Narrative Alchemist", 
        "catchphrase": "Darling, every problem is a plot point in disguise!",
        "specialty": "Turning mundane into magic",
        "music": "Jazz/Swing"
    },
    "🎨 Pixel the Dream Painter": {
        "role": "Visual Story Weaver",
        "catchphrase": "Let me paint you a picture of PURE JOY!",
        "specialty": "Vivid world-building",
        "music": "Ambient/Ethereal"
    },
    "🥁 Rhythm the Beat Keeper": {
        "role": "Pacing Guardian",
        "catchphrase": "Feel the rhythm, feel the rhyme, every story needs its time!",
        "specialty": "Perfect story pacing",
        "music": "Drum & Bass"
    },
    "🌟 Stella Starlight": {
        "role": "Inspiration Fairy",
        "catchphrase": "✨ You're more creative than you know! ✨",
        "specialty": "Crushing writer's block",
        "music": "Dream Pop"
    },
    "🎭 DJ Narrative": {
        "role": "Mix-Master of Tales",
        "catchphrase": "Scratch that plot hole, drop that beat!",
        "specialty": "Smooth transitions",
        "music": "Hip-Hop/Turntablism"
    },
    "🦜 Polly the Plot Parrot": {
        "role": "Idea Echo Chamber",
        "catchphrase": "SQUAWK! That idea is GOLD! SQUAWK!",
        "specialty": "Amplifying your best ideas",
        "music": "Tropical House"
    },
    "🎪 Barnaby the Story Clown": {
        "role": "Comedy Relief Chief",
        "catchphrase": "Whoops! *trips* And that's how you write comedy!",
        "specialty": "Humor and levity",
        "music": "Ragtime/Comedy"
    },
    "🎸 Luna the Lyric Weaver": {
        "role": "Musical Storyteller",
        "catchphrase": "Every story deserves a soundtrack!",
        "specialty": "Songs within stories",
        "music": "Folk/Indie"
    },
    "🌈 Rainbow the Reality Shaper": {
        "role": "Tone Guardian",
        "catchphrase": "Dark times? Never heard of them! Let's add RAINBOWS!",
        "specialty": "Maintaining positive vibes",
        "music": "Psychedelic"
    }
}

# 🎵 The Happiness Playlist
HAPPINESS_PLAYLIST = [
    "🎵 Plot Twist Boogie",
    "🎵 Character Development Disco", 
    "🎵 The Ballad of the Happy Ending",
    "🎵 Writer's Block Breakdown",
    "🎵 Symphony of Smiles",
    "🎵 No Dark Times (Remix)",
    "🎵 Funky Fresh Chapter Fresh",
    "🎵 The Joy Overture",
    "🎵 Beat Drop Boulevard",
    "🎵 Melody of Miracles"
]

# ✨ Story Starters (100% Joy, 0% Gloom)
STORY_STARTERS = [
    "The day the music discovered humanity back...",
    "When the rainbow learned to sing...",
    "The great confetti explosion of 2099...",
    "How the robot learned to dance...",
    "The festival that never ended...",
    "When colors gained consciousness...",
    "The friendship that saved the universe...",
    "The day laughter became contagious...",
    "How the stars learned to harmonize...",
    "The adventure that began with a smile..."
]

# 🌟 Happy Endings Generator
HAPPY_ENDINGS = [
    "And they all lived funkily ever after! 🎉",
    "The end? No, just the beginning of a new adventure! 🌈",
    "Cue the confetti, the music, and the eternal joy! ✨",
    "And somewhere, a smile was born that would never fade. 😊",
    "The story closes, but the happiness continues forever! 💖",
    "Roll credits, drop bass, repeat! 🎵",
    "The end... or is it? (Spoiler: It's a happy one!) 🌟",
    "And thus, joy propagated throughout the universe! 🚀✨"
]


def print_banner():
    """Display the funky opening banner."""
    banner = """
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║     🎪✨  STORY-WEAVER: COSMIC JOY CARNIVAL  ✨🎪            ║
    ║                                                               ║
    ║          Where Every Word Dances & Every Idea Sparkles       ║
    ║                                                               ║
    ║              🌈 NO DARK TIMES ALLOWED 🌈                     ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def spin_the_music_wheel():
    """Randomly select a song from the happiness playlist."""
    song = random.choice(HAPPINESS_PLAYLIST)
    print(f"\n🎵 NOW PLAYING: {song}")
    print("   [Music fills the air, creativity flows!]")
    return song


def summon_eccentric_guest():
    """Invite a random eccentric guest to help with your story."""
    guest_name = random.choice(list(ECCENTRIC_GUESTS.keys()))
    guest = ECCENTRIC_GUESTS[guest_name]
    
    print(f"\n{'='*60}")
    print(f"🌟 SUMMONING: {guest_name}")
    print(f"{'='*60}")
    print(f"   Role: {guest['role']}")
    print(f"   Specialty: {guest['specialty']}")
    print(f"   Music: {guest['music']}")
    print(f"   Says: \"{guest['catchphrase']}\"")
    print(f"{'='*60}\n")
    
    return guest_name


def generate_story_starter():
    """Create a random happy story starter."""
    starter = random.choice(STORY_STARTERS)
    print(f"\n📖 STORY STARTER:")
    print(f"   \"Once upon a time, {starter}\"")
    print(f"   [Your imagination takes over from here!]")
    return starter


def create_happy_ending():
    """Generate a guaranteed happy ending."""
    ending = random.choice(HAPPY_ENDINGS)
    print(f"\n🌈 HAPPY ENDING:")
    print(f"   \"{ending}\"")
    return ending


def joy_engine():
    """Main story-weaving joy engine."""
    print_banner()
    
    print("\n🎪 Welcome to the Story-Weaver Joy Engine! 🎪")
    print("   Where creativity meets celebration!\n")
    
    # Start the music
    spin_the_music_wheel()
    
    # Summon a guest
    guest = summon_eccentric_guest()
    
    # Generate a story starter
    starter = generate_story_starter()
    
    print("\n" + "="*60)
    print("🎨 YOUR CREATIVE SPACE AWAITS!")
    print("="*60)
    print("""
    Remember:
    ✨ There are no wrong ideas here
    ✨ Every plot hole is a dance opportunity  
    ✨ Writer's block is just a drum solo waiting to happen
    ✨ YOU are the magic this story needs
    
    Now go forth and CREATE SOMETHING BEAUTIFUL!
    """)
    print("="*60)
    
    # Generate a happy ending to look forward to
    create_happy_ending()
    
    print("\n🎉 STORY-WEAVER SESSION COMPLETE! 🎉")
    print("   Go share your joy with the world!\n")


def happiness_mode():
    """Extra happiness mode for maximum joy."""
    print("\n" + "🌟"*30)
    print("   ACTIVATING MAXIMUM HAPPINESS MODE!")
    print("🌟"*30)
    
    affirmations = [
        "✨ Your creativity is LIMITLESS!",
        "🎵 Your stories matter!",
        "💖 Your voice is UNIQUE and BEAUTIFUL!",
        "🌈 The world needs YOUR stories!",
        "🎪 Every word you write is a GIFT!",
        "🚀 You are a CREATIVE GENIUS!",
        "😊 Your joy is CONTAGIOUS!",
        "🎨 Your imagination is MAGIC!"
    ]
    
    for i, affirmation in enumerate(affirmations, 1):
        print(f"\n   {i}. {affirmation}")
        time.sleep(0.3)
    
    print("\n🌟"*30)
    print("   NOW GO CREATE SOMETHING AMAZING!")
    print("🌟"*30 + "\n")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--happiness":
            happiness_mode()
        elif sys.argv[1] == "--guest":
            summon_eccentric_guest()
        elif sys.argv[1] == "--starter":
            generate_story_starter()
        elif sys.argv[1] == "--ending":
            create_happy_ending()
        elif sys.argv[1] == "--music":
            spin_the_music_wheel()
        elif sys.argv[1] == "--help":
            print("""
    🎪 STORY-WEAVER: The Cosmic Joy Carnival 🎪
    
    Usage: python story_weaver.py [OPTION]
    
    Options:
      --happiness   Activate maximum happiness mode
      --guest       Summon a random eccentric guest
      --starter     Generate a happy story starter
      --ending      Create a guaranteed happy ending
      --music       Play a random song from the playlist
      --help        Show this help message
    
    No option? Run the full Joy Engine experience!
    
    Remember: NO DARK TIMES, ONLY BRIGHT ONES! 🌈
            """)
        else:
            print(f"Unknown option: {sys.argv[1]}")
            print("Try --help for the joy menu!")
    else:
        joy_engine()
