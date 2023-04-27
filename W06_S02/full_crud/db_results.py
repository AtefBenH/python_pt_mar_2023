"""
Running Query: 
        SELECT * FROM singers ;

[
        {'id': 1, 'name': 'Frank Sinatra', 'nationality': 'American', 'image': 'https://t3.gstatic.com/licensed-image?q=tbn:ANd9GcTVrrNWvVMBMYe7h94wgO3zFVxjZld9zI_zNWJ_AgUw8aEvFBJfa_pVQFpfcvPRwq9s84bxA0Myi0K6ZiI', 'rate': 10, 'best_song': 'Fly MeTo TheLMoon', 'created_at': datetime.datetime(2023, 4, 25, 20, 34, 51), 'updated_at': datetime.datetime(2023, 4, 25, 
20, 34, 51)},
        {'id': 2, 'name': 'Julio Iglesias\n', 'nationality': 'Espanish', 'image': 'https://t3.gstatic.com/licensed-image?q=tbn:ANd9GcTZ93kbXxQpNpML0p737X6l5hvhMPCEVzdnJx0UNBO4d45_LbEDfikh9Z4ChsFJXXekegkpcJOCZAAUnio', 'rate': 10, 'best_song': 'Vous Les Femmes', 'created_at': datetime.datetime(2023, 4, 25, 21, 0, 15), 'updated_at': datetime.datetime(2023, 4, 25, 21, 0, 15)}
] *************************



Running Query: 
        SELECT * FROM singers WHERE id = 1;

[
        {'id': 1, 'name': 'Frank Sinatra', 'nationality': 'American', 'image': 'https://t3.gstatic.com/licensed-image?q=tbn:ANd9GcTVrrNWvVMBMYe7h94wgO3zFVxjZld9zI_zNWJ_AgUw8aEvFBJfa_pVQFpfcvPRwq9s84bxA0Myi0K6ZiI',
          'rate': 10, 'best_song': 'Fly MeTo TheLMoon', 'created_at': datetime.datetime(2023, 4, 25, 20, 34, 51), 'updated_at': datetime.datetime(2023, 4, 25, 20, 34, 51)
          }
] +-+
"""


