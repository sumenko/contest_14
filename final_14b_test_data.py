tests = (
    ('#1', """5
alla 4 100
gena 6 1000
gosha 2 90
rita 2 90
timofey 4 80""", """gena
timofey
alla
gosha
rita
"""), ('#2', """5
alla 0 0
gena 0 0
gosha 0 0
rita 0 0
timofey 0 0""", """alla
gena
gosha
rita
timofey
""")
)
