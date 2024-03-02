import Text.Printf

get_values str pos = do
                    if (drop (pos-1) (take pos str) == " ")
                        then (take pos str, drop pos str)
                    else
                        get_values str (pos+1)

-- removePunc xs = [ x | x <- xs, not (x `elem` "\"") ]

main = do
        str <- getLine
        let (str_a, str_b) = get_values str 1
        let a = read str_a
        let b = read str_b
	let result = 100*(b-a)/a
	printf "%.2f%s" (result::Float) "%\n"
