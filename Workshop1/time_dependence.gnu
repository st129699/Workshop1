set terminal pngcairo size 800,600
set output 'time_dependence.png'
set title "Зависимость результатов наблюдений от времени"
set xlabel "Номер измерения"
set ylabel "Частота, кГц"
set grid
plot 'tochnaya_shkala.txt' using 1:2 with points pt 7 ps 1.5 title "Измерения"