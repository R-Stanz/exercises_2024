tls :: String -> [(Char, Int)]
tls s = whipe (s, [])
        where whipe (remain, result) = if (null remain)
                                        then result
                                    else
                                        whipe (reduce remain result)
              reduce remain result = (no'head'char remain, result ++ count'head'char remain)
              count'head'char remain = [(head remain, length [x | x <- remain, x == head remain])]
              no'head'char remain = [x | x <- remain, x /= head remain]

sfq :: String -> (String, Int)
sfq s = (" ", 0)
