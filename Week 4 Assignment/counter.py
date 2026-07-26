# Name: Bibhushi Karki
text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""
def word_frequency(text):
    text = text.lower()
    text = text.replace(".", "")
    text = text.replace(",", "")

    words = text.split()
    count = {}
    for word in words:
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1
    top_words = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return top_words[:3]
result = word_frequency(text)
print("Top 3 words:")
for word, number in result:
    print(f"{word} - {number} times")