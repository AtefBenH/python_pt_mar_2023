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
        # * EXECUTING THE QUERY AND SAVING THE RETURN 
        results = connectToMySQL("music_db").query_db(query)
        print(results,"*"*25)
        all_singers = []
        for row in results:
            # singer = cls(row)
            # all_singers.append(singer)
            all_singers.append(cls(row))
        print(all_singers,"-"*20)
        return all_singers