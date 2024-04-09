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
lsSplit ls = (before ls, maximum ls, after ls)
             where before ls = [ls !! i | i <- [0..(max_index ls)-1]]
                   after ls = [ls !! i | i <- [(max_index ls) + 1 .. (length ls)-1]]
                   max_index ls = find_index ls (maximum ls) 0
                   find_index ls max index = if (ls !! index == max)
                                                 then index
                                             else find_index ls max (index+1)

-- 3

selectionSort :: Ord a => [a] -> [a]
selectionSort ls = select ls []
                   where select [] ord_ls = ord_ls
                         select ls ord_ls = select ((before_min ls) ++ (after_min ls)) (ord_ls ++ [minimum ls])
                         before_min ls = [ls !! i | i <- [0..(min_index ls)-1]]
                         after_min ls = [ls !! i | i <- [(min_index ls) + 1 .. (length ls)-1]]
                         min_index ls = find_index ls (minimum ls) 0
                         find_index ls val index = if (ls !! index == val)
                                                       then index
                                                   else find_index ls val (index+1)
