import pandas as pd

class DatasetParser:
    def __init__(self, dataset_path) -> None:
        self.dataset_path = dataset_path
        self.df = pd.read_csv(dataset_path)

    def get_product_price(self, product):
        row_index = self.df.index[self.df['product']==product].tolist()
        if len(row_index) > 1:
            raise Exception("there is more than one data for the product!")
        row_index=row_index[0]

        price = self.df['price'].iloc[row_index]
        return price

    def get_product_expiry_date(self, product):
        row_index = self.df.index[self.df['product']==product].tolist()
        if len(row_index) > 1:
            raise Exception("there is more than one data for the product!")
        row_index=row_index[0]

        expiry_date = self.df['expiry_date'].iloc[row_index]
        return expiry_date

    def get_product_remaining_stock(self, product):
        row_index = self.df.index[self.df['product']==product].tolist()
        if len(row_index) > 1:
            raise Exception("there is more than one data for the product!")
        row_index=row_index[0]

        current_stock = self.df['current_stock'].iloc[row_index]
        return current_stock

    def get_product_original_stock(self, product):
        row_index = self.df.index[self.df['product']==product].tolist()
        if len(row_index) > 1:
            raise Exception("there is more than one data for the product!")
        row_index=row_index[0]

        original_stock = self.df['original_stock'].iloc[row_index]
        return original_stock

