def sıcaklıkoku():  #def komutu ile istediğim sıcaklıkoku() isminde fonsiyon tanımlarım.

    import matplotlib.pyplot as plt   #grafik ile ilgili kütüphane tanımlamaları yapılır.
    import matplotlib.animation as animation
    from matplotlib import style

    style.use('fivethirtyeight')     #stle.use ile matplotlib için önceden tanımlanan stil tanımlanır.

    fig = plt.figure()            #matplotlib için figur tanımlaması yapılır.grafik için kullanılacak
    ax1 = fig.add_subplot(1,1,1)   #grafigin matematik mantığı için tanmlama yapılır.

    def animate(i):   #anime adlı fonksiyon tanımlanır. i degeri içine  verilir.
        graph_data = open('sicaklik.txt','r').read() #ana koddan alınan verilerin okunması sağlanır sıcaklık.txt ile.
        lines = graph_data.split('\n')
        xs = []  # x ekseni belirtilir
        ys = []  # y eksenii belirtilir.
        for line in lines:  #grafiğin sıra ile geçisi sağlanır.
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(x)   #degerler x ve y eksenlerine oturtulur.
                ys.append(y)
        ax1.clear()
        ax1.plot(xs, ys)   #eksenlere sıra ile degerler oturtulur.
    ani = animation.FuncAnimation(fig, animate, interval=10)
    plt.show()  #grafigi ekrana ver komutu.
sıcaklıkoku()   #sıcaklıkokudan alınan verilerle oluşturulan grafik ekrana verilir.
