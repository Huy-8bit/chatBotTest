import pickle


with open('words.pkl', 'rb') as f:
    data = pickle.load(f)
    
for word in data:
    print(word) 