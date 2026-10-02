import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os


load_dotenv()

model = ChatOpenAI(
    model=os.getenv("model"),
    api_key=os.getenv("api_key"),
    base_url=os.getenv("base_url")
)

# UI 
books = [
    # Classics & Foundational
    "The Lean Startup",
    "Zero to One",
    "The Hard Thing About Hard Things",
    "The Startup Owner's Manual",
    "The E-Myth Revisited",
    "The Mom Test",
    "Traction",
    "High Output Management",
    "Crossing the Chasm",
    "The Innovator's Dilemma",
    "The Four Steps to the Epiphany",
    "Business Model Generation",
    "The Art of the Start 2.0",
    "Built to Last",
    "Good to Great",
    "The Goal",
    "Measure What Matters",
    "Hooked",
    "Blitzscaling",
    "The Power Law",

    # Strategy & Innovation
    "Blue Ocean Strategy",
    "The Innovator's Solution",
    "Disruptive Innovation",
    "Competing Against Luck",
    "The Tipping Point",
    "Made to Stick",
    "Positioning",
    "The 22 Immutable Laws of Marketing",
    "Playing to Win",
    "Good Strategy Bad Strategy",

    # Marketing & Sales
    "Purple Cow",
    "This Is Marketing",
    "Building a StoryBrand",
    "Contagious",
    "Influence",
    "Pre-Suasion",
    "To Sell Is Human",
    "Never Split the Difference",
    "Pitch Anything",
    "The Sales Acceleration Formula",
    "Predictable Revenue",
    "Fanatical Prospecting",
    "Sell Like Crazy",
    "Copywriting Secrets",
    "DotCom Secrets",
    "Expert Secrets",
    "Oversubscribed",
    "The 1-Page Marketing Plan",
    "They Ask, You Answer",
    "Jab, Jab, Jab, Right Hook",

    # Leadership & Management
    "The One Minute Manager",
    "Radical Candor",
    "No Rules Rules",
    "Creativity, Inc.",
    "The Making of a Manager",
    "Scaling People",
    "Who: The A Method for Hiring",
    "The Five Dysfunctions of a Team",
    "Leaders Eat Last",
    "Extreme Ownership",
    "Multipliers",
    "The Coaching Habit",
    "Crucial Conversations",
    "Difficult Conversations",
    "Thanks for the Feedback",

    # Founder Stories & Memoirs
    "Shoe Dog",
    "Steve Jobs",
    "Founders at Work",
    "The Everything Store",
    "Bad Blood",
    "The Big Billion Startup",
    "The Diary of a CEO",
    "Lost and Founder",
    "That Will Never Work",
    "The Airbnb Story",
    "Super Pumped",
    "The Upstarts",
    "Elon Musk",
    "The Thinking Machine",
    "Like, Share, and Subscribe",

    # Mindset & Psychology
    "Mindset",
    "Thinking, Fast and Slow",
    "Atomic Habits",
    "Deep Work",
    "The Psychology of Money",
    "Antifragile",
    "The Black Swan",
    "Fooled by Randomness",
    "The Almanack of Naval Ravikant",
    "Principles",
    "Sapiens",
    "Educated",
    "Grit",
    "Peak Performance",
    "The Talent Code",

    # Finance & Fundraising
    "Venture Deals",
    "The Intelligent Investor",
    "Profit First",
    "Rich Dad Poor Dad",
    "The Total Money Makeover",
    "Financial Intelligence",
    "The Only Investment Guide You'll Ever Need",
    "Angel",
    "Secrets of Sand Hill Road",

    # Productivity & Systems
    "The 4-Hour Workweek",
    "Rework",
    "Remote",
    "The 12-Week Year",
    "Getting Things Done",
    "Eat That Frog",
    "The One Thing",
    "Essentialism",
    "Make Time",
    "Hyperfocus",

    # Niche & Specialized
    "The Minimalist Entrepreneur",
    "The $100 Startup",
    "Million Dollar Weekend",
    "Side Hustle",
    "Will It Fly?",
    "The Right It",
    "Running Lean",
    "Design Sprint",
    "Lean Analytics",
    "The Startup Way",
    "The Corporate Startup",
    "Disciplined Entrepreneurship",
    "The Founder's Dilemmas",
    "Venture Capitalists at Work",
    "Mastering the VC Game",

    # Indian Context & Emerging Markets
    "The Golden Tap",
    "Stay Hungry Stay Foolish",
    "Dream With Your Eyes Open",
    "Zero to Startup",
    "The Making of an Entrepreneur",
]

explaination_type=["Beginner Friendly", "Techinical", "Rule of list", "Paragraph wise", "Central Idea"]

Book_name = st.selectbox("Select the book for explaination", books)
input_style = st.selectbox("Select Explaination type", explaination_type)
length = st.selectbox("Select length of explaination", ["short explaination (1-3 lines)", "Medium explaination (3-8 lines)", "Long explaination (5-15 lines)", "choose length to clear concept (other)"])

st.header("Summaries Books")

template = PromptTemplate(
    template = """
Please summaries book titled {Book_name} with the following specification:

Explain style: {input_style},
Explain length: {length},

Analogy:
    User relatable analogies to simplify complex ideas, 
    simplify based on user demand 

Rules:
    if rules available in the book then list at the last all from the book 

Ensure the summary is clear, accurate and aligned with the provided style and length

"""
)


# Fill in place holder
prompt = template.invoke(
    {
        "Book_name": Book_name,
        "input_style": input_style,
        "length": length
    }
)

if st.button("Summaries"):
    result = model.invoke(prompt)
    st.write(result.content)
