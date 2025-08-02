
from recommender.book import BookRecommender

def main():
      recommender = BookRecommender("data/book.csv")
      print("Recommendations for  Book_Author='Richard Bruce Wright',Year_Of_Publication=2001:")
      print(recommender.recommend(Book_Author='Richard Bruce Wright', Year_Of_Publication=2001))

if __name__ == "__main__":
      main()
