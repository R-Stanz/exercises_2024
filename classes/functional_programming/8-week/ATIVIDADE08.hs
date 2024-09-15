-- Árvore binária de busca (BST)
data BST a = Null
           | Node a (BST a) (BST a)
           deriving (Show, Eq)


-- Questão 1: Retorna a versão parentizada de uma BST dada
parentize :: BST Int -> String
parentize Null = ""
parentize (Node value left right) = "(" ++ show value ++ sub'tree'string left ++ sub'tree'string right ++ ")"
    where sub'tree'string side
              | side == Null = ""
              | otherwise = " " ++ parentize side

-- EXEMPLO: da questão 01.
-- Se você inserir os valores 14, 7, 20, 9, 1, 10 na BST, a representação parentizada seria: "(14 (7 (1) (9 (10))) (20))"

-- Questão 2: Constrói uma BST a partir da inserção consecutiva das chaves de uma lista de inteiros dada
addFromVec :: [Int] -> BST Int
addFromVec [] = Null
addFromVec ls = insert (last ls) (addFromVec (init ls))

insert :: Int -> BST Int -> BST Int
insert new'value Null = Node new'value Null Null
insert new'value (Node value left right)
    | new'value < value = Node value (insert new'value left) right
    | new'value > value = Node value left (insert new'value right)
    | otherwise = error "A BST can't have repeated values"

-- Questão 3: Calcula a altura de uma árvore binária de entrada
height :: BST a -> Int
height Null = 0 
height (Node _ left right) = 1 + max (height left) (height right)
