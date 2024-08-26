data Stack a = Empty | Value a (Stack a) 

push :: (Stack a) -> a -> (Stack a)
push Empty val = Value val Empty
push (Value a as) val = Value val (Value a as)

pop :: (Stack a) -> (Stack a)
pop Empty = Empty
pop (Value _ as) = as

top :: (Stack a) -> (Maybe a)
top Empty = Nothing
top (Value a _) = Just a

is'empty :: (Stack a) -> Bool
is'empty Empty = True 
is'empty _ = False

pos'fixa :: [Char] -> [Char]
pos'fixa str = new'eq str 0 "" Empty
    where 
        new'eq str marker new'str operators
            | length str <= marker = ending'fill new'str operators
            | (str !! marker >= 'a') && (str !! marker <= 'z') = new'eq str (marker+1) (new'str ++ [str !! marker]) operators
            | (str !! marker >= 'A') && (str !! marker <= 'Z') = new'eq str (marker+1) (new'str ++ [str !! marker]) operators
            | (str !! marker >= '0') && (str !! marker <= '9') = new'eq str (marker+1) (new'str ++ [str !! marker]) operators
            | str !! marker == '(' = new'eq str (marker+1) new'str (push operators '(')
            | str !! marker == ')', let (new'str', operators') = (close'parenthesis'fill new'str operators) = new'eq str (marker+1) new'str' (pop operators')
            | let operator = str !! marker, elem operator "+-*/^", let (new'str', operators') = (operator'fill new'str operators operator) = new'eq str (marker+1) new'str' (push operators' operator)
            | otherwise = error "Unknow Char"

        ending'fill str Empty = str
        ending'fill str operators = ending'fill (append'operator str (top operators)) (pop operators)

        append'operator str Nothing = str
        append'operator str (Just operator) = str ++ [operator]
 
        close'parenthesis'fill str operators
            | is'empty operators = (str, operators)
            | (top operators) == (Just '(') = (str, operators)
            | otherwise = close'parenthesis'fill (append'operator str (top operators)) (pop operators)

        operator'fill str operators operator
            | is'empty operators = (str, operators)
            | (elem operator "/*") && (elem (get'chr (top operators)) "+-/*") = operator'fill (append'operator str (top operators)) (pop operators) operator
            | (elem operator "+-") && (elem (get'chr (top operators)) "+-") = operator'fill (append'operator str (top operators)) (pop operators) operator
            | otherwise = (str, operators)

        get'chr Nothing = ' '
        get'chr (Just c) = c
