set terminal pngcairo size 800,600
set output 'relative_freq.png'
set title "График относительной частоты"
set xlabel "Частота, кГц"
set ylabel "δn = Δn/n"
set grid
plot 'relative_freq.txt' using 1:2 with points pt 7 ps 2 title ""