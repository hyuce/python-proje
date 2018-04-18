def nemoku():   #def komutu ile istediğim nemoku() isminde fonsiyon tanımlarım.
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation     #grafik ile ilgili kütüphane tanımlamaları yapılır.
    from matplotlib import style

    style.use('fivethirtyeight')     #stle.use ile matplotlib için önceden tanımlanan stil tanımlanır.

    fig = plt.figure()           #matplotlib için figur tanımlaması yapılır.grafik için kullanılacak
    ax1 = fig.add_subplot(1,1,1) #grafigin matematik mantığı için tanmlama yapılır.

    def animate(i):   #anime adlı fonksiyon tanımlanır. i degeri içine  verilir.
        graph_data = open('nem.txt','r').read()  #ana koddan alınan verilerin okunması sağlanır nem.txt ile.
        lines = graph_data.split('\n')
        xs = [] # x ekseni belirtilir
        ys = [] # y eksenii belirtilir.
        for line in lines: #grafiğin sıra ile geçisi sağlanır.
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(x)  #degerler x ve y eksenlerine oturtulur.
                ys.append(y)
        ax1.clear()
        ax1.plot(xs, ys)  #eksenlere sıra ile degerler oturtulur.
    ani = animation.FuncAnimation(fig, animate, interval=10)
    plt.show() #grafigi ekrana ver komutu.
nemoku() #nemokudan alınan verilerle oluşturulan grafik ekrana verilir.