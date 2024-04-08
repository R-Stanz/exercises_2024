--  1

replace :: [Char] -> [Char] -> [Char] -> [Char]
replace text from to = evaluate_replace text from to "" 0
                       where evaluate_replace text from to new_text index = if (index == (length text))
                                                                                then new_text
                                                                            else if((head from == text !! index) && ([text !! i | i <- [index..(index+(length from)-1)]] == from))
                                                                                then evaluate_replace text from to (new_text ++ to) (index + (length from))
                                                                            else evaluate_replace text from to (new_text ++ [text !! index]) (index + 1)

-- 2

lsSplit :: [Int] -> ([Int], Int, [Int])
lsSplit ls = ([], 0, [])

-- 3

selectionSort :: Ord a => [a] -> [a]
selectionSort ls = []
