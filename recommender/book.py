
import pandas as pd

class BookRecommender:
  def __init__(self, csv_path):
    self.data = pd.read_csv(csv_path)

  def recommend(self, Book_Title=None,Book_Author=None,Year_Of_Publication=None):
    result = self.data
    if Book_Title:
      result = result[result['Book-Title'].str.lower() == Book_Title.lower()]
    if Book_Author:
      result = result[result['Book-Author'].str.lower() == Book_Author.lower()]
    if Year_Of_Publication:
      result = result[result['Year-Of-Publication'].astype(str) == str(Year_Of_Publication)]
    return result['Book-Title'].tolist()

