from models.db_connection import BBDD

class ProductModel:
    def __init__(self, conection:BBDD) -> None:
        self.con = conection.con
        self.cursor = conection.cursor
    
    def create_product(self, name:str=None, price:str=None, stock:str=None, description:str=None, category:str=None):
        try:
            product_id = ''.join(('PR', category[:3], name[:3], '0000', 'PR'))
            self.cursor.execute(
                '''
                    INSERT INTO PRODUCT (
                        PRODUCT_ID, 
                        PRODUCT_NAME, 
                        PRODUCT_PRICE, 
                        RODUCT_STOCK, 
                        PRODUCT_DESCRIPTION, 
                        PRODUCT_CATEGORY_ID
                    ) VALUES (
                        ?, ?, ?, ?, ?, ?
                    )
                ''',
                (product_id, name, price, stock, description, category)
            )
            self.con.commit()
            return True
        except:
            return False
    
    def search_product_by_name (self, word):
        search_word = f'%{word}%'
        query = '''
            SELECT *
            FROM PRODUCT
            WHERE PRODUCT_NAME LIKE ?
        '''
        try:
            self.cursor.execute(query, search_word)
            return self.cursor.fetchall()
        except:
            return None
    
    def search_product_by_category (self, category_id):
        cat_ir = f'%{category_id}%'
        query = '''
            SELECT PRODUCT.*
            FROM PRODUCT
            JOIN CATEGORY ON PRODUCT.PRODUCT_CATEGORY_ID = CATEGORY.CATEGORY_ID
            WHERE CATEGORY.CATEGORY_ID = ?
        '''
        try:
            self.cursor.execute(query, cat_ir)
            return self.cursor.fetchall
        except:
            return None
    
    def _search_product_by_id (self, id):
        product_id = f'%{id}%'
        query = '''
            SELECT *
            FROM PRODUCT
            WHERE PRODUCT_ID = ?
        '''
        try:
            self.cursor.execute(query, product_id)
            return self.cursor.fetchall()
        except:
            return None
    
    def update_product (self, id_product, **product_kwargs):
        if self._search_product_by_id(id_product):
            set_clause = ", ".join([f"{key} = ?" for key in product_kwargs.keys()])
            query = f"UPDATE PRODUCT SET {set_clause} WHERE PRODUCT_ID = ?"
            values = list(product_kwargs.values()) + [id_product]
            try:
                self.cursor.execute(query, values)
                self.con.commit()
                return True
            except:
                return False
        else:
            return False
        
    def delete_product (self, id_product):
        if self._search_product_by_id(id_product):
            try:
                self.cursor.execute("DELETE FROM PRODUCT WHERE PRODUCT_ID=?", (id_product,))
                self.con.commit()
                return True
            except:
                return False
        else:
            return False