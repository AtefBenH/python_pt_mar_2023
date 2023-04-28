from mysqlconnection import connectToMySQL

class Singer:
    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.nationality = data_dict['nationality']
        self.image = data_dict['image']
        self.rate = data_dict['rate']
        self.best_song = data_dict['best_song']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    # CRUD Queries == CREATE READ(all/one) UPDATE DELETE

    # ! ALL Queries Are Class Methods

    # -READ ALL
    @classmethod
    def get_all(cls):
        # * 1 WRITE THE QUERY
        query = """
        SELECT * FROM singers ;
        """
        # * 2 EXECUTING THE QUERY AND SAVING THE RETURN 
        results = connectToMySQL("music_db").query_db(query)
        print(results,"*"*25)
        all_singers = []
        for row in results:
            # singer = cls(row)
            # all_singers.append(singer)
            all_singers.append(cls(row))
        print(all_singers,"-"*20)
        return all_singers
    
    # -CREATE SINGER
    @classmethod
    def create(cls,data):
        # ! data = {name:value,nationality:value,image:value,rate:value,best_song:value}
        # * 1 WRITE THE QUERY
        query = """
        INSERT INTO singers (name,nationality, image,rate,best_song)
        VALUES (%(name)s, %(nationality)s, %(image)s, %(rate)s, %(best_song)s);
        """
        # * 2 EXECUTING THE QUERY AND SAVING THE RETURN 
        result = connectToMySQL("music_db").query_db(query,data)
        print("-"*20,result,"-"*20)
        return result
    
    # - READ One singer
    @classmethod
    def get_one(cls,data):
        # ! data = {id:value}
        query = """
        SELECT * FROM singers WHERE id = %(id)s;
        """
        results = connectToMySQL("music_db").query_db(query,data)
        print(results,"+-+")
        return cls(results[0])
    # - UPDATE Singer
    @classmethod
    def update(cls,data):
        query = """
        UPDATE singers 
        SET 
        name = %(name)s,nationality = %(nationality)s,
        image = %(image)s,rate = %(rate)s,best_song = %(best_song)s 
        WHERE id = %(id)s;
        """
        return connectToMySQL("music_db").query_db(query,data)

    # - DELETE
    @classmethod
    def delete(cls,data):

        query = """
        DELETE FROM singers WHERE id = %(id)s;
        """
        return connectToMySQL("music_db").query_db(query,data)