movies = {
    "3 idiots": ["Taare Zameen Par", "Chhichhore", "Munna Bhai M.B.B.S"],
    "taare zameen par": ["3 Idiots", "Chhichhore", "Stanley Ka Dabba"],
    "chhichhore": ["3 Idiots", "Taare Zameen Par", "Yeh Jawaani Hai Deewani"],
    "dangal": ["Chak De! India", "Mary Kom", "Bhaag Milkha Bhaag"],
    "chak de! india": ["Dangal", "Mary Kom", "Bhaag Milkha Bhaag"]
}

print("=== Movie Recommendation System ===")
print("Type 'exit' to quit.")

while True:
    choice = input("\nEnter movie name: ").strip()
    if choice.lower() == "exit":
        print("Thank you for using the Recommendation System!")
        break

    recommendations = movies.get(choice.lower(), [])
    if recommendations:
        print("\nRecommended Movies:")
        for movie in recommendations:
            print("-", movie)
    else:
        print("Movie not found. Try: 3 Idiots, Taare Zameen Par, Chhichhore, Dangal, Chak De! India")
