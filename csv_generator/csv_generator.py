import json_to_csv_converter
import pandas as pd
import os

__dir__ = "data" # modify dataset directory if needed
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), __dir__)
)

class CsvGenerator():
    
    def __init__(self, business_filename: str, review_filename: str):
        self.business_filename = business_filename
        self.review_filename = review_filename
        self.business_ids = set()
        
    def read_csv(self):
        business_df = pd.read_csv(os.path.join(__location__, self.business_filename))
        review_df = pd.read_csv(os.path.join(__location__, self.review_filename))
        print("read csv files successfully...")
        
        return business_df, review_df

    def __clean_business_data(self, df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
        df = df[df['is_open'] == 1]
        df = df[columns]
        df = df[df["categories"].str.contains("Cafe", na=False) | df['categories'].str.contains("Coffee", na=False)]
        self.business_ids = set(df['business_id'])
        print("cleaned business data")
        
        return df

    def __clean_review_data(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        df = df[columns]
        df = df[df['business_id'].isin(self.business_ids)]
        print("cleaned review data")
        
        return df

    def save_to_csv(self, df: pd.DataFrame, filename: str) -> None:
        df.to_csv(os.path.join(__location__, filename))
        print("saved updated csv")
    
    def run(self, business_columns: list[str], review_columns: list[str]) -> None:

        business_df, review_df = self.read_csv()
        business_df = self.__clean_business_data(business_df, business_columns)
        review_df = self.__clean_review_data(review_df, review_columns)
        self.save_to_csv(business_df, "business.csv")
        self.save_to_csv(review_df, "review.csv")
    

        
        
if __name__ == "__main__":
    """
    hardcoded filenames, columns for now, need modification later
    """
    csv_generator = CsvGenerator("yelp_academic_dataset_business.csv", "yelp_academic_dataset_review.csv")
    business_columns = ['postal_code', 'latitude',
       'name', 'business_id', 'categories','address','city',
       'longitude','hours', 'stars','state','review_count']
    review_columns = ['business_id', 'text', 'stars', 'review_id', 'date']
    csv_generator.run(business_columns, review_columns)