-- 01
-- crie uma função que determine se uma string é anagrama de outra
anagrama :: [Char] -> [Char] -> Bool 
anagrama "" "" = True
anagrama "" _ = False
anagrama _ "" = False
anagrama str1 str2 
    | (head'pos'in'2 str1 str2 0) == (length str2) = False
    | otherwise = anagrama (tail str1) [str2 !! i | i <- [0..((length str2) - 1)], i /= (head'pos'in'2 str1 str2 0)]
    where head'pos'in'2 str1 str2 count
            | count == (length str2) = count
            | (head str1) == (str2 !! count) = count
            | otherwise = head'pos'in'2 str1 str2 (count+1)
-- teste 
-- $ anagrama rau loa
-- true

-- 02
-- construa função que elimine repetções de uma dada string s
--  sem alterar a sequência original 
-- dos caracteres de s.
unique :: [Char] -> [Char]
unique x = generate [head x] (tail x)
    where generate str "" = str
          generate str old'str
              | (has'chr str (head old'str)) = generate str (tail old'str)
              | otherwise = generate (str ++ [head old'str]) (tail old'str)
          has'chr "" chr = False
          has'chr str chr
              | head str == chr = True
              | otherwise = has'chr (tail str) chr
-- unique _ = ""
-- teste
-- $ unique "aabbxa" 
-- $ "abx"

-- 03
-- implemente uma função que determine a string formada pelos 
-- caracteres comuns a duas strins de entrada a e b. A saida não 
-- deve ter duplicadas.
intersec :: [Char] -> [Char] -> [Char]
intersec a b = get'intersec a b ""
    where get'intersec "" b str = str
          get'intersec a b str
              | (has'chr b (head a)) && (not (has'chr str (head a))) = get'intersec (tail a) b (str ++ [head a])
              | otherwise = get'intersec (tail a) b str
          has'chr "" chr = False
          has'chr str chr
              | head str == chr = True
              | otherwise = has'chr (tail str) chr
-- teste
-- $ intersec "abcd" "cdef"
-- $ "cd"

-- 04
-- dado três listas zipálas numa lista de triplas de forma 
-- semelhante ao comando zip. 
zip'linha :: [a] -> [b] -> [c] -> [(a,b,c)] 
zip'linha ls1 ls2 ls3 = [(ls1 !! x, ls2 !! x, ls3 !! x) | x <- [0..((smallest'len ls1 ls2 ls3) -1)]]
    where smallest'len ls1 ls2 ls3 
            | length ls1 <= length ls2 && length ls1 <= length ls2 = length ls1
            | length ls2 <= length ls1 && length ls2 <= length ls3 = length ls2
            | otherwise = length ls3
-- teste 01
-- zip'linha
-- $ [1,2,3] "abc" [TRUE,FALSE,TRUE] 
-- $ [(1,"a", TRUE), (2, "b", FALSE), (3, "c", TRUE)] 
-- teste 02
-- $ zip'linha [1,2,3,4] "abc" [TRUE] 
-- $ [(1,"a",TRUE)]
