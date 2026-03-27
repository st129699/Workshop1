set terminal pngcairo size 800,600
set output 'histogram.png'
set title "Гистограмма распределения"
set xlabel "Частота, кГц"
set ylabel "Число наблюдений"
set style fill solid 0.5
set boxwidth 0.02
plot 'histogram_data.txt' using 1:2 with boxes title ""