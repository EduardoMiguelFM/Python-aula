produtos = [ {"nome": "Camisa", "preço": 50, "em_estoque": True}, 
            {"nome": "Calça", "preço": 80, "em_estoque": False}, 
            {"nome": "Chapéu", "preço": 30, "em_estoque": True}, ] 


filtro_em_estoque = lambda estoque : estoque ["em_estoque"] == True 

filtro_em_estoque = filter(filtro_em_estoque, produtos)

print(list(filtro_em_estoque))
