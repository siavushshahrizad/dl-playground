# This is a terminal mini deployment of a neural net trained
# on tweets to classify others as lonely or not. See the 
# loneliness_tweets.ipynb for details of data and model training

from transformers import pipeline

MODEL_PATH = "./bert_model"

# Initialize the classifier once
classifier = pipeline("text-classification", model=MODEL_PATH, tokenizer=MODEL_PATH)

def classify_text(txt: str) -> str:
    result = classifier(txt)[0]['label']
    print(f"The model classified the tweet as: {'not lonely' if result == 'LABEL_0' else 'lonely'}")

def greet_users():
    print("Hello!")
    print("I am a neural net classifier. Please input some text and I will tell you")
    print("if the person who wrote it is lonely or not. ")
    return input("Your text: ")

def main():
    text = greet_users()
    classify_text(text)

if __name__ == '__main__':
    main()